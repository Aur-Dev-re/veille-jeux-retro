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
ENV_LOCAL_PATH = RACINE / ".env"

# Petite pause entre deux recherches, pour rester raisonnable vis-à-vis d'eBay.
PAUSE_ENTRE_RECHERCHES_SECONDES = 0.3

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


def executer_veille_ebay(annonces_vues: dict) -> None:
    recherches_completes = charger_recherches(CONFIG_PATH)
    consoles_et_marques = charger_consoles_et_marques(CONFIG_PATH)

    # Première exécution : aucune annonce connue pour eBay -> on apprend ce qui
    # existe déjà sans envoyer une notification par annonce (pour ne pas noyer
    # la première utilisation sous des centaines de notifications d'annonces
    # qui étaient déjà en ligne avant le démarrage de la veille).
    premiere_execution = "ebay" not in annonces_vues
    if premiere_execution:
        print("[eBay] Première exécution : les annonces déjà en ligne seront mémorisées sans notification.")

    # Un même objet a le même identifiant eBay quel que soit le marketplace
    # utilisé pour le trouver : un seul ensemble suffit pour tous les pays.
    vues_ebay = set(annonces_vues.get("ebay", []))

    def traiter_recherche(mot_cle: str, marketplace: str) -> None:
        annonces = rechercher(mot_cle, marketplace=marketplace)
        nouvelles = [a for a in annonces if a["id"] and a["id"] not in vues_ebay]

        for annonce in nouvelles:
            if not premiere_execution:
                prix = f"{annonce['prix']} {annonce['devise']}" if annonce["prix"] else "prix non précisé"
                envoyer_notification(
                    titre=f"eBay {NOMS_MARKETPLACES.get(marketplace, marketplace)} : {mot_cle}",
                    message=f"{annonce['titre']} — {prix}",
                    lien=annonce["lien"],
                )
            vues_ebay.add(annonce["id"])

        time.sleep(PAUSE_ENTRE_RECHERCHES_SECONDES)

    print(f"[eBay] France : {len(recherches_completes)} recherches (champ lexical complet).")
    for mot_cle in recherches_completes:
        traiter_recherche(mot_cle, "EBAY_FR")

    print(
        f"[eBay] Autres pays UE ({', '.join(NOMS_MARKETPLACES[m] for m in MARKETPLACES_SUPPLEMENTAIRES)}) : "
        f"{len(consoles_et_marques)} recherches (noms de consoles/marques uniquement)."
    )
    for marketplace in MARKETPLACES_SUPPLEMENTAIRES:
        for mot_cle in consoles_et_marques:
            traiter_recherche(mot_cle, marketplace)

    annonces_vues["ebay"] = sorted(vues_ebay)
    print(f"[eBay] Terminé. {len(vues_ebay)} annonces au total mémorisées.")


def main() -> None:
    charger_env_local(ENV_LOCAL_PATH)

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Fichier de configuration introuvable : {CONFIG_PATH}")

    annonces_vues = charger_annonces_vues(ANNONCES_VUES_PATH)

    try:
        executer_veille_ebay(annonces_vues)
    except RuntimeError as erreur:
        # Ex: clés EBAY_CLIENT_ID/SECRET absentes -> on prévient sans faire
        # échouer toute la veille (les autres plateformes pourront tourner).
        print(f"[eBay] Veille eBay ignorée : {erreur}")

    sauvegarder_annonces_vues(ANNONCES_VUES_PATH, annonces_vues)

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
