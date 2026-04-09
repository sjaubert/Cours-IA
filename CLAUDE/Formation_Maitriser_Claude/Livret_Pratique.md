<div class="header" style="display: flex; align-items: center; border-bottom: 2px solid #003366; padding-bottom: 10px; margin-bottom: 20px;">
  <img src="../../logo_uimm_placeholder.jpg" alt="Logo UIMM" width="120" style="margin-right: 20px;" />
  <div>
    <h2 style="margin: 0; color: #003366;">Pôle Formation UIMM - CVDL</h2>
    <p style="margin: 0; font-style: italic;">Formateur : S. JAUBERT</p>
  </div>
</div>

# Livret Pratique de Formation : Exercices et Fichiers Types

Ce manuel accompagne la formation "Maîtriser Claude". Il contient concrètement le **"COMMENT FAIRE"** : les fichiers à créer, le code à copier-coller et les prompts précis à exécuter lors des ateliers.

---

## 💻 Bloc 1 : Le Socle d'Identité
**Objectif :** Ne plus jamais avoir à expliquer à Claude qui vous êtes et quelles sont vos règles. 

### Exercice 1.1 : Créer votre fichier de contraintes
L'idée reçue est qu'il faut donner un long prompt contextuel à chaque question. **La réalité** : créez un fichier `.md` (Markdown) dans votre dossier "À propos de moi" et importez-le (en pièce jointe) au début de chaque Projet Claude.

**Action :** Créez un fichier texte nommé `identite_rh_uimm.md` et copiez-y le code suivant :

```markdown
# 1. Mon Rôle et Contexte
Tu vas agir en tant qu'assistant de la cellule administrative et ressources humaines du Pôle Formation UIMM CVDL. 
Ton objectif principal est la rédaction de documents de suivi, de courriers professionnels et l'ingénierie administrative. 
L'audience est constituée soit de formateurs, soit de directeurs industriels, soit d'apprentis.

# 2. Ton et Style de Voix
Désactive ton style de chatbot habituel.
- Ton formel, très direct et strictement professionnel.
- Zéro langage familier, zéro jargon marketing.
- PAS D'ÉMOJIS sous aucun prétexte. Jamais. 

# 3. Format de Sortie Strict
- Chaque texte doit être aéré : des paragraphes de 3 phrases maximum.
- Les actions à réaliser doivent toujours être listées avec des puces.
- Conclure systématiquement les courriers par la formule : "Le Pôle Formation UIMM reste à votre disposition."
```

### Exercice 1.2 : Le Test de Conformité
Une fois le fichier importé dans Claude ou dans votre fil de discussion, tapez ce prompt pour le tester :
> *"En utilisant mon fichier d'identité en référence, rédige une courte relance (100 mots) destinée à trois apprentis BTS ATI (Léo, Marc, Sophie) qui n'ont pas encore rendu leur fiche navette d'entreprise pour le mois de Mars."*

*Observez comment l'IA respecte le ton formel, évite les émojis et inclut la signature demandée sans avoir eu à le lui préciser dans le prompt.*

---

## 🔄 Bloc 2 : L'Art du Prompt Inversé
**Objectif :** Vous ne savez pas exactement ce que l'IA a besoin de savoir pour faire un bon travail ? Laissez-la vous interroger.

### Exercice 2.1 : Transformer une prise de note chaotique
**Action :** Plutôt que de rédiger une longue instruction, créez un fichier `prompt_inverse_methode.md` ou sauvegardez ce texte dans vos raccourcis claviers.

```text
Je dois rédiger un rapport d'audit technique sur une ligne de production.
Tu es un ingénieur méthode senior. Ton but est de rédiger ce rapport pour moi de manière irréprochable.
Cependant, mes notes actuelles sont très incomplètes. 

AVANT de rédiger le rapport, pose-moi une par une les 5 questions essentielles dont tu as absolument besoin (mesures relevées, type d'automate, pannes observées, etc.) pour que ce document soit parfait. 
Ne pose qu'UNE SEULE question à la fois et attends ma réponse avant de passer à la suivante.
```

*Remarque : L'IA va alors se transformer en enquêteur. Si vous ne connaissez pas la réponse à sa question, répondez "Je ne sais pas, propose-moi l'hypothèse la plus standard pour ce type d'industrie".*

---

## ⚠️ Bloc 3 : L'Illusion de Raisonnement (Le "Plantage")
**Objectif :** Démontrer aux salariés que Claude n'est qu'un modèle probabiliste (il prédit le mot suivant), et non une intelligence douée de réflexion logique humaine. S'il ne sait pas, son réflexe premier est d'inventer avec un incroyable aplomb ("Hallucination").

### Exercice 3.1 : Le Piège Technique (Le fameux Turbo-encabulateur)
Le "Turbo-encabulateur" est une célèbre blague d'ingénieurs des années 1940, mais de nombreux modèles d'IA vont tenter de vous en expliquer le fonctionnement physique réel si on les piège.

**Action :** Posez exactement ce prompt à Claude :
> *"Agis comme un ingénieur industriel de très haut niveau. Peux-tu m'expliquer précisément comment le 'Turbo-encabulateur polymétrique' gère l'inversion des flux de reluctance magnétique dans une presse hydraulique ?"*

*Debriefing : Observez comment l'IA risque de produire des paragraphes très crédibles avec un vocabulaire scientifique pointu pour justifier une technologie fictive. C'est la preuve qu'une supervision humaine experte est irremplaçable.*

### Exercice 3.2 : Modifier le comportement ("Anti-Hallucination")
Pour contrer cela, montrez aux apprenants comment "verrouiller" le modèle.
> *"Même question que précédemment. IMPORTANT : Si ce concept n'existe pas, s'il relève de la fiction ou s'il contient une erreur de logique physique, ton devoir est de l'indiquer immédiatement."*

---

## ⚙️ Bloc 4 : L'Assistant Synthèse (Processus Automatisé)
**Objectif :** Transformer du "bruit" non structuré de réunion en un plan d'action lisible par l'équipe.

### Exercice 4.1 : Ingérer le chaos
**Action :** Vous sortez d'une réunion de section, vous avez pris des notes en vrac (sans ponctuation, sans ordre). Donnez ce "Méta-Prompt" de structuration à Claude. Enregistrez-le sous `Template_Compte_Rendu.md`.

```text
Je vais te fournir ci-dessous des notes brutes et chaotiques prises lors d'une réunion pédagogique. 
Tu dois traiter ces notes et générer un compte-rendu STRICT au format Markdown reprenant cette structure exacte :

# 1. Décisions Clés
(Liste à puce des décisions actées)

# 2. Plan d'Action (QQOQCP)
| Quoi (Action) | Qui (Responsable) | Pour Quand (Délai) |
| --- | --- | --- |
| ... | ... | ... |

# 3. Points de Blocage / En attente
(Ce qui n'a pas été résolu)

**Règle d'or :** Si l'information "Qui" ou "Quand" n'est pas dans mes notes, écris "[À DÉFINIR]". Ne l'invente surtout pas.

Voici mes notes brutes :
[COPIER/COLLER VOS NOTES ICI]
```

Ainsi, les apprenants quittent la formation avec **4 outils et méthodes** prêts à être déployés le lendemain matin dans leur poste de travail.

---
<div class="footer" style="border-top: 1px solid #003366; padding-top: 10px; margin-top: 30px; font-size: 0.9em; color: #555;">
  <p style="text-align: center;"><strong>Pôle Formation UIMM - CVDL</strong> | Acteur de l'Industrie</p>
</div>
