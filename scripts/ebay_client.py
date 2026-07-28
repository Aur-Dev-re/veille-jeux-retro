"""Client pour l'API officielle eBay Browse (Buy APIs).

Utilise le mode "Client Credentials" (identifiants de l'application uniquement,
pas de compte eBay personnel requis) pour rechercher des annonces publiques
par mots-clés. Documentation officielle :
https://developer.ebay.com/api-docs/buy/browse/overview.html
"""

import base64
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

OAUTH_URL = "https://api.ebay.com/identity/v1/oauth2/token"
SEARCH_URL = "https://api.ebay.com/buy/browse/v1/item_summary/search"
ITEM_URL = "https://api.ebay.com/buy/browse/v1/item"
SCOPE = "https://api.ebay.com/oauth/api_scope"

# Catégorie de repli si config/categories_ebay.yml est absent ou vide :
# "Video Games & Consoles", commune à tous les marketplaces eBay utilisés ici.
CATEGORIE_JEUX_VIDEO_DEFAUT = "1249"
CATEGORIES_CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "categories_ebay.yml"


def _categories_actives() -> str:
    """Lit config/categories_ebay.yml et retourne les IDs actifs, séparés par une virgule."""
    try:
        with CATEGORIES_CONFIG_PATH.open("r", encoding="utf-8") as fichier:
            donnees = yaml.safe_load(fichier) or {}
    except FileNotFoundError:
        return CATEGORIE_JEUX_VIDEO_DEFAUT

    ids = [
        str(categorie["id"]).strip()
        for categorie in donnees.get("categories", [])
        if categorie.get("actif") and str(categorie.get("id", "")).strip()
    ]
    return ",".join(ids) if ids else CATEGORIE_JEUX_VIDEO_DEFAUT

# Jeton d'accès mis en cache en mémoire le temps de l'exécution du script
# (il reste valide ~2h, largement plus que la durée d'une exécution).
_jeton_cache: dict[str, float | str] = {}


def _obtenir_jeton() -> str:
    """Récupère un jeton d'accès applicatif, en le réutilisant s'il est encore valide."""
    maintenant = time.time()
    if _jeton_cache.get("valeur") and _jeton_cache.get("expire_a", 0.0) > maintenant:
        return str(_jeton_cache["valeur"])

    client_id = os.environ.get("EBAY_CLIENT_ID")
    client_secret = os.environ.get("EBAY_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise RuntimeError(
            "EBAY_CLIENT_ID / EBAY_CLIENT_SECRET ne sont pas définis. "
            "Configure-les dans .env en local ou dans les Secrets GitHub."
        )

    identifiants = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")
    corps = urllib.parse.urlencode({"grant_type": "client_credentials", "scope": SCOPE}).encode("utf-8")
    requete = urllib.request.Request(
        OAUTH_URL,
        data=corps,
        headers={
            "Authorization": f"Basic {identifiants}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
    )
    with urllib.request.urlopen(requete, timeout=15) as reponse:
        donnees = json.loads(reponse.read().decode("utf-8"))

    _jeton_cache["valeur"] = donnees["access_token"]
    # Marge de sécurité de 60s avant l'expiration réelle du jeton.
    _jeton_cache["expire_a"] = maintenant + float(donnees.get("expires_in", 7200)) - 60
    return str(_jeton_cache["valeur"])


def rechercher(mot_cle: str, marketplace: str = "EBAY_FR", limite: int = 20) -> list[dict]:
    """Recherche des annonces eBay publiques correspondant à un mot-clé.

    Ne filtre pas par type de vendeur : la Browse API ne propose pas
    l'équivalent du filtre "Vendeur particulier" du site eBay (voir
    docs/plateformes.md, fiche eBay France, section Limitations).

    Retourne une liste de dictionnaires simplifiés (id, titre, prix, devise,
    lien, état). En cas d'erreur pour ce mot-clé précis (ex: quota momentané
    dépassé), retourne une liste vide plutôt que d'interrompre toute la veille.
    """
    jeton = _obtenir_jeton()
    parametres = urllib.parse.urlencode(
        {"q": mot_cle, "limit": str(limite), "category_ids": _categories_actives()}
    )
    requete = urllib.request.Request(
        f"{SEARCH_URL}?{parametres}",
        headers={
            "Authorization": f"Bearer {jeton}",
            "X-EBAY-C-MARKETPLACE-ID": marketplace,
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(requete, timeout=20) as reponse:
            donnees = json.loads(reponse.read().decode("utf-8"))
    except urllib.error.HTTPError as erreur:
        print(f"[eBay] Erreur pour la recherche '{mot_cle}' : {erreur.code} {erreur.reason}")
        return []

    annonces = []
    for item in donnees.get("itemSummaries", []):
        prix = item.get("price", {})
        valeur_prix = prix.get("value")
        try:
            prix_nombre = float(valeur_prix) if valeur_prix is not None else None
        except (TypeError, ValueError):
            prix_nombre = None

        categories_item = item.get("categories") or []

        annonces.append(
            {
                "id": item.get("itemId"),
                "titre": item.get("title"),
                "prix": valeur_prix,
                "prix_nombre": prix_nombre,
                "devise": prix.get("currency"),
                "lien": item.get("itemWebUrl"),
                "etat": item.get("condition"),
                "image": (item.get("image") or {}).get("imageUrl"),
                "categorie": categories_item[0].get("categoryName") if categories_item else None,
            }
        )
    return annonces


def obtenir_details(item_id: str, marketplace: str = "EBAY_FR") -> dict:
    """Récupère la description complète d'une annonce (get_item).

    N'est appelé que pour les annonces qui ont déjà dépassé le seuil de score
    sur le titre seul (voir scripts/filtrage.py) : jamais pour toutes les
    annonces d'un coup, pour garder le nombre d'appels API maîtrisé.

    Retourne un dictionnaire avec au moins la clé "description" (chaîne vide
    si indisponible). En cas d'erreur, retourne une description vide plutôt
    que d'interrompre la veille.
    """
    jeton = _obtenir_jeton()
    requete = urllib.request.Request(
        f"{ITEM_URL}/{urllib.parse.quote(item_id, safe='')}",
        headers={
            "Authorization": f"Bearer {jeton}",
            "X-EBAY-C-MARKETPLACE-ID": marketplace,
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(requete, timeout=20) as reponse:
            donnees = json.loads(reponse.read().decode("utf-8"))
    except urllib.error.HTTPError as erreur:
        print(f"[eBay] Erreur en récupérant le détail de {item_id} : {erreur.code} {erreur.reason}")
        return {"description": ""}

    return {"description": donnees.get("description") or ""}
