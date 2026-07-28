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

1. Le programme recherche des annonces selon trois types de recherche : précises (noms de consoles/jeux), vagues (annonces mal décrites) et contextuelles (vocabulaire indiquant un vendeur qui débarrasse un objet mal identifié). Seules les catégories eBay pertinentes sont interrogées (`config/categories_ebay.yml`), pour écarter d'emblée l'essentiel du hors-sujet (vêtements, goodies...).
2. Chaque nouvelle annonce passe ensuite un entonnoir de pertinence (`scripts/filtrage.py`) : un score textuel (titre puis description, avec tolérance aux fautes de frappe) doit dépasser un seuil minimal avant d'aller plus loin — jamais le prix, qui n'est utilisé que comme déclencheur (point 3), jamais comme critère de tri.
3. Pour les recherches précises de noms de consoles/marques, une notification n'est envoyée en plus que si le prix demandé est au moins 20 % en dessous du prix habituellement observé pour cette recherche (`data/reference_prix.json`). Cette moyenne est calculée par le programme lui-même à partir des annonces qu'il observe au fil du temps : eBay ne donne pas accès aux prix de vente réels en dehors de gros partenaires approuvés, donc il ne s'agit pas d'un historique officiel des ventes, mais d'une approximation qui s'affine progressivement. Les recherches vagues et contextuelles n'ont pas ce filtre de prix (une moyenne n'aurait pas de sens pour elles).
4. Chaque annonce qui franchit l'entonnoir crée une **Issue GitHub** de validation (photo, titre, catégorie, description, score, lien) plutôt qu'une décision automatique définitive : c'est toujours la personne qui valide, en choisissant une étiquette (très intéressant / intéressant / sans intérêt / faux positif / à revoir plus tard). Une notification (ntfy) pointant vers cette Issue est envoyée pour prévenir en temps réel.
5. Aucune donnée personnelle n'est stockée dans ce dépôt : seules les informations strictement nécessaires au fonctionnement de la veille y figurent. Les informations sensibles (adresse de notification, éventuelles clés) sont stockées dans des "Secrets" GitHub chiffrés, jamais dans le code.

## Règles de fonctionnement

Ce système respecte strictement les règles suivantes :
- aucune tentative de contournement de CAPTCHA, de connexion ou de protection anti-robot ;
- aucune automatisation d'achat ou d'envoi de message aux vendeurs ;
- aucun usage de proxy ou de changement d'adresse IP ;
- utilisation prioritaire des méthodes officielles (API, alertes, flux RSS, recherches enregistrées) ;
- fréquence de vérification raisonnable, jamais agressive.
