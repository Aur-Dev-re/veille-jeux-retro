# Veille Jeux Rétro

Système de veille automatisée pour repérer des annonces intéressantes de jeux vidéo, consoles et accessoires gaming vendus principalement par des particuliers (Leboncoin, Facebook Marketplace, Vinted, eBay, et d'autres plateformes françaises et européennes).

Ce projet est **entièrement indépendant** : il ne dépend d'aucun autre projet, service ou logiciel externe pour fonctionner.

## Structure du projet

- `config/` — fichiers de configuration (champ lexical de recherche, liste des plateformes).
- `data/` — état de la veille (annonces déjà vues, pour éviter les doublons).
- `scripts/` — code Python de la veille (recherche, analyse, notification).
- `docs/` — fiches d'analyse détaillées par plateforme.
- `.github/workflows/` — planification automatique (GitHub Actions).

## Fonctionnement

1. Le programme recherche des annonces selon trois types de recherche : précises (noms de consoles/jeux), vagues (annonces mal décrites) et contextuelles (vocabulaire indiquant un vendeur qui débarrasse un objet mal identifié).
2. Les nouvelles annonces trouvées sont envoyées sous forme de notification (ntfy).
3. Aucune donnée personnelle n'est stockée dans ce dépôt : seules les informations strictement nécessaires au fonctionnement de la veille y figurent. Les informations sensibles (adresse de notification, éventuelles clés) sont stockées dans des "Secrets" GitHub chiffrés, jamais dans le code.

## Règles de fonctionnement

Ce système respecte strictement les règles suivantes :
- aucune tentative de contournement de CAPTCHA, de connexion ou de protection anti-robot ;
- aucune automatisation d'achat ou d'envoi de message aux vendeurs ;
- aucun usage de proxy ou de changement d'adresse IP ;
- utilisation prioritaire des méthodes officielles (API, alertes, flux RSS, recherches enregistrées) ;
- fréquence de vérification raisonnable, jamais agressive.
