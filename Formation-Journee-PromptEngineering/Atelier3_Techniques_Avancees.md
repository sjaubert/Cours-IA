![Logo Pôle Formation UIMM-CVDL](logo_uimm_placeholder.jpg)

# Pôle Formation UIMM-CVDL

---

# ATELIER 3 : Techniques de Prompting Avancées

## Durée : 1h30

---

## Objectifs Pédagogiques

À la fin de cet atelier, les participants seront capables de :

- Différencier les 4 techniques principales : Zero-Shot, Few-Shot, Chain-of-Thought, Prompt Chaining
- Choisir la technique adaptée selon la complexité de la tâche
- Appliquer le Few-Shot Learning avec des exemples efficaces
- Guider le raisonnement de l'IA avec Chain-of-Thought
- Décomposer une tâche complexe en chaîne de prompts

---

## Introduction (10 min)

### Mise en Situation

**Question au groupe** :
> "Vous demandez à un collègue de faire un rapport. Deux approches :
>
> - A) 'Fais-moi un rapport sur la production'
> - B) 'Voici 2 rapports que j'ai faits le mois dernier [exemples]. Fais-moi le même format pour les données de cette semaine.'
>
> Laquelle donnera le meilleur résultat ?"

**→ C'est exactement le principe du Few-Shot !**

### Vue d'Ensemble des Techniques

```
COMPLEXITÉ DE LA TÂCHE
  │
  │   [Prompt Chaining]     ← Projet multi-étapes
  │          ▲
  │   [Chain-of-Thought]    ← Raisonnement complexe
  │          ▲
  │   [Few-Shot]            ← Qualité et format précis
  │          ▲
  │   [Zero-Shot]           ← Tâche simple et directe
  │
  └────────────────────────────────────────────▶
                EFFORT DE CRÉATION DU PROMPT
```

---

## PARTIE 1 : Zero-Shot (Basique mais Perfectible)

### Définition

**Zero-Shot** = Poser une question directe sans exemple ni contexte élaboré.

### Quand l'utiliser ?

OUI - Tâches simples et universelles
OUI - Questions factuelles
OUI - Génération rapide d'idées
OUI - Premières itérations (brouillon)

NON - Formats spécifiques
NON - Tâches nécessitant un raisonnement
NON - Cas métier très spécifiques

### Exemples

#### OUI - Bon Usage (Tâche Simple)

```
Donne-moi 5 idées de titres accrocheurs pour un article sur la transition énergétique.
```

#### NON - Mauvais Usage (Tâche Complexe)

```
Analyse les données de production du trimestre et propose des améliorations.
```

**Problème** : Trop vague, pas de structure, l'IA va deviner le format.

---

### EXERCICE 1 - Zero-Shot : Quand ça marche et quand ça coince (10 min)

#### Instructions

Testez ces 4 prompts Zero-Shot. Pour chacun, notez s'il est **adapté** ou **inadapté**.

**Prompt A** :

```
Explique ce qu'est un diagramme de Pareto.
```

- [ ] Adapté  
- [ ] Inadapté

**Prompt B** :

```
Rédige un rapport d'incident de sécurité pour notre usine.
```

- [ ] Adapté  
- [ ] Inadapté

**Prompt C** :

```
Traduis "machine learning" en français.
```

- [ ] Adapté  
- [ ] Inadapté

**Prompt D** :

```
Crée un plan de formation complet sur la maintenance préventive.
```

- [ ] Adapté  
- [ ] Inadapté

#### Correction

- **A** → OUI - Adapté (définition simple et universelle)
- **B** → NON - Inadapté (format spécifique, contexte manquant, données absentes)
- **C** → OUI - Adapté (traduction directe)
- **D** → NON - Inadapté (tâche complexe, beaucoup de paramètres à définir)

#### Débrief (3 min)

- Règle générale : Si vous dites "il faudrait que l'IA sache que...", alors Zero-Shot ne suffit pas !

---

## PARTIE 2 : Few-Shot Learning (La Puissance des Exemples)

### Définition

**Few-Shot** = Donner 1 à 3 exemples pour montrer exactement ce que vous attendez.

### Pourquoi c'est si efficace ?

L'IA apprend **par imitation**. Un exemple vaut mieux que 10 lignes d'explication.

### Structure Typique

```
Tâche : [Description]

Exemple 1 :
Entrée : [...]
Sortie attendue : [...]

Exemple 2 :
Entrée : [...]
Sortie attendue : [...]

Maintenant, fais la même chose pour :
Entrée : [nouvelle situation]
```

---

### Exemple Comparatif : Traduction d'Expressions

#### NON - Zero-Shot (Résultat Moyen)

```
Traduis cette expression anglaise en français : "Break the ice"
```

**Réponse possible** : "Casser la glace" ← Littéral, pas idiomatique !

#### OUI - Few-Shot (Résultat Excellent)

```
Tâche : Traduire des expressions idiomatiques anglaises en leur équivalent français idiomatique.

Exemple 1 :
Anglais : "It's raining cats and dogs"
Français : "Il pleut des cordes"

Exemple 2 :
Anglais : "Piece of cake"
Français : "Un jeu d'enfant"

Maintenant traduis :
Anglais : "Break the ice"
```

**Réponse attendue** : "Briser la glace" / "Détendre l'atmosphère"

---

### EXERCICE 2 - Few-Shot : Créer des Exemples Efficaces (20 min)

#### Scénario

Vous recevez régulièrement des emails de fournisseurs avec des formats variés. Vous voulez que l'IA extraie toujours les mêmes informations : **nom du fournisseur, produit, quantité, prix unitaire, délai de livraison**.

#### Partie A : Prompts sans Exemples (5 min)

**Consigne** : Écrivez un prompt Zero-Shot pour cette tâche.

#### Partie B : Amélioration Few-Shot (15 min)

**Étape 1** : Créez 2 exemples d'emails avec les données extraites dans le format souhaité.

**Email Exemple 1** :

```
Bonjour,
Suite à votre demande, nous pouvons vous fournir :
- Roulements SKF réf. 6205
- Quantité : 500 unités
- Prix : 12,50€ HT/unité
Livraison sous 3 semaines.
Cordialement,
Jean Dupont - TechSupply
```

**Extraction Attendue** :

```
| Fournisseur | Produit | Quantité | Prix Unitaire | Délai |
|-------------|---------|----------|---------------|-------|
| TechSupply  | Roulements SKF réf. 6205 | 500 | 12,50€ HT | 3 semaines |
```

**Email Exemple 2** :

```
Madame, Monsieur,
Nous confirmons disponibilité immédiate pour vis CHC M8x40 (inox A2).
Stock : 10000 pièces. Tarif unitaire 0,85 EUR HT.
Expédition J+5.
Bien à vous,
Sophie Martin - BoulonExpress
```

**Extraction Attendue** :

```
| Fournisseur | Produit | Quantité | Prix Unitaire | Délai |
|-------------|---------|----------|---------------|-------|
| BoulonExpress | Vis CHC M8x40 (inox A2) | 10000 | 0,85€ HT | 5 jours |
```

**Étape 2** : Rédigez le prompt Few-Shot complet

#### Corrigé

```
Tâche : Extraire les informations fournisseur d'emails commerciaux.

FORMAT DE SORTIE : Tableau avec ces colonnes exactes :
| Fournisseur | Produit | Quantité | Prix Unitaire | Délai |

EXEMPLE 1 :
Email reçu :
"Bonjour,
Suite à votre demande, nous pouvons vous fournir :
- Roulements SKF réf. 6205
- Quantité : 500 unités
- Prix : 12,50€ HT/unité
Livraison sous 3 semaines.
Cordialement,
Jean Dupont - TechSupply"

Extraction :
| Fournisseur | Produit | Quantité | Prix Unitaire | Délai |
|-------------|---------|----------|---------------|-------|
| TechSupply  | Roulements SKF réf. 6205 | 500 | 12,50€ HT | 3 semaines |

EXEMPLE 2 :
[Insérer exemple 2]

Maintenant, extrait les informations de cet email :
[Nouvel email à traiter]
```

#### Mise en Commun

- Quels exemples avez-vous choisis ?
- Pourquoi 2 exemples plutôt qu'un seul ? (Variété des formats)
- Combien d'exemples faut-il ? **Règle empirique : 2-3 exemples suffisent généralement**

---

## PARTIE 3 : Chain-of-Thought (CoT) - Guider le Raisonnement

### Définition

**Chain-of-Thought** = Demander à l'IA de "raisonner étape par étape" avant de donner la réponse finale.

### Pourquoi c'est crucial ?

L'IA a tendance à "sauter" aux conclusions. En la forçant à expliciter son raisonnement, on obtient :

- OUI - Réponses plus précises
- OUI - Moins d'erreurs logiques
- OUI - Traçabilité du raisonnement (on peut vérifier)

### La Phrase Magique
>
> **"Réfléchis étape par étape avant de répondre."**
> Ou : **"Procède par étapes : 1) ... 2) ... 3) ..."**

---

### Exemple Comparatif : Problème de Logique

#### NON - Sans CoT (Erreur Probable)

```
Une équipe de 8 opérateurs travaille sur une ligne. Chaque opérateur produit 15 pièces/heure. 
La ligne fonctionne 7h/jour. Deux opérateurs sont absents aujourd'hui.
Combien de pièces seront produites aujourd'hui ?
```

**Réponse IA sans CoT** : "840 pièces" NON - (erreur : a oublié les absents)

---

#### OUI - Avec CoT (Réponse Correcte)

```
Une équipe de 8 opérateurs travaille sur une ligne. Chaque opérateur produit 15 pièces/heure. 
La ligne fonctionne 7h/jour. Deux opérateurs sont absents aujourd'hui.
Combien de pièces seront produites aujourd'hui ?

**Réfléchis étape par étape avant de donner la réponse finale.**
```

**Réponse IA avec CoT** :

```
Étape 1 : Nombre d'opérateurs présents = 8 - 2 = 6 opérateurs
Étape 2 : Production par opérateur par jour = 15 pièces/h × 7h = 105 pièces
Étape 3 : Production totale = 6 opérateurs × 105 pièces = 630 pièces

Réponse finale : 630 pièces seront produites aujourd'hui.
```

---

### EXERCICE 3 - Chain-of-Thought : Problèmes Complexes (20 min)

#### Problème 1 : Planification (10 min)

**Scénario** :
Vous devez organiser une formation de 2 jours pour 20 personnes. Vous avez :

- 3 salles disponibles : Salle A (capacité 8), Salle B (capacité 12), Salle C (capacité 6)
- 4 formateurs : Alice (disponible jour 1 matin), Bob (disponible jour 2), Clara (disponible tout le temps), David (disponible jour 1 après-midi et jour 2 matin)
- Contrainte : Maximum 3 sessions simultanées
- Contrainte : Chaque participant doit assister à 4 sessions de 3h (2 par jour)

**Question** : Proposez un planning réalisable.

**Instructions** :

1. Écrivez d'abord un prompt SANS Chain-of-Thought
2. Puis réécrivez-le AVEC Chain-of-Thought en guidant les étapes de raisonnement

#### Exemple de Prompt CoT

```
[Copier le scénario ci-dessus]

Procède par étapes pour créer le planning :

Étape 1 : Liste les contraintes fermes (disponibilités formateurs, capacités salles)
Étape 2 : Calcule le nombre total de sessions nécessaires (20 personnes × 4 sessions / capacité moyenne)
Étape 3 : Répartis les sessions sur les 2 jours en respectant les disponibilités
Étape 4 : Assigne les salles en optimisant les capacités
Étape 5 : Vérifie qu'aucune contrainte n'est violée
Étape 6 : Présente le planning final sous forme de tableau

Format de sortie :
[Jour] [Horaire] [Salle] [Formateur] [Nombre de participants]
```

---

#### Problème 2 : Analyse de Données (10 min)

**Scénario** :
Voici les données de production d'une semaine :

- Lundi : 450 pièces (8 opérateurs)
- Mardi : 380 pièces (8 opérateurs)
- Mercredi : 520 pièces (9 opérateurs, heures sup)
- Jeudi : 410 pièces (7 opérateurs, 1 absent)
- Vendredi : 390 pièces (8 opérateurs)

**Question** : Identifie les anomalies et explique-les.

**Consigne** : Créez un prompt avec Chain-of-Thought qui guide l'analyse.

#### Exemple de Structure

```
Analyse ces données de production.

Procède en 4 étapes :
1. Calcule la production moyenne par opérateur pour chaque jour
2. Identifie les jours avec des écarts significatifs (>10% de la moyenne)
3. Corrèle les écarts avec les événements (absences, heures sup)
4. Formule des hypothèses explicatives

Présente sous forme :
| Jour | Production/opérateur | Écart à la moyenne | Explication probable |
```

---

## PARTIE 4 : Prompt Chaining (La Décomposition Stratégique)

### Définition

**Prompt Chaining** = Découper une tâche complexe en une **séquence de prompts simples**, où chaque sortie devient l'entrée du suivant.

### Analogie

Construire une maison :

- NON - Un seul prompt : "Construis-moi une maison"
- OUI - Chaining :
  1. "Dessine les plans"
  2. "À partir de ces plans, liste les matériaux nécessaires"
  3. "Avec cette liste, estime le budget"
  4. "Crée le planning de construction basé sur le budget"

---

### Exemple Guidé : Création d'un Module de Formation

#### Tâche Globale

Créer un module de formation complet sur "L'utilisation d'un pied à coulisse" pour des apprentis.

#### Approche Zero-Shot (NON - Résultat Médiocre)

```
Crée un module de formation complet sur l'utilisation d'un pied à coulisse.
```

**Problème** : Trop vague, l'IA va improviser la structure, le niveau, le format...

---

#### Approche Prompt Chaining (OUI - Résultat Professionnel)

**Prompt 1 : Définir les Objectifs Pédagogiques**

```
Tu es un formateur technique.
Tâche : Définis 5 objectifs pédagogiques SMART pour un module de formation 
sur "L'utilisation du pied à coulisse".
Public : Apprentis en première année (niveau CAP).
Durée : 2 heures (1h théorie + 1h pratique).

Format : 
Pour chaque objectif, utilise la formule "À la fin de ce module, l'apprenant sera capable de..."
```

**Sortie attendue** :

```
1. À la fin de ce module, l'apprenant sera capable de nommer les 3 parties principales du pied à coulisse.
2. À la fin de ce module, l'apprenant sera capable de mesurer une pièce avec une précision de ±0,1 mm.
[...]
```

---

**Prompt 2 : Structurer le Contenu (utilise la sortie du Prompt 1)**

```
À partir de ces objectifs pédagogiques :
[Copier-coller les 5 objectifs]

Crée un plan de séquence détaillé pour 2 heures.

Structure :
| Séquence | Durée | Activité | Modalité (théorie/pratique) | Objectif visé |

Contraintes :
- Alterner théorie et pratique
- Progression du simple au complexe
- Inclure une évaluation finale (10 min)
```

---

**Prompt 3 : Créer les Supports (utilise la sortie du Prompt 2)**

```
À partir de ce plan de séquence :
[Copier-coller le tableau]

Crée le support de présentation pour la partie théorique (séquences 1 à 3).

Format : 
Pour chaque slide :
- Titre
- Contenu (max 3 bullet points)
- Illustration suggérée

Contraintes :
- Langage simple (niveau CAP)
- Analogies avec des objets du quotidien
```

---

**Prompt 4 : Concevoir les Exercices Pratiques**

```
À partir des objectifs 2 et 4 :
[Copier-coller les objectifs]

Crée 3 exercices pratiques progressifs.

Pour chaque exercice :
- Consigne pour l'apprenant
- Pièce à mesurer (description ou schéma)
- Critère de réussite
- Temps alloué

Niveau : Facile → Moyen → Difficile
```

---

**Prompt 5 : Élaborer l'Évaluation Finale**

```
Crée un QCM de 10 questions pour valider les 5 objectifs pédagogiques :
[Copier-coller les objectifs]

2 questions par objectif.
Format : Question + 4 réponses (1 seule correcte) + justification brève.
Niveau : 70% de réussite attendu.
```

---

### EXERCICE 4 - Prompt Chaining : À Vous de Jouer ! (25 min)

#### Mission

Vous devez créer un **guide complet d'onboarding** pour un nouveau collaborateur dans votre service.

#### Votre Tâche

Concevez une **chaîne de 4 à 6 prompts** pour générer ce guide de manière structurée.

#### Étapes Suggérées (Exemples)

1. Identifier les informations essentielles à transmettre
2. Structurer le guide (table des matières)
3. Rédiger la section "Premier jour"
4. Créer la checklist des outils/accès nécessaires
5. Concevoir un planning des 30 premiers jours
6. Élaborer un quiz de validation (fin de période d'essai)

#### Instructions

**Travail en binôme** (15 min) :

1. Choisissez le contexte : quel service ? Quel type de poste ?
2. Définissez les 4-6 prompts de votre chaîne
3. Rédigez au moins les 3 premiers prompts en détail

**Présentation** (10 min) :

- 3 binômes présentent leur chaîne (2-3 min chacun)
- Le groupe identifie les points forts de chaque approche

#### Grille d'Analyse

**Pour évaluer une chaîne de prompts :**

- [ ] Chaque prompt a un objectif clair et unique
- [ ] La sortie d'un prompt peut servir d'entrée au suivant
- [ ] L'ordre des prompts est logique (dépendances respectées)
- [ ] Chaque prompt est "exécutable" indépendamment si besoin
- [ ] Le découpage simplifie vraiment la tâche (vs. un gros prompt monolithique)

---

## Tableau Comparatif : Quelle Technique Pour Quelle Situation ?

| Technique | Complexité | Temps de Préparation | Qualité du Résultat | Cas d'Usage Idéal |
|-----------|-----------|---------------------|---------------------|-------------------|
| **Zero-Shot** | Faible | <1 min | 65% | Questions simples, brainstorming, définitions |
| **Few-Shot** | Moyenne | 3-5 min | 85% | Formats spécifiques, tâches répétitives, extraction de données |
| **Chain-of-Thought** | Élevée | 2-3 min | 90% | Calculs, analyses, décisions complexes, diagnostics |
| **Prompt Chaining** | Très élevée | 10-20 min | 95% | Projets multi-étapes, création de contenus élaborés |

---

## QUIZ DE SYNTHÈSE (10 min)

**Question 1** : Pour extraire 50 adresses email d'une liste hétérogène, quelle technique est LA PLUS adaptée ?

- A) Zero-Shot
- B) Few-Shot OUI - (montrer 2-3 formats d'extraction)
- C) Chain-of-Thought
- D) Prompt Chaining

---

**Question 2** : Vous devez résoudre un problème de logistique avec plusieurs contraintes interdépendantes. Quelle technique privilégier ?

- A) Zero-Shot
- B) Few-Shot
- C) Chain-of-Thought OUI - (forcer le raisonnement étape par étape)
- D) Prompt Chaining

---

**Question 3** : Vous créez une campagne marketing complète (personas → messages → visuels → calendrier). Quelle approche ?

- A) Zero-Shot
- B) Few-Shot
- C) Chain-of-Thought
- D) Prompt Chaining OUI - (décomposition en séquence logique)

---

**Question 4** : Combien d'exemples faut-il typiquement pour du Few-Shot ?

- A) 1 exemple suffit toujours
- B) 2-3 exemples OUI - (compromis efficacité/effort)
- C) Au moins 10 exemples
- D) Ça ne sert à rien, mieux vaut tout expliquer par du texte

---

**Question 5** : La phrase "Réfléchis étape par étape" améliore surtout :

- A) La vitesse de réponse
- B) La créativité
- C) La précision du raisonnement OUI - - D) Le style d'écriture

---

## Aide-Mémoire : "Choisir Sa Technique"

### Arbre de Décision

```
┌─────────────────────────────────────┐
│  Ma tâche est-elle SIMPLE ?         │
│  (définition, traduction, idées...) │
└─────────┬───────────────────────────┘
          │
      OUI │           NON
          ▼              ▼
   ┌──────────┐    ┌──────────────────────────┐
   │Zero-Shot │    │ Ai-je un FORMAT précis ? │
   └──────────┘    └───────┬──────────────────┘
                           │
                       OUI │           NON
                           ▼              ▼
                     ┌──────────┐   ┌──────────────────────────────┐
                     │Few-Shot  │   │ Tâche nécessite RAISONNEMENT │
                     │+exemples │   │ ou CALCULS ?                  │
                     └──────────┘   └───────┬──────────────────────┘
                                            │
                                        OUI │           NON
                                            ▼              ▼
                                    ┌──────────────┐  ┌─────────────┐
                                    │Chain-of-     │  │Tâche MULTI- │
                                    │Thought       │  │ÉTAPES ?     │
                                    └──────────────┘  └──────┬──────┘
                                                             │
                                                         OUI │
                                                             ▼
                                                      ┌─────────────┐
                                                      │Prompt       │
                                                      │Chaining     │
                                                      └─────────────┘
```

---

## Transition vers Atelier 4

> "Vous maîtrisez maintenant les techniques avancées. Il est temps de les appliquer à **vos cas d'usage métier réels**. Dans l'atelier suivant, vous travaillerez en groupe sur des scénarios professionnels concrets."

---

## Notes pour le Formateur

### Timing Serré - Points de Contrôle

- 10:00 → Fin Introduction
- 10:20 → Fin Zero-Shot + Exercice 1
- 10:50 → Fin Few-Shot + Exercice 2
- 11:20 → Fin Chain-of-Thought + Exercice 3
- 11:40 → Fin Prompt Chaining + Exercice 4
- 11:50 → Quiz de synthèse

**Si retard** :

- Exercice 4 peut être donné "à finir pendant la pause"
- Quiz peut être fait pendant le déjeuner (version Kahoot sur smartphone)

### Messages Clés à Marteler

1. **Few-Shot = La technique la plus rentable** (peu d'effort, gros gain de qualité)
2. **CoT = Obligatoire pour calculs/logique** (sinon erreurs quasi garanties)
3. **Chaining = Pour éviter le prompt "usine à gaz"** (découper pour mieux régner)

### Matériel

- OUI - Slides avec exemples comparatifs Avant/Après
- OUI - Exercices imprimés (ou accès IA en direct si possible)
- OUI - Tableau/paperboard pour l'arbre de décision
- OUI - Chronomètre pour exercices chronométrés
- OUI - Aide-mémoire à distribuer

### Adaptation Selon Public

- **Si techniciens/ingénieurs** : Insister sur CoT (ils adorent le raisonnement structuré)
- **Si commerciaux/RH** : Insister sur Few-Shot (formats répétitifs)
- **Si managers** : Insister sur Chaining (projets complexes)

### Moment Fort

L'exercice Few-Shot (extraction d'emails) est souvent le "déclic" : les participants réalisent qu'un bon exemple vaut mieux que 10 lignes d'explication.

---

*Créé par S. JAUBERT - Pôle Formation UIMM CVDL*
