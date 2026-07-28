# Fiches d'analyse des plateformes

Pour chaque plateforme : pays, type de vendeurs, possibilité de filtrer les
particuliers, système d'alertes officiel, recherches enregistrées, API
officielle, possibilité raisonnable de surveiller une page publique, connexion
obligatoire, fréquence de surveillance recommandée, niveau de risque de
blocage, méthode retenue, limitations, coût éventuel.

Statut : les 4 plateformes prioritaires sont traitées ci-dessous. Les autres
plateformes (européennes et complémentaires) seront ajoutées par lots.

---

## 1. Leboncoin (priorité)

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Particuliers et professionnels |
| Filtre particuliers | Oui, filtre "Particuliers" disponible dans la recherche |
| Système d'alertes officiel | Oui — fonctionnalité **"Mes recherches"** (le nom officiel n'est pas "alertes", ce qui prête à confusion) : notification par e-mail ou dans l'app à chaque nouvelle annonce correspondante |
| Recherches enregistrées | Oui, natives, illimitées en pratique |
| API officielle | Non — aucune API publique pour les particuliers/développeurs |
| Flux RSS officiel | Non — Leboncoin ne propose pas de RSS officiel (des générateurs tiers non officiels existent, à éviter) |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, pour créer et activer une recherche/alerte (compte gratuit) |
| Fréquence recommandée | Sans objet : c'est Leboncoin qui notifie, pas de vérification périodique à faire |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une recherche "Mes recherches" pour chaque combinaison utile du champ lexical, avec notification e-mail activée |
| Limitations | Une recherche à créer par requête ; le contenu des e-mails reçus n'est pas encore traité automatiquement (prévu en phase ultérieure, avec autorisation) |
| Coût | Gratuit |

Sources : [Centre d'aide Leboncoin — programmer des alertes](https://assistance.leboncoin.info/hc/fr/articles/360000969319), [Guide API Leboncoin (Stream Estate)](https://stream.estate/fr/guides/leboncoin-api)

---

## 2. Facebook Marketplace (priorité)

| Champ | Détail |
|---|---|
| Pays | International, dont France |
| Type de vendeurs | Particuliers et professionnels |
| Filtre particuliers | Partiel (filtre par catégorie, pas de filtre strict "particulier uniquement") |
| Système d'alertes officiel | Non — pas d'alerte e-mail/push pour une recherche sauvegardée sur Marketplace |
| Recherches enregistrées | Non disponible nativement sur Marketplace |
| API officielle | Non — Meta n'a jamais publié d'API pour Marketplace ; le "Commerce Platform API" est réservé aux partenaires professionnels approuvés (vente, pas recherche) |
| Flux RSS officiel | Non |
| Surveillance page publique raisonnable | Non recommandée : connexion obligatoire, conditions d'utilisation restrictives, risque de blocage élevé en cas d'automatisation |
| Connexion obligatoire | Oui |
| Fréquence recommandée | Sans objet (pas d'automatisation retenue) |
| Risque de blocage | Élevé si automatisation tentée |
| **Méthode retenue** | Vérification **manuelle** régulière (1 à 2 fois par jour) par toi-même ; possibilité de compléter via les groupes Facebook spécialisés jeux vidéo (voir section groupes) |
| Limitations | Aucune solution automatisée conforme aux règles n'existe actuellement |
| Coût | Gratuit |

Sources : [SociaVault — Facebook Marketplace API : pourquoi il n'y en a pas](https://sociavault.com/blog/facebook-marketplace-api-alternative), [api2cart — Facebook Marketplace API guide 2026](https://api2cart.com/api-technology/facebook-marketplace-api/)

---

## 3. Vinted (priorité)

| Champ | Détail |
|---|---|
| Pays | France, et autres pays européens accessibles depuis le compte |
| Type de vendeurs | Particuliers (plateforme C2C par nature) |
| Filtre particuliers | Natif (tous les vendeurs sont des particuliers) |
| Système d'alertes officiel | **Non** — malgré une forte demande des utilisateurs depuis des années, Vinted n'offre pas de notification automatique pour une recherche sauvegardée |
| Recherches enregistrées | Possibilité de mettre une recherche en favori, mais sans notification fiable associée |
| API officielle | Non |
| Flux RSS officiel | Non |
| Surveillance page publique raisonnable | Vérification manuelle de l'app recommandée, pas de surveillance automatisée (ToS restrictif) |
| Connexion obligatoire | Oui, pour sauvegarder une recherche |
| Fréquence recommandée | Vérification manuelle 1 à 2 fois par jour |
| Risque de blocage | Élevé en cas d'automatisation — non tentée |
| **Méthode retenue** | Procédure manuelle : ouvrir l'app matin et soir, consulter les recherches sauvegardées |
| Limitations | Entièrement dépendant de la vérification manuelle, aucune automatisation possible sans enfreindre le ToS |
| Coût | Gratuit |

Sources : [Vintify — alerte Vinted](https://vintify.io/blog/alerte-vinted-notification-nouvel-article), [Telvin-bot — alertes Vinted temps réel 2026](https://www.telvin-bot.com/en/blog/vinted-alerts-how-to-get-notified-real-time/)

---

## 4. eBay France (priorité)

| Champ | Détail |
|---|---|
| Pays | France (ebay.fr), portée internationale |
| Type de vendeurs | Particuliers et professionnels |
| Filtre particuliers | Oui, filtre "Vendeur particulier" disponible dans les résultats |
| Système d'alertes officiel | **Oui** — "Recherches sauvegardées" (Saved Searches) dans "Mon eBay" : e-mail envoyé (par défaut environ une fois par jour) quand de nouvelles annonces correspondent |
| Recherches enregistrées | Oui, natives |
| API officielle | **Oui** — **Browse API** (REST, gratuite avec clé développeur via l'eBay Developer Program), permet une recherche programmatique par mots-clés/catégories. L'ancienne "Finding API" a été **décommissionnée le 5 février 2025** : ne pas s'y référer, utiliser la Browse API |
| Flux RSS officiel | Non confirmé actuellement disponible (fonctionnalité ancienne potentiellement retirée) |
| Surveillance page publique raisonnable | Non nécessaire, l'API officielle couvre le besoin |
| Connexion obligatoire | Compte développeur eBay gratuit pour la clé API ; compte eBay classique pour les alertes e-mail |
| Fréquence recommandée | Alertes e-mail natives quotidiennes ; requêtes API à fréquence raisonnable (quelques fois par jour), dans les quotas gratuits du programme développeur |
| Risque de blocage | Très faible (méthode 100 % officielle) |
| **Méthode retenue** | Combinaison **Browse API** (recherches précises/vagues/contextuelles automatisées) + **Recherches sauvegardées** natives en complément |
| Limitations | Nécessite la création d'un compte développeur eBay (gratuit) ; quotas de requêtes définis par eBay |
| Coût | Gratuit dans les limites du quota développeur standard |

Sources : [eBay Developers — Browse API Overview](https://developer.ebay.com/api-docs/buy/browse/overview.html), [eBay — Saved searches](https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051), [eBay Community — décommissionnement Finding API](https://community.ebay.com/t5/Traditional-APIs-Search/Alert-Finding-API-and-Shopping-API-to-be-decommissioned-in-2025/m-p/34631345/highlight/true)

---

## Plateformes restantes (à traiter par lots)

Françaises : Rakuten France, ParuVendu, Geev, Interencheres, Drouot, Catawiki,
Whatnot France, Delcampe, Easy Cash, Cash Express, Cash Converters, Gamecash,
Cultura Occasion, Fnac Occasion, Amazon Seconde main.

Européennes : Wallapop (Espagne), Kleinanzeigen (Allemagne), Subito (Italie),
Marktplaats (Pays-Bas), 2ememain (Belgique), Vinted UE, eBay Allemagne/Espagne/
Italie/Belgique/Royaume-Uni, Gumtree UK, Shpock, Todocoleccion (Espagne).

Complémentaires : groupes Facebook locaux et spécialisés jeux vidéo,
groupes de vide-maison, pages d'associations, sites de commissaires-priseurs,
salles des ventes locales, sites de vide-maison, brocantes/vide-greniers,
ressourceries/recycleries, Emmaüs en ligne, enchères du Domaine, liquidations
judiciaires.
