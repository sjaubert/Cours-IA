![Logo Pôle Formation UIMM-CVDL](logo_uimm_placeholder.jpg)

# Pôle Formation UIMM-CVDL

---

# CORRIGÉS - Atelier 2 : Exercices Pratiques

## Usage de ce Document

Ce document contient les **corrigés détaillés** des 5 exercices progressifs de l'Atelier 2.

**Destiné uniquement au formateur** pour :

- Préparer les corrections
- Avoir des exemples de prompts complets
- Adapter les solutions selon le public
- Guider le peer review de l'exercice 3

---

## EXERCICE 1 - Email Simple (Débutant)

### Scénario

Informer l'équipe d'un changement dans les horaires de la réunion hebdomadaire.

### Corrigé Type - Version Complète

```
RÔLE & CONTEXTE :
Tu es un manager d'équipe dans une entreprise industrielle.
L'équipe est composée de 8 personnes (techniciens et ingénieurs).

OBJECTIF :
Informer l'équipe du changement d'horaire de la réunion hebdomadaire
sans créer de confusion ni mécontentement.

TÂCHE :
Rédige un email professionnel et clair.

CONTRAINTES :
- Ton : professionnel mais chaleureux
- Longueur : maximum 150 mots
- Préciser l'ancien ET le nouvel horaire pour éviter toute confusion
- Expliquer brièvement la raison du changement (transparence)

FORMAT :
Email classique avec :
- Objet clair et précis
- Salutation appropriée
- Corps en 3 paragraphes :
  1. Annonce du changement avec raison
  2. Détails précis (ancien → nouveau horaire)
  3. Action attendue (confirmation)
- Formule de politesse
```

### Points Pédagogiques à Souligner

**Ce que le prompt fait bien :**

- Rôle ET contexte (type d'équipe)
- Objectif double (informer + éviter confusion)
- Contraintes claires (ton, longueur, éléments obligatoires)
- Format structuré

**Variante possible selon le public :**
Si l'équipe est très technique, ajouter :

```
CONTRAINTES (ajout) :
- Proposer un lien vers l'invitation calendar mise à jour
```

---

## EXERCICE 2 - Procédure Qualité (Intermédiaire)

### Scénario

Créer une procédure de contrôle visuel pour les opérateurs suite à des non-conformités.

### Corrigé Type - Version Complète

```
RÔLE & CONTEXTE :
Tu es un ingénieur qualité dans l'industrie automobile avec 10 ans d'expérience.
Tu t'adresses à des opérateurs de production de niveau CAP à BAC+2.
Contexte : Ligne de production de pièces usinées, plusieurs non-conformités récentes.

OBJECTIF :
Permettre aux opérateurs de réaliser un contrôle visuel et dimensionnel fiable 
en moins de 2 minutes, réduisant ainsi les non-conformités de 80%.

TÂCHE :
Crée une procédure de contrôle visuel pour une pièce usinée cylindrique.

CONTRAINTES :
- Format : A4 imprimable, lisible à 2 mètres de distance
- Langage : simple, pas de jargon technique (éviter termes comme "coaxialité")
- Points de contrôle obligatoires : dimensions, aspect surface, bavures
- Temps d'exécution : maximum 2 minutes par pièce
- Outils référencés : pied à coulisse, jauge de profondeur, loupe x10
- Tolérances : ±0.1mm sur dimensions critiques

FORMAT :
Tableau en 4 colonnes :
| Étape | Point de Contrôle | Outil Utilisé | Critère OK/NOK |
|-------|-------------------|---------------|----------------|
| 1     | ...               | ...           | ...            |

Ajouter en bas du tableau :
Section "Que faire en cas de NOK ?" avec marche à suivre

ÉTAPES DE CONSTRUCTION :
1. Liste d'abord les 5-6 points critiques à contrôler par ordre d'importance
2. Organise-les dans l'ordre logique de contrôle (du simple au complexe)
3. Pour chaque critère, formule de manière binaire : OK si [condition], NOK sinon
4. Ajoute les actions en cas de non-conformité (rebut/retouche/alerte superviseur)
```

### Variantes Selon le Niveau

**Si groupe avancé (techniciens expérimentés) :**
Ajouter dans les contraintes :

```
- Intégrer la référence aux normes ISO pertinentes
- Préciser les cotes critiques selon plan de définition
```

**Si groupe débutant :**
Simplifier :

```
- Ajouter des schémas/photos pour chaque point de contrôle
- Utiliser des codes couleur (vert = OK, rouge = NOK)
```

### Points Pédagogiques

**Piliers particulièrement importants ici :**

1. **Rôle précis** : "10 ans d'expérience" → légitime le niveau de détail
2. **Public défini** : "CAP à BAC+2" → adapte le vocabulaire
3. **Format tableau** : lecture rapide, essentiel pour un poste de travail
4. **Étapes de construction** : guide le raisonnement de l'IA

---

## EXERCICE 3 - Quiz de Formation (Intermédiaire+ avec Peer Review)

### Scénario

Créer un quiz interactif de 10 questions sur les bases de la cybersécurité.

### Corrigé Type - Version Complète

```
RÔLE & CONTEXTE :
Tu es un formateur expert en cybersécurité et en pédagogie active.
Public cible : employés de bureau tous niveaux (administratifs, commerciaux, RH)
sans formation technique préalable.

OBJECTIF :
Sensibiliser aux bons réflexes de sécurité ET évaluer la compréhension
pour identifier les points à approfondir avant la fin de la formation.

TÂCHE :
Crée un quiz interactif de 10 questions sur "Les bases de la cybersécurité".

CONTRAINTES :
- Format : QCM avec 4 réponses possibles (1 seule correcte)
- Difficulté : accessible mais pas évident (éviter les questions trop simples)
- Thèmes à couvrir équitablement :
  * Mots de passe (3 questions)
  * Phishing et emails suspects (3 questions)
  * Mises à jour et sécurité logicielle (2 questions)
  * Protection des données sensibles (2 questions)
- Mélanger les niveaux :
  * 3 questions de connaissance (définitions)
  * 4 questions de compréhension (pourquoi/comment)
  * 3 questions d'application (que faire dans cette situation ?)
- Langage : professionnel mais accessible, éviter le jargon informatique

FORMAT pour chaque question :
Question N : [Énoncé clair et concret]
A) [Proposition 1]
B) [Proposition 2]
C) [Proposition 3]
D) [Proposition 4]

Réponse correcte : [Lettre]
Explication : [Pourquoi cette réponse en 1-2 phrases, pour faciliter le débriefing]

ÉTAPES :
1. Répartis les 10 questions selon la grille thématique imposée
2. Pour chaque question, choisis le niveau de cognition approprié
3. Formule des distracteurs plausibles (réponses fausses mais crédibles)
4. Vérifie qu'UNE SEULE réponse est incontestablement correcte
5. Rédige une explication pédagogique pour chaque bonne réponse
```

### Grille d'Auto-Évaluation pour le Peer Review

**Instructions pour l'échange entre participants :**

Quand vous recevez le prompt de votre voisin, vérifiez :

| Critère | Présent ? | Suggestion d'amélioration |
|---------|-----------|---------------------------|
| Rôle précis (formateur ou expert ?) | ☐ | |
| Objectif clair : sensibiliser vs évaluer vs les deux ? | ☐ | |
| Contraintes de difficulté spécifiées | ☐ | |
| Format EXACT du QCM précisé (nombre de choix) | ☐ | |
| Répartition thématique demandée | ☐ | |
| Niveau de langage adapté au public | ☐ | |

**Questions à poser à votre voisin :**

1. "Si je suis l'IA, est-ce que je sais combien de réponses proposer par question ?"
2. "Est-ce que le niveau de difficulté est assez précis ?"

### Variante Avancée

```
Ajout possible dans ÉTAPES :
6. Pour les questions d'application, utilise des scénarios réalistes du quotidien
   (ex: email reçu, popup sur l'ordinateur, demande par téléphone)
```

---

## EXERCICE 4 - Rapport de Synthèse (Avancé)

### Scénario

Transformer des notes de réunion désorganisées en rapport pour la direction.

### Données Fournies (Notes Brutes)

```
- Problème ligne 3 : cadence trop lente (actuellement 45 pièces/h, objectif 60)
- Jean propose de réorganiser le poste d'emballage
- Coût estimé : 15K€
- Marie pense qu'il faut d'abord former les nouveaux
- Le budget formation est serré cette année
- Délai de mise en œuvre si on valide : 3 mois
- ROI estimé : 12 mois selon les calculs de Sophie
- Le directeur veut une réponse avant fin de semaine
- Points positifs : équipe motivée, bon esprit
- Risques : période de forte charge en juin (mauvais timing ?)
- Alternative proposée : investir dans un automate (50K€, ROI 18 mois)
```

### Corrigé Type - Version Complète

```
RÔLE & CONTEXTE :
Tu es un responsable de production expérimenté (15 ans dans l'industrie).
Tu rapportes à la direction générale qui attend des synthèses factuelles
et chiffrées pour prendre des décisions rapides.

OBJECTIF :
Faciliter la prise de décision de la direction en présentant de manière claire
et objective les enjeux, les options et leur impact chiffré.

TÂCHE :
Transforme ces notes de réunion en rapport de synthèse structuré pour la direction.

[DONNÉES BRUTES ICI]

CONTRAINTES :
- Longueur : maximum 1 page A4 (~ 400 mots)
- Ton : factuel, neutre, professionnel (pas d'opinion personnelle marquée)
- Public : direction générale (peu de temps, besoin de chiffres)
- Deadline : fin de semaine (mentionner dans le rapport)
- Éléments obligatoires :
  * Problématique chiffrée
  * Options avec comparaison coût/bénéfice
  * Risques et opportunités
  * Recommandation avec justification

FORMAT :
Rapport structuré en 5 sections :

1. CONTEXTE (2-3 lignes)
   Problème, enjeu chiffré

2. SITUATION ACTUELLE vs OBJECTIF (tableau)
   | Indicateur | Actuel | Objectif | Écart |

3. OPTIONS ENVISAGÉES (tableau comparatif)
   | Option | Investissement | ROI | Délai | Avantages | Inconvénients |

4. ANALYSE RISQUES/OPPORTUNITÉS
   - Risques identifiés (timing, budget...)
   - Facteurs favorables (motivation équipe...)

5. RECOMMANDATION
   Option préconisée avec justification chiffrée en 3-4 lignes

ÉTAPES D'ANALYSE :
1. Extrait et structure d'abord toutes les données chiffrées des notes
2. Identifie les 2 options principales et compare-les objectivement
3. Liste les risques ET les opportunités de manière équilibrée
4. Formule une recommandation basée sur les chiffres (ROI, délais, risques)
5. Vérifie que le rapport tient sur 1 page A4
```

### Points Clés pour le Formateur

**Ce prompt gère bien :**

- Transformation de **désordre → structure**
- Ton adapté (direction = factuel + chiffres)
- Format tableau = lecture rapide
- Étapes qui forcent l'analyse avant la synthèse

**Débriefing Important :**
Insister sur 3 points :

1. **Format tableau** : La direction n'a pas le temps de lire des pavés de texte
2. **Ton neutre** : La direction décide, on n'impose pas notre choix
3. **Chiffres systématiques** : Toujours quantifier (coût, ROI, délais, %)

**Erreur Fréquente à Anticiper :**
Participants qui oublient de demander un ton neutre → l'IA fait souvent une recommandation trop directive

---

## EXERCICE 5 - Challenge Personnel (Application)

### Instructions pour le Formateur

Cet exercice est **très ouvert** car chaque participant crée un prompt pour SON besoin réel.

### Grille d'Évaluation Rapide (Tour de salle)

Pendant que les participants travaillent, circuler et vérifier rapidement :

**Checklist minute (30 secondes par participant) :**

- [ ] Le prompt est-il compréhensible sans contexte supplémentaire ?
- [ ] Les 6 piliers sont-ils présents (au moins 5/6) ?
- [ ] Le format de sortie est-il précisément défini ?
- [ ] Y a-t-il au moins 2 contraintes pertinentes ?

**Si un pilier manque :** Poser une question guidante plutôt que donner la réponse

- Pilier manquant : Rôle → "Pour qui parle l'IA ?"
- Pilier manquant : Format → "À quoi doit ressembler le résultat ?"
- Pilier manquant : Contraintes → "Quelles limites ou règles ?"

### Exemples de Prompts Personnels Bien Construits

#### Exemple 1 : RH - Offre d'Emploi

```
RÔLE : Tu es un consultant en recrutement spécialisé dans l'industrie.
OBJECTIF : Attirer des candidats qualifiés ET filtrer les profils inadaptés.
TÂCHE : Rédige une offre d'emploi pour un Technicien de Maintenance H/F.
CONTRAINTES :
- Ton : attractif mais professionnel
- Longueur : 300-400 mots
- Mettre en avant : évolution, formation, CDI
FORMAT : Titre accrocheur + 4 sections (Entreprise/Poste/Profil/Avantages)
```

#### Exemple 2 : Commercial - Proposition

```
RÔLE : Expert commercial B2B dans l'équipement industriel.
OBJECTIF : Convaincre un prospect de passer à l'action (RDV ou devis).
TÂCHE : Rédige une proposition commerciale personnalisée pour [Client XPTO].
CONTRAINTES :
- Basée sur le besoin identifié : réduction temps de cycle
- Chiffrer les gains potentiels
- Maximum 2 pages
FORMAT : Email de présentation + PDF structuré (Besoin/Solution/Bénéfices/Tarif)
```

### Débriefing Collectif (5 min)

**Questions à poser au groupe :**

1. "Quel pilier avez-vous trouvé le plus difficile à remplir ?"
2. "Quelqu'un veut partager son prompt et recevoir du feedback ?"

**Message final :**
> "Le prompt que vous venez de créer, testez-le cette semaine sur un vrai besoin.
> Et n'hésitez pas à l'améliorer après le premier test. **L'itération est la clé !**"

---

## Bilan de l'Atelier - Points de Débriefing

### Les 3 Erreurs Les Plus Fréquentes (Observées)

1. **Oublier le public cible** → Impact énorme sur vocabulaire
   - Solution : Toujours se demander "Pour qui ?"

2. **Format trop vague** → L'IA invente et se trompe souvent
   - Solution : Montrer un exemple ou donner une structure précise

3. **Pas d'exemples pour les formats complexes**
   - Solution : "Un exemple vaut 10 lignes d'explication"

### Les 3 Bonnes Pratiques à Retenir

1. **Toujours commencer par le template** (automatisme mental)
2. **Se mettre à la place de l'IA** : "Ai-je TOUT pour répondre ?"
3. **Tester et itérer** : le 1er prompt n'est jamais parfait

### Adaptation Selon le Public

**Si public homogène (ex: tous RH) :**

- Remplacer TOUS les exemples par des cas RH
- Exercice 5 : proposer 3-4 cas RH types au choix

**Si groupe en difficulté :**

- Donner le début du prompt, demander de compléter
- Faire l'exercice 1 tous ensemble au tableau

**Si groupe très avancé :**

- Exercice 5 : demander de créer 2 prompts (1 simple + 1 complexe)
- Challenge : "Créez le prompt le plus court possible qui reste efficace"

---

## Matériel de Correction à Préparer

- [ ] Corrigés imprimés pour Exercices 1, 2, 4
- [ ] Grille peer review pour Exercice 3 (1 par participant)
- [ ] Exemples de prompts métier (bibliothèque starter)
- [ ] Chronomètre pour respecter les timings
- [ ] Tableau/paperboard pour noter les erreurs fréquentes en temps réel

---

*Document à usage exclusif du formateur - Ne pas distribuer aux participants*
