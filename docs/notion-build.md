# Construction Notion — carte technique (V1, 11 novembre 2026)

Tout se trouve dans l'espace de Huxxley, sous « Foyer — QG du projet » → « Le modèle » → **« Foyer »** (la page racine du produit).

## Pages

| Page | ID |
| --- | --- |
| Foyer (racine, accueil « Aujourd'hui ») | 4152d89c296e81e1aa0cccb63916d60b |
| Tâches du foyer | 4152d89c296e81a3959acdd22e9fc940 |
| Stock & courses | 4152d89c296e81d4854cc3f69f3cc71e |
| Repas | 4152d89c296e81728177e8cd652ba6b5 |
| Préparer ma semaine | 4152d89c296e8100939ed5a7d433d2ba |
| Démarrer en 15 minutes | 4152d89c296e81d8a69efda02f98da27 |
| Coulisses (bases sources) | 4152d89c296e81708e61e4dfa02b483d |

## Bases (dans Coulisses)

| Base | Data source | Contenu d'exemple |
| --- | --- | --- |
| Tâches du foyer | 82f566ca-be94-47e0-b895-0a2acf857eb7 | 74 tâches, 9 domaines |
| Produits | 35ce8f36-f431-450f-9f99-a666d1886df1 | 48 produits, dont 5 pour le stock 72 h |
| Recettes | 125fe4fb-0c71-44ed-9f7f-c33dbea08591 | 10 recettes |
| Ingrédients des recettes | c88c9e7e-d965-4061-be72-d522fa1bda0a | 45 lignes |
| Menu de la semaine | 1477e309-2956-4abb-a618-a62c083cd2d6 | 7 repas (9 au 15 novembre) |

## Chaînes de calcul (plan gratuit : formules, relations et rollups seulement)

**Tâches**
- Intervalle (jours) est calculé à partir de la Fréquence.
- Prochaine fois = Dernière fois + Intervalle.
- État = Prochaine fois − aujourd'hui, ce qui donne : En retard, Aujourd'hui, Cette semaine ou Plus tard.

**Stock**
1. Menu.Cuisiné (case cochée).
2. Recettes.Fois cuisinée (rollup qui compte les cases cochées).
3. Recettes.Nb cuisinée = toNumber(Fois cuisinée). Cette formule intermédiaire est nécessaire car Notion refuse un rollup de rollup.
4. Ingrédients.Fois cuisinée (rollup, somme).
5. Ingrédients.Consommé = Quantité × Fois cuisinée.
6. Produits.Total consommé (rollup, somme).
7. Stock actuel = Stock initial + Racheté depuis − Total consommé.
8. À racheter = Stock actuel ≤ Seuil.

**Prêt à cuisiner**
1. Ingrédients.Stock du produit (rollup).
2. Disponible = Stock du produit ≥ Quantité.
3. Recettes.Ingrédients dispo (rollup, pourcentage de cases cochées).

## Vérifié via le connecteur (requête « rows » avec filtres sur formules)

- Riz : 1 700 g. Carottes : 100 g, donc à racheter.
- Liquide vaisselle : à racheter.
- 10 tâches en retard.

## Limites connues du connecteur

- La DSL des vues ignore les filtres sur formules et sur rollups. À faire à la main : « À racheter » coché, « État » différent de « Plus tard ».
- Les propriétés Bouton, les automatisations et les modèles récurrents ne se créent que dans l'interface.
- Les valeurs des formules ne sont pas lisibles en clair. On peut en revanche filtrer dessus en mode `rows` pour vérifier.

## Filtres posés dans l'interface (le DSL des vues ignore les filtres sur formules)

| Vue | Filtre |
| --- | --- |
| Accueil › Mes tâches | Responsable = moi · État ne contient pas « PLUS TARD » |
| Tâches du foyer › À faire | État ne contient pas « PLUS TARD » |
| Accueil › Liste de courses | À racheter = cochée |
| Stock & courses › Liste de courses | À racheter = cochée |

À refaire à la main si une de ces vues est recréée par l'API.

Couvertures : composition centrée dans les 70 % centraux (Notion rogne des deux côtés selon la largeur), URL en `?v=4`.

## Passe UX (11 nov. 2026)

- **Tâches › À faire** : tableau Kanban groupé par la formule État. Colonnes En retard / Aujourd'hui / Cette semaine ; « PLUS TARD » masqué et ordre des colonnes réglés dans l'interface. L'ancien tableau devient l'onglet **Tout** (sans filtre).
- **Bouton « Fait »** (propriété bouton, créée dans l'interface) : Dernière fois = date de déclenchement. Visible dans À faire, Tout, Mes tâches (page Tâches et accueil).
- **Recettes** : couverture de page = étiquette `assets/v2/recettes/*.png` ; aperçu de carte = image de couverture (réglé dans l'interface). Nouvelles formules `Placard` (PRÊT À CUISINER / MANQUE n INGRÉDIENT(S)) et `Durée` (« 45 min »).
- **Repas › Cette semaine** : filtre Date ≥ aujourd'hui OU non cuisiné ; Recette élargie, Cuisiné juste après.
- **Produits** : formule `Reste` (« reste 100 g · seuil 300 g ») affichée dans les listes de courses.
- **Données d'exemple** : dates « Dernière fois » réparties pour 2 tâches en retard et 3 aujourd'hui au 11 nov. 2026.

À surveiller : les dates d'exemple sont figées. Un acheteur qui duplique le modèle plus tard verra tout en retard. À traiter avant la mise en vente (ex. étape « Remettre à zéro » dans Démarrer).

## Passe UX 2 (11 nov. 2026)

- **Kanban À faire** : couleur conditionnelle (interface) — cartes rouges si État contient « EN RETARD », jaunes si « AUJOURD'HUI ».
- **Repas** : nouvelle vue liste « Cette semaine » en premier onglet ; l'ancien tableau devient « Tableau ». Accueil « Au menu » : Repas, Recette, Cuisiné.
- **Recettes** : couverture = type (`assets/v2/types/*.png`, couleur alignée sur l'option Notion) ; la carte montre Recette, Placard, Durée. Tri alphabétique pour mélanger les couleurs.
- **Encadrés** raccourcis à une phrase (Tâches, Repas, Stock, Préparer ma semaine).
- **Couvertures v6** : titre centré dans les 36 % du milieu (zone visible sur téléphone), étiquettes réparties de chaque côté, remontées pour ne pas toucher l'icône.
- **Accueil** : les 4 liens passent en 2 × 2.
- Vérifié en mode clair et en largeur 420 px.
