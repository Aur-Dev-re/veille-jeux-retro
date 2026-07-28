# Fiches d'analyse des plateformes

Pour chaque plateforme : pays, type de vendeurs, possibilité de filtrer les
particuliers, système d'alertes officiel, recherches enregistrées, API
officielle, possibilité raisonnable de surveiller une page publique, connexion
obligatoire, fréquence de surveillance recommandée, niveau de risque de
blocage, méthode retenue, limitations, coût éventuel.

Statut : les 40 fiches sont terminées (4 prioritaires, 15 françaises
complémentaires, 10 européennes, 11 sources complémentaires type groupes
Facebook, brocantes, ressourceries, etc.). L'étape 1 du projet est achevée.

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

## 5. Rakuten France

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Particuliers et professionnels (marketplace, ex-PriceMinister) |
| Filtre particuliers | Non confirmé publiquement (structure en fiches produit de catalogue, pas en petites annonces libres) |
| Système d'alertes officiel | Oui, mais limité : alerte e-mail liée à une **fiche produit précise** (prévenu quand le produit revient en vente au prix souhaité), pas une recherche libre par mots-clés |
| Recherches enregistrées | Non, pas de recherche libre enregistrée (fonctionnement en catalogue de produits, pas en annonces texte libre) |
| API officielle | Oui, mais réservée aux **vendeurs professionnels** (publication/synchronisation de produits) — aucune API de recherche pour les acheteurs |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non pertinente : structure en catalogue, peu adaptée aux recherches vagues/contextuelles visées par ce projet |
| Connexion obligatoire | Oui, pour créer une alerte produit |
| Fréquence recommandée | Sans objet (pas de méthode automatisée retenue) |
| Risque de blocage | Nul (aucune automatisation prévue) |
| **Méthode retenue** | **Vérification manuelle occasionnelle uniquement**, priorité faible |
| Limitations | **Rakuten France envisagerait un arrêt progressif de son activité à partir du T3 2026** (recherche d'un repreneur par le groupe japonais) : à surveiller, ne pas investir de développement dessus tant que la situation n'est pas stabilisée. Structure catalogue peu compatible avec les recherches vagues/contextuelles du projet |
| Coût | Gratuit |

Sources : [Univers Colis — Rakuten France menacé en 2026](https://www.universcolis.fr/actualites/rakuten-france-menace-2026-colis-retours-garanties), [Service Client Rakuten France — recherches](https://help.fr.shopping.rakuten.net/hc/fr/articles/17967431814930-Comment-trouver-un-article-lors-de-mes-recherches)

---

## 6. ParuVendu

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Particuliers et professionnels (petites annonces généralistes) |
| Filtre particuliers | Filtre par catégorie disponible ; filtre strict "particulier uniquement" non confirmé |
| Système d'alertes officiel | Oui — **alerte e-mail** gratuite créable depuis une liste d'annonces ("Créer une alerte mail"), au choix quotidienne ou à chaque nouvelle annonce |
| Recherches enregistrées | Oui, gérées dans "Mon compte" > "Alertes" (modification/suppression/désactivation possibles) |
| API officielle | Non — aucune API publique pour les acheteurs |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, pour créer une alerte (compte gratuit) |
| Fréquence recommandée | Sans objet : notification native, pas de vérification périodique à faire |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une alerte e-mail pour chaque combinaison utile du champ lexical |
| Limitations | Une alerte à créer par requête ; traitement automatique du contenu des e-mails prévu en phase ultérieure (comme pour Leboncoin) |
| Coût | Gratuit |

Sources : [Aide ParuVendu — créer une alerte email](https://www.paruvendu.fr/aide/comment-creer-alerte-email-28/), [Aide ParuVendu — modifier/supprimer une alerte](https://www.paruvendu.fr/aide/comment-modifier-ou-supprimer-alerte-email-29/)

---

## 7. Geev

| Champ | Détail |
|---|---|
| Pays | France (également actif dans d'autres pays) |
| Type de vendeurs | Particuliers uniquement — **attention : Geev est un site de dons gratuits, pas de vente** (objets à récupérer gratuitement, pas à acheter) |
| Filtre particuliers | Natif (tous les utilisateurs sont des particuliers) |
| Système d'alertes officiel | Oui — "recherches enregistrées" avec notification en temps réel (icône cloche) dès qu'un don correspondant est publié à proximité |
| Recherches enregistrées | Oui, natives, **limitées à 20 par compte** |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, pour créer une recherche enregistrée (compte gratuit) |
| Fréquence recommandée | Sans objet : notification native en temps réel |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une recherche enregistrée pour les termes du champ lexical les plus pertinents (en priorisant, vu la limite de 20) |
| Limitations | Maximum 20 recherches enregistrées par compte ; objets gratuits donc rotation rapide et quantités probablement limitées ; ce sont des dons, pas des achats — bonne source complémentaire mais différente en nature |
| Coût | Gratuit |

Sources : [Centre d'aide Geev — les recherches enregistrées](https://geev.zendesk.com/hc/fr/articles/360022048791-Les-recherches-enregistr%C3%A9es-sur-Geev), [Centre d'aide Geev — créer une recherche enregistrée](https://geev.zendesk.com/hc/fr/articles/360028738971-Cr%C3%A9er-une-Recherche-enregistr%C3%A9e-sur-Geev)

---

## 8. Interencheres

| Champ | Détail |
|---|---|
| Pays | France (agrège plus de 700 maisons de ventes européennes) |
| Type de vendeurs | Maisons de ventes aux enchères (professionnels) — pas de particuliers |
| Filtre particuliers | Sans objet (vendeurs toujours professionnels : commissaires-priseurs) |
| Système d'alertes officiel | Oui — alerte e-mail gratuite quand un lot correspondant à la recherche est mis en vente ; recherche dans la description du lot **et** les catalogues PDF joints ; possibilité de restreindre par région/département |
| Recherches enregistrées | Oui, natives, gérées via les alertes |
| API officielle | Non confirmée publiquement |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit |
| Fréquence recommandée | Sans objet : notification native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une alerte pour les recherches **précises** du champ lexical (noms de consoles/jeux) |
| Limitations | Adapté aux objets rares/collector passant en vente aux enchères ; peu pertinent pour les recherches vagues/contextuelles (un commissaire-priseur décrit toujours précisément ses lots, contrairement à un particulier) |
| Coût | Gratuit |

Sources : [Aide Interencheres — comment faire une recherche](https://help.interencheres.com/hc/fr/articles/13444527386001-Comment-faire-une-recherche)

---

## 9. Drouot.com

| Champ | Détail |
|---|---|
| Pays | France, portée internationale |
| Type de vendeurs | Maisons de ventes aux enchères (professionnels) — pas de particuliers |
| Filtre particuliers | Sans objet (vendeurs toujours professionnels) |
| Système d'alertes officiel | Oui — enregistrer une recherche par mots-clés et filtres, alerte par e-mail ou notification dans l'app à chaque nouvelle annonce correspondante |
| Recherches enregistrées | Oui, natives, gérées dans l'onglet "Alertes" du profil |
| API officielle | Non confirmée publiquement |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit |
| Fréquence recommandée | Sans objet : notification native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une alerte pour les recherches **précises** du champ lexical (même logique qu'Interencheres) |
| Limitations | Même limitation qu'Interencheres : peu pertinent pour les recherches vagues/contextuelles |
| Coût | Gratuit |

Sources : [Centre d'aide Drouot.com](https://drouot.com/fr/faq)

---

## 10. Catawiki

| Champ | Détail |
|---|---|
| Pays | Pays-Bas (siège), actif en France, portée internationale |
| Type de vendeurs | Particuliers et professionnels, objets sélectionnés par des experts avant mise en vente (enchères spécialisées collection) |
| Filtre particuliers | Sans objet (structure en enchères curatées, pas en annonces libres) |
| Système d'alertes officiel | Oui — "auction alerts" par e-mail, mais **au maximum un e-mail par semaine** regroupant tous les lots correspondant aux mots-clés (pas de notification immédiate) |
| Recherches enregistrées | Oui, natives, gérées sur la page dédiée du compte |
| API officielle | Non pour les acheteurs — des scrapers tiers non officiels existent (Apify) mais **à exclure**, contraires aux règles du projet |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit |
| Fréquence recommandée | Sans objet : alerte native hebdomadaire, non configurable |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une alerte pour les recherches **précises** du champ lexical (objets de collection identifiés) |
| Limitations | Alerte native limitée à 1×/semaine, non modifiable ; adapté aux objets de valeur/collection, peu pertinent pour les recherches vagues/contextuelles |
| Coût | Gratuit (abonnements "Club+" payants optionnels, non nécessaires) |

Sources : [Catawiki — Auction alerts](https://www.catawiki.com/en/stories/5041-how-auction-alerts-can-help-you-find-what-you-re-looking-for)

---

## 11. Whatnot (France)

| Champ | Détail |
|---|---|
| Pays | États-Unis d'origine, actif en France depuis peu |
| Type de vendeurs | Particuliers et professionnels, vente en direct vidéo (live shopping) |
| Filtre particuliers | Sans objet (structure en lives vidéo, pas en annonces texte) |
| Système d'alertes officiel | Partiel — possibilité de "suivre" un vendeur et d'être notifié quand il passe en direct, mais **aucune alerte par mots-clés/catégorie** |
| Recherches enregistrées | Non trouvée |
| API officielle | Non — aucune API publique ; des scrapers tiers non officiels existent mais **à exclure**, contraires aux règles du projet |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non retenue : plateforme récente en France, fonctionnement par live vidéo peu compatible avec une veille automatisée respectueuse des règles |
| Connexion obligatoire | Oui, pour suivre des vendeurs |
| Fréquence recommandée | Sans objet, aucune méthode automatisée retenue |
| Risque de blocage | Élevé si scraping tenté — non tenté |
| **Méthode retenue** | Vérification **manuelle** occasionnelle : suivre quelques vendeurs identifiés spécialisés jeux vidéo rétro, consulter leurs lives ponctuellement |
| Limitations | Aucune solution automatisée conforme aux règles n'existe actuellement ; plateforme encore jeune en France |
| Coût | Gratuit |

Sources : [France Info — Whatnot, l'appli qui réinvente le téléshopping](https://www.franceinfo.fr/economie/commerce/e-commerce-whatnot-l-appli-qui-reinvente-le-teleshopping_7616171.html)

---

## 12. Delcampe

| Champ | Détail |
|---|---|
| Pays | Belgique (siège), actif en France, orienté objets de collection |
| Type de vendeurs | Particuliers et professionnels collectionneurs |
| Filtre particuliers | Non confirmé de filtre strict ; nature "collection" implique une forte proportion de particuliers |
| Système d'alertes officiel | Oui — créer une "recherche favorite" avec case "recevoir une alerte e-mail pour les nouveaux objets" : e-mail quotidien récapitulatif des nouveaux objets correspondants |
| Recherches enregistrées | Oui, natives ; **nombre limité selon l'abonnement** : Gratuit = 10, Bronze = 25, Silver = 50, Gold = 100 |
| API officielle | Oui, mais réservée aux **vendeurs professionnels abonnés Club+ Gold** (synchronisation de catalogue e-commerce) — pas d'API de recherche pour les acheteurs |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit |
| Fréquence recommandée | Sans objet : alerte quotidienne native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une recherche favorite avec alerte e-mail activée, pour les requêtes les plus utiles du champ lexical (dans la limite des 10 gratuites) |
| Limitations | Compte gratuit limité à 10 recherches favorites avec alerte ; prioriser les requêtes les plus productives ou envisager un abonnement payant si besoin |
| Coût | Gratuit (limité à 10 alertes), abonnements payants pour plus |

Sources : [Centre d'aide Delcampe — créer une recherche favorite](https://www.delcampe.net/fr/help-center/article/360015672939-creer-une-recherche-favorite), [Centre d'aide Delcampe — être informé des nouvelles ventes](https://www.delcampe.net/fr/help-center/article/360015686819-comment-etre-informe-des-nouvelles-ventes)

---

## 13. Easy Cash

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | **Professionnel uniquement** — enseigne de rachat-revente ; le vendeur affiché est toujours le magasin, jamais le particulier d'origine |
| Filtre particuliers | Sans objet (vendeur toujours professionnel) |
| Système d'alertes officiel | Non trouvé sur le site/l'app |
| Recherches enregistrées | Non trouvée |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non retenue en priorité : catalogue classé par catégorie/prix, pas par description libre — peu compatible avec les recherches vagues/contextuelles du projet |
| Connexion obligatoire | Non, pour consulter le catalogue en ligne |
| Fréquence recommandée | Sans objet, aucune méthode automatisée retenue |
| Risque de blocage | Non évalué, non tenté par choix |
| **Méthode retenue** | Vérification **manuelle** occasionnelle du catalogue en ligne "jeux vidéo rétro" |
| Limitations | Aucune méthode officielle d'alerte disponible ; structure catalogue peu adaptée aux recherches vagues/contextuelles |
| Coût | Gratuit à consulter |

---

## 14. Cash Express

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | **Professionnel uniquement** — même logique qu'Easy Cash (enseigne de rachat-revente) |
| Filtre particuliers | Sans objet |
| Système d'alertes officiel | Non trouvé |
| Recherches enregistrées | Non trouvée |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non retenue en priorité, mêmes raisons qu'Easy Cash |
| Connexion obligatoire | Non, pour consulter le catalogue |
| Fréquence recommandée | Sans objet |
| Risque de blocage | Non évalué, non tenté par choix |
| **Méthode retenue** | Vérification **manuelle** occasionnelle du catalogue en ligne |
| Limitations | Aucune méthode officielle d'alerte disponible |
| Coût | Gratuit à consulter |

---

## 15. Cash Converters

| Champ | Détail |
|---|---|
| Pays | France (enseigne internationale) |
| Type de vendeurs | **Professionnel uniquement** — même logique qu'Easy Cash et Cash Express |
| Filtre particuliers | Sans objet |
| Système d'alertes officiel | Non trouvé |
| Recherches enregistrées | Non trouvée |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non retenue en priorité, mêmes raisons |
| Connexion obligatoire | Non, pour consulter le catalogue |
| Fréquence recommandée | Sans objet |
| Risque de blocage | Non évalué, non tenté par choix |
| **Méthode retenue** | Vérification **manuelle** occasionnelle du catalogue en ligne |
| Limitations | Aucune méthode officielle d'alerte disponible |
| Coût | Gratuit à consulter |

---

## 16. Gamecash

| Champ | Détail |
|---|---|
| Pays | France (une cinquantaine de magasins, dont outre-mer) |
| Type de vendeurs | **Professionnel principalement** — spécialiste historique du jeu vidéo d'occasion, avec une marketplace en ligne permettant l'achat/revente ; diversifié depuis vers le high-tech et le rétrogaming |
| Filtre particuliers | Non confirmé pour la marketplace en ligne |
| Système d'alertes officiel | Non trouvé |
| Recherches enregistrées | Non trouvée |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Envisageable en dernier recours pour le rayon rétrogaming, mais non prioritaire faute d'alerte native |
| Connexion obligatoire | Non, pour consulter le catalogue |
| Fréquence recommandée | Sans objet, aucune méthode automatisée retenue pour l'instant |
| Risque de blocage | Non évalué, non tenté par choix |
| **Méthode retenue** | Vérification **manuelle** occasionnelle du catalogue en ligne, rayon rétrogaming en priorité (spécialiste historique du secteur) |
| Limitations | Aucune méthode officielle d'alerte disponible |
| Coût | Gratuit à consulter |

Sources : [Observatoire de la franchise — enseignes d'achat-cash](https://www.observatoiredelafranchise.fr/dossier-franchise/trois-enseignes-d-achat-cash-qui-comptent-1980.htm)

---

## 17. Cultura Occasion

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | **Professionnel** — jeux vidéo d'occasion vendus par Cultura et ses vendeurs partenaires marketplace |
| Filtre particuliers | Sans objet (marketplace professionnelle, pas d'annonces de particuliers) |
| Système d'alertes officiel | Non trouvé |
| Recherches enregistrées | Non trouvée |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non prioritaire faute d'alerte native ; catalogue produit standardisé, peu adapté aux recherches vagues/contextuelles |
| Connexion obligatoire | Non, pour consulter le catalogue |
| Fréquence recommandée | Sans objet |
| Risque de blocage | Non évalué, non tenté par choix |
| **Méthode retenue** | Vérification **manuelle** occasionnelle de la rubrique "jeux vidéo et consoles d'occasion" |
| Limitations | Aucune méthode officielle d'alerte disponible ; structure catalogue, pas annonces libres |
| Coût | Gratuit à consulter |

Sources : [Cultura — Jeux vidéo d'occasion](https://www.cultura.com/jeux-video-consoles/jeux-video--consoles-d-occasion/jeux-video-d-occasion.html)

---

## 18. Fnac Occasion (Fnac Marketplace)

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Particuliers et professionnels via la Fnac Marketplace (les vendeurs professionnels paient un abonnement mensuel + commission ; les particuliers peuvent aussi y vendre ponctuellement) |
| Filtre particuliers | Non confirmé de filtre strict pour l'acheteur |
| Système d'alertes officiel | Non trouvé de système d'alerte natif pour les acheteurs (par mots-clés) |
| Recherches enregistrées | Non trouvée |
| API officielle | Existe côté vendeur (gestion catalogue/stock), aucune API de recherche pour les acheteurs |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non prioritaire faute d'alerte native ; structure catalogue produit standardisé |
| Connexion obligatoire | Non, pour consulter le catalogue |
| Fréquence recommandée | Sans objet |
| Risque de blocage | Non évalué, non tenté par choix |
| **Méthode retenue** | Vérification **manuelle** occasionnelle de la rubrique jeux vidéo d'occasion |
| Limitations | Aucune méthode officielle d'alerte disponible pour les acheteurs ; structure catalogue produit, pas annonces libres de particuliers |
| Coût | Gratuit à consulter |

Sources : [Expert Marketplace — vendre sur Fnac Marketplace](https://www.expert-marketplace.fr/blog/vendre-sur-fnac-marketplace-guide-vendeur-2025/)

---

## 19. Amazon Seconde main (Amazon Marketplace occasion)

| Champ | Détail |
|---|---|
| Pays | France (amazon.fr) |
| Type de vendeurs | Particuliers (comptes vendeurs individuels) et professionnels, sur les fiches produit standardisées Amazon |
| Filtre particuliers | Partiel — Amazon distingue le nom du vendeur tiers sur chaque offre, mais pas de filtre global "particuliers uniquement" |
| Système d'alertes officiel | Non — pas d'alerte native par mots-clés pour une offre d'occasion à un prix donné (des outils tiers non officiels de suivi de prix existent, hors sujet ici) |
| Recherches enregistrées | Non trouvée pour les offres d'occasion |
| API officielle | Oui — **Product Advertising API**, mais orientée catalogue produit/affiliation, non conçue pour repérer une offre d'occasion précise d'un vendeur particulier |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non prioritaire : structure en fiche produit standardisée, peu compatible avec les recherches vagues/contextuelles visées par ce projet |
| Connexion obligatoire | Non, pour consulter les fiches produit |
| Fréquence recommandée | Sans objet, aucune méthode automatisée retenue |
| Risque de blocage | Non évalué, non tenté par choix |
| **Méthode retenue** | Vérification **manuelle** très occasionnelle, priorité **basse** — cette plateforme est peu adaptée à l'objectif du projet (annonces mal décrites de particuliers) |
| Limitations | Structure catalogue produit standardisé, incompatible avec les recherches vagues/contextuelles qui sont la priorité du projet |
| Coût | Gratuit à consulter |

---

## 20. Wallapop (Espagne)

| Champ | Détail |
|---|---|
| Pays | Espagne (présent aussi en Italie/Portugal, marché principal espagnol) |
| Type de vendeurs | Particuliers principalement (C2C) |
| Filtre particuliers | Natif, majoritairement particuliers |
| Système d'alertes officiel | Oui — "alertas de búsqueda" natives : notification quand une nouvelle annonce correspond aux critères (mots-clés, localisation, prix, catégorie) |
| Recherches enregistrées | Oui, natives, gérées dans "Favoritos > Búsquedas guardadas", pas de limite pratique connue |
| API officielle | Non trouvée pour les acheteurs |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit |
| Fréquence recommandée | Sans objet : notification native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une alerte de recherche pour chaque combinaison utile du champ lexical |
| Limitations | Interface principalement en espagnol ; une alerte à créer par requête |
| Coût | Gratuit |

Sources : [El Grupo Informático — activer les alertes de recherche Wallapop](https://www.elgrupoinformatico.com/tutoriales/como-activar-las-alertas-busqueda-wallapop-t74197.html)

---

## 21. Kleinanzeigen (Allemagne)

| Champ | Détail |
|---|---|
| Pays | Allemagne (ex-eBay Kleinanzeigen) |
| Type de vendeurs | Particuliers et professionnels |
| Filtre particuliers | Oui, filtre "Privat"/"Gewerblich" disponible |
| Système d'alertes officiel | Oui — "Suchauftrag speichern" (enregistrer la recherche) avec notification e-mail pour les nouvelles annonces correspondantes |
| Recherches enregistrées | Oui, natives |
| API officielle | **Non** — pas d'accès API public sans contrat spécial ; la plateforme ne souhaite pas en fournir pour un usage grand public |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit pour l'alerte |
| Fréquence recommandée | Sans objet : notification native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer un "Suchauftrag" avec notification e-mail pour chaque combinaison utile du champ lexical |
| Limitations | Interface en allemand ; aucune API donc entièrement dépendant de l'alerte native |
| Coût | Gratuit |

Sources : [Kleinanzeigen Help Center — recevoir automatiquement les nouveaux résultats](https://hilfe.kleinanzeigen.de/hc/de/articles/17102975598492)

---

## 22. Subito (Italie)

| Champ | Détail |
|---|---|
| Pays | Italie |
| Type de vendeurs | Particuliers et professionnels |
| Filtre particuliers | Oui, disponible dans les filtres |
| Système d'alertes officiel | Oui — "Salva ricerca" + bouton "Avvisami" : notification par e-mail, par push dans l'app, ou aucune, au choix |
| Recherches enregistrées | Oui, natives |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit pour l'alerte |
| Fréquence recommandée | Sans objet : notification native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une recherche sauvegardée avec "Avvisami" activé pour chaque combinaison utile du champ lexical |
| Limitations | Interface en italien |
| Coût | Gratuit |

Sources : [Assistenza Subito — Salvare una ricerca](https://assistenza.subito.it/hc/it/articles/360002172138-Salvare-una-ricerca)

---

## 23. Marktplaats (Pays-Bas)

| Champ | Détail |
|---|---|
| Pays | Pays-Bas |
| Type de vendeurs | Particuliers et professionnels |
| Filtre particuliers | Oui, disponible |
| Système d'alertes officiel | Oui — recherche sauvegardée avec notification, mais **une seule fois par jour** (pas de notification en temps réel) |
| Recherches enregistrées | Oui, natives |
| API officielle | **Oui** — API Marktplaats officielle (recherche par mots-clés/catégorie/prix/localisation), nécessite une inscription développeur et une authentification |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire, l'alerte native ou l'API couvrent le besoin |
| Connexion obligatoire | Compte gratuit pour l'alerte ; inscription développeur pour l'API |
| Fréquence recommandée | Alerte native quotidienne ; si l'API est utilisée, fréquence raisonnable dans les quotas développeur |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Recherche sauvegardée native en premier lieu (simple, gratuite) ; API officielle envisageable plus tard pour automatiser les recherches vagues/contextuelles si nécessaire |
| Limitations | Alerte native limitée à 1×/jour ; l'API nécessite une inscription développeur et le respect de quotas |
| Coût | Gratuit |

Sources : [Marktplaats API — documentation officielle](https://api.marktplaats.nl/docs/v1/index.html)

---

## 24. 2ememain (Belgique)

| Champ | Détail |
|---|---|
| Pays | Belgique (même groupe Adevinta que Marktplaats) |
| Type de vendeurs | Particuliers et professionnels |
| Filtre particuliers | Oui, disponible |
| Système d'alertes officiel | Oui — recherche sauvegardée avec notification (fonctionnement similaire à Marktplaats) |
| Recherches enregistrées | Oui, natives |
| API officielle | Une API existe ("Admarkt") mais **réservée aux vendeurs professionnels** pour publier des annonces automatiquement — pas d'API de recherche pour les acheteurs |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit pour l'alerte |
| Fréquence recommandée | Sans objet : notification native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une recherche sauvegardée avec notification pour chaque combinaison utile du champ lexical |
| Limitations | L'API existante est réservée aux vendeurs professionnels, inutilisable pour la recherche acheteur |
| Coût | Gratuit |

Sources : [2ememain.be Professionnel — API Admarkt](https://www.2ememainprofessionnel.be/admarkt2ememain/demarrer/api/)

---

## 25. Vinted (autres pays européens)

| Champ | Détail |
|---|---|
| Pays | Autres pays où Vinted est présent (Allemagne, Italie, Espagne, etc.), accessibles depuis le même compte en changeant de pays dans les paramètres |
| Type de vendeurs | Particuliers (identique à Vinted France) |
| Filtre particuliers | Natif |
| Système d'alertes officiel | **Non** — même limitation que Vinted France : pas de notification fiable pour une recherche sauvegardée, quel que soit le pays |
| Recherches enregistrées | Favoris possibles mais sans notification fiable associée |
| API officielle | Non |
| Flux RSS officiel | Non |
| Surveillance page publique raisonnable | Non recommandée, mêmes raisons que Vinted France (ToS restrictif) |
| Connexion obligatoire | Oui, même compte que Vinted France |
| Fréquence recommandée | Vérification manuelle 1 à 2 fois par jour |
| Risque de blocage | Élevé en cas d'automatisation — non tentée |
| **Méthode retenue** | Procédure **manuelle** identique à Vinted France, en changeant occasionnellement de pays dans l'app pour élargir la zone de recherche si pertinent |
| Limitations | Entièrement dépendant de la vérification manuelle, aucune automatisation possible sans enfreindre le ToS |
| Coût | Gratuit |

---

## 26. eBay (autres pays européens : Allemagne, Espagne, Italie, Belgique, Royaume-Uni)

| Champ | Détail |
|---|---|
| Pays | Allemagne, Espagne, Italie, Belgique, Royaume-Uni (sites eBay locaux) |
| Type de vendeurs | Particuliers et professionnels |
| Filtre particuliers | Oui (comme eBay France) |
| Système d'alertes officiel | Oui — recherches sauvegardées natives propres à chaque site local |
| Recherches enregistrées | Oui |
| API officielle | **Oui** — la **même Browse API** que pour eBay France, avec un identifiant de marketplace différent par pays (`EBAY_DE`, `EBAY_ES`, `EBAY_IT`, `EBAY_BE`, `EBAY_GB`), transmis dans l'en-tête `X-EBAY-C-MARKETPLACE-ID` |
| Flux RSS officiel | Non confirmé disponible |
| Surveillance page publique raisonnable | Non nécessaire, l'API officielle couvre le besoin |
| Connexion obligatoire | Même compte développeur eBay que pour la France |
| Fréquence recommandée | Identique à eBay France (quelques fois par jour, dans les quotas gratuits) |
| Risque de blocage | Très faible (méthode 100 % officielle) |
| **Méthode retenue** | Étendre la logique déjà prévue pour eBay France (Browse API) à ces marketplaces, avec le même compte développeur, en changeant simplement l'identifiant de marketplace dans la requête |
| Limitations | Léger travail de développement supplémentaire pour gérer plusieurs identifiants de marketplace ; aucune nouvelle inscription nécessaire |
| Coût | Gratuit dans les mêmes limites de quota développeur |

Sources : [eBay Developers — MarketplaceIdEnum (Browse API)](https://developer.ebay.com/api-docs/buy/browse/types/ba:MarketplaceIdEnum)

---

## 27. Gumtree (Royaume-Uni)

| Champ | Détail |
|---|---|
| Pays | Royaume-Uni |
| Type de vendeurs | Particuliers et professionnels |
| Filtre particuliers | Oui, disponible |
| Système d'alertes officiel | Oui — "Set Search Alert" créable depuis une recherche, géré dans "My Alerts" / "Saved searches" |
| Recherches enregistrées | Oui, natives |
| API officielle | Non trouvée pour la recherche acheteur (des scrapers tiers existent mais **à exclure**, contraires aux règles du projet) |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit pour l'alerte |
| Fréquence recommandée | Sans objet : notification native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une alerte de recherche pour chaque combinaison utile du champ lexical |
| Limitations | Interface en anglais britannique, prix en livres sterling |
| Coût | Gratuit |

Sources : [Gumtree Help Desk — Creating & Managing Alerts](https://help.gumtree.com/s/basics?amp=&article=Creating-Managing-Alerts2&cat=Searching_Replying)

---

## 28. Shpock

| Champ | Détail |
|---|---|
| Pays | Présent dans plusieurs pays européens (dont Royaume-Uni, Autriche, Allemagne) |
| Type de vendeurs | Particuliers principalement |
| Filtre particuliers | Natif, orienté C2C |
| Système d'alertes officiel | Oui — recherche sauvegardée (icône cloche), avec choix entre notification push ou e-mail |
| Recherches enregistrées | Oui, natives |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit |
| Fréquence recommandée | Sans objet : notification native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une recherche sauvegardée avec alerte activée pour chaque combinaison utile du champ lexical |
| Limitations | Audience plus réduite que Wallapop/Vinted selon les pays |
| Coût | Gratuit |

Sources : [Shpock Help — Search alerts](https://www.shpock.com/en-gb/help/360015900098)

---

## 29. Todocoleccion (Espagne)

| Champ | Détail |
|---|---|
| Pays | Espagne, orienté objets de collection |
| Type de vendeurs | Particuliers et professionnels collectionneurs |
| Filtre particuliers | Non confirmé de filtre strict ; nature "collection" implique une forte proportion de particuliers |
| Système d'alertes officiel | Oui — "alertas de búsqueda" : un e-mail quotidien récapitulatif de tous les nouveaux lots correspondants |
| Recherches enregistrées | Oui, liées aux alertes |
| API officielle | Oui, réservée aux vendeurs professionnels avancés (gestion de catalogue) — pas d'API de recherche pour les acheteurs |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit pour l'alerte |
| Fréquence recommandée | Sans objet : alerte quotidienne native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une alerte de recherche pour chaque combinaison utile du champ lexical, en pensant à la renouveler avant expiration |
| Limitations | **L'alerte expire après 90 jours si elle n'est pas renouvelée** — point de vigilance à surveiller |
| Coût | Gratuit |

Sources : [todocoleccion blog — Alertas de Búsqueda](https://www.todocoleccionblog.net/alertas-de-busqueda-con-una-palabra-basta/)

---

## 30. Groupes Facebook locaux et spécialisés jeux vidéo

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Particuliers essentiellement |
| Filtre particuliers | Natif (structure de groupe entre particuliers) |
| Système d'alertes officiel | Non — Facebook ne propose pas d'alerte par mot-clé à l'intérieur d'un groupe |
| Recherches enregistrées | Non disponible |
| API officielle | Non — mêmes limitations que Facebook Marketplace (pas d'API grand public, conditions d'utilisation restrictives) |
| Flux RSS officiel | Non |
| Surveillance page publique raisonnable | Non recommandée : connexion obligatoire, ToS restrictif, risque de blocage élevé en cas d'automatisation |
| Connexion obligatoire | Oui |
| Fréquence recommandée | Vérification manuelle régulière (par exemple 1 fois par jour) |
| Risque de blocage | Élevé si automatisation tentée |
| **Méthode retenue** | Vérification **manuelle** régulière d'une sélection de groupes rejoints (groupes locaux de ta région + groupes nationaux spécialisés jeux vidéo/rétrogaming) |
| Limitations | Nécessite de rejoindre les groupes au préalable (validation par un modérateur parfois requise) ; dépend entièrement de la vérification manuelle |
| Coût | Gratuit |

---

## 31. Groupes de vide-maison (Facebook)

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Particuliers (souvent familles gérant une succession ou un déménagement) |
| Filtre particuliers | Natif |
| Système d'alertes officiel | Non |
| Recherches enregistrées | Non disponible |
| API officielle | Non |
| Flux RSS officiel | Non |
| Surveillance page publique raisonnable | Non recommandée, mêmes raisons que les groupes Facebook jeux vidéo |
| Connexion obligatoire | Oui |
| Fréquence recommandée | Vérification manuelle régulière |
| Risque de blocage | Élevé si automatisation tentée |
| **Méthode retenue** | Vérification **manuelle** régulière, en priorité intéressante car ce type de groupe correspond bien aux recherches vagues/contextuelles (objets retrouvés en vidant une maison) |
| Limitations | Dépend entièrement de la vérification manuelle |
| Coût | Gratuit |

---

## 32. Pages d'associations

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Associations caritatives, dépôts-ventes associatifs |
| Filtre particuliers | Sans objet (vendeur = l'association) |
| Système d'alertes officiel | Non |
| Recherches enregistrées | Non disponible |
| API officielle | Non |
| Flux RSS officiel | Non |
| Surveillance page publique raisonnable | Envisageable ponctuellement pour une page publique consultée sans connexion, avec une fréquence très faible |
| Connexion obligatoire | Non, pour consulter une page publique |
| Fréquence recommandée | Vérification manuelle occasionnelle (quelques associations locales identifiées) |
| Risque de blocage | Nul (simple consultation occasionnelle) |
| **Méthode retenue** | Vérification **manuelle** occasionnelle d'une sélection de pages d'associations locales |
| Limitations | Couverture partielle, dépend des associations actives dans ta région |
| Coût | Gratuit |

---

## 33. Sites de commissaires-priseurs (indépendants)

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Commissaires-priseurs (professionnels) |
| Filtre particuliers | Sans objet |
| Système d'alertes officiel | La majorité des maisons de ventes sont déjà agrégées par **Interencheres** et **Drouot.com** (fiches 8 et 9), qui couvrent donc déjà l'essentiel de ce point |
| Recherches enregistrées | Voir fiches Interencheres/Drouot |
| API officielle | Non confirmée pour les quelques sites indépendants restants |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire pour les maisons déjà couvertes par Interencheres/Drouot |
| Connexion obligatoire | Variable selon le site indépendant |
| Fréquence recommandée | Sans objet |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | S'appuyer sur les alertes **Interencheres** et **Drouot.com** déjà en place (fiches 8 et 9) ; pas de développement spécifique supplémentaire nécessaire pour ce point |
| Limitations | Quelques commissaires-priseurs indépendants non agrégés peuvent échapper à la veille ; impact jugé faible |
| Coût | Gratuit |

---

## 34. Salles des ventes locales

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Maisons de ventes locales (professionnelles) |
| Filtre particuliers | Sans objet |
| Système d'alertes officiel | Déjà couvert dans la majorité des cas par Interencheres/Drouot (fiches 8 et 9), qui agrègent les salles des ventes locales adhérentes |
| Recherches enregistrées | Voir fiches Interencheres/Drouot |
| API officielle | Non confirmée pour les salles non agrégées |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire pour les salles déjà couvertes |
| Connexion obligatoire | Variable |
| Fréquence recommandée | Sans objet |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Identique à la fiche 33 : s'appuyer sur les alertes Interencheres/Drouot déjà en place |
| Limitations | Salles non agrégées non couvertes ; impact jugé faible |
| Coût | Gratuit |

---

## 35. Sites de vide-maison (services de débarras)

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Entreprises de débarras/vide-maison (professionnelles), qui revendent parfois les objets de valeur trouvés |
| Filtre particuliers | Sans objet |
| Système d'alertes officiel | Non trouvé — peu d'entreprises de ce secteur publient un catalogue en ligne consultable |
| Recherches enregistrées | Non disponible |
| API officielle | Non |
| Flux RSS officiel | Non |
| Surveillance page publique raisonnable | Envisageable ponctuellement si une entreprise locale publie ses trouvailles sur une page publique (Facebook, site vitrine) |
| Connexion obligatoire | Non |
| Fréquence recommandée | Vérification manuelle très occasionnelle |
| Risque de blocage | Nul |
| **Méthode retenue** | Vérification **manuelle** très occasionnelle, priorité basse : peu d'entreprises de débarras publient un catalogue exploitable en ligne |
| Limitations | Couverture faible et inégale selon les entreprises locales |
| Coût | Gratuit |

---

## 36. Brocantes / vide-greniers

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Particuliers (exposants de brocantes/vide-greniers) |
| Filtre particuliers | Natif |
| Système d'alertes officiel | Oui, mais **sur les événements, pas sur les objets** : le site **Brocabrac.fr** recense plus de 25 000 événements par an (brocantes, vide-greniers, vide-dressing) avec un agenda et des alertes par lieu/type d'événement |
| Recherches enregistrées | Alertes possibles par zone géographique/type d'événement, pas par objet recherché |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non pertinente : ce type de site indique où et quand chiner, pas ce qui est en vente |
| Connexion obligatoire | Non, pour consulter l'agenda |
| Fréquence recommandée | Consultation occasionnelle de l'agenda pour repérer les événements proches |
| Risque de blocage | Nul |
| **Méthode retenue** | Consultation **manuelle** occasionnelle de Brocabrac.fr pour repérer les brocantes/vide-greniers proches à visiter physiquement — hors périmètre d'automatisation, car il s'agit d'un agenda d'événements et non d'annonces d'objets |
| Limitations | Aucune automatisation possible par nature (il faut se déplacer physiquement pour voir les objets) |
| Coût | Gratuit |

Sources : [Brocabrac — agenda des brocantes et vide-greniers](https://brocabrac.fr/)

---

## 37. Ressourceries / recycleries

| Champ | Détail |
|---|---|
| Pays | France (Métropole et Outre-mer) |
| Type de vendeurs | Structures associatives de l'Économie Sociale et Solidaire (plus de 300 structures en réseau national) |
| Filtre particuliers | Sans objet (structure associative, objets donnés par des particuliers puis revendus à bas prix) |
| Système d'alertes officiel | Non — pas de catalogue en ligne centralisé, chaque structure gère son propre stock physique |
| Recherches enregistrées | Non disponible |
| API officielle | Non |
| Flux RSS officiel | Non |
| Surveillance page publique raisonnable | Envisageable ponctuellement pour les quelques ressourceries qui publient leurs nouveautés sur une page Facebook publique |
| Connexion obligatoire | Non |
| Fréquence recommandée | Vérification manuelle occasionnelle (visite physique ou consultation de la carte du réseau national pour repérer les structures proches) |
| Risque de blocage | Nul |
| **Méthode retenue** | Repérer les ressourceries/recycleries proches via la carte du réseau national, puis vérification **manuelle** occasionnelle (visite physique ou page Facebook si elle existe) |
| Limitations | Aucun catalogue en ligne centralisé ; dépend fortement de la visite physique |
| Coût | Gratuit |

Sources : [Réseau National des Ressourceries et Recycleries](https://ressourcerie.fr/les-ressourceries-et-recycleries/)

---

## 38. Emmaüs en ligne (Label Emmaüs)

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Structures de l'Économie Sociale et Solidaire du mouvement Emmaüs et partenaires (175 structures), objets de réemploi issus de dons de particuliers |
| Filtre particuliers | Sans objet (vendeur = la structure solidaire) |
| Système d'alertes officiel | Oui — "Gérer mes alertes" : e-mail quotidien récapitulatif des nouveaux objets correspondant aux critères enregistrés |
| Recherches enregistrées | Oui, natives (au moins un critère de recherche requis pour créer une alerte) |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Oui, compte gratuit pour créer une alerte |
| Fréquence recommandée | Sans objet : alerte quotidienne native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une alerte pour chaque combinaison utile du champ lexical |
| Limitations | Une alerte à créer par requête |
| Coût | Gratuit |

Sources : [Label Emmaüs — vente en ligne solidaire](https://www.label-emmaus.co/fr/)

---

## 39. Enchères du Domaine (encheres-domaine.gouv.fr)

| Champ | Détail |
|---|---|
| Pays | France (site officiel de l'État : DGFiP, AGRASC, Douane) |
| Type de vendeurs | L'État français (biens saisis, confisqués, abandonnés ou domaniaux) — pas de particuliers |
| Filtre particuliers | Sans objet |
| Système d'alertes officiel | Oui — possibilité de laisser son e-mail pour recevoir une alerte sur les ventes correspondant à ses centres d'intérêt |
| Recherches enregistrées | Oui, via l'alerte e-mail |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non nécessaire : l'alerte native suffit |
| Connexion obligatoire | Non confirmé, a priori juste une adresse e-mail suffit |
| Fréquence recommandée | Sans objet : alerte native |
| Risque de blocage | Nul avec la méthode retenue |
| **Méthode retenue** | Créer une alerte "jeux vidéo"/"consoles" si une catégorie adaptée existe lors de la création (à vérifier au moment de la mise en place) |
| Limitations | Catalogue de ventes assez rare pour des objets aussi spécifiques que des jeux vidéo (davantage orienté véhicules, mobilier, bijoux) → **priorité basse** |
| Coût | Gratuit |

Sources : [economie.gouv.fr — ventes aux enchères publiques](https://www.economie.gouv.fr/particuliers/mes-droits-conso/bien-consommer/ventes-aux-encheres-publiques-vous-pouvez-y-participer), [encheres-domaine.gouv.fr](https://encheres-domaine.gouv.fr/)

---

## 40. Liquidations judiciaires (Enchères-Publiques.com, Agorastore, etc.)

| Champ | Détail |
|---|---|
| Pays | France |
| Type de vendeurs | Liquidateurs judiciaires / commissaires de justice (professionnels) |
| Filtre particuliers | Sans objet |
| Système d'alertes officiel | Variable selon le site (à vérifier au cas par cas lors de la mise en place, non confirmé de façon homogène) |
| Recherches enregistrées | Non confirmée de façon homogène |
| API officielle | Non trouvée |
| Flux RSS officiel | Non trouvé |
| Surveillance page publique raisonnable | Non prioritaire |
| Connexion obligatoire | Variable |
| Fréquence recommandée | Sans objet |
| Risque de blocage | Nul (aucune automatisation prévue) |
| **Méthode retenue** | Vérification **manuelle** très occasionnelle, **priorité basse** : ce type de plateforme est surtout orienté matériel professionnel/industriel et immobilier, peu adapté aux jeux vidéo/consoles de particuliers |
| Limitations | Peu pertinent pour l'objectif du projet |
| Coût | Gratuit à consulter |

Sources : [Enchères-Publiques.com](https://www.encheres-publiques.com/), [ProcedureCollective.fr](https://www.procedurecollective.fr/fr/)

---

Toutes les plateformes identifiées au démarrage du projet sont désormais
documentées (40 fiches). D'éventuelles nouvelles plateformes pourront être
ajoutées ici au fil du temps si besoin.
