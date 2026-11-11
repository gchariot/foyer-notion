---
workflowType: 'prd'
status: 'provisoire — V1'
date: '2026-11-11'
inputDocuments: [product-brief.md, research/market-foyer-notion-research-2026-11-11.md]
---

# PRD — Foyer V1 (modèle Notion)

## 1. Objectif

Livrer un modèle Notion duplicable qui fonctionne sur le **plan gratuit**, utilisable à deux (une membre plus un invité), avec trois modules reliés : tâches, stock et courses, repas.

## 2. Contraintes non négociables (NFR)

- **NFR-1 Plan gratuit :** formules, relations et rollups uniquement. Les automatisations sont acceptées seulement si elles sont livrées avec le modèle (les acheteuses du plan gratuit peuvent les utiliser sans les modifier). Elles sont à tester.
- **NFR-2 Partage :** tout le système vit sous une page racine. Le partenaire est invité *en invité* sur cette page, sans devenir membre de l'espace, pour éviter la limite de 1 000 blocs.
- **NFR-3 Mobile :** chaque action fréquente prend moins de 10 secondes sur téléphone (cocher une tâche, marquer un repas cuisiné, ajouter un produit à racheter).
- **NFR-4 Français :** tous les textes sont en français, avec la typographie française (espaces insécables, guillemets « »).
- **NFR-5 Débutants :** un guide « Démarrer en 15 minutes » est intégré, et des données d'exemple peuvent s'effacer en un geste.
- **NFR-6 Pas de dépendance externe :** aucun lien vers un service payant, aucune image hébergée ailleurs.

## 3. Exigences fonctionnelles

### Module A — Tâches du foyer

- **FR-A1** Base « Tâches du foyer » :
  - Tâche (titre), Domaine (sélection), Fréquence (sélection), Responsable (personne), Durée (min) ;
  - Dernière fois (date), Visible (case : tâche invisible), Notes ;
  - formules : Intervalle (jours), Prochaine fois (date), État (En retard / Aujourd'hui / Cette semaine / Plus tard).
- **FR-A2** Environ 80 tâches préremplies sur 9 domaines : Cuisine, Linge, Ménage, Salle de bain, Courses & stock, Administratif, Logement, Extérieur & voiture, Vie de couple & famille.
- **FR-A3** Marquer une tâche faite : renseigner « Dernière fois » à aujourd'hui (puis un bouton « Fait ✓ » en finition manuelle). La prochaine échéance se recalcule toute seule.
- **FR-A4** Vues :
  - « À faire » (triée par prochaine fois) ;
  - « Mes tâches » (filtre Responsable = moi) ;
  - « Par domaine » (tableau Kanban) ;
  - « Répartition » (groupée par responsable, somme des durées) ;
  - « Toutes ».
- **FR-A5** Rappels (à tester) : une automatisation « Envoyer une notification à Responsable » quand une tâche passe « Aujourd'hui ». À défaut, la vue « Aujourd'hui » de l'accueil.

### Module B — Stock et courses

- **FR-B1** Base « Produits » :
  - Produit, Zone (Réserve / Quotidien), Rayon, Enseigne, Unité ;
  - Stock initial, Seuil, Racheté depuis (nombre) ;
  - formules : Stock actuel, À racheter.
- **FR-B2** Décompte automatique : Stock actuel = Stock initial + Racheté − consommé. Le consommé vient des recettes cuisinées dans le menu (chaîne déjà prototypée et testée).
- **FR-B3** Environ 60 produits courants préremplis, plus une liste « Stock 72 h » (recommandation officielle) dans la réserve.
- **FR-B4** Vues :
  - « Liste de courses » (À racheter, groupée par enseigne puis triée par rayon, adaptée au mobile) ;
  - « Réserve » ;
  - « Quotidien » ;
  - « Tout le stock ».
- **FR-B5** Après les courses : augmenter « Racheté depuis », ou mettre à jour le stock initial (procédure dans le guide).

### Module C — Repas

- **FR-C1** Base « Recettes » : Recette, Type (Plat / Batch / Dessert / Petit-déj), Temps (min), Source (URL / livre / maison), Portions, relation Ingrédients.
- **FR-C2** Base « Ingrédients des recettes » : Ligne, relation Recette, relation Produit, Quantité, formule Consommé.
- **FR-C3** Base « Menu de la semaine » : Repas, Date, Moment (Midi / Soir), relation Recette, Qui cuisine (personne), Cuisiné (case).
- **FR-C4** Environ 12 recettes simples de batch cooking préremplies et reliées aux produits.
- **FR-C5** Vues : « Cette semaine » (tableau ou calendrier), « Livre de recettes » (galerie).

### Pages

- **FR-P1** « Aujourd'hui » (accueil) : mes tâches à faire, le menu du jour, la liste de courses, et des liens rapides.
- **FR-P2** « Préparer ma semaine » : checklist du dimanche (10 minutes).
- **FR-P3** « Démarrer en 15 minutes » : dupliquer, inviter le partenaire en invité, renseigner les responsables, effacer les exemples, régler les rappels.
- **FR-P4** « Finitions » (interne, pas livré) : ce qui doit être fait à la main dans l'interface (boutons, filtres sur formules, automatisations).

## 4. Critères d'acceptation clés

- Cocher « Cuisiné » sur un repas fait baisser le stock des produits de la recette et coche « À racheter » sous le seuil (Given/When/Then dans la page de test).
- Changer « Dernière fois » d'une tâche hebdomadaire à aujourd'hui fait passer Prochaine fois à J+7 et l'État à « Plus tard ».
- Le modèle dupliqué dans un espace gratuit vierge fonctionne sans message d'offre payante.
- Un invité peut cocher ses tâches et la liste de courses depuis son téléphone.

## 5. V2 (hors périmètre)

Enfants et bébé, animaux, administratif et papiers (avec échéances annuelles), budget partagé, cadeaux et anniversaires, valises, prompt « assistant de la semaine », version anglaise.
