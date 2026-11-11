---
workflowType: 'ux-design'
status: 'provisoire — ambiance à choisir'
date: '2026-11-11'
inputDocuments: [prd.md, product-brief.md]
---

# Spec UX — Foyer V1

## 1. Principes

1. **Une page, une question.** L'accueil répond à « qu'est-ce que je fais aujourd'hui ? ». Le reste est à un clic.
2. **Le partenaire ne voit que l'essentiel.** Sur mobile : « Mes tâches », « Liste de courses », « Menu ».
3. **Rien à configurer pour commencer.** Les exemples sont préremplis, et le guide tient en 15 minutes.
4. **La chaleur vient de la typographie et des couleurs, pas des émojis partout.** Une icône par page, et c'est tout.

## 2. Parcours

| Moment | Qui | Où | Parcours |
| --- | --- | --- | --- |
| Le matin | Les deux | Téléphone | Aujourd'hui → mes tâches → cocher |
| En cuisine | Celui qui cuisine | Téléphone | Menu de la semaine → recette → cocher « Cuisiné » |
| En magasin | Celui qui fait les courses | Téléphone | Liste de courses (par enseigne) → mettre à jour le stock |
| Dimanche soir | Les deux | Ordinateur | Préparer ma semaine → menus → répartition → courses |
| Premier jour | L'acheteuse | Ordinateur | Démarrer → inviter → effacer les exemples |

## 3. Architecture des pages

```
🏡 Foyer (page racine, partagée en invité)
├── Aujourd'hui (accueil = la page racine elle-même)
├── Préparer ma semaine
├── Tâches du foyer (base)
├── Stock & courses (page : Produits + Liste de courses)
├── Repas (page : Menu de la semaine + Recettes)
├── Démarrer en 15 minutes
└── Coulisses (bases techniques : Ingrédients des recettes)
```

## 4. Ambiances proposées (à choisir)

| | A — « Maison douce » (recommandée) | B — « Carnet minimal » | C — « Cuisine solaire » |
| --- | --- | --- | --- |
| Couverture | Dégradé crème et terracotta | Papier blanc cassé | Jaune moutarde et olive |
| Couleurs des bases | Orange, marron, vert | Gris, défaut | Jaune, vert, rouge |
| Encadrés | Fond orange ou marron clair | Fond gris | Fond jaune |
| Pour qui | Le cœur de cible, chaleureux sans être enfantin | Fans de Notion minimaliste | Plus jeune, « Instagram » |

**Recommandation :** A. Elle colle au vocabulaire « foyer » et « maison », se distingue des modèles pastel roses d'Etsy, et reste lisible en mode sombre.

## 5. Codes couleur fonctionnels

- **État des tâches :** rouge = en retard, orange = aujourd'hui, jaune = cette semaine, gris = plus tard.
- **Zone du stock :** marron = réserve, vert = quotidien.
- **Domaines :** une couleur par domaine, la même dans toutes les vues.

## 6. Mobile

- Vues en **liste** (pas en tableau) pour « Mes tâches » et « Liste de courses ».
- Au maximum 3 propriétés affichées par ligne.
- Liens rapides en haut de l'accueil, pour éviter de faire défiler.

## 7. Visuels de vente (plus tard)

5 captures : accueil, liste de courses sur téléphone, répartition, menu et recettes, guide. Plus une vidéo écran de 20 secondes, sans visage, montrant « je coche cuisiné → le stock baisse ».
