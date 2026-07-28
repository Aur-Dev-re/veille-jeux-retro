"""
Point d'entrée principal de la veille.

Ce script sera exécuté automatiquement par GitHub Actions selon la planification
définie dans .github/workflows/veille.yml (à créer à l'étape suivante).

Pour l'instant, il ne fait rien d'autre que vérifier que tout est bien en place :
la logique de recherche par plateforme sera ajoutée aux étapes suivantes.
"""

import os
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))


def main() -> None:
    config_path = RACINE / "config" / "search_phrases.yml"
    if not config_path.exists():
        raise FileNotFoundError(f"Fichier de configuration introuvable : {config_path}")
    print("Configuration trouvée. Le moteur de veille sera ajouté aux prochaines étapes.")

    # Test ponctuel de bout en bout (Secret GitHub -> Actions -> ntfy).
    # Ne se déclenche que si on le demande explicitement (bouton "Run workflow"
    # avec la case cochée) : ne spamme jamais les exécutions automatiques.
    if os.environ.get("TEST_NOTIFICATION") == "true":
        from notifier import envoyer_notification

        envoyer_notification(
            titre="Veille Jeux Rétro",
            message="Test de bout en bout réussi : GitHub Actions, le Secret et ntfy fonctionnent ensemble.",
        )
        print("Notification de test envoyée.")


if __name__ == "__main__":
    main()
