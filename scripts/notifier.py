"""
Envoi des notifications de veille via ntfy.

Ce module sera complété à l'étape "Mettre en place le canal de notification ntfy".
Il lira l'adresse du topic ntfy depuis une variable d'environnement (NTFY_TOPIC_URL),
jamais depuis une valeur écrite en clair dans ce fichier.
"""

import os
import urllib.request


def envoyer_notification(titre: str, message: str, lien: str | None = None) -> None:
    """Envoie une notification via ntfy.

    titre : titre court de la notification (ex: nom de la plateforme)
    message : contenu de l'annonce repérée
    lien : URL de l'annonce, si disponible
    """
    topic_url = os.environ.get("NTFY_TOPIC_URL")
    if not topic_url:
        raise RuntimeError(
            "NTFY_TOPIC_URL n'est pas défini. "
            "Configure-le dans un fichier .env local ou dans les Secrets GitHub."
        )

    headers = {"Title": titre.encode("utf-8")}
    if lien:
        headers["Click"] = lien.encode("utf-8")

    request = urllib.request.Request(
        topic_url,
        data=message.encode("utf-8"),
        headers=headers,
        method="POST",
    )
    urllib.request.urlopen(request, timeout=15)
