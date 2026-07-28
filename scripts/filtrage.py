"""Filtre textuel et priorisation des annonces (entonnoir, étapes 3-4).

Ce module ne fait jamais appel à un service externe : uniquement de la
comparaison de texte (bibliothèque standard `difflib`), avec une tolérance
aux fautes de frappe et aux accents. Le prix n'intervient JAMAIS ici : il
reste géré séparément dans scripts/main.py comme un déclencheur binaire pour
les recherches précises, jamais comme un critère de tri (décision explicite).
"""

import difflib
import unicodedata

# Un mot-clé "matche" un texte soit s'il y apparaît tel quel, soit si une
# fenêtre de mots du texte lui ressemble à au moins ce taux (tolère les
# fautes de frappe/orthographe sans déclencher sur un mot complètement
# différent).
SEUIL_SIMILARITE = 0.82

# Poids relatif de chaque catégorie de mots-clés dans le score final.
POIDS_PRECIS = 1.0
POIDS_VAGUE = 1.0
POIDS_CONTEXTUEL = 2.0  # "lot", "succession", "vide-maison"... sont un signal fort


def normaliser(texte: str) -> str:
    """Minuscules, sans accents, espaces compressés."""
    texte = (texte or "").lower()
    texte = unicodedata.normalize("NFKD", texte)
    texte = "".join(caractere for caractere in texte if not unicodedata.combining(caractere))
    return " ".join(texte.split())


def _correspond(mot_cle: str, texte_norm: str) -> bool:
    mot_norm = normaliser(mot_cle)
    if not mot_norm:
        return False
    if mot_norm in texte_norm:
        return True

    # Tolérance aux fautes de frappe : compare chaque fenêtre de mots du texte
    # (de même longueur que le mot-clé) au mot-clé, plutôt que le texte entier
    # (qui serait toujours très différent d'un mot-clé court).
    mots_texte = texte_norm.split()
    mots_cle = mot_norm.split()
    taille_fenetre = len(mots_cle)
    if taille_fenetre == 0 or len(mots_texte) < taille_fenetre:
        return False

    for debut in range(len(mots_texte) - taille_fenetre + 1):
        fenetre = " ".join(mots_texte[debut : debut + taille_fenetre])
        if difflib.SequenceMatcher(None, fenetre, mot_norm).ratio() >= SEUIL_SIMILARITE:
            return True
    return False


def mots_cles_correspondants(texte: str, mots_cles: list[str]) -> list[str]:
    """Retourne les mots-clés de la liste qui correspondent au texte (avec tolérance aux fautes)."""
    texte_norm = normaliser(texte)
    return [mot for mot in mots_cles if _correspond(mot, texte_norm)]


def score_final(
    titre: str,
    description: str,
    termes_precis: list[str],
    termes_vagues: list[str],
    termes_contextuels: list[str],
    poids_appris: dict | None = None,
) -> tuple[float, list[str]]:
    """Calcule un score de pertinence à partir du texte (titre + description).

    Ne tient jamais compte du prix. `poids_appris` (optionnel) est un
    dictionnaire mot-clé -> ajustement, alimenté par l'apprentissage à partir
    des validations humaines (voir Partie 2 du plan) ; absent au départ.
    """
    texte_complet = f"{titre or ''} {description or ''}".strip()

    matches_precis = mots_cles_correspondants(texte_complet, termes_precis)
    matches_vagues = mots_cles_correspondants(texte_complet, termes_vagues)
    matches_contextuels = mots_cles_correspondants(texte_complet, termes_contextuels)

    score = (
        POIDS_PRECIS * len(matches_precis)
        + POIDS_VAGUE * len(matches_vagues)
        + POIDS_CONTEXTUEL * len(matches_contextuels)
    )

    tous_matches = sorted(set(matches_precis + matches_vagues + matches_contextuels))

    if poids_appris:
        for mot in tous_matches:
            score += poids_appris.get(mot, 0.0)

    return score, tous_matches
