![Logo Pôle Formation UIMM-CVDL](logo_uimm_placeholder.jpg)

# Pôle Formation UIMM-CVDL

---

# CORRIGÉS - Atelier 1 : Les 6 Piliers d'un Prompt Parfait

## Usage de ce Document

Ce document contient les **corrigés détaillés** de tous les exercices de l'Atelier 1. Il est destiné **uniquement au formateur** pour :

- Préparer la session
- Guider la correction collective
- Avoir des exemples de réponses attendues
- Adapter les corrigés selon le public

---

## EXERCICE FLASH : Trouver le Bon Rôle (2 min)

### Énoncé

Trouvez le bon rôle pour expliquer la cybersécurité à :

1. Des dirigeants d'entreprise
2. Des développeurs juniors
3. Des enfants de 10 ans

### Corrigé Proposé

**1. Pour des dirigeants d'entreprise :**

```
Tu es un consultant en cybersécurité spécialisé dans la gestion des risques.
Tu t'adresses à des dirigeants d'entreprise pour les sensibiliser 
aux enjeux stratégiques et financiers de la cybersécurité.
```

**Points clés :**

- Vocabulaire business (ROI, risques, conformité)
- Angle stratégique, pas technique
- Chiffrage des risques et des investissements

**2. Pour des développeurs juniors :**

```
Tu es un développeur sénior expert en sécurité applicative.
Tu formes des développeurs juniors aux bonnes pratiques de développement sécurisé.
```

**Points clés :**

- Vocabulaire technique adapté (authentification, injection SQL, XSS)
- Exemples de code
- Approche pratique et concrète

**3. Pour des enfants de 10 ans :**

```
Tu es un éducateur spécialisé en médiation numérique.
Tu expliques la cybersécurité à des enfants de 10 ans de manière ludique 
et accessible, en utilisant des comparaisons avec leur quotidien.
```

**Points clés :**

- Langage simple, pas de jargon
- Métaphores et analogies (la maison avec des serrures)
- Exemples concrets de leur vie (mots de passe, réseaux sociaux)

---

## EXERCICE : Transformer des Tâches Vagues

### Énoncé

Transformez ces tâches vagues en tâches précises :

1. "Dis-moi des choses sur la qualité" → ?
2. "Aide-moi avec mon rapport" → ?

### Corrigé Proposé

**1. "Dis-moi des choses sur la qualité"**

**Version Précise :**

```
Rédige une liste de 5 principes fondamentaux de la qualité industrielle,
en expliquant chacun en 2-3 phrases avec un exemple concret d'application 
dans l'industrie automobile.
```

**Amélioration apportée :**

- Verbe d'action précis : "Rédige une liste"
- Quantité définie : 5 principes
- Format clair : liste avec explications
- Contexte précisé : industrie automobile

**2. "Aide-moi avec mon rapport"**

**Version Précise :**

```
Analyse ce rapport de production et synthétise-le en un résumé exécutif 
de 200 mots maximum, structuré en 3 sections : 
- Faits principaux
- Problèmes identifiés
- Recommandations d'action
```

**Amélioration apportée :**

- Verbe d'action : "Analyse" et "Synthétise"
- Contrainte quantitative : 200 mots maximum
- Format structuré : 3 sections définies
- Objectif clair : résumé exécutif

---

## EXERCICE PRATIQUE 1 : Identifier les Piliers Manquants (15 min)

### Prompt A : Email de Changement de Planning

**Énoncé :**

```
Rédige un email pour informer l'équipe du changement de planning.
```

### Grille d'Analyse - Corrigé

| Pilier | Présent ? | Justification |
|--------|-----------|---------------|
| **Rôle & Contexte** | ❌ NON | Pas de rôle défini, pas de contexte professionnel |
| **Objectif Précis** | ❌ NON | "Informer" est trop vague, quel est le but réel ? |
| **Tâche Claire** | ✅ OUI | "Rédige un email" est clair |
| **Contraintes** | ❌ NON | Pas de ton, longueur, public défini |
| **Format & Exemples** | ❌ NON | Structure de l'email non précisée |
| **Étapes Critiques** | ❌ NON | Non nécessaire pour cette tâche simple |

**Score : 1/6** (très incomplet)

**Version Améliorée :**

```
Tu es le responsable d'équipe dans une entreprise industrielle.
Objectif : Informer l'équipe du changement d'horaire de la réunion hebdomadaire
          sans créer de confusion ni mécontentement.
Tâche : Rédige un email professionnel.

Contraintes :
- Ton : professionnel mais chaleureux
- Longueur : maximum 150 mots
- Préciser ancien ET nouvel horaire
- Expliquer la raison du changement

Format :
- Objet clair
- Salutation
- 3 paragraphes (raison, changement, action attendue)
- Formule de politesse
```

---

### Prompt B : Présentation 5S

**Énoncé :**

```
Tu es le responsable qualité d'une usine automobile.
Objectif : Expliquer l'importance du 5S aux nouveaux opérateurs.
Tâche : Crée une présentation de 5 slides.
Public : Opérateurs débutants (formation initiale).
Format : Pour chaque S, donne 1 définition + 1 exemple concret de l'atelier.
Contraintes : Langage simple, exemples visuels.
```

### Grille d'Analyse - Corrigé

| Pilier | Présent ? | Justification |
|--------|-----------|---------------|
| **Rôle & Contexte** | ✅ OUI | "Responsable qualité d'une usine automobile" |
| **Objectif Précis** | ✅ OUI | "Expliquer l'importance du 5S" |
| **Tâche Claire** | ✅ OUI | "Crée une présentation de 5 slides" |
| **Contraintes** | ✅ OUI | "Langage simple, exemples visuels" |
| **Format & Exemples** | ✅ OUI | Structure précise : 1 définition + 1 exemple par S |
| **Étapes Critiques** | ❌ NON | Non nécessaire (tâche assez simple) |

**Score : 5/6** (excellent prompt !)

**Point d'amélioration possible :**
On pourrait ajouter une contrainte de temps : "Présentation pour 15 minutes"

---

### Prompt C : Analyse de Données

**Énoncé :**

```
Analyse ces données de production et dis-moi ce qui ne va pas.
Fais ça méthodiquement.
```

### Grille d'Analyse - Corrigé

| Pilier | Présent ? | Justification |
|--------|-----------|---------------|
| **Rôle & Contexte** | ❌ NON | Pas de rôle, pas de contexte |
| **Objectif Précis** | ❌ NON | "Ce qui ne va pas" est trop vague |
| **Tâche Claire** | 🟡 PARTIEL | "Analyse" est OK, mais "dis-moi" est faible |
| **Contraintes** | ❌ NON | Aucune contrainte définie |
| **Format & Exemples** | ❌ NON | Format de sortie non précisé |
| **Étapes Critiques** | 🟡 PARTIEL | "Méthodiquement" suggère des étapes mais ne les définit pas |

**Score : 1/6** (très incomplet)

**Version Améliorée :**

```
Tu es un ingénieur méthodes expert en analyse de production.
Contexte : Usine automobile, ligne de montage, objectif : identifier les goulets d'étranglement.

Objectif : Identifier les 3 principales anomalies dans ces données de production
          et proposer des actions correctives prioritaires.

Tâche : Analyse ces données de production [données ici]

Contraintes :
- Approche factuelle, basée sur les chiffres
- Focus sur les écarts > 10% par rapport à la norme

Format de sortie :
| Anomalie | Impact Chiffré | Cause Probable | Action Recommandée | Priorité |

Étapes d'analyse :
1. Calcule d'abord les écarts par rapport aux objectifs
2. Identifie les 3 écarts les plus importants
3. Propose une hypothèse de cause racine pour chacun
4. Recommande une action concrète et chiffrée
```

---

## JEU : "Le Constructeur de Prompt" (15 min)

### Scénarios avec Corrigés Types

#### Scénario 1 : Procédure de Maintenance Machine CNC

**Prompt Complet Attendu :**

```
RÔLE & CONTEXTE :
Tu es un technicien de maintenance industrielle expert en machines CNC.
Tu t'adresses à des opérateurs de niveau CAP/BAC PRO.

OBJECTIF :
Permettre aux opérateurs de réaliser la maintenance préventive de 1er niveau
pour éviter les pannes et prolonger la durée de vie de la machine.

TÂCHE :
Rédige une procédure de maintenance préventive hebdomadaire pour une fraiseuse CNC.

CONTRAINTES :
- Langage simple, pas de jargon technique
- Temps d'exécution : 30 minutes maximum
- Pas d'intervention mécanique complexe (maintenance de niveau 1 uniquement)
- Sécurité : rappeler les EPI obligatoires

FORMAT :
Tableau en 4 colonnes :
| Étape | Action à Réaliser | Contrôle/Vérification | Fréquence |

Ajouter une section "Points d'Attention Sécurité" en début de procédure.

ÉTAPES :
1. Liste les 6-8 points de contrôle essentiels
2. Organise-les dans l'ordre logique d'intervention
3. Pour chaque point, précise l'action ET le critère de validation
4. Termine par les consignes de traçabilité
```

---

#### Scénario 2 : Quiz de Validation en Fin de Formation

**Prompt Complet Attendu :**

```
RÔLE & CONTEXTE :
Tu es un formateur technique spécialisé en pédagogie active.
Public : Participants à une formation sur la sécurité au travail (niveau débutant).

OBJECTIF :
Évaluer la compréhension des participants et identifier les points à revoir
avant la fin de la formation.

TÂCHE :
Crée un quiz de validation de 10 questions sur les bases de la sécurité au travail.

CONTRAINTES :
- Format : QCM avec 4 propositions (1 seule bonne réponse)
- Difficulté : accessible mais pas évidente (éviter le trop facile)
- Couvrir 4 thèmes : EPI, risques chimiques, gestes et postures, incendie
- Mélanger niveaux de cognition (connaissance + compréhension + application)

FORMAT :
Pour chaque question :
Question X : [Énoncé clair]
A) [Proposition 1]
B) [Proposition 2]
C) [Proposition 3]
D) [Proposition 4]
Réponse correcte : [Lettre] - [Explication en 1 phrase]

ÉTAPES :
1. Répartis les 10 questions équitablement sur les 4 thèmes
2. Varie les types de questions (définition, cas pratique, identification d'erreur)
3. Pour chaque question, vérifie qu'une seule réponse est clairement correcte
4. Justifie chaque bonne réponse pour faciliter le débriefing
```

---

## QUIZ FINAL - Corrigé Commenté

### Question 1 : Lequel N'EST PAS un des 6 piliers ?

**Réponse : B) Budget disponible**

**Explication pédagogique :**
Le budget n'est pas un pilier de la construction d'un prompt. Les 6 piliers sont :

1. Rôle & Contexte
2. Objectif Précis
3. Tâche Claire
4. Contraintes
5. Format & Exemples
6. Étapes Critiques

Le budget peut être une **contrainte** dans certains cas (ex: "Solutions à moins de 10 000€"), mais ce n'est pas un pilier structurant.

---

### Question 2 : Pourquoi donner un rôle à l'IA ?

**Réponse : B) Ça adapte le vocabulaire et la profondeur de la réponse**

**Explication pédagogique :**
Le rôle permet à l'IA de :

- Adapter son **vocabulaire** (technique vs vulgarisé)
- Ajuster le **niveau de détail** (expert vs débutant)
- Choisir le **ton** approprié (formel vs pédagogique)

Exemple concret :

- "Expert comptable" → termes techniques, normes IFRS
- "Éducateur pour enfants" → métaphores, langage simple

---

### Question 3 : Quel verbe est le PLUS précis ?

**Réponse : C) "Rédige un tableau comparatif avec..."**

**Explication pédagogique :**
Les verbes faibles créent de l'ambiguïté :

- ❌ "Pense à..." → Que doit produire l'IA ?
- ❌ "Vois si..." → Résultat attendu flou

Les verbes d'action forts sont **observables** et **mesurables** :

- ✅ Rédige, Liste, Compare, Analyse, Synthétise, Crée, Génère, Classe, Extraie

**Conseil formateur :** Utiliser la taxonomie de Bloom pour choisir les bons verbes d'action.

---

### Question 4 : Les contraintes servent à

**Réponse : B) Cadrer la réponse pour la rendre utilisable**

**Explication pédagogique :**
Sans contraintes, l'IA peut générer :

- Un texte trop long ou trop court
- Un ton inapproprié au contexte
- Un format inadapté au besoin

Les contraintes **cadrent** sans **brider** :

- Longueur → adaptée au support (email vs rapport)
- Ton → adapté au public (client vs collègue)
- Limitations → éviter le hors-sujet

---

### Question 5 : Quand utiliser "Étapes Critiques" ?

**Réponse : C) Pour les tâches complexes nécessitant un raisonnement**

**Explication pédagogique :**
Le pilier "Étapes Critiques" (Chain-of-Thought) est utile pour :

- Calculs complexes
- Analyses multi-critères
- Décisions avec plusieurs facteurs
- Problèmes nécessitant un raisonnement structuré

**Non nécessaire pour :**

- Questions factuelles simples
- Génération de texte créatif
- Tâches très guidées par le format

**Phrase magique :** "Réfléchis étape par étape avant de répondre"

---

## Points de Débriefing pour le Formateur

### Messages Clés à Faire Passer

1. **Les 6 piliers sont un guide, pas une prison**
   - Tous ne sont pas toujours nécessaires
   - S'adapter selon la complexité de la tâche

2. **Le pilier le plus souvent oublié : le Public**
   - Impact énorme sur le vocabulaire et le niveau de détail
   - Toujours se demander : "Pour qui ?"

3. **Le format fait gagner 50% du temps**
   - Un bon exemple vaut mieux que 10 lignes d'explication
   - Montrer plutôt qu'expliquer

4. **Itérer est normal**
   - Le premier prompt n'est jamais parfait
   - Tester → Ajuster → Retester

### Adaptations Selon le Public

**Si public technique (ingénieurs, techniciens) :**

- Insister sur les "Étapes Critiques" (ils adorent la logique)
- Donner des exemples très techniques

**Si public RH/Communication :**

- Insister sur "Rôle & Contexte" et "Ton"
- Exemples liés à leur métier (offres d'emploi, communication interne)

**Si public qualité/méthodes :**

- Focus sur "Contraintes" et "Format"
- Exemples de procédures, checklists, audits

---

## Matériel à Préparer

- [ ] Jeu de cartes "Constructeur de Prompt" imprimé
- [ ] Grilles d'analyse vierges pour Prompt A, B, C
- [ ] Template universel (1 par participant)
- [ ] Quiz imprimé ou version Kahoot prête
- [ ] Exemples de prompts métier adaptés au public

---

*Document à usage exclusif du formateur - Ne pas distribuer aux participants*
