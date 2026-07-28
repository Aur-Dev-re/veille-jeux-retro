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


def charger_annonces_vues(chemin: Path) -> dict:
    if not chemin.exists():
        return {}
    with chemin.open("r", encoding="utf-8") as fichier:
        return json.load(fichier)


def sauvegarder_annonces_vues(chemin: Path, donnees: dict) -> None:
    with chemin.open("w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2, sort_keys=True)


def executer_veille_ebay(annonces_vues: dict) -> None:
    recherches = charger_recherches(CONFIG_PATH)

    # Première exécution : aucune annonce connue pour eBay -> on apprend ce qui
    # existe déjà sans envoyer une notification par annonce (pour ne pas noyer
    # la première utilisation sous des centaines de notifications d'annonces
    # qui étaient déjà en ligne avant le démarrage de la veille).
    premiere_execution = "ebay" not in annonces_vues
    if premiere_execution:
        print("[eBay] Première exécution : les annonces déjà en ligne seront mémorisées sans notification.")

    vues_ebay = set(annonces_vues.get("ebay", []))
    print(f"[eBay] {len(recherches)} recherches à effectuer.")

    for mot_cle in recherches:
        annonces = rechercher(mot_cle)
        nouvelles = [a for a in annonces if a["id"] and a["id"] not in vues_ebay]

        for annonce in nouvelles:
            if not premiere_execution:
                prix = f"{annonce['prix']} {annonce['devise']}" if annonce["prix"] else "prix non précisé"
                envoyer_notification(
                    titre=f"eBay : {mot_cle}",
                    message=f"{annonce['titre']} — {prix}",
                    lien=annonce["lien"],
                )
            vues_ebay.add(annonce["id"])

        time.sleep(PAUSE_ENTRE_RECHERCHES_SECONDES)

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
