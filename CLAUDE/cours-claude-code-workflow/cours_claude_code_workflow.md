# Masterclass : Claude Code & Workflow

**Pôle Formation UIMM - CVDL | Formateur : S. JAUBERT**

---

> Ce cours s'adresse à des salariés d'entreprise souhaitant maîtriser Claude Code et son écosystème de fichiers de configuration, de compétences (Skills), de déclencheurs automatiques (Hooks) et de workflow quotidien. Aucune connaissance préalable en développement n'est requise.

---

## Table des Matières

1. [Premiers Pas — Installer et lancer Claude Code](#1-premiers-pas)
2. [Comprendre CLAUDE.md — La mémoire persistante](#2-comprendre-claudemd)
3. [Hiérarchie mémoire — Les 4 niveaux de contexte](#3-hiérarchie-mémoire)
4. [Bonnes pratiques avec Claude](#4-bonnes-pratiques)
5. [Structure des fichiers d'un projet](#5-structure-des-fichiers)
6. [Les Skills — Le superpouvoir de Claude](#6-les-skills)
7. [Skills populaires — Exemples concrets](#7-skills-populaires)
8. [Configuration des Hooks — Automatiser la sécurité](#8-configuration-des-hooks)
9. [Permissions & Sécurité — Ce que Claude peut faire](#9-permissions-et-sécurité)
10. [L'architecture en 4 Couches](#10-larchitecture-en-4-couches)
11. [Modèle de workflow quotidien](#11-workflow-quotidien)
12. [Commandes clavier essentielles](#12-commandes-clavier)

---

## 1. Premiers Pas

### Qu'est-ce que Claude Code ?

Claude Code est un **assistant IA de développement en ligne de commande** (terminal). Contrairement aux chatbots classiques que l'on utilise dans un navigateur, Claude Code s'intègre directement dans votre environnement de travail : il peut lire vos fichiers, proposer des modifications, exécuter des commandes et comprendre la structure de votre projet.

**Analogie** : Imaginez un expert consultant qui s'installe à votre bureau, ouvre votre dossier de travail, lit tous vos documents et vous aide en connaissant déjà tout le contexte de votre projet — plutôt que de devoir tout lui expliquer à chaque fois.

### Installation

**Prérequis** : Node.js version 18 ou supérieure doit être installé sur votre machine.

```bash
# Étape 1 : Installer Claude Code globalement
curl -fsSL https://claude.ai/install.sh | bash

# Étape 2 : Se placer dans votre projet
cd votre-projet

# Étape 3 : Lancer Claude Code
claude

# Étape 4 : Initialiser la mémoire du projet
/init
```

### Que fait la commande `/init` ?

La commande `/init` est une étape cruciale. Elle **analyse l'intégralité de votre projet** (fichiers, structure, technologies utilisées) et crée automatiquement un fichier `CLAUDE.md` à la racine. Ce fichier sera le point de départ de la mémoire de Claude pour toutes vos sessions futures.

**Exemple de ce que Claude analyse** :
- Quel langage de programmation est utilisé (Python, JavaScript, etc.)
- Quel framework (React, Django, etc.)
- Quelles commandes sont disponibles (`npm run dev`, `python manage.py runserver`, etc.)
- La structure des dossiers

---

## 2. Comprendre CLAUDE.md

### Définition

`CLAUDE.md` est le **fichier de mémoire persistante** de Claude pour votre projet. Il est **chargé automatiquement au début de chaque session** : vous n'avez pas à tout réexpliquer à chaque fois que vous recommencez à travailler.

**Analogie** : C'est comme le cahier de bord d'un technicien de maintenance. Chaque fois qu'un technicien prend son poste, il lit le cahier pour connaître l'état de la machine, les problèmes récents et les procédures à suivre. CLAUDE.md joue ce rôle pour l'IA.

### Structure recommandée d'un CLAUDE.md

Un bon fichier CLAUDE.md répond à trois questions fondamentales :

| QUOI | POURQUOI | COMMENT |
|------|----------|---------|
| Stack technique | Objectif de chaque composant | Commandes de build/test |
| Arborescence du projet | Décisions de design | Workflows |
| Architecture générale | Contraintes métier | Points d'attention (Gotchas) |

### Exemple concret : Projet MonApp

```markdown
# Projet : MonApp
API REST FastAPI + SPA React + PostgreSQL

## Objectif
Application de suivi de production pour l'atelier d'usinage.
Permet aux opérateurs de saisir les données de contrôle qualité.

## Stack technique
- Backend : Python FastAPI (API REST)
- Frontend : React (interface utilisateur)
- Base de données : PostgreSQL
- Déploiement : Docker sur serveur interne

## Commandes essentielles
npm run dev        # Démarrer le serveur de développement
npm run test       # Lancer les tests automatiques
npm run lint       # Vérifier la qualité du code

## Architecture
/app     → pages Next.js (App Router, pages de l'interface)
/lib     → utilitaires partagés (fonctions communes)
/prisma  → Schéma DB & migrations (structure de la base de données)

## Règles de travail
- Toujours écrire les commentaires en français
- Valider les données côté serveur avant d'insérer en base
- Ne jamais stocker de mots de passe en clair

## Points d'attention (Gotchas)
- La connexion PostgreSQL nécessite le VPN interne
- Les tests peuvent prendre 2-3 minutes (base de test volumineuse)
```

### Exemple générique pour un service RH

```markdown
# Projet : Portail RH
Application web de gestion des congés et formations

## Stack technique
- Microsoft SharePoint pour l'hébergement
- Power Apps pour les formulaires
- Power Automate pour les workflows de validation

## Commandes
(aucune commande technique — déploiement via interface graphique)

## Processus métier
- Demandes de congés → validation manager → notification RH
- Formations → inscription → validation budget → convocation

## Règles importantes
- RGPD : ne jamais inclure de données personnelles dans les logs
- Toujours conserver un historique des modifications
```

---

## 3. Hiérarchie Mémoire

### Principe

Claude peut avoir plusieurs fichiers `CLAUDE.md` à différents niveaux de votre système de fichiers. Ils sont **tous chargés en même temps**, du plus global au plus spécifique. Le fichier le plus local **affine** le contexte sans **écraser** le contexte global.

### Les 4 niveaux

```
~/.claude/CLAUDE.md              ← Niveau 1 : Global (tous vos projets)
        ↓
/monorepo/CLAUDE.md              ← Niveau 2 : Racine du dépôt (projet parent)
        ↓
/monorepo/.claude/CLAUDE.md      ← Niveau 3 : Configuration locale (ignorée par Git)
        ↓
/monorepo/frontend/CLAUDE.md     ← Niveau 4 : Sous-dossier (contexte limité)
```

### Règles d'or

- **Gardez chaque fichier sous 200 lignes** : Au-delà, la mémoire de Claude se charge trop lentement et le contexte se dilue.
- **Les fichiers de sous-dossier ajoutent du contexte** : Ils ne remplacent pas, ils complètent.
- **N'écrasez jamais le contexte parent** : Si le fichier global dit "utiliser Python 3.11", le fichier local ne doit pas contredire cela sans raison valable.

### Exemple pratique

**`~/.claude/CLAUDE.md`** (votre profil global) :
```markdown
# Préférences globales de Jean-Pierre
- Langue : toujours répondre en français
- Style de code : commentaires en français, noms de variables en anglais
- Jamais de données sensibles dans les exemples
```

**`/projet-usine/CLAUDE.md`** (spécifique au projet) :
```markdown
# Projet Usine — Contrôle Qualité
Ce projet gère les données de contrôle qualité de la ligne 3.

## Technologies
Python + SQLite + Pandas

## Règles métier
- Les valeurs hors tolérance doivent déclencher une alerte
- Conserver 3 ans d'historique minimum (obligations réglementaires)
```

**`/projet-usine/rapports/CLAUDE.md`** (sous-dossier rapports) :
```markdown
# Module Rapports
Ce sous-dossier génère les rapports PDF mensuels.
Utiliser la bibliothèque ReportLab. Format : A4 portrait, logo en en-tête.
```

---

## 4. Bonnes Pratiques avec Claude

### Les 7 règles d'or

**1. Exécutez `/init` d'abord, puis affinez**
Ne commencez pas à demander des choses à Claude avant de l'avoir initialisé. Laissez-le analyser votre projet, puis complétez ce qu'il a généré.

**2. Soyez précis dans les instructions**
Au lieu de dire : *"Améliore ce code"*
Dites : *"Améliore les performances de la fonction `calculer_moyenne()` en utilisant NumPy plutôt qu'une boucle for."*

**3. Ajoutez les pièges que Claude ne peut pas deviner**
Documentez dans CLAUDE.md les contraintes non-évidentes :
- *"Le serveur de test est souvent lent le mardi matin."*
- *"Ne pas utiliser la librairie X, elle a un problème de licence."*

**4. Référencez les docs avec `@nomfichier`**
Vous pouvez mentionner des fichiers spécifiques dans vos demandes :
```
@CLAUDE.md Mets à jour la section Architecture avec le nouveau module de paiement.
```

**5. Ajoutez des règles de workflow**
Dans CLAUDE.md, indiquez votre façon de travailler :
```markdown
## Workflow équipe
- Toujours créer une branche Git avant de modifier du code
- Faire valider par un collègue avant de merger
- Les tests doivent passer avant tout déploiement
```

**6. Gardez la mémoire concise**
Revoyez régulièrement CLAUDE.md et supprimez les informations obsolètes. Un fichier de 50 lignes est plus efficace qu'un fichier de 500 lignes.

**7. Commitez sur Git pour le partage en équipe**
Incluez CLAUDE.md dans votre dépôt Git. Ainsi, tous les membres de l'équipe bénéficient du même contexte partagé.

---

## 5. Structure des Fichiers d'un Projet

### Arborescence standard

Voici la structure de fichiers recommandée pour un projet utilisant Claude Code :

```
votre-projet/
├── CLAUDE.md                    ← Mémoire persistante du projet
├── .claude/                     ← Dossier de configuration Claude
│   ├── settings.json            ← Paramètres (permissions, hooks)
│   └── settings.local.json      ← Paramètres locaux (non partagés)
├── skills/                      ← Vos compétences personnalisées
│   ├── code-review/
│   │   └── SKILL.md             ← Skill : revue de code
│   └── testing/
│       ├── SKILL.md             ← Skill : tests automatisés
│       └── helpers.py           ← Fichier support du skill
├── commands/
│   └── deploy.md                ← Commande personnalisée : déploiement
├── agents/
│   └── security-reviewer.md     ← Agent spécialisé : audit sécurité
└── .gitignore                   ← Fichiers à exclure de Git
```

### Rôle de chaque élément

| Fichier/Dossier | Rôle | Analogie métier |
|-----------------|------|-----------------|
| `CLAUDE.md` | Mémoire et règles du projet | Cahier de bord technique |
| `.claude/settings.json` | Permissions et hooks | Règlement intérieur |
| `skills/` | Compétences spécialisées | Fiches de postes |
| `commands/deploy.md` | Procédures automatisées | Mode opératoire |
| `agents/` | Sous-experts spécialisés | Équipes dédiées |

### Exemple : `commands/deploy.md`

```markdown
# Commande : Déployer en production

## Description
Lance le processus de déploiement complet vers le serveur de production.

## Étapes
1. Vérifier que tous les tests passent (`npm run test`)
2. Construire l'application (`npm run build`)
3. Vérifier les variables d'environnement (`NODE_ENV=production`)
4. Envoyer sur le serveur (`rsync -avz dist/ serveur:/var/www/app`)
5. Redémarrer le service (`sudo systemctl restart monapp`)
6. Vérifier que l'application répond (http://monserveur/health)

## En cas d'erreur
Si l'étape 4 échoue : vérifier la connexion VPN au réseau interne.
Contacter l'administrateur système : poste 2847.
```

---

## 6. Les Skills — Le Superpouvoir de Claude

### Qu'est-ce qu'un Skill ?

Un **Skill** (compétence) est un **guide Markdown que Claude auto-invoque via le langage naturel**. Quand vous demandez quelque chose à Claude, il cherche automatiquement s'il existe un Skill correspondant et l'utilise comme guide d'expert.

**Analogie** : Les Skills sont comme des **fiches de procédures** dans un classeur d'atelier. Quand un opérateur a besoin d'effectuer une tâche spécifique (changer un outil, calibrer une machine), il consulte la fiche correspondante. Claude fait de même automatiquement.

### Deux types de Skills

**Skill de projet** (partagé avec l'équipe) :
```
.claude/skills/<nom>/SKILL.md
```

**Skill personnel** (pour vous seul, tous projets) :
```
~/.claude/skills/<nom>/SKILL.md
```

### Structure d'un SKILL.md

```markdown
---
name: nom-du-skill
description: Description précise de ce que fait ce skill (TRÈS IMPORTANT pour l'auto-activation)
allowed-tools: Read, Grep, Bash, Write
---

# Nom du Skill

## Quand utiliser ce skill
[Conditions d'activation]

## Procédure
[Étapes détaillées]

## Exemples
[Exemples concrets]
```

> **Point clé** : Le champ `description` est **essentiel pour l'auto-activation**. Claude lit cette description pour décider si le skill correspond à votre demande. Une description vague = skill jamais utilisé.

### Exemple 1 : Skill de revue de code

```markdown
---
name: code-review
description: Effectue une revue de code professionnelle en vérifiant la lisibilité, la sécurité, les performances et le respect des bonnes pratiques
allowed-tools: Read, Grep
---

# Revue de Code

## Checklist de vérification
- [ ] Les noms de variables sont explicites
- [ ] Les fonctions font une seule chose
- [ ] Les cas d'erreur sont gérés
- [ ] Pas de données sensibles en dur (mots de passe, clés API)
- [ ] Les commentaires expliquent le "pourquoi", pas le "comment"

## Format du rapport
Pour chaque problème trouvé :
- **Fichier et ligne** : où se trouve le problème
- **Sévérité** : Critique / Important / Mineur
- **Description** : ce qui pose problème
- **Suggestion** : comment corriger

## Critères de priorité
- CRITIQUE : faille de sécurité, bug bloquant
- IMPORTANT : performance, maintenabilité
- MINEUR : style, cosmétique
```

### Exemple 2 : Skill de documentation

```markdown
---
name: documentation-technique
description: Génère ou met à jour la documentation technique d'un module ou d'une fonction en français, au format Markdown
allowed-tools: Read, Write
---

# Documentation Technique

## Structure à produire
1. **Description** : À quoi sert ce code ?
2. **Paramètres d'entrée** : Quelles données reçoit-il ?
3. **Valeur de retour** : Que produit-il ?
4. **Exemple d'utilisation** : Code concret
5. **Cas d'erreur** : Que se passe-t-il si ça échoue ?

## Style
- Écrire en français
- Utiliser des analogies métier quand possible
- Inclure un exemple minimal qui fonctionne
```

### Exemple 3 : Skill de messages de commit Git

```markdown
---
name: commit-messages
description: Formule des messages de commit Git clairs, structurés et en français selon la convention Conventional Commits
allowed-tools: Bash
---

# Messages de Commit

## Convention
[TYPE]: Résumé court en français (max 72 caractères)

Corps optionnel : pourquoi ce changement ?

## Types disponibles
- feat: nouvelle fonctionnalité
- fix: correction de bug
- docs: documentation uniquement
- refactor: amélioration sans changement de comportement
- test: ajout ou modification de tests
- chore: tâches de maintenance

## Exemples
feat: ajouter la validation des données de formulaire de congés
fix: corriger le calcul des jours ouvrés lors des ponts
docs: mettre à jour le README avec les instructions d'installation
```

---

## 7. Skills Populaires — Exemples Concrets

Voici des exemples de Skills fréquemment utilisés en entreprise :

### `code-review` — Revue de code
**Utilisation** : *"Fais une revue de ce fichier avant que je l'envoie en production."*

### `testing-patterns` — Modèles de test
**Utilisation** : *"Écris des tests pour cette fonction."*

Approche AAA (Arrange, Act, Assert) :
```python
# Arrange : préparer les données
donnees = [10, 20, 30, 40, 50]

# Act : exécuter la fonction à tester
resultat = calculer_moyenne(donnees)

# Assert : vérifier le résultat
assert resultat == 30.0
```

### `commit-messages` — Messages de commit
**Utilisation** : *"Propose un message de commit pour ces modifications."*

### `docker-deploy` — Déploiement Docker
**Utilisation** : *"Déploie cette application avec Docker."*

Exemple de fichier support `deploy.md` :
```markdown
# Déploiement Docker

## Étapes standard
1. `docker build -t monapp:latest .`
2. `docker run -d -p 80:3000 --name monapp monapp:latest`
3. Vérifier : `docker ps` et `curl http://localhost/health`

## En cas d'erreur
- Port déjà utilisé : `docker stop $(docker ps -q)` puis réessayer
- Image corrompue : `docker rmi monapp:latest` puis rebuilder
```

### `codebase-visualizer` — Visualisation du code
**Utilisation** : *"Génère un diagramme de l'architecture de ce projet."*

### `api-design` — Conception d'API
**Utilisation** : *"Conçois l'API REST pour ce module de gestion des stocks."*

---

## 8. Configuration des Hooks

### Qu'est-ce qu'un Hook ?

Un **Hook** est un **callback déterministe** : c'est un script qui s'exécute **automatiquement** à des moments précis de l'interaction avec Claude.

**Analogie** : Les Hooks sont comme les **procédures de sécurité** dans une usine — des contrôles qui s'exécutent automatiquement à des étapes définies, indépendamment de l'opérateur. Avant de démarrer la machine (PreToolUse), après l'arrêt (PostToolUse), ou pour notification.

### Les 3 types de Hooks

| Type | Quand s'exécute-t-il ? | Utilisation typique |
|------|------------------------|---------------------|
| `PreToolUse` | Avant qu'un outil soit utilisé | Vérifications de sécurité |
| `PostToolUse` | Après qu'un outil a été utilisé | Nettoyage, journalisation |
| `Notification` | Pour envoyer des alertes | Notify sur Teams/Slack |

### Exemple de configuration des Hooks

Dans `.claude/settings.json` :

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/securite.sh",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

**Que fait ce Hook ?**
- Il s'active avant chaque exécution d'une commande Bash
- Il lance le script `securite.sh` qui peut vérifier les permissions
- Timeout de 5 secondes : si le script prend plus de 5s, il est abandonné

### Codes de sortie (Exit codes)

Le résultat d'un Hook détermine si Claude continue ou s'arrête :

| Code | Signification | Exemple |
|------|---------------|---------|
| `0` | Autoriser l'action | Tout est OK, continuer |
| `2` | Bloquer l'action | Opération non autorisée |

### Exemple concret : Script de sécurité

```bash
#!/bin/bash
# scripts/securite.sh
# Vérifie que Claude ne modifie pas des fichiers critiques

FICHIER_CIBLE="$1"
FICHIERS_PROTEGES=("config/production.env" "secrets/" "backup/")

for protected in "${FICHIERS_PROTEGES[@]}"; do
    if [[ "$FICHIER_CIBLE" == *"$protected"* ]]; then
        echo "ERREUR : Modification interdite sur $protected"
        exit 2  # Bloquer l'action
    fi
done

exit 0  # Autoriser l'action
```

---

## 9. Permissions et Sécurité

### Principe

Claude ne peut accéder qu'aux ressources que vous lui autorisez explicitement. La configuration des permissions se fait dans `.claude/settings.json`.

**Analogie** : C'est comme les **droits d'accès** dans un immeuble de bureaux. Une carte badge peut ouvrir certaines portes (autorisées) mais pas d'autres (refusées). On ne donne pas les clés de toute l'usine à tout le monde.

### Structure des permissions

```json
{
  "permissions": {
    "allow": [
      "Read:*",
      "Bash:git:*",
      "Write:*:*:*.md"
    ],
    "deny": [
      "Read:env:*",
      "Bash:sudo:*"
    ]
  }
}
```

### Décryptage des règles

**Syntaxe** : `Action:Ressource:Pattern`

| Règle | Signification |
|-------|---------------|
| `Read:*` | Peut lire tous les fichiers |
| `Bash:git:*` | Peut exécuter toutes les commandes `git` |
| `Write:*:*:*.md` | Peut écrire uniquement les fichiers `.md` |
| `Read:env:*` | **INTERDIT** : ne pas lire les variables d'environnement (mots de passe !) |
| `Bash:sudo:*` | **INTERDIT** : ne pas exécuter de commandes administrateur |

### Exemple de politique de sécurité pour une PME

```json
{
  "permissions": {
    "allow": [
      "Read:*",
      "Bash:npm:*",
      "Bash:git:*",
      "Write:src:*",
      "Write:docs:*"
    ],
    "deny": [
      "Read:*.env",
      "Read:secrets:*",
      "Bash:sudo:*",
      "Bash:rm:-rf:*",
      "Write:config/production:*"
    ]
  }
}
```

**Ce que Claude PEUT faire** :
- Lire tous les fichiers du projet
- Lancer `npm` (installer des paquets, lancer des scripts)
- Utiliser `git` (commit, push, pull)
- Écrire dans les dossiers `src` et `docs`

**Ce que Claude NE PEUT PAS faire** :
- Lire les fichiers `.env` (contiennent les mots de passe)
- Accéder au dossier `secrets`
- Utiliser `sudo` (droits administrateur)
- Supprimer des dossiers entiers (`rm -rf`)
- Modifier la configuration de production

---

## 10. L'Architecture en 4 Couches

### Vue d'ensemble

Claude Code fonctionne selon une architecture en 4 couches superposées, chacune avec un rôle précis :

```
┌─────────────────────────────────┐
│  L1 – CLAUDE.md                 │  Contexte et règles persistants
│  "La mémoire long terme"        │
├─────────────────────────────────┤
│  L2 – Skills                    │  Packs de connaissances auto-invoqués
│  "Les fiches de procédures"     │
├─────────────────────────────────┤
│  L3 – Hooks                     │  Passerelles de sécurité et automatisation
│  "Les contrôles automatiques"   │
├─────────────────────────────────┤
│  L4 – Agents                    │  Sous-agents avec leur propre contexte
│  "Les équipes spécialisées"     │
└─────────────────────────────────┘
```

### Couche 1 : CLAUDE.md — Contexte et Règles Persistants

- **Rôle** : Fournir le contexte qui ne change pas (stack technique, règles métier, architecture)
- **Persistance** : Chargé à chaque session automatiquement
- **Exemple** : "Ce projet utilise Python 3.11. Toujours écrire les commentaires en français."

### Couche 2 : Skills — Packs de Connaissances Auto-Invoqués

- **Rôle** : Expertise spécialisée activée à la demande
- **Persistance** : Chargé uniquement quand pertinent
- **Exemple** : Le skill "code-review" se lance quand vous demandez une revue de code

### Couche 3 : Hooks — Passerelles de Sécurité et Automatisation

- **Rôle** : Contrôles automatiques, indépendants de Claude
- **Persistance** : S'exécutent à chaque événement défini
- **Exemple** : Vérification de sécurité avant toute commande Bash

### Couche 4 : Agents — Sous-agents avec leur Propre Contexte

- **Rôle** : Tâches complexes déléguées à des sous-assistants spécialisés
- **Persistance** : Contexte propre, indépendant du contexte principal
- **Exemple** : Un agent "security-reviewer" qui analyse le code de sécurité en parallèle

**Analogie globale** :
- L1 = Le cahier de bord de l'équipe
- L2 = Les fiches de procédures métier
- L3 = Les capteurs de sécurité automatiques
- L4 = Les sous-traitants spécialisés

---

## 11. Workflow Quotidien

### La routine recommandée

Voici le flux de travail optimal avec Claude Code, étape par étape :

```
1. cd projet && claude
         ↓
2. Shift + Tab + Tab → Mode Plan
         ↓
3. Décrire l'intention de la fonctionnalité
         ↓
4. Shift + Tab → Acceptation automatique
         ↓
5. /compact (comprimer le contexte)
         ↓
6. Esc Esc → revenir en arrière (rewind)
         ↓
7. Committer fréquemment sur Git
         ↓
8. Commencer une nouvelle session par fonctionnalité
```

### Détail de chaque étape

**Étape 1 : Ouvrir le projet**
```bash
cd /chemin/vers/mon-projet
claude
```
Claude charge automatiquement CLAUDE.md et retrouve le contexte.

**Étape 2 : Activer le Mode Plan**
Utilisez `Shift + Tab + Tab` pour passer en **mode planification**.
Dans ce mode, Claude vous présente un plan d'action avant d'exécuter : il réfléchit avant d'agir.

**Analogie** : C'est comme demander à un technicien de vous expliquer ce qu'il va faire avant de toucher à la machine. Vous validez le plan, puis il agit.

**Étape 3 : Décrire votre intention**
```
Ajoute un formulaire de validation des données de contrôle qualité.
Il doit vérifier que la valeur est dans la plage [0.95, 1.05] et 
afficher un message d'erreur rouge si ce n'est pas le cas.
```

**Étape 4 : Acceptation automatique**
`Shift + Tab` active l'acceptation automatique : Claude peut exécuter les opérations approuvées sans vous demander à chaque fois.

**Étape 5 : /compact — Compresser le contexte**
Après une longue session, la mémoire de contexte se remplit. `/compact` résume les échanges pour libérer de l'espace.

**Analogie** : C'est comme faire une synthèse de réunion en cours de séance pour ne pas saturer le tableau blanc.

**Étape 6 : Esc Esc — Rewind**
Si Claude fait une erreur ou s'écarte de ce que vous vouliez, double-`Esc` permet de revenir en arrière et de reformuler.

**Étape 7 : Committer fréquemment**
```bash
git add .
git commit -m "feat: ajouter la validation du formulaire QC"
```
Chaque fonctionnalité terminée → un commit. Cela permet de sauvegarder votre progression et d'annuler facilement si besoin.

**Étape 8 : Une session par fonctionnalité**
Pour garder la mémoire de contexte propre, commencez une nouvelle session Claude pour chaque nouvelle fonctionnalité. Le contexte de la session précédente n'interférera pas.

### Exemple de session complète

**Scénario** : Vous voulez ajouter un tableau de bord pour les managers.

```
1. claude                           # Ouvrir Claude (CLAUDE.md chargé)
2. [Shift+Tab+Tab]                  # Mode Plan
3. "Crée un tableau de bord pour    # Votre demande
   les managers montrant les KPIs
   de production de la semaine"
4. [Claude présente le plan]        # Claude explique ce qu'il va faire
5. [Vous validez]                   # OK, c'est ce que je veux
6. [Shift+Tab]                      # Acceptation auto
7. [Claude travaille...]            # Fichiers créés
8. /compact                         # Si la session devient longue
9. git commit -m "feat: dashboard   # Sauvegarder
   manager KPIs production"
10. [Nouvelle session pour la       # Passer à la fonctionnalité suivante
    prochaine fonctionnalité]
```

---

## 12. Commandes Clavier Essentielles

### Tableau de référence rapide

| Commande | Action | Quand l'utiliser |
|----------|--------|------------------|
| `/init` | Générer CLAUDE.md | Au démarrage d'un nouveau projet |
| `/doccat` | Vérifier l'installation | En cas de problème de configuration |
| `/compact` | Compresser le contexte | Quand la session dure longtemps |
| `Shift + Tab` | Changer de mode / Acceptation auto | Pour valider les actions en masse |
| `Tab` | Activer/désactiver la pensée étendue | Pour les problèmes complexes |
| `Esc Esc` | Menu de retour arrière (rewind) | Pour annuler et reformuler |

### Explication des modes

**Pensée étendue (Extended Thinking) — touche `Tab`**

La pensée étendue est une fonctionnalité qui permet à Claude de **raisonner plus longuement et en profondeur** avant de répondre. C'est utile pour :
- Les problèmes d'architecture complexes
- Les choix techniques avec de nombreuses implications
- Le débogage de bugs difficiles à reproduire

**Analogie** : C'est comme la différence entre demander une réponse immédiate à un expert ou lui donner 15 minutes pour réfléchir au tableau blanc. La deuxième option produit souvent une réponse plus réfléchie.

**Mode Plan (Shift + Tab + Tab)**

Dans ce mode, Claude décompose votre demande en étapes, vous présente le plan, et attend votre validation avant d'agir. Indispensable pour les modifications importantes.

**Rewind (Esc Esc)**

Permet de revenir en arrière dans la conversation et de repartir sur une branche différente, sans perdre le contexte. Équivalent d'un "Ctrl+Z" intelligent.

---

## Conclusion

### Ce que vous avez appris

Vous maîtrisez maintenant l'écosystème Claude Code dans sa totalité :

1. **CLAUDE.md** : La mémoire persistante qui évite de tout réexpliquer
2. **Hiérarchie mémoire** : Contexte global → projet → local → sous-dossier
3. **Skills** : Guides Markdown auto-invoqués pour l'expertise spécialisée
4. **Hooks** : Contrôles de sécurité automatiques avant/après chaque action
5. **Permissions** : Ce que Claude peut et ne peut pas faire
6. **Architecture 4 couches** : CLAUDE.md + Skills + Hooks + Agents
7. **Workflow quotidien** : La routine optimale pour travailler efficacement

### Récapitulatif visuel

```
VOUS ──→ [CLAUDE.md] ──→ Claude comprend votre projet
VOUS ──→ [Skills]    ──→ Claude a des expertises spécialisées
VOUS ──→ [Hooks]     ──→ Sécurité et automatisation garanties
VOUS ──→ [Agents]    ──→ Délégation de tâches complexes
```

### Prochaines étapes

- [ ] Créer votre premier `CLAUDE.md` avec `/init`
- [ ] Rédiger un Skill adapté à votre métier
- [ ] Configurer les permissions selon votre politique de sécurité
- [ ] Mettre en place un Hook de vérification avant déploiement
- [ ] Partager CLAUDE.md avec votre équipe via Git

---

*Pôle Formation UIMM - CVDL | Formateur : S. JAUBERT*
*Formation IA en entreprise — Édition 2026*
