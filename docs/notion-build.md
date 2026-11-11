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
