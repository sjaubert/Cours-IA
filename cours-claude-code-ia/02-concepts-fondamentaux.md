# Module 2 — Concepts Fondamentaux
## Glossaire illustré de l'écosystème Claude Code

> **Durée :** 2h  
> **Objectif :** Maîtriser le vocabulaire et les mécanismes de base pour lire et utiliser les ressources de l'écosystème

---

## 2.1 L'architecture d'un agent IA

Avant de définir les termes un par un, voici comment les pièces s'assemblent dans un système agentique :

```
┌─────────────────────────────────────────────────────┐
│                   UTILISATEUR                       │
│         (instruction en langage naturel)            │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│                AGENT PRINCIPAL                      │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │ Prompt Système│  │    Skills    │  │   Hooks   │ │
│  │  (CLAUDE.md) │  │  (SKILL.md)  │  │           │ │
│  └──────────────┘  └──────────────┘  └───────────┘ │
│                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │  Sous-Agent  │  │  Sous-Agent  │  │   Outils  │ │
│  │  (Analyste)  │  │  (Rédacteur) │  │  (MCP)    │ │
│  └──────────────┘  └──────────────┘  └───────────┘ │
└─────────────────────────────────────────────────────┘
```

---

## 2.2 Glossaire des concepts essentiels

### Agent (Agent IA)

**Définition :** Un système IA capable de percevoir son environnement, prendre des décisions et agir de façon autonome pour atteindre un objectif.

**Analogie métier :** Un chef de projet qui reçoit un brief, décompose le travail, délègue aux bonnes personnes et livre le résultat — sans vous demander à chaque étape comment faire.

**Exemple concret :**
> *"Analyse tous les emails reçus cette semaine, identifie les actions urgentes, crée des entrées dans mon agenda et prépare un résumé pour ma réunion de lundi."*

---

### Sous-agent (Subagent)

**Définition :** Un agent spécialisé invoqué par l'agent principal pour réaliser une tâche précise. Il a un rôle défini, des outils spécifiques et un contexte limité à sa mission.

**Analogie métier :** Dans une équipe projet, vous avez un chef de projet (agent principal), un expert technique, un juriste, un rédacteur… Chacun est un "sous-agent" qui traite sa partie.

**Exemple concret :**
```
Agent principal → reçoit "Prépare le rapport mensuel"
    ├── Sous-agent "Analyste" → collecte les données
    ├── Sous-agent "Rédacteur" → rédige le corps du rapport
    └── Sous-agent "Qualité" → vérifie la cohérence et le style
```

Le dépôt [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) propose plus de 100 sous-agents prêts à l'emploi, couvrant des domaines aussi variés que la sécurité informatique, l'administration, la santé ou la recherche.

---

### Prompt système (System Prompt)

**Définition :** Un ensemble d'instructions données à l'agent *avant* la conversation. Il définit sa personnalité, ses règles de comportement, ses contraintes et son contexte de travail.

**Analogie métier :** La fiche de poste et le règlement intérieur d'un collaborateur. Avant de commencer à travailler, l'agent sait exactement ce qu'on attend de lui.

**Exemple simplifié :**
```
Tu es un assistant RH pour une entreprise industrielle de 500 personnes.
Tu réponds toujours en français.
Tu ne communiques jamais d'informations nominatives sans confirmation.
Lorsqu'on te demande de rédiger une offre d'emploi, tu utilises 
toujours le modèle de l'entreprise en annexe.
```

Le dépôt [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) expose les prompts systèmes internes de nombreux outils IA du marché — une ressource précieuse pour comprendre leur comportement.

---

### CLAUDE.md

**Définition :** Un fichier texte placé à la racine d'un projet qui sert d'instruction permanente à Claude pour ce projet précis. C'est le "contexte de travail" que l'agent relit à chaque session.

**Analogie métier :** Le "livret d'accueil" d'un dossier de travail. Tout nouveau collaborateur (ou agent) qui prend en charge ce projet commence par le lire.

**Exemple de contenu :**
```markdown
# Projet : Rapport Qualité Mensuel

## Contexte
Ce projet génère le rapport qualité mensuel de l'usine de Valenciennes.

## Règles
- Toujours utiliser les données de la base SQL "qualite_prod"
- Le format de sortie est XLSX avec le template /templates/rapport_qualite.xlsx
- Les seuils d'alerte : rouge > 5% de rebuts, orange > 3%

## Contacts
- Validateur : Jean Dupont (jean.dupont@entreprise.fr)
- Destinataires : direction@entreprise.fr
```

---

### Skills (Compétences)

**Définition :** Des modules de capacités que l'on "greffe" sur Claude pour lui donner des comportements spécialisés. Un skill est défini dans un fichier `SKILL.md` et contient des instructions détaillées pour une tâche précise.

**Analogie métier :** Les certifications d'un collaborateur. Un technicien qualité "certifié ISO 9001" sait exactement comment mener un audit — le skill lui donne cette compétence structurée.

**Exemples de skills disponibles dans l'écosystème :**
- `docx` — créer et modifier des documents Word
- `xlsx` — créer et analyser des feuilles de calcul Excel  
- `pptx` — générer des présentations PowerPoint
- `pdf` — extraire, créer et manipuler des PDF
- `code-review` — revoir du code selon des standards définis
- `incident-response` — gérer une crise selon un protocole établi

---

### Hooks

**Définition :** Des déclencheurs qui exécutent automatiquement une action à un moment précis du workflow de l'agent (avant une action, après, en cas d'erreur…).

**Analogie métier :** Les contrôles automatiques dans un processus industriel. Avant de valider une commande fournisseur, le système vérifie automatiquement le budget disponible.

**Exemples de hooks utiles :**
- **Pre-action hook :** "Avant d'envoyer un email, vérifier que le destinataire est dans la liste approuvée"
- **Post-action hook :** "Après avoir modifié un document, créer automatiquement une sauvegarde datée"
- **Error hook :** "Si une erreur se produit, alerter le responsable par Slack"

---

### MCP (Model Context Protocol)

**Définition :** Un protocole standard qui permet à Claude de se connecter à des outils et services externes (Slack, Google Drive, bases de données, APIs…) de façon sécurisée et structurée.

**Analogie métier :** Le port USB universel de l'IA. Il vous permet de connecter n'importe quel périphérique (outil) à votre ordinateur (Claude) avec le même standard.

**Exemples de connexions MCP disponibles :**
- Google Drive / OneDrive (lecture/écriture de fichiers)
- Gmail / Outlook (envoi et lecture d'emails)
- Slack / Teams (messages et notifications)
- Calendriers (Google Calendar, Outlook Calendar)
- Bases de données SQL
- Jira, Linear, Asana (gestion de projets)
- GitHub (code et issues)

---

### CLI (Command Line Interface)

**Définition :** L'interface en ligne de commande — la façon la plus directe d'utiliser Claude Code, en tapant des instructions dans un terminal.

**Pour les non-techniques :** Pas d'inquiétude — dans la plupart des cas d'usage métier, vous n'aurez pas besoin de la CLI. Des interfaces graphiques (comme Cowork ou Claude.ai) font le travail.

---

### TDD (Test-Driven Development)

**Définition :** Une méthodologie de développement qui consiste à écrire les *tests de validation* avant d'écrire le code lui-même. On définit d'abord ce qu'on attend, puis on produit ce qui doit satisfaire ces attentes.

**Appliqué aux agents IA :** Avant de laisser l'agent travailler, on définit précisément les critères de succès. L'agent travaille, vérifie lui-même si les critères sont satisfaits, et recommence si nécessaire.

**Analogie métier :** Le cahier des charges de réception. Avant de commander une machine, vous définissez les tests d'acceptation. Le fournisseur ne peut livrer qu'une fois ces tests passés.

Le framework [Superpowers](https://github.com/obra/superpowers) applique rigoureusement cette philosophie — tout code écrit avant les tests est automatiquement supprimé.

---

### CI/CD (Intégration Continue / Déploiement Continu)

**Définition :** Des pipelines automatisés qui exécutent une série de vérifications à chaque modification d'un projet (tests, revue de qualité, déploiement…).

**Avec Claude Code :** L'agent peut être intégré directement dans ce pipeline. Il réalise des revues de code automatiques, propose des corrections, génère de la documentation — sans intervention humaine sur les tâches de routine.

**Coût indicatif :** Pour une équipe réalisant 50 pull requests par mois, l'intégration via [claude-code-action](https://github.com/anthropics/claude-code-action) coûte moins de 5 € par mois.

---

### Orchestration d'agents

**Définition :** La coordination de plusieurs agents qui travaillent en parallèle ou en séquence sur une tâche complexe, avec des rôles, des responsabilités et des règles de handoff définis.

**Exemple d'orchestration pour un rapport annuel :**
```
Directeur de projet (agent principal)
├── Collecteur de données → extrait les chiffres des systèmes
├── Analyste → interprète les tendances
├── Rédacteur → produit le texte
├── Graphiste IA → crée les visuels
└── Réviseur → vérifie la cohérence globale
```

Le dépôt [gstack](https://github.com/garrytan/gstack) de Garry Tan montre comment structurer une telle équipe avec des rôles nommés (CEO, Designer, Engineering Manager, QA…).

---

## 2.3 Les primitives de Claude Code

Claude Code s'articule autour de quatre primitives fondamentales :

### 1. Les commandes slash (/commande)

Raccourcis pour déclencher des comportements prédéfinis :
- `/review` — déclenche une revue de document
- `/summarize` — résume le contenu actuel
- `/plan` — demande à l'agent de planifier avant d'agir

### 2. Les fichiers d'instructions

- `CLAUDE.md` — instructions globales du projet
- `SKILL.md` — définition d'une compétence spécifique
- `.claudeignore` — fichiers à ignorer (comme `.gitignore`)

### 3. Les paramètres (settings)

Configuration du comportement : modèle à utiliser, niveau de verbosité, règles de sécurité, limites d'actions autonomes…

### 4. Les outils intégrés

Actions que Claude peut réaliser nativement : lire/écrire des fichiers, exécuter du code, faire des recherches web, appeler des APIs…

---

## 2.4 La notion de contexte

### Qu'est-ce que le contexte ?

Le "contexte" est la quantité d'information qu'un agent peut traiter simultanément. Imaginez-le comme la mémoire de travail d'une personne : au-delà d'une certaine charge, des éléments importants commencent à "tomber".

### Pourquoi c'est important ?

- Un agent avec un contexte surchargé peut "oublier" des instructions du début
- Les workflows longs nécessitent des stratégies de gestion du contexte
- Certains dépôts (comme [get-shit-done](https://github.com/gsd-build/get-shit-done)) ont été créés précisément pour résoudre ce problème

### Stratégies de gestion du contexte

- Découper les tâches longues en sessions courtes
- Utiliser des fichiers de mémoire persistants (CLAUDE.md)
- Compresser régulièrement le contexte (résumés intermédiaires)
- Utiliser des sous-agents avec des contextes isolés

---

## 2.5 Récapitulatif visuel

| Concept | Rôle | Analogie |
|---------|------|----------|
| Agent | Acteur autonome | Collaborateur autonome |
| Sous-agent | Spécialiste délégué | Expert métier |
| Prompt système | Instructions permanentes | Fiche de poste |
| CLAUDE.md | Contexte projet | Livret d'accueil dossier |
| Skill | Compétence ajoutée | Certification |
| Hook | Contrôle automatique | Vérification processus |
| MCP | Connecteur externe | Port USB universel |
| TDD | Validation avant production | Cahier des charges réception |
| Orchestration | Coordination d'équipe | Gestion de projet |

---

## Points clés à retenir

- Les agents IA fonctionnent avec des instructions structurées (CLAUDE.md, prompts système)
- Les skills permettent de spécialiser Claude sans redéfinir son comportement de base
- Les hooks automatisent les contrôles et la sécurité
- MCP est la porte d'entrée vers tous vos outils existants
- La gestion du contexte est cruciale pour les tâches longues

---

## Questions de révision

1. Expliquez la différence entre un agent principal et un sous-agent avec un exemple de votre métier.
2. À quoi sert un fichier CLAUDE.md ? Quel contenu mettriez-vous dans un CLAUDE.md pour un projet de votre travail ?
3. Qu'est-ce que le MCP et pourquoi est-il stratégique pour l'intégration de l'IA en entreprise ?

---

*Module précédent : [← Introduction](01-introduction-ia-agentique.md) | Prochain module : [Les 15 ressources GitHub →](03-ressources-github.md)*
