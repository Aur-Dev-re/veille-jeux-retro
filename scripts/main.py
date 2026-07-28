"""
Point d'entrée principal de la veille.

Ce script sera exécuté automatiquement par GitHub Actions selon la planification
définie dans .github/workflows/veille.yml (à créer à l'étape suivante).

Pour l'instant, il ne fait rien d'autre que vérifier que tout est bien en place :
la logique de recherche par plateforme sera ajoutée aux étapes suivantes.
"""

from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def main() -> None:
    config_path = RACINE / "config" / "search_phrases.yml"
    if not config_path.exists():
        raise FileNotFoundError(f"Fichier de configuration introuvable : {config_path}")
    print("Configuration trouvée. Le moteur de veille sera ajouté aux prochaines étapes.")


if __name__ == "__main__":
    main()
