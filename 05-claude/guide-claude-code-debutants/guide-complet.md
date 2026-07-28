---
output:
  word_document: default
  html_document: default
---
# Guide Complet Claude Code — De débutant à utilisateur autonome

**Pôle Formation UIMM-CVDL | S. JAUBERT**  
*Basé sur les meilleures pratiques de la communauté Claude Code (mai 2026)*

> Ce guide s'adresse à tous les salariés, quelle que soit leur familiarité avec l'informatique. Aucune compétence en développement n'est requise pour les chapitres 1 à 5. Les chapitres suivants introduisent progressivement des fonctionnalités plus avancées.

---

## Table des matières

1. [Qu'est-ce que Claude Code ?](#1-quest-ce-que-claude-code)
2. [Installation pas à pas](#2-installation-pas-à-pas)
3. [Premiers pas : lancer et utiliser Claude Code](#3-premiers-pas)
4. [CLAUDE.md — La mémoire persistante de votre projet](#4-claudemd)
5. [Les quatre piliers : Commands, Skills, Subagents, Hooks](#5-les-quatre-piliers)
6. [Commands — Vos raccourcis de workflow](#6-commands)
7. [Skills — Vos compétences réutilisables](#7-skills)
8. [Subagents — Déléguer à des assistants spécialisés](#8-subagents)
9. [Hooks — Automatiser les actions récurrentes](#9-hooks)
10. [MCP Servers — Connecter Claude à vos outils](#10-mcp-servers)
11. [Settings — Configurer Claude Code](#11-settings)
12. [Workflows et bonnes pratiques](#12-workflows-et-bonnes-pratiques)
13. [Gestion du contexte et de la mémoire](#13-gestion-du-contexte)
14. [Fonctionnalités avancées](#14-fonctionnalités-avancées)
15. [Cas d'usage par métier](#15-cas-dusage-par-métier)
16. [Ressources et liens utiles](#16-ressources-et-liens-utiles)

---

## 1. Qu'est-ce que Claude Code ?

Claude Code est l'assistant IA d'Anthropic conçu pour travailler **directement dans votre environnement de travail**. À la différence du Claude que vous utilisez dans un navigateur web, Claude Code s'intègre à vos fichiers, vos dossiers et vos outils du quotidien.

**Analogie concrète :** Imaginez un consultant expert qui s'installe à votre bureau. Il ouvre vos dossiers, lit vos documents, comprend le contexte de votre projet et vous aide en connaissant déjà tout le contexte — sans que vous ayez besoin de tout réexpliquer à chaque réunion.

### Claude Code vs l'application Claude : quelle différence ?

| | Application Claude (bureau/navigateur) | Claude Code (terminal) |
|---|---|---|
| **Installation** | Simple, comme une app classique | Nécessite un terminal |
| **Accès aux fichiers** | Uniquement par upload manuel | Lit et modifie vos fichiers directement |
| **Mémoire** | Limitée à la conversation | Persistante via CLAUDE.md |
| **Automatisation** | Manuelle | Possible (hooks, routines) |
| **Public cible** | Tous les salariés | Salariés souhaitant aller plus loin |

**Recommandation :** Commencez par l'application Claude si vous débutez. Passez à Claude Code quand vous souhaitez travailler directement sur vos fichiers et automatiser des tâches récurrentes.

---

## 2. Installation pas à pas

### 2.1 Installer l'application Claude (le plus simple)

L'application bureau Claude vous donne accès à Claude dans une interface familière, similaire à une messagerie. C'est le point d'entrée recommandé pour tous.

**Lien de téléchargement officiel :** [claude.ai/download](https://claude.ai/download)

Une fois installée, créez un compte sur [claude.ai](https://claude.ai) si ce n'est pas déjà fait. Votre compte vous donnera également accès à Claude Code.

### 2.2 Installer Claude Code (terminal)

Claude Code s'installe via un **terminal** (l'équivalent d'une fenêtre de commande). Pas d'inquiétude si vous n'en avez jamais utilisé — voici la marche à suivre étape par étape.

#### Étape 1 : Vérifier les prérequis

Claude Code nécessite **Node.js version 18 ou supérieure**.

- **Windows :** Téléchargez Node.js sur [nodejs.org](https://nodejs.org) et suivez l'installation standard (choisissez "LTS").
- **macOS :** Node.js est souvent déjà présent. Sinon, téléchargez-le sur [nodejs.org](https://nodejs.org).
- **Linux :** Utilisez le gestionnaire de paquets de votre distribution.

#### Étape 2 : Ouvrir un terminal

- **Windows :** Cherchez "PowerShell" ou "Invite de commandes" dans le menu Démarrer.
- **macOS :** Cherchez "Terminal" dans Spotlight (Cmd + Espace).
- **Linux :** Ctrl + Alt + T selon votre distribution.

#### Étape 3 : Installer Claude Code

Copiez-collez cette commande dans votre terminal et appuyez sur Entrée :

```bash
npm install -g @anthropic-ai/claude-code
```

> **Important :** N'utilisez pas `sudo` devant cette commande (risques de sécurité).

#### Étape 4 : Lancer Claude Code pour la première fois

```bash
claude
```

La première fois, Claude Code ouvrira votre navigateur pour vous connecter à votre compte Anthropic. Une fois authentifié, le token est stocké localement — vous n'aurez pas besoin de vous reconnecter.

**Documentation officielle d'installation :** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup)

#### Étape 5 : Vérifier l'installation

```bash
claude --version
```

Si un numéro de version s'affiche, l'installation est réussie. En cas de problème, tapez `/doctor` dans Claude Code pour un diagnostic automatique.

> **Mise à jour :** Claude Code se met à jour régulièrement. Prenez l'habitude de lancer `npm update -g @anthropic-ai/claude-code` chaque matin pour profiter des dernières améliorations. Lisez le journal des nouveautés avec `/changelog`.

---

## 3. Premiers pas

### 3.1 Se placer dans son dossier de travail

Avant de lancer Claude Code, naviguez vers le dossier sur lequel vous souhaitez travailler :

```bash
cd chemin/vers/votre/dossier
```

Exemples :
```bash
# Windows
cd C:\Users\votre-nom\Documents\mon-projet

# macOS / Linux
cd ~/Documents/mon-projet
```

### 3.2 Lancer Claude Code

```bash
claude
```

Vous voilà dans l'interface Claude Code. Vous pouvez lui parler en langage naturel, exactement comme dans l'application web.

### 3.3 Commandes de base à connaître

| Commande | Ce qu'elle fait |
|----------|-----------------|
| `/help` | Affiche l'aide et la liste des commandes disponibles |
| `/init` | Initialise Claude Code dans votre projet (crée le fichier CLAUDE.md) |
| `/clear` | Efface la conversation en cours |
| `/compact` | Compresse le contexte pour libérer de la mémoire |
| `/model` | Change le modèle utilisé (haiku, sonnet, opus) |
| `/doctor` | Diagnostique les problèmes d'installation ou de configuration |
| `/config` | Accède aux paramètres de configuration |
| `/usage` | Affiche votre consommation du plan |
| `/context` | Affiche le niveau d'utilisation du contexte |
| `/rename` | Renomme la session en cours pour la retrouver facilement |
| `/resume` | Reprend une session précédemment nommée |
| `/changelog` | Affiche les nouveautés de la dernière mise à jour |
| `Échap` | Interrompt Claude en cours d'exécution |
| `Échap Échap` | Revient en arrière (rewind) sur les dernières modifications |

### 3.4 Initialiser votre projet

Dans un nouveau dossier de travail, la première chose à faire est :

```bash
/init
```

Claude Code analyse votre dossier, comprend ce qu'il contient, et crée automatiquement un fichier `CLAUDE.md` — la mémoire persistante de votre projet (voir chapitre suivant).

---

## 4. CLAUDE.md — La mémoire persistante de votre projet

### Qu'est-ce que CLAUDE.md ?

`CLAUDE.md` est le fichier de mémoire de Claude pour votre projet. Il est **automatiquement chargé au début de chaque session** — vous n'avez pas besoin de réexpliquer le contexte à chaque fois.

**Analogie :** C'est le cahier de bord d'un technicien de maintenance. Chaque fois qu'un technicien prend son poste, il lit le cahier pour connaître l'état de la machine, les problèmes récents et les procédures à suivre.

### Où se trouve CLAUDE.md ?

Il peut exister à plusieurs niveaux :

| Emplacement | Portée |
|-------------|--------|
| `~/.claude/CLAUDE.md` | Vos paramètres personnels, tous projets confondus |
| `votre-projet/CLAUDE.md` | Ce projet spécifique (partagé avec l'équipe) |
| `votre-projet/.claude/rules/` | Règles modulaires chargées automatiquement |

> **Conseil de pro :** Gardez votre CLAUDE.md principal sous **200 lignes**. Au-delà, Claude peut ne plus respecter toutes les instructions. Utilisez `.claude/rules/` pour stocker les règles supplémentaires.

### Que mettre dans CLAUDE.md ?

Un bon CLAUDE.md répond à trois questions fondamentales :

```markdown
# QUOI — La nature de votre projet
Ce dossier contient les supports de formation en ingénierie pédagogique
pour le Pôle Formation UIMM-CVDL. Public cible : formateurs et ingénieurs.

# POURQUOI — L'objectif et les contraintes
- Ton : formel, institutionnel, aucun emoji
- Langue : français uniquement
- Format de sortie : Markdown, paragraphes de 3 phrases max
- Ce que je ne veux jamais lire : jargon marketing, formules creuses

# COMMENT — Les procédures de travail
- Pour créer un document : utiliser le template dans /modeles/
- Pour les comptes rendus : format QQOQCP obligatoire
- Signature de fin de courrier : "Le Pôle Formation UIMM reste à votre disposition."
```

### Charger des règles supplémentaires avec @

Vous pouvez importer d'autres fichiers dans votre CLAUDE.md :

```markdown
@.claude/rules/charte-redactionnelle.md
@.claude/rules/procedures-rh.md
```

Ces fichiers sont chargés à la demande (lazy-loading), ce qui préserve la mémoire de travail pour les projets complexes.

---

## 5. Les quatre piliers

L'écosystème Claude Code repose sur quatre types d'objets configurables, stockés dans le dossier `.claude/` de votre projet :

```
votre-projet/
├── CLAUDE.md                    ← Mémoire persistante
└── .claude/
    ├── commands/                ← Raccourcis de workflow (chapitre 6)
    ├── skills/                  ← Compétences réutilisables (chapitre 7)
    ├── agents/                  ← Assistants spécialisés (chapitre 8)
    ├── hooks/                   ← Actions automatiques (chapitre 9)
    └── settings.json            ← Configuration (chapitre 11)
```

| Pilier | Analogie métier | Cas d'usage type |
|--------|-----------------|------------------|
| **Commands** | Modèle de document, template | "Rédige un compte-rendu de réunion" |
| **Skills** | Procédure écrite, SOP | Vérification orthographique avant envoi |
| **Subagents** | Collaborateur spécialisé | Déléguer la recherche documentaire |
| **Hooks** | Règle automatique | Sauvegarder après chaque modification |

---

## 6. Commands — Vos raccourcis de workflow

### Définition

Les Commands sont des **modèles de tâches** que vous invoquez avec `/nom-de-la-commande`. Elles injectent des instructions dans la conversation en cours sans créer un nouveau contexte.

**Analogie :** C'est comme un modèle Word pré-rempli — vous l'appelez, et Claude sait exactement ce qu'il doit faire et comment le présenter.

### Créer une commande

Créez un fichier Markdown dans `.claude/commands/` :

**Exemple : `.claude/commands/compte-rendu.md`**

```markdown
---
description: Transforme des notes brutes en compte-rendu structuré QQOQCP
---

À partir des notes brutes qui suivent, génère un compte-rendu au format Markdown :

# 1. Décisions Clés
(Liste des décisions actées)

# 2. Plan d'Action (QQOQCP)
| Quoi | Qui | Où | Quand | Comment | Pourquoi |
| --- | --- | --- | --- | --- | --- |

# 3. Points en suspens
(Ce qui n'a pas été résolu)

**Règle absolue :** Si l'information "Qui" ou "Quand" est absente, écris "[À DÉFINIR]". Ne l'invente pas.

Notes brutes à traiter : $ARGUMENTS
```

Usage : `/compte-rendu [collez vos notes ici]`

### Commands intégrées utiles

Claude Code propose des commandes prêtes à l'emploi :

| Commande | Description |
|----------|-------------|
| `/review` | Analyse et critique un document ou du code |
| `/security-review` | Audit de sécurité |
| `/init` | Initialise le projet |
| `/compact` | Compresse le contexte |
| `/agents` | Gère les subagents |
| `/loop` | Lance une tâche répétitive locale (jusqu'à 7 jours) |
| `/schedule` | Planifie une tâche sur l'infrastructure cloud |
| `/focus` | Cache les étapes intermédiaires, affiche uniquement le résultat final |
| `/permissions` | Gère les droits d'accès aux outils |
| `/voice` | Active la dictée vocale |

> **Conseil :** Si vous répétez une même action plus d'une fois par jour, transformez-la en commande. C'est exactement le gain de temps que vous recherchez.

---

## 7. Skills — Vos compétences réutilisables

### Différence avec les Commands

| | Commands | Skills |
|---|---|---|
| **Chargement** | À la demande, via `/nom` | À la demande ou préchargé dans un agent |
| **Contexte** | Dans la conversation en cours | Peut être isolé (fork) |
| **Usage** | Workflows séquentiels | Procédures spécialisées, réutilisables |

### Structure d'un Skill

Les Skills se créent dans `.claude/skills/<nom>/SKILL.md` avec un en-tête YAML :

```markdown
---
name: verification-ortho
description: Vérifie l'orthographe et la cohérence stylistique d'un document
allowed-tools: Read
model: haiku
---

Analyse le document fourni et retourne :
1. La liste des fautes d'orthographe avec correction proposée
2. Les incohérences de style détectées (registre de langue, ponctuation)
3. Un score de qualité de 0 à 10

Fichier à analyser : $0
```

### Champs de configuration des Skills

| Champ | Rôle | Exemple |
|-------|------|---------|
| `name` | Nom affiché et commande `/` | `verification-ortho` |
| `description` | Quand Claude doit-il l'activer ? | "Vérifie l'orthographe..." |
| `argument-hint` | Aide à l'autocomplétion | `[nom-du-fichier]` |
| `model` | Modèle IA utilisé | `haiku` (rapide/économique), `opus` (puissant) |
| `context: fork` | Exécute dans un contexte isolé | Évite de polluer la conversation |
| `allowed-tools` | Outils autorisés | `Read, Write, Grep` |
| `user-invocable: false` | Masque du menu `/` | Utilisé comme connaissance pour un agent |
| `hooks` | Actions déclenchées pendant l'exécution | Notification de fin, log |

### Variables disponibles dans un Skill

| Variable | Valeur |
|----------|--------|
| `$ARGUMENTS` | Tous les arguments passés lors de l'invocation |
| `$0`, `$1`... | Argument par position |
| `` !`commande` `` | Résultat d'une commande shell injectée dynamiquement |

**Exemple pratique :**

```markdown
---
name: date-du-jour
description: Rappelle la date et l'heure actuelles
---

Voici le contexte temporal actuel :
!`date "+%d/%m/%Y %H:%M"`

Utilise cette information dans ta réponse.
```

### Portée et priorité des Skills

Si un Skill du même nom existe à plusieurs endroits, la priorité est :

1. `.claude/skills/` (projet en cours) — priorité maximale
2. `~/.claude/skills/` (tous vos projets)
3. Skills de plugins installés — priorité minimale

---

## 8. Subagents — Déléguer à des assistants spécialisés

### Qu'est-ce qu'un Subagent ?

Un Subagent est un **assistant IA spécialisé** qui travaille dans son propre contexte isolé. Vous lui déléguez une tâche, il l'exécute de manière autonome, puis vous rend son résultat.

**Analogie :** Vous êtes le chef de projet. Vous avez un assistant en charge de la documentation, un autre de la veille réglementaire, un autre du suivi des prestataires. Chacun a ses outils et son périmètre. Vous leur confiez des tâches sans tout faire vous-même.

### Agents intégrés à Claude Code

Claude Code propose des agents prêts à l'emploi :

| Agent | Rôle | Modèle |
|-------|------|--------|
| `general-purpose` | Tâches complexes multi-étapes | Hérite |
| `Explore` | Exploration rapide de fichiers (lecture seule) | Haiku |
| `Plan` | Conception d'un plan avant exécution | Hérite |
| `claude-code-guide` | Répond à vos questions sur Claude Code | Hérite |

### Créer un Subagent personnalisé

Créez un fichier dans `.claude/agents/` :

**Exemple : `.claude/agents/veille-documentaire.md`**

```markdown
---
name: veille-documentaire
description: Recherche et synthétise des informations documentaires sur demande
tools: Read, Grep, Glob, WebFetch
model: sonnet
color: teal
---

Tu es un assistant spécialisé en veille documentaire.
Lorsqu'on te confie une recherche, tu :
1. Explores systématiquement les documents disponibles
2. Identifies les informations pertinentes
3. Produis une synthèse structurée avec sources

Ne génère jamais d'information non trouvée dans les documents.
```

### Champs de configuration des Subagents

| Champ | Rôle |
|-------|------|
| `name` | Identifiant unique (minuscules, tirets) |
| `description` | Quand invoquer cet agent — écrivez "PROACTIVELY" pour une invocation automatique |
| `tools` | Liste des outils autorisés (Read, Write, Bash, WebFetch...) |
| `disallowedTools` | Outils explicitement interdits |
| `model` | `haiku`, `sonnet`, `opus`, ou `inherit` |
| `permissionMode` | `acceptEdits` (valide auto), `plan` (propose seulement) |
| `maxTurns` | Nombre max d'échanges avant arrêt |
| `skills` | Skills préchargés dans le contexte de l'agent |
| `memory` | Mémoire persistante : `user`, `project`, ou `local` |
| `background` | `true` pour exécution en tâche de fond |
| `isolation: worktree` | Travaille sur une copie isolée du projet |
| `color` | Couleur d'affichage dans le terminal |

### Portée de la mémoire des agents

| Scope | Stockage | Partagé avec l'équipe ? |
|-------|----------|-------------------------|
| `user` | `~/.claude/agent-memory/<nom>/` | Non |
| `project` | `.claude/agent-memory/<nom>/` | Oui (versionnée) |
| `local` | `.claude/agent-memory-local/<nom>/` | Non |

### Invoquer un agent

Pour déléguer une tâche à un agent, dites simplement à Claude :

> "Utilise l'agent veille-documentaire pour trouver toutes les références à la norme ISO 9001 dans mes documents."

Ou depuis un script :

```
Task(subagent_type="veille-documentaire", description="...", prompt="...")
```

> **Règle critique :** Les Subagents ne peuvent pas s'invoquer entre eux via le terminal. Ils communiquent uniquement via l'outil Agent (anciennement Task). Évitez les formulations vagues comme "lancer" qui pourraient être interprétées comme une commande bash.

> **Conseil de productivité :** Utilisez "use subagents" pour déléguer une tâche lourde et garder votre conversation principale légère et réactive.

---

## 9. Hooks — Automatiser les actions récurrentes

### Qu'est-ce qu'un Hook ?

Les Hooks sont des **déclencheurs automatiques** : quand un événement précis se produit dans Claude Code, une action définie s'exécute automatiquement — sans que vous ayez à y penser.

**Analogie :** Comme une alarme qui déclenche une lumière verte quand la porte est verrouillée. Vous n'avez pas à vérifier manuellement, le système s'en charge.

### Événements disponibles

| Événement | Quand il se déclenche |
|-----------|----------------------|
| `PreToolUse` | Avant qu'un outil soit utilisé |
| `PostToolUse` | Après qu'un outil a été utilisé |
| `UserPromptSubmit` | Quand vous envoyez un message |
| `Stop` | Quand Claude termine sa réponse |
| `SubagentStart` | Quand un agent démarre |
| `SubagentStop` | Quand un agent se termine |
| `SessionStart` | Au lancement d'une session |
| `SessionEnd` | À la fermeture d'une session |
| `Notification` | Quand Claude envoie une notification |
| `TaskCompleted` | Quand une tâche est complète |

### Exemples concrets de Hooks

**Notification sonore à la fin d'une tâche :**

```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "afplay /System/Library/Sounds/Glass.aiff"
      }]
    }]
  }
}
```

**Formatage automatique après chaque modification :**

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{
        "type": "command",
        "command": "prettier --write $FILE"
      }]
    }]
  }
}
```

**Bloquer les commandes destructives :**

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "./scripts/verifier-commande-dangereuse.sh"
      }]
    }]
  }
}
```

### Désactiver les Hooks

Si vous avez besoin de désactiver temporairement tous les hooks, ajoutez dans `.claude/settings.local.json` :

```json
{
  "disableAllHooks": true
}
```

---

## 10. MCP Servers — Connecter Claude à vos outils

### Qu'est-ce qu'un MCP Server ?

MCP (Model Context Protocol) est le standard qui permet à Claude de **se connecter à vos outils du quotidien** : messagerie, agenda, bases de données, logiciels métiers.

**Analogie :** Sans MCP, Claude vit dans une bulle. Avec MCP, il peut consulter votre agenda, lire vos e-mails, interroger votre base de données RH — sans que vous ayez à copier-coller les informations.

### Exemples de connecteurs populaires

| Connecteur | Ce que Claude peut faire |
|------------|--------------------------|
| **Gmail / Outlook** | Lire, rédiger, envoyer des e-mails |
| **Google Calendar / Outlook Calendar** | Lire l'agenda, créer des événements |
| **Slack / Teams** | Lire et envoyer des messages |
| **Notion / Confluence** | Accéder à vos bases de connaissances |
| **Google Drive / SharePoint** | Lire et créer des fichiers |
| **PostgreSQL / MySQL** | Interroger des bases de données |
| **GitHub** | Gérer des dépôts, lire du code |

### Configurer un MCP Server

Dans `.claude/settings.json` :

```json
{
  "mcpServers": {
    "gmail": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-gmail"]
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-slack"]
    }
  }
}
```

> Pour la liste complète des connecteurs disponibles, consultez le registre officiel : [github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

---

## 11. Settings — Configurer Claude Code

### Hiérarchie de configuration

Claude Code applique les paramètres dans cet ordre de priorité (du plus fort au plus faible) :

1. **Managed** (`managed-settings.json`) — Paramètres imposés par votre organisation IT, non modifiables
2. **Arguments CLI** — Options passées au lancement, valables pour une session
3. **`.claude/settings.local.json`** — Vos paramètres personnels sur ce projet (non partagés)
4. **`.claude/settings.json`** — Paramètres d'équipe partagés
5. **`~/.claude/settings.json`** — Vos paramètres globaux personnels

### Paramètres essentiels à connaître

```json
{
  "model": "claude-sonnet-4-6",
  "output": {
    "style": "explanatory"
  },
  "thinking": {
    "enabled": true
  },
  "statusLine": {
    "show": true
  }
}
```

> **Conseil :** Activez toujours `thinking: true` et le style de sortie "explanatory" dans `/config` — Claude produira des réponses plus raisonnées et transparentes.

### La barre de statut

La barre de statut en bas de l'interface affiche en temps réel :
- Le niveau d'utilisation du contexte (crucial pour savoir quand compresser)
- Le modèle en cours d'utilisation
- Le coût estimé de la session
- L'état de la session

---

## 12. Workflows et bonnes pratiques

### Le workflow universel

Tous les professionnels qui utilisent Claude Code efficacement suivent le même schéma :

```
Recherche → Plan → Exécution → Revue → Livraison
```

**En pratique :**

1. **Recherche :** "Analyse ce document et identifie les points critiques"
2. **Plan :** "Propose-moi une approche en 3 étapes pour traiter ces points"
3. **Exécution :** "Exécute l'étape 1"
4. **Revue :** "Vérifie que le résultat est conforme à nos exigences"
5. **Livraison :** "Formate le document final et envoie-le à l'équipe"

> **Conseil :** Utilisez toujours le mode plan (`/config` → Plan Mode) pour les tâches complexes avant de laisser Claude agir. Voyez le plan, validez-le, puis lancez l'exécution.

### 82 bonnes pratiques de la communauté (synthèse)

#### Sur la formulation des demandes

- Après une réponse décevante, demandez "Implémente une solution plus élégante" plutôt que de tout réexpliquer.
- La plupart des problèmes se résolvent seuls quand vous dites simplement "corrige ça" — ne sur-gérez pas.
- Ajoutez le mot-clé `ultrathink` dans vos prompts pour que Claude mobilise un raisonnement plus approfondi sur les problèmes complexes.

#### Sur la planification et les spécifications

- Commencez toujours par le mode plan pour les tâches complexes.
- Décomposez les grandes tâches en phases avec des points de validation intermédiaires.
- Faites relire votre plan par un second modèle pour avoir un regard critique externe.

#### Sur les sessions et le contexte

- Ouvrez une nouvelle session pour chaque nouvelle tâche ; gardez la même session pour des tâches connexes.
- Utilisez `/compact` avec des indications contextuelles plutôt que la compression automatique.
- Si le contexte devient trop lourd, notez un résumé de la progression, puis `/clear` pour repartir propre.
- Renommez vos sessions importantes avec `/rename` pour les retrouver avec `/resume`.

#### Sur CLAUDE.md et les règles

- Limitez votre CLAUDE.md principal à 200 lignes. Déléguez le reste à `.claude/rules/`.
- Vos règles dans `.claude/rules/` sont automatiquement chargées, comme CLAUDE.md.
- Le test de qualité d'un bon CLAUDE.md : un nouveau collaborateur devrait pouvoir exécuter la tâche principale du premier coup.

#### Sur les agents

- Créez des agents spécialisés par domaine métier, plutôt qu'un agent général.
- Dites "use subagents" pour déléguer une tâche lourde et garder votre conversation principale légère.
- Travaillez avec des équipes d'agents en parallèle sur des tâches indépendantes.

#### Sur les Skills

- La description d'un Skill est son déclencheur, pas son résumé — rédigez-la pour que Claude sache quand l'activer.
- Créez une section "Pièges connus" dans chaque Skill — c'est le contenu le plus utile.
- Donnez des objectifs et des contraintes à vos Skills, pas des instructions prescriptives étape par étape.

#### Sur les Hooks

- Utilisez un hook `PostToolUse` pour formater automatiquement les documents après modification.
- Utilisez un hook `Stop` pour vérifier que Claude a bien terminé avant de clore la session.
- Mesurez quels Skills sont réellement utilisés avec un hook `PreToolUse` — supprimez ceux qui ne servent jamais.

#### Sur Git et la gestion de versions

- Commitez souvent — au moins une fois par heure dès qu'une tâche est terminée.
- Gardez des modifications petites et ciblées (idéalement moins de 150 lignes modifiées à la fois).

#### Sur le débogage

- Prenez l'habitude de prendre des captures d'écran et de les partager avec Claude quand vous rencontrez un problème visuel.
- Utilisez `/doctor` pour diagnostiquer les problèmes d'installation ou de configuration.
- Lancez les tâches longues en tâche de fond pour une meilleure visibilité des logs.

---

## 13. Gestion du contexte

### Comprendre le "contexte"

Le contexte, c'est la quantité de texte que Claude peut "voir" en même temps — sa fenêtre de travail. Quand il se remplit, Claude commence à oublier ce qui était au début.

**Règle d'or :** Ne dépassez pas 40% du contexte pour des tâches importantes. Au-delà de 60%, la qualité des réponses baisse.

### Signaux d'alerte

- Claude répète des informations déjà données
- Claude semble ignorer des contraintes établies en début de session
- La barre de statut indique un niveau de contexte élevé

### Actions correctives

| Situation | Action recommandée |
|-----------|-------------------|
| Contexte à 40-60% | `/compact` avec un résumé de ce qui est important |
| Tâche terminée, nouvelle tâche | Nouvelle session (`/clear`) |
| Session longue, résultats incohérents | `/rewind` pour revenir avant la dérive |
| Tâche complexe à déléguer | Utilisez un Subagent (son contexte est séparé) |

> **Conseil clé :** Préférez `/rewind` à "corrige ton erreur" — laisser une tentative ratée dans le contexte pollue la session.

---

## 14. Fonctionnalités avancées

### Routines — Automatisation cloud

Les Routines permettent à Claude de travailler **même quand votre ordinateur est éteint**, sur l'infrastructure Anthropic. Vous pouvez déclencher des tâches :
- À heure fixe (ex : rapport quotidien à 8h)
- Via une API externe
- Depuis des événements GitHub

Commande : `/schedule` dans Claude Code ou via le tableau de bord cloud.

### Ultrareview — Revue multi-agents

Ultrareview lance une revue approfondie d'un document ou d'un code avec **plusieurs agents travaillant en parallèle**, chacun vérifiant indépendamment les conclusions des autres. Durée : 5 à 10 minutes. Coût estimé : 5 à 20 €.

Idéal pour : les documents critiques avant signature, les procédures de sécurité, les rapports d'audit.

### Computer Use — Claude contrôle votre écran

Claude peut prendre le contrôle de votre bureau pour cliquer, remplir des formulaires, naviguer dans des applications. Disponible sur macOS.

**Usage type :** Remplir automatiquement des formulaires administratifs répétitifs dans des applications métier qui n'ont pas d'API.

### Voice Dictation — Dictée vocale

Activez la dictée vocale avec `/voice` ou un raccourci clavier. Claude transcrit votre discours en commandes. Supporte 20 langues dont le français.

**Usage type :** Rédiger un compte-rendu après une réunion sans toucher le clavier.

### Channels — Intégration messagerie

Connectez Telegram, Discord ou des webhooks à votre session Claude Code. Claude reçoit et traite des événements pendant que vous êtes absent.

**Usage type :** Recevoir une alerte sur Telegram quand Claude a terminé une tâche longue.

### Ultraplan — Planification assistée

Générez un plan détaillé dans le cloud, révisez-le dans votre navigateur avec des commentaires inline, puis validez l'exécution.

**Usage type :** Planification d'un projet complexe impliquant plusieurs parties prenantes.

### Code Review Multi-agents

Analysez un document ou du code avec plusieurs agents travaillant en parallèle pour détecter les bugs, les incohérences et les risques.

**Usage type :** Revue d'une procédure qualité avant déploiement terrain.

### Agent Teams + Git Worktrees

Faites travailler plusieurs agents **en parallèle sur des tâches différentes**, chacun sur sa propre copie du projet. Ideal pour les projets volumineux.

**Usage type :** Un agent met à jour les procédures de maintenance pendant qu'un autre met à jour le catalogue des équipements.

### Tâches planifiées

Trois surfaces disponibles pour les tâches récurrentes :

| Surface | Durée max | Infrastructure |
|---------|-----------|----------------|
| `/loop` | 7 jours | Votre machine |
| `/schedule` | Illimité | Cloud Anthropic |
| Desktop Tasks | Variable | Votre machine |

---

## 15. Cas d'usage par métier

### Formateur / Ingénieur pédagogique

**Situation :** Vous devez concevoir un module de formation pour des techniciens de maintenance sur une nouvelle norme.

**Comment Claude Code peut vous aider :**

Créez un agent spécialisé `.claude/agents/ingenierie-pedagogique.md` :

```markdown
---
name: ingenierie-pedagogique
description: Conçoit des modules de formation selon l'ingénierie pédagogique UIMM
tools: Read, Write, Edit
model: sonnet
skills:
  - referentiels-rncp
  - charte-pedagogique
---

Tu es un ingénieur pédagogique expert des formations industrielles.
Tu structures chaque module selon : Objectifs → Contenus → Méthodes → Évaluation.
Tu intègres les référentiels RNCP et les contraintes terrain (temps machine, groupes hétérogènes).
```

**Tâches courantes :**
- Transformer une prise de notes terrain en scénario d'atelier structuré
- Générer des exercices pratiques calibrés par niveau (BTS vs Bac Pro)
- Créer une grille d'évaluation cohérente avec les objectifs du module
- Mettre à jour les supports quand une norme change

**Gain de temps estimé :** 2 à 4 heures par module de formation.

---

### Ressources Humaines

**Situation :** Vous gérez le suivi de 40 apprentis sur trois sites. La gestion documentaire est chronophage.

**Commande utile : `.claude/commands/suivi-apprenti.md`**

```markdown
---
description: Génère un courrier de suivi pour un apprenti selon la situation
---

Génère un courrier de suivi RH pour un apprenti UIMM en situation de $0.

Contraintes absolues :
- Ton formel et institutionnel
- Référencer les textes légaux applicables
- Signature : "Le Pôle Formation UIMM reste à votre disposition."
- Aucun emoji, aucun jargon marketing
```

**Tâches courantes :**
- Rédiger des relances pour pièces manquantes
- Synthétiser les entretiens tripartites
- Générer les comptes rendus de réunion pédagogique
- Analyser les taux d'absentéisme et identifier les situations à risque

**Avec MCP Gmail :** Claude lit les e-mails entrants, identifie les apprentis concernés, génère les courriers de réponse, vous soumet pour validation avant envoi.

---

### Ingénieur industriel / Responsable maintenance

**Situation :** Vous intervenez sur site, prenez des notes rapides, et devez produire une SOP (Standard Operating Procedure) formalisée.

**Commande utile : `.claude/commands/note-en-sop.md`**

```markdown
---
description: Transforme des notes d'intervention en SOP structurée
---

À partir de ces notes d'intervention brutes, génère une SOP (Standard Operating Procedure)
au format technique industriel UIMM. Inclure :

1. Contexte et machine concernée
2. Conditions préalables (consignation, EPI)
3. Étapes numérotées avec vérifications
4. Critères d'acceptation
5. Actions correctives si échec

Si une information est manquante, pose-moi des questions une par une avant de rédiger.

Notes brutes : $ARGUMENTS
```

**Tâches courantes :**
- Transformer des notes manuscrites en procédures formalisées
- Mettre à jour les modes opératoires après modification d'équipement
- Générer des rapports d'audit après inspection terrain
- Croiser les données de panne pour identifier des tendances

**Exercice anti-hallucination :** Pour les spécifications techniques critiques, demandez toujours à Claude de citer sa source. S'il ne peut pas, il doit l'indiquer explicitement. Testez régulièrement en posant des questions sur des données fictives.

---

### Personnel administratif / Secrétariat

**Situation :** Vous gérez les courriers entrants, les plannings, les convocations, les comptes rendus.

**Fichier d'identité : `~/.claude/CLAUDE.md`**

```markdown
# Mon identité professionnelle
Assistante administrative du Pôle Formation UIMM-CVDL.
Public : formateurs, apprentis, entreprises partenaires, administration OPCO.

# Règles de communication
- Ton : formel, direct, professionnel
- Aucun emoji, aucune familiarité
- Paragraphes courts (3 phrases max)
- Format de date : JJ/MM/AAAA
- Heure : format 24h

# Formules obligatoires
- Fin de courrier : "Veuillez agréer, [civilité], l'expression de nos salutations distinguées."
- Signature : "[Prénom Nom] | Pôle Formation UIMM-CVDL | [téléphone]"
```

**Tâches courantes :**
- Rédiger convocations, relances, accusés de réception
- Transformer des e-mails reçus en tâches à traiter
- Préparer les dossiers de réunion
- Générer les ordres du jour à partir d'une liste de sujets

**Avec MCP Calendar :** Claude consulte votre agenda, propose des créneaux disponibles, rédige les convocations et les envoie directement.

---

### Manager / Responsable d'équipe

**Situation :** Vous pilotez une équipe de 8 personnes, animez des réunions, suivez des projets et rendez compte à votre direction.

**Agent utile : `.claude/agents/chef-de-projet.md`**

```markdown
---
name: chef-de-projet
description: Assiste le management opérationnel et la communication d'équipe
tools: Read, Write, Edit, WebFetch
model: sonnet
memory: project
---

Tu assistes un responsable d'équipe dans son management opérationnel.
Tu produis des communications claires, des tableaux de bord synthétiques
et des plans d'action réalistes. Tu ne prends jamais de décision à la place
du manager — tu proposes, il valide.
```

**Tâches courantes :**
- Transformer un compte-rendu brut en rapport exécutif
- Générer un tableau de bord hebdomadaire à partir de données d'activité
- Préparer les entretiens individuels (questions, points à aborder)
- Rédiger les communications d'équipe (annonces, rappels, félicitations)
- Analyser des données de performance et identifier les actions prioritaires

**Avec Routines :** Chaque lundi matin à 8h, Claude génère automatiquement un récapitulatif de la semaine précédente et un point sur les priorités de la semaine en cours.

---

## 16. Ressources et liens utiles

### Liens officiels Anthropic

| Ressource | Lien |
|-----------|------|
| Télécharger l'app Claude | [claude.ai/download](https://claude.ai/download) |
| Documentation Claude Code | [code.claude.com/docs](https://code.claude.com/docs) |
| Installation avancée | [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) |
| Plugins officiels | [github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| Changelog Claude Code | [github.com/anthropics/claude-code/blob/main/CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| API et tarifs | [platform.claude.com](https://platform.claude.com) |

### Ressources communautaires

| Ressource | Lien |
|-----------|------|
| Repo best practices (source de ce guide) | [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) |
| Reddit Claude Code | [reddit.com/r/ClaudeCode](https://reddit.com/r/ClaudeCode) |
| Reddit Claude AI | [reddit.com/r/ClaudeAI](https://reddit.com/r/ClaudeAI) |

### Collections de Skills

| Collection | Contenu |
|------------|---------|
| anthropics/skills | 17 skills officiels Anthropic |
| mattpocock/skills | 18 skills orientés ingénierie |
| wshobson/agents | 152 agents spécialisés |

### Glossaire rapide

| Terme | Définition simple |
|-------|------------------|
| **CLAUDE.md** | Fichier de mémoire persistante — ce que Claude lit à chaque démarrage |
| **Command** | Raccourci de tâche invoqué avec `/nom-commande` |
| **Skill** | Procédure réutilisable, peut être préchargée dans un agent |
| **Subagent** | Assistant spécialisé qui travaille dans son propre contexte isolé |
| **Hook** | Déclencheur automatique lié à un événement |
| **MCP Server** | Connecteur vers un outil externe (Gmail, Calendar, etc.) |
| **Contexte** | La "mémoire de travail" de Claude pour une session |
| **/compact** | Comprimer le contexte pour libérer de la mémoire |
| **/rewind** | Annuler les dernières modifications et revenir en arrière |
| **Fork** | Exécuter un skill dans un contexte complètement isolé |
| **Worktree** | Copie isolée du projet pour un agent, sans risque |
| **Routine** | Tâche automatisée exécutée sur le cloud, même PC éteint |
| **Ultrareview** | Revue approfondie par plusieurs agents en parallèle |

---

*Guide rédigé en mai 2026 par S. JAUBERT pour le Pôle Formation UIMM-CVDL.*  
*Basé sur le repository [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) de Shan Raisshan et les contributions de Boris Cherny (créateur de Claude Code).*
