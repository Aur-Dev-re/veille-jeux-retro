"""
Point d'entrée principal de la veille.

Ce script est exécuté automatiquement par GitHub Actions selon la planification
définie dans .github/workflows/veille.yml (toutes les 2h + déclenchement manuel).
"""

import json
import os
import sys
import time
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

from ebay_client import rechercher  # noqa: E402
from notifier import envoyer_notification  # noqa: E402

CONFIG_PATH = RACINE / "config" / "search_phrases.yml"
ANNONCES_VUES_PATH = RACINE / "data" / "seen_listings.json"
REFERENCE_PRIX_PATH = RACINE / "data" / "reference_prix.json"
ENV_LOCAL_PATH = RACINE / ".env"

# Petite pause entre deux recherches, pour rester raisonnable vis-à-vis d'eBay.
PAUSE_ENTRE_RECHERCHES_SECONDES = 0.3

# ntfy (offre gratuite) limite les envois en rafale (~12/min en usage prolongé) :
# une petite pause entre deux notifications évite de se faire rejeter (HTTP 429).
PAUSE_ENTRE_NOTIFICATIONS_SECONDES = 1.0

# eBay France reçoit le champ lexical complet (précises + vagues + contextuelles,
# toutes en français). Les autres marketplaces eBay ne reçoivent que les noms de
# consoles/marques (universels d'une langue à l'autre) : les recherches vagues et
# contextuelles sont rédigées en français et ne matcheraient presque rien chez un
# vendeur allemand, espagnol, italien ou anglais. Voir docs/plateformes.md, fiche 26.
NOMS_MARKETPLACES = {
    "EBAY_FR": "France",
    "EBAY_DE": "Allemagne",
    "EBAY_ES": "Espagne",
    "EBAY_IT": "Italie",
    "EBAY_BE": "Belgique",
    "EBAY_GB": "Royaume-Uni",
}
MARKETPLACES_SUPPLEMENTAIRES = ["EBAY_DE", "EBAY_ES", "EBAY_IT", "EBAY_BE", "EBAY_GB"]

# Filtre "bonne affaire" : ne s'applique qu'aux recherches précises de noms de
# consoles/marques (une moyenne de prix n'a pas de sens pour une recherche vague
# ou contextuelle, qui peut désigner un simple jeu ou tout un lot hétéroclite).
#
# eBay ne donne accès aux prix de vente réels qu'aux gros partenaires approuvés
# (Marketplace Insights API, accès restreint) : impossible à obtenir pour ce
# projet. La "moyenne" ci-dessous est donc calculée par le programme lui-même,
# à partir des prix DEMANDÉS sur les annonces en cours qu'il observe au fil du
# temps (moyenne mobile) — une approximation qui s'affine progressivement,
# pas un vrai historique de ventes.
SEUIL_REDUCTION_PRIX = 0.20  # notifie seulement si le prix est au moins 20% sous la moyenne
NOMBRE_MIN_ECHANTILLONS_PRIX = 5  # annonces à observer avant de faire confiance à la moyenne
ALPHA_MOYENNE_MOBILE = 0.15  # poids donné à chaque nouvelle observation dans la moyenne


def charger_env_local(chemin: Path) -> None:
    """Charge .env en local uniquement (tests sur ta machine).

    Sur GitHub Actions, ce fichier n'existe pas : les vraies valeurs viennent
    des Secrets du dépôt, injectés directement comme variables d'environnement.
    """
    if not chemin.exists():
        return
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#") or "=" not in ligne:
            continue
        cle, valeur = ligne.split("=", 1)
        os.environ.setdefault(cle.strip(), valeur.strip())


def charger_recherches(config_path: Path) -> list[str]:
    """Aplati config/search_phrases.yml en une simple liste de mots-clés à rechercher."""
    with config_path.open("r", encoding="utf-8") as fichier:
        donnees = yaml.safe_load(fichier)

    recherches: list[str] = []

    def ajouter(valeur) -> None:
        if isinstance(valeur, dict):
            for sous_valeur in valeur.values():
                ajouter(sous_valeur)
        elif isinstance(valeur, list):
            recherches.extend(valeur)

    for groupe in ("recherches_precises", "recherches_vagues", "recherches_contextuelles"):
        ajouter(donnees.get(groupe))

    return recherches


def charger_consoles_et_marques(config_path: Path) -> list[str]:
    """Ne récupère que les noms de consoles/marques (universels d'une langue à l'autre)."""
    with config_path.open("r", encoding="utf-8") as fichier:
        donnees = yaml.safe_load(fichier)
    return list(donnees.get("recherches_precises", {}).get("consoles_et_marques", []))


def charger_annonces_vues(chemin: Path) -> dict:
    if not chemin.exists():
        return {}
    with chemin.open("r", encoding="utf-8") as fichier:
        return json.load(fichier)


def sauvegarder_annonces_vues(chemin: Path, donnees: dict) -> None:
    with chemin.open("w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2, sort_keys=True)


def charger_reference_prix(chemin: Path) -> dict:
    if not chemin.exists():
        return {}
    with chemin.open("r", encoding="utf-8") as fichier:
        return json.load(fichier)


def sauvegarder_reference_prix(chemin: Path, donnees: dict) -> None:
    with chemin.open("w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2, sort_keys=True)


def cle_reference_prix(marketplace: str, mot_cle: str) -> str:
    return f"{marketplace}::{mot_cle}"


def mettre_a_jour_moyenne_prix(reference_prix: dict, cle: str, prix: float) -> None:
    entree = reference_prix.get(cle)
    if entree is None:
        reference_prix[cle] = {"moyenne": prix, "nombre": 1}
        return
    nouvelle_moyenne = entree["moyenne"] + ALPHA_MOYENNE_MOBILE * (prix - entree["moyenne"])
    reference_prix[cle] = {"moyenne": nouvelle_moyenne, "nombre": entree["nombre"] + 1}


def est_une_bonne_affaire(reference_prix: dict, cle: str, prix: float) -> bool:
    entree = reference_prix.get(cle)
    if not entree or entree["nombre"] < NOMBRE_MIN_ECHANTILLONS_PRIX:
        return False
    return prix <= entree["moyenne"] * (1 - SEUIL_REDUCTION_PRIX)


def etat_ebay(annonces_vues: dict) -> tuple[set, set]:
    """Récupère (annonces déjà vues, marketplaces déjà initialisés) pour eBay.

    Gère la migration depuis l'ancien format (une simple liste d'identifiants),
    utilisé avant l'ajout du suivi par marketplace.
    """
    etat = annonces_vues.get("ebay", {})
    if isinstance(etat, list):
        # Ancien format : seule eBay France avait été interrogée jusque-là.
        return set(etat), {"EBAY_FR"}
    return set(etat.get("vus", [])), set(etat.get("marketplaces_initialisees", []))


def envoyer_notification_prudente(**kwargs) -> None:
    """Envoie une notification sans jamais faire planter toute la veille si ça échoue
    (ex: ntfy momentanément saturé) : on log l'erreur et on continue.
    """
    try:
        envoyer_notification(**kwargs)
    except Exception as erreur:  # noqa: BLE001 - on ne veut jamais interrompre la veille ici
        print(f"[notifier] Échec d'envoi d'une notification, on continue : {erreur}")
    time.sleep(PAUSE_ENTRE_NOTIFICATIONS_SECONDES)


def executer_veille_ebay(annonces_vues: dict, reference_prix: dict) -> None:
    recherches_completes = charger_recherches(CONFIG_PATH)
    consoles_et_marques = charger_consoles_et_marques(CONFIG_PATH)
    mots_cles_avec_filtre_prix = set(consoles_et_marques)

    vues_ebay, marketplaces_initialisees = etat_ebay(annonces_vues)

    def sauvegarder_progres() -> None:
        # Appelé aussi en cas d'erreur en cours de route (voir le "finally" plus
        # bas) : ce qui a déjà été trouvé ne doit jamais être perdu.
        annonces_vues["ebay"] = {
            "vus": sorted(vues_ebay),
            "marketplaces_initialisees": sorted(marketplaces_initialisees),
        }

    def traiter_recherche(mot_cle: str, marketplace: str, premiere_fois_marketplace: bool) -> None:
        annonces = rechercher(mot_cle, marketplace=marketplace)
        filtrer_par_prix = mot_cle in mots_cles_avec_filtre_prix
        cle_prix = cle_reference_prix(marketplace, mot_cle)

        if filtrer_par_prix:
            # On affine la moyenne avec TOUTES les annonces observées (pas
            # seulement les nouvelles), pour qu'elle reflète les prix
            # actuellement demandés sur le marché.
            for annonce in annonces:
                if annonce["prix_nombre"] is not None:
                    mettre_a_jour_moyenne_prix(reference_prix, cle_prix, annonce["prix_nombre"])

        nouvelles = [a for a in annonces if a["id"] and a["id"] not in vues_ebay]

        for annonce in nouvelles:
            if not premiere_fois_marketplace:
                doit_notifier = True
                complement = ""

                if filtrer_par_prix:
                    doit_notifier = annonce["prix_nombre"] is not None and est_une_bonne_affaire(
                        reference_prix, cle_prix, annonce["prix_nombre"]
                    )
                    if doit_notifier:
                        moyenne = reference_prix[cle_prix]["moyenne"]
                        complement = f" (moyenne habituelle : {moyenne:.2f} {annonce['devise']})"

                if doit_notifier:
                    prix = f"{annonce['prix']} {annonce['devise']}" if annonce["prix"] else "prix non précisé"
                    envoyer_notification_prudente(
                        titre=f"eBay {NOMS_MARKETPLACES.get(marketplace, marketplace)} : {mot_cle}",
                        message=f"{annonce['titre']} — {prix}{complement}",
                        lien=annonce["lien"],
                    )
            vues_ebay.add(annonce["id"])

        time.sleep(PAUSE_ENTRE_RECHERCHES_SECONDES)

    def traiter_marketplace(marketplace: str, mots_cles: list[str], description: str) -> None:
        # Première fois qu'on interroge CE marketplace : on mémorise les annonces
        # déjà en ligne sans notifier, pour ne pas noyer la mise en route sous des
        # notifications rétroactives (voir la même logique pour la toute première
        # exécution du projet, appliquée ici par marketplace).
        premiere_fois = marketplace not in marketplaces_initialisees
        if premiere_fois:
            print(f"[eBay] {description} : première interrogation, mémorisation sans notification.")
        else:
            print(f"[eBay] {description}.")

        for mot_cle in mots_cles:
            traiter_recherche(mot_cle, marketplace, premiere_fois)

        marketplaces_initialisees.add(marketplace)

    try:
        traiter_marketplace(
            "EBAY_FR",
            recherches_completes,
            f"France : {len(recherches_completes)} recherches (champ lexical complet)",
        )

        for marketplace in MARKETPLACES_SUPPLEMENTAIRES:
            traiter_marketplace(
                marketplace,
                consoles_et_marques,
                f"{NOMS_MARKETPLACES[marketplace]} : {len(consoles_et_marques)} recherches "
                "(noms de consoles/marques uniquement)",
            )
    finally:
        sauvegarder_progres()
        print(f"[eBay] Terminé. {len(vues_ebay)} annonces au total mémorisées.")


def main() -> None:
    charger_env_local(ENV_LOCAL_PATH)

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Fichier de configuration introuvable : {CONFIG_PATH}")

    annonces_vues = charger_annonces_vues(ANNONCES_VUES_PATH)
    reference_prix = charger_reference_prix(REFERENCE_PRIX_PATH)

    try:
        executer_veille_ebay(annonces_vues, reference_prix)
    except Exception as erreur:  # noqa: BLE001
        # On ne laisse jamais un souci (clés manquantes, erreur réseau, quota
        # eBay dépassé...) faire perdre tout le travail déjà accompli : ce qui
        # a été trouvé avant l'erreur est quand même sauvegardé juste après.
        print(f"[eBay] Veille eBay interrompue par une erreur, mais l'état déjà trouvé sera sauvegardé : {erreur}")
    finally:
        sauvegarder_annonces_vues(ANNONCES_VUES_PATH, annonces_vues)
        sauvegarder_reference_prix(REFERENCE_PRIX_PATH, reference_prix)

    # Test ponctuel de bout en bout (Secret GitHub -> Actions -> ntfy).
    # Ne se déclenche que si on le demande explicitement (bouton "Run workflow"
    # avec la case cochée) : ne spamme jamais les exécutions automatiques.
    if os.environ.get("TEST_NOTIFICATION") == "true":
        envoyer_notification(
            titre="Veille Jeux Rétro",
            message="Test de bout en bout réussi : GitHub Actions, le Secret et ntfy fonctionnent ensemble.",
        )
        print("Notification de test envoyée.")


if __name__ == "__main__":
    main()
