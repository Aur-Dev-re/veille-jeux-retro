"""Crée les Issues GitHub servant d'interface de validation humaine (étape 7).

Utilise l'API REST officielle de GitHub (déjà utilisée nulle part ailleurs
dans ce projet, mais gratuite et incluse avec le dépôt) via `urllib`, comme
le reste du projet (notifier.py, ebay_client.py) : aucune nouvelle
dépendance.

Authentification : le jeton fourni automatiquement par GitHub Actions
(`GITHUB_TOKEN`, voir .github/workflows/veille.yml) suffit, à condition que
le workflow déclare la permission `issues: write`.
"""

import json
import os
import urllib.error
import urllib.request

API_URL = "https://api.github.com"
USER_AGENT = "veille-jeux-retro"

# Les 5 choix de validation possibles (voir docs/plateformes.md et le plan de
# refonte). Une couleur par étiquette, purement pour la lisibilité dans
# l'interface GitHub.
LABELS_VALIDATION = {
    "très-intéressant": "1a7f37",
    "intéressant": "2da44e",
    "sans-intérêt": "d1d5da",
    "faux-positif": "d73a49",
    "à-revoir-plus-tard": "dbab09",
}


def _informations_repo() -> tuple[str, str]:
    depot = os.environ.get("GITHUB_REPOSITORY")
    if not depot or "/" not in depot:
        raise RuntimeError(
            "GITHUB_REPOSITORY n'est pas défini (format attendu : 'utilisateur/depot'). "
            "Sur GitHub Actions, cette variable est fournie automatiquement."
        )
    proprietaire, nom_depot = depot.split("/", 1)
    return proprietaire, nom_depot


def _jeton() -> str:
    jeton = os.environ.get("GITHUB_TOKEN")
    if not jeton:
        raise RuntimeError(
            "GITHUB_TOKEN n'est pas défini. Sur GitHub Actions, transmets "
            "${{ github.token }} en variable d'environnement du job."
        )
    return jeton


def _appel_api(methode: str, chemin: str, corps: dict | None = None) -> dict | list:
    proprietaire, nom_depot = _informations_repo()
    url = f"{API_URL}/repos/{proprietaire}/{nom_depot}{chemin}"
    donnees = json.dumps(corps).encode("utf-8") if corps is not None else None

    requete = urllib.request.Request(
        url,
        data=donnees,
        method=methode,
        headers={
            "Authorization": f"Bearer {_jeton()}",
            "Accept": "application/vnd.github+json",
            "User-Agent": USER_AGENT,
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(requete, timeout=20) as reponse:
        contenu = reponse.read().decode("utf-8")
        return json.loads(contenu) if contenu else {}


def creer_labels_si_absents() -> None:
    """Crée les 5 étiquettes de validation si elles n'existent pas déjà (idempotent)."""
    try:
        labels_existants = {label["name"] for label in _appel_api("GET", "/labels?per_page=100")}
    except urllib.error.HTTPError as erreur:
        print(f"[github_issues] Impossible de lister les étiquettes : {erreur.code} {erreur.reason}")
        return

    for nom, couleur in LABELS_VALIDATION.items():
        if nom in labels_existants:
            continue
        try:
            _appel_api("POST", "/labels", {"name": nom, "color": couleur})
            print(f"[github_issues] Étiquette créée : {nom}")
        except urllib.error.HTTPError as erreur:
            print(f"[github_issues] Impossible de créer l'étiquette '{nom}' : {erreur.code} {erreur.reason}")


def creer_issue(annonce: dict, marketplace_nom: str, mot_cle: str, score: float, mots_cles_matches: list[str]) -> str | None:
    """Crée une Issue de validation pour une annonce retenue par l'entonnoir.

    Retourne l'URL de l'Issue créée (utilisée comme lien de la notification
    ntfy), ou None en cas d'échec (la veille continue sans bloquer).
    """
    prix = f"{annonce['prix']} {annonce['devise']}" if annonce.get("prix") else "prix non précisé"
    photo = f"![photo]({annonce['image']})\n\n" if annonce.get("image") else ""

    corps = (
        f"{photo}"
        f"**Plateforme :** eBay {marketplace_nom}\n"
        f"**Recherche :** {mot_cle}\n"
        f"**Catégorie eBay :** {annonce.get('categorie') or 'non précisée'}\n"
        f"**Prix :** {prix}\n"
        f"**Score de pertinence :** {score:.1f}\n"
        f"**Mots-clés correspondants :** {', '.join(mots_cles_matches) or 'aucun'}\n\n"
        f"**Lien de l'annonce :** {annonce.get('lien')}\n\n"
        f"---\n"
        f"Choisis une étiquette ci-contre pour valider cette annonce : "
        f"très-intéressant, intéressant, sans-intérêt, faux-positif ou à-revoir-plus-tard.\n\n"
        f"<!-- veille-meta: {json.dumps({'mots_cles': mots_cles_matches, 'mot_cle_recherche': mot_cle, 'score': score, 'marketplace': marketplace_nom}, ensure_ascii=False)} -->"
    )

    titre = f"eBay {marketplace_nom} : {annonce.get('titre') or mot_cle}"[:250]

    try:
        issue = _appel_api("POST", "/issues", {"title": titre, "body": corps})
    except urllib.error.HTTPError as erreur:
        print(f"[github_issues] Impossible de créer l'Issue pour '{titre}' : {erreur.code} {erreur.reason}")
        return None

    return issue.get("html_url")
