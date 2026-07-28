![Logo Pôle Formation UIMM-CVDL](logo_uimm_placeholder.jpg)

# Pôle Formation UIMM-CVDL

---

# CORRIGÉS - Atelier 3 : Techniques de Prompting Avancées

## Usage de ce Document

Ce document contient les **corrigés détaillés** des exercices de l'Atelier 3 sur les 4 techniques avancées de prompting.

**Destiné uniquement au formateur** pour :

- Comprendre en profondeur chaque technique
- Avoir des exemples concrets de chaque approche
- Guider les participants dans le choix de la bonne technique
- Corriger efficacement les 4 exercices

---

## EXERCICE 1 - Identification du Zero-Shot

### Objectif de l'Exercice

Faire comprendre **quand utiliser** et **quand éviter** le Zero-Shot.

### Cas d'Usage Typiques - Corrigé

**✅ BON pour Zero-Shot :**

1. **Génération rapide d'idées**

```
Donne-moi 10 idées de noms pour une nouvelle gamme de produits 
écologiques dans le secteur automobile.
```

1. **Questions factuelles simples**

```
Quelle est la différence entre ISO 9001 et ISO 14001 ?
```

1. **Définitions**

```
Explique ce qu'est la méthode 5S en 3 phrases simples.
```

**❌ MAUVAIS pour Zero-Shot (trop complexe) :**

1. **Formats spécifiques**

```
Crée une procédure de maintenance.
```

→ Problème : Quel format ? Quelle structure ? L'IA va deviner.

1. **Analyse nécessitant un raisonnement**

```
Analyse ces données de production et propose des améliorations.
```

→ Problème : Pas de méthode d'analyse définie, résultat superficiel.

### Points Pédagogiques

**Message clé :**
> "Zero-Shot = rapide et pratique pour le brouillon, mais rarement suffisant pour du travail de qualité professionnelle."

---

## EXERCICE 2 - Few-Shot : Extraction d'Emails (20 min)

### Scénario

Extraire systématiquement : nom fournisseur, produit, quantité, prix unitaire, délai de livraison depuis des emails variés.

### Corrigé Type - Prompt Few-Shot Complet

```
TÂCHE : Extraire les informations clés des emails de fournisseurs

Tu vas recevoir des emails de fournisseurs avec des formats variés.
Ta mission est d'extraire TOUJOURS les 5 informations suivantes :
- Nom du fournisseur
- Produit
- Quantité
- Prix unitaire
- Délai de livraison

---

EXEMPLE 1 :

Email reçu :
"Bonjour,
Suite à votre demande, nous confirmons la disponibilité de nos roulements SKF réf. 6205.
Nous pouvons vous livrer 500 unités à 12,50€ l'unité.
Délai : 10 jours ouvrés.
Cordialement,
Société MECATECH"

Extraction :
| Fournisseur | Produit | Quantité | Prix Unitaire | Délai |
|-------------|---------|----------|---------------|-------|
| MECATECH | Roulements SKF réf. 6205 | 500 | 12,50€ | 10 jours ouvrés |

---

EXEMPLE 2 :

Email reçu :
"Cher client,
Tarif pour visserie inox M8 : 0,45€ pièce (commande min. 1000 pcs).
Expédition sous 48h.
Bien à vous,
FIXATION PRO"

Extraction :
| Fournisseur | Produit | Quantité | Prix Unitaire | Délai |
|-------------|---------|----------|---------------|-------|
| FIXATION PRO | Visserie inox M8 | 1000 (min.) | 0,45€ | 48h |

---

Maintenant, extrais les informations de cet email :

[EMAIL À TRAITER]
```

### Points Pédagogiques

**Ce que le Few-Shot apporte ici :**

1. **Montre le format de sortie** (tableau) → l'IA sait exactement comment structurer
2. **Gère les variantes de formulation** :
   - "Délai : 10 jours" vs "Expédition sous 48h" → normalisé dans la colonne Délai
   - Prix écrit différemment → toujours dans "Prix Unitaire"
3. **Explicite les cas limites** :
   - Quantité minimum dans Exemple 2 → "1000 (min.)"

**Débriefing Important :**
> "Avec 2-3 bons exemples, vous montrez à l'IA EXACTEMENT ce que vous voulez.
> C'est 10x plus efficace que d'expliquer avec des mots."

### Erreurs Fréquentes à Anticiper

❌ Participants qui donnent 1 seul exemple → pas assez, l'IA manque de pattern
✅ Optimal : 2-3 exemples qui montrent la variété des cas

❌ Exemples trop similaires → l'IA ne généralise pas
✅ Varier les formulations, formats, structures

---

## EXERCICE 3 - Chain-of-Thought : Planification et Analyse (20 min)

### Scénario

Analyser des données de production hebdomadaire et identifier les anomalies.

### Corrigé Type - Prompt avec Chain-of-Thought

```
RÔLE & CONTEXTE :
Tu es un ingénieur méthodes expert en analyse de performance industrielle.
Ligne de production automobile, objectif d'OEE > 85%.

TÂCHE :
Analyse ces données de production de la semaine écoulée et identifie 
les 3 principales anomalies.

DONNÉES :
Ligne 1 :
- Lundi : 450 pièces (objectif 500), 2 arrêts non planifiés (total 45 min)
- Mardi : 480 pièces, 1 arrêt (15 min)
- Mercredi : 520 pièces, 0 arrêt
- Jeudi : 380 pièces, 4 arrêts (total 120 min) ← ANORMAL
- Vendredi : 490 pièces, 1 arrêt (20 min)

Ligne 2 :
- Lundi à Vendredi : moyenne stable à 510 pièces/jour (objectif 500)
- Taux de rebut : 2,5% (objectif < 2%) ← ANORMAL

CONSIGNE CRITIQUE :
**Réfléchis étape par étape avant de proposer les anomalies.**

Procède en 4 étapes :
1. Calcule d'abord l'écart de chaque jour par rapport à l'objectif
2. Identifie les journées avec écart > 15%
3. Analyse les causes potentielles (arrêts, taux de rebut, etc.)
4. Liste les 3 anomalies principales par ordre d'impact

FORMAT de sortie :
| Anomalie | Impact Chiffré | Cause Probable | Priorité (1-3) |
```

### Réponse Attendue de l'IA (avec CoT)

```
ÉTAPE 1 - Calcul des écarts :
Ligne 1 :
- Lundi : -50 pièces (-10%)
- Mardi : -20 pièces (-4%)
- Mercredi : +20 pièces (+4%)
- Jeudi : -120 pièces (-24%) ← ÉCART MAJEUR
- Vendredi : -10 pièces (-2%)

Ligne 2 :
- Production : +2% (bon)
- Rebut : +0.5% par rapport à objectif

ÉTAPE 2 - Journées critiques :
- Jeudi Ligne 1 : écart de -24% (> 15%) ← CRITIQUE

ÉTAPE 3 - Analyse des causes :
- Jeudi : 4 arrêts totalisant 120 min → cause probable des 120 pièces manquantes
- Ligne 2 : rebut à 2,5% alors que production normale → problème qualité

ÉTAPE 4 - Anomalies principales :

| Anomalie | Impact Chiffré | Cause Probable | Priorité |
|----------|----------------|----------------|----------|
| Jeudi L1 : Arrêts répétés | -120 pièces (-24%) | 4 arrêts non planifiés (120 min) | 1 |
| L2 : Taux de rebut élevé | +0,5 point de rebut | Problème qualité process | 2 |
| L1 : Performance hebdo | -80 pièces sur la semaine | Arrêts cumulés impactent l'objectif | 3 |

RECOMMANDATIONS :
1. Enquête urgente sur les arrêts du jeudi Ligne 1 (maintenance préventive défaillante ?)
2. Audit qualité Ligne 2 pour identifier source du rebut
3. Plan d'action pour récupérer les 80 pièces manquantes semaine prochaine
```

### Points Pédagogiques

**L'Impact du Chain-of-Thought :**

**SANS CoT :** L'IA saute directement aux conclusions

- Risque : oubli de certaines anomalies
- Pas de traçabilité du raisonnement
- Difficile de vérifier la logique

**AVEC CoT :** L'IA explicite ses calculs

- Chaque anomalie est justifiée par des chiffres
- On peut vérifier chaque étape
- Approche méthodique et complète

**Message Clé :**
> "Pour tout ce qui nécessite des calculs ou un raisonnement logique,
> la phrase magique est : **'Réfléchis étape par étape'**"

### Erreurs Fréquentes

❌ Oublier de dire "étape par étape" → l'IA donne directement la réponse (souvent fausse)
✅ Toujours forcer l'explicitation du raisonnement

---

## EXERCICE 4 - Prompt Chaining : Guide d'Onboarding (25 min)

### Scénario

Créer un guide complet d'onboarding pour un nouveau collaborateur.

### Corrigé Type - Chaîne de 5 Prompts

#### PROMPT 1 : Identifier les Besoins d'Onboarding

```
RÔLE : Tu es un responsable RH expert en intégration de nouveaux collaborateurs.

CONTEXTE :
- Entreprise : PME industrielle (150 salariés)
- Poste du nouveau : Technicien de maintenance (profil junior)
- Durée d'intégration prévue : 1 mois

TÂCHE :
Liste les 10 éléments essentiels que doit couvrir un guide d'onboarding 
pour ce profil.

FORMAT :
Pour chaque élément :
- Nom de la section
- Objectif (en 1 phrase)
- Priorité (1=essentiel, 2=important, 3=secondaire)

CONSIGNE :
Classe ces éléments par ordre chronologique d'intégration 
(J1, Semaine 1, Semaine 2-4).
```

#### PROMPT 2 : Structurer le Guide (Utilise la Sortie du Prompt 1)

```
RÔLE : Expert en documentation RH et pédagogie d'entreprise.

TÂCHE :
À partir de ces 10 éléments d'onboarding :

[COPIER-COLLER LA LISTE DU PROMPT 1]

Crée la structure détaillée du guide d'onboarding.

FORMAT :
| Jour/Semaine | Section | Contenu à Inclure | Responsable | Durée Estimée |

CONTRAINTES :
- J1 : max 4h de contenu (éviter la surcharge)
- Semaine 1 : focus administratif + sécurité
- Semaines 2-4 : formation technique progressive
- Prévoir points de suivi (J7, J15, J30)
```

#### PROMPT 3 : Créer le Contenu de la Section "Sécurité"

```
RÔLE : Responsable HSE (Hygiène Sécurité Environnement) en milieu industriel.

TÂCHE :
Rédige le contenu complet de la section "Sécurité et EPI" du guide d'onboarding.

PUBLIC : Technicien de maintenance junior (première expérience industrielle).

CONTRAINTES :
- Ton : pédagogique mais ferme sur les obligations
- Inclure : EPI obligatoires, zones à risque, procédures d'urgence, habilitations
- Format : checklist + explications courtes
- Longueur : 2 pages A4 maximum

FORMAT :
1. Introduction (pourquoi la sécurité est prioritaire)
2. EPI obligatoires avec photos/schémas
3. Zones à risque de l'atelier (plan annoté)
4. Procédures d'urgence (incendie, accident)
5. Habilitations nécessaires (électrique, CACES, etc.)
6. Quiz de validation (5 questions)
```

#### PROMPT 4 : Créer le Plan de Formation Technique (Semaines 2-4)

```
RÔLE : Responsable formation technique en maintenance industrielle.

CONTEXTE :
Nouveau technicien de maintenance, niveau junior.
Équipements de l'entreprise : CNC, robots de soudure, convoyeurs.

TÂCHE :
Crée un plan de formation progressive sur 3 semaines pour monter en compétence 
le nouveau technicien.

ÉTAPES :
1. Liste les 8-10 compétences clés à acquérir
2. Classe-les par ordre de complexité (simple → avancé)
3. Répartis-les sur 3 semaines avec progression pédagogique
4. Pour chaque compétence, définis : objectif, durée, modalité, évaluation

FORMAT :
| Semaine | Compétence | Objectif | Durée | Modalité | Évaluation | Tuteur |

CONTRAINTES :
- Semaine 2 : observation + gestes de base (80% accompagné)
- Semaine 3 : pratique supervisée (50% autonomie)
- Semaine 4 : autonomie progressive (20% supervisé)
```

#### PROMPT 5 : Synthétiser et Finaliser le Guide Complet

```
RÔLE : Chef de projet RH, expert en création de supports.

TÂCHE :
Compile tous les éléments créés précédemment en un guide d'onboarding 
complet et professionnel.

ÉLÉMENTS À COMPILER :
1. [Structure du Prompt 2]
2. [Contenu Sécurité du Prompt 3]
3. [Plan de Formation du Prompt 4]

Ajoute les sections manquantes :
- Page de garde avec message de bienvenue
- Sommaire interactif
- Glossaire des termes techniques
- Contacts utiles (RH, manager, tuteur, médecine du travail)
- Feuille d'émargement des étapes validées

FORMAT FINAL :
Document PDF structuré de 15-20 pages avec :
- Table des matières cliquable
- Encarts visuels pour les points importants
- Checklist de progression (à cocher par le collaborateur)
- Page finale : "Feedback après 30 jours" (questionnaire)

CONTRAINTES :
- Ton : accueillant et rassurant
- Design : sobre et professionnel (couleurs entreprise)
- Praticité : utilisable en autonomie
```

### Points Pédagogiques du Chaining

**Pourquoi Découper en 5 Prompts ?**

1. **Chaque prompt = une expertise précise**
   - Prompt 1 : Vision RH globale
   - Prompt 3 : Expertise HSE
   - Prompt 4 : Expertise formation technique

2. **Qualité supérieure**
   - Un seul mega-prompt → résultat superficiel
   - 5 prompts ciblés → chaque partie est approfondie

3. **Contrôle et ajustement**
   - On valide chaque sortie avant de passer à la suivante
   - On peut modifier un prompt si le résultat n'est pas bon

4. **Réutilisabilité**
   - Le Prompt 3 (Sécurité) peut être réutilisé pour d'autres onboardings
   - Le Prompt 4 s'adapte facilement à d'autres profils techniques

**Message Clé :**
> "Pour les projets complexes, la règle est simple :
> **Découper pour mieux régner.** Un prompt = une mission précise."

### Variante Simplifiée (Si Manque de Temps)

Chaîne réduite à 3 prompts :

1. Structure globale
2. Contenu d'une section clé (au choix)
3. Synthèse finale

---

## QUIZ DE SYNTHÈSE - Corrigés Commentés

### Question 1 : Extraction d'Emails

**Réponse : B) Few-Shot**

**Explication :**
Few-Shot est **parfait** pour les tâches répétitives avec format précis :

- 2-3 exemples montrent le format de sortie attendu
- L'IA comprend comment extraire malgré la variété des emails
- Gain de temps énorme : pas besoin d'expliquer avec des mots

Alternative moins bonne :

- Zero-Shot : résultat moyen, format incohérent
- CoT : inutile, pas de raisonnement complexe ici
- Chaining : overkill pour cette tâche simple

---

### Question 2 : Logistique avec Contraintes

**Réponse : C) Chain-of-Thought**

**Explication :**
Problème de logistique = **raisonnement multi-critères** :

- Contraintes interdépendantes (coût, délai, capacité, etc.)
- Besoin d'expliciter les calculs et arbitrages
- CoT force l'IA à raisonner étape par étape

Exemple de prompt CoT pour logistique :

```
Réfléchis étape par étape :
1. Liste toutes les contraintes et leur impact
2. Évalue chaque option de transport selon ces contraintes
3. Calcule le score de chaque option
4. Recommande la meilleure avec justification chiffrée
```

---

### Question 3 : Campagne Marketing Complète

**Réponse : D) Prompt Chaining**

**Explication :**
Projet multi-étapes (personas → messages → visuels → calendrier) :

- Trop complexe pour un seul prompt
- Chaque étape nécessite une expertise différente
- La sortie d'une étape alimente la suivante

Chaîne typique :

1. Prompt 1 : Créer les personas cibles
2. Prompt 2 : Rédiger les messages pour chaque persona
3. Prompt 3 : Générer les concepts visuels basés sur les messages
4. Prompt 4 : Créer le calendrier de diffusion

---

### Question 4 : Nombre d'Exemples Few-Shot

**Réponse : B) 2-3 exemples**

**Explication :**
**Compromis optimal** entre efficacité et effort :

- 1 exemple : pas assez, l'IA manque de pattern
- 2-3 exemples : **sweet spot** → l'IA généralise bien
- 10+ exemples : effort inutile, pas de gain supplémentaire

**Règle pratique :**

- Tâche simple : 2 exemples suffisent
- Tâche avec variantes : 3 exemples recommandés
- Plus de 5 exemples : rarement utile

---

### Question 5 : "Réfléchis Étape par Étape"

**Réponse : C) La précision du raisonnement**

**Explication :**
Cette phrase magique force l'IA à :

- ✅ Expliciter son raisonnement (traçabilité)
- ✅ Réduire les erreurs logiques (20-30% de gain)
- ✅ Faire des calculs corrects (évite les shortcuts)

Ce qu'elle NE fait PAS :

- ❌ Accélérer la réponse (au contraire, plus long)
- ❌ Améliorer la créativité (pas l'objectif)
- ❌ Changer le style (juste la méthode)

---

## Arbre de Décision - Guide d'Utilisation pour le Formateur

### Comment Présenter l'Arbre

1. **Commencer par un cas concret**
   - Prenez un besoin d'un participant
   - Parcourez l'arbre ensemble
   - Arrivez à la technique appropriée

2. **Faire pratiquer en groupe**
   - Proposer 5-6 cas variés
   - Demander au groupe de choisir la technique
   - Débattre des choix

### Cas d'Entraînement pour l'Arbre

**Cas 1 : "Rédiger un règlement intérieur"**

- Simple ? NON
- Format précis ? OUI → **Few-Shot** (montrer 2-3 exemples de sections)

**Cas 2 : "Calculer la rentabilité d'un investissement"**

- Simple ? NON
- Format précis ? NON
- Raisonnement/Calculs ? OUI → **Chain-of-Thought**

**Cas 3 : "Créer un programme de formation complet"**

- Multi-étapes ? OUI → **Prompt Chaining**

**Cas 4 : "Donner 5 idées de team building"**

- Simple ? OUI → **Zero-Shot**

---

## Adaptations Selon le Public (Recommandations)

### Public Technique (Ingénieurs, Techniciens)

**Insister sur :**

- Chain-of-Thought (ils adorent la logique)
- Prompt Chaining (approche systématique)

**Exercices à privilégier :**

- CoT sur calculs de dimensionnement
- Chaining sur création de cahier des charges

### Public Commercial / RH

**Insister sur :**

- Few-Shot (formats répétitifs : emails, offres, propositions)
- Zero-Shot pour brainstorming

**Exercices à privilégier :**

- Few-Shot sur propositions commerciales
- Chaining sur campagnes de recrutement

### Public Managers

**Insister sur :**

- Prompt Chaining (projets complexes)
- Chain-of-Thought (décisions stratégiques)

**Exercices à privilégier :**

- Chaining sur plans d'action
- CoT sur analyses décisionnelles

---

## Points de Vigilance pour le Formateur

### Timing Serré (1h30)

**Si retard :**

1. Sacrifier Exercice 4 (Chaining) → donner en "à terminer pendant la pause"
2. Réduire le quiz à 3 questions au lieu de 5
3. Présenter l'arbre de décision rapidement (5 min au lieu de 10)

**Si avance :**

1. Approfondir le débat sur l'arbre de décision
2. Faire un exercice supplémentaire en groupe
3. Laisser plus de temps pour questions/réponses

### Messages à Marteler

1. **Few-Shot = Technique la plus rentable**
   - Peu d'effort (2-3 exemples)
   - Gros gain de qualité (+20-30%)

2. **CoT = Obligatoire pour calculs/logique**
   - Phrase magique à retenir
   - Évite 80% des erreurs de raisonnement

3. **Chaining = Ne pas tout mettre dans 1 prompt**
   - Découper = Qualité
   - 1 prompt = 1 mission précise

---

## Matériel à Préparer

- [ ] Slides avec exemples Avant/Après pour chaque technique
- [ ] Exercices imprimés (ou accès IA en direct)
- [ ] Arbre de décision au format A3 (affichage mural)
- [ ] Chronomètre visible
- [ ] Aide-mémoire synthétique (1 page recto-verso par participant)
- [ ] Tableau comparatif des 4 techniques (version imprimable)

---

*Document à usage exclusif du formateur - Ne pas distribuer aux participants*
