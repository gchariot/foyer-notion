# DESIGN.md — Foyer, système « L'étiqueteuse »

Le contrat de direction est dans [docs/design/direction.md](docs/design/direction.md). Les visuels sont dans `assets/v2/` et se régénèrent avec `python3 assets/v2/generate.py`. Il faut pour cela `rsvg-convert` et la police Barlow Condensed (OFL) installée localement.

## Matières

- **Fond :** carton kraft #C3A47C, avec un grain de fibres (SVG feTurbulence). Il est réservé aux couvertures et aux images de recettes. Les pages Notion restent sur le fond natif.
- **Rubans :** plastique d'étiqueteuse. Chaque ruban porte un léger reflet en haut et une ombre portée de 5 px.

## Couleurs de ruban (rôle → hex → couleur Notion native)

| Rôle | Ruban | Notion |
| --- | --- | --- |
| Foyer, structure, réserve | Noir #1D1D1B | default |
| Tâches, urgence, en retard | Rouge #D7262B | red |
| Stock | Bleu #1F4E9B | blue |
| Repas | Vert #1E7A46 | green |
| À racheter, aujourd'hui | Jaune #F2C230 (lettres noires) | yellow |
| Secondaire, coulisses | Gris #5B5B5B | gray |

Dans Notion, on n'utilise que ces six couleurs pour les sélections. Pas d'orange, de marron, de rose ni de violet.

## Typographie

- **Dans les images :** Barlow Condensed 800, en capitales. Les lettres sont gaufrées : un contre-jour noir à +1,6 px et un reflet blanc à −1 px. La ligne de base varie de ±3 % de la taille des lettres, pour imiter une vraie étiqueteuse. L'interlettrage vaut 0,16 em.
- **Dans Notion :** la police par défaut. L'état des tâches s'affiche en capitales grasses colorées, avec `style()` dans la formule.

## Composants

- **Couverture** (1500 × 600) : une grande étiquette à gauche, entre 96 et 150 px de haut. En dessous, une rangée de petites étiquettes de 44 px, espacées de 28 px. En option, une étiquette d'accent en haut à droite. Tout tient en dessous de x = 1460.
- **Icône** (280 × 280) : une pastille de ruban avec une lettre ou un chiffre (F, T, S, R, 7, 1, C).
- **Titre de section** (1600 × 170, transparent) : un ruban de 78 px aligné à gauche. Il remplace les titres H3 sur les pages.
- **Couverture de recette** (800 × 500) : du kraft avec une seule étiquette au nom du plat, inclinée de −2°.
- **Encadré** : fond `gray_bg` et icône-pastille. Jamais d'émoji.

## Interdits

- Émojis comme icônes, y compris dans les onglets de vues et sur les pages de base.
- Pastels, fond crème, illustrations naïves.
- Encadrés colorés autres que gris.
