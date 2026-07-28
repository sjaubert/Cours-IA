---
output:
  word_document: default
  html_document: default
---
# Fiche procédurale — Les plugins Claude

**Auteur :** S. Jaubert  
**Organisme :** Pôle Formation UIMM-CVDL  
**Date :** Mai 2026  
**Usage :** Formation "Maîtriser Claude et l'IA Agentique"

---

## Avertissement préalable — Deux environnements distincts

Ce document est issu d'une source orientée **Claude Code**, l'outil en ligne de commande d'Anthropic. Les commandes d'installation présentées (de la forme `claude plugin install ...`) s'appliquent exclusivement à cet environnement CLI.

**Ces commandes ne fonctionnent pas dans l'application Claude bureau.** Les deux produits disposent de mécanismes de gestion de plugins indépendants.

| Environnement | Mode d'installation des plugins |
|---|---|
| Claude Code (terminal) | Commande `claude plugin install ...` |
| Application Claude bureau / Cowork | Interface graphique — Paramètres > Extensions |

Les concepts décrits dans cette fiche restent valables dans les deux environnements (types de plugins, utilités, protocole MCP). Seule la procédure d'installation diffère.

### Installer un plugin dans l'application Claude bureau

L'application Claude bureau propose deux mécanismes complémentaires.

**1. Le répertoire de connecteurs (Connectors Directory)**

Anthropic met à disposition un catalogue d'outils validés, accessible à l'adresse [claude.ai/directory](https://claude.ai/directory) ou depuis l'application via Paramètres > Extensions > Parcourir les extensions. On y trouve des connecteurs vers des services externes (Google Workspace, Slack, GitHub, etc.) et des extensions desktop.

Procedure :

1. Ouvrir l'application Claude bureau.
2. Aller dans Paramètres > Extensions.
3. Cliquer sur "Parcourir les extensions" pour consulter le catalogue officiel.
4. Cliquer sur "Connecter" (pour un connecteur web) ou "Installer" (pour une extension desktop).
5. Suivre les étapes d'authentification si le service externe le requiert.

Note : les connecteurs vers des services distants (Google, Slack, etc.) sont réservés aux abonnements payants.

**2. Les extensions desktop au format .mcpb**

Une extension desktop est un fichier `.mcpb` (MCP Bundle) qui regroupe un serveur MCP et toutes ses dépendances en un seul paquet installable, sans configuration manuelle de fichiers JSON. C'est l'équivalent d'une extension de navigateur, appliqué à Claude.

Procedure :

1. Récupérer le fichier `.mcpb` auprès de son auteur ou via le catalogue officiel.
2. Dans l'application Claude bureau : Paramètres > Extensions > Installer une extension.
3. Sélectionner le fichier `.mcpb` et suivre les invites de configuration.

Le catalogue officiel des extensions est également consultable sur [anthropic.com/partners/mcp](https://www.anthropic.com/news/connectors-directory).

---

## 1. Qu'est-ce qu'un plugin Claude ?

Un plugin Claude est une extension qui connecte l'assistant à des outils, services ou données externes. Sans plugin, Claude se limite à la génération de texte dans une fenêtre de conversation. Avec des plugins, il devient un agent autonome capable d'agir sur votre environnement de travail.

Le protocole technique qui rend cela possible s'appelle le **Model Context Protocol (MCP)**, un standard ouvert publié par Anthropic en décembre 2025. Il standardise la manière dont les modèles d'IA se connectent à des ressources externes, sans nécessiter de développement spécifique pour chaque service.

---

## 2. Les quatre types de plugins

Il existe quatre catégories de plugins dans l'écosystème Claude.

**Serveurs MCP** : connectent Claude à des services externes tels que GitHub, Slack ou des bases de données. Ce sont les plugins les plus courants.

**Skills (compétences)** : fonctionnalités que Claude active automatiquement selon le contexte de la demande. Aucune commande spécifique n'est requise.

**Commands (commandes)** : raccourcis personnalisés déclenchés manuellement, par exemple `/code-review` pour lancer une revue de code.

**Hooks (déclencheurs)** : automatisations activées par des événements précis, comme l'application de normes de qualité à chaque modification de fichier.

---

## 3. Procédure d'installation générale (Claude Code — terminal uniquement)

Les commandes suivantes s'appliquent exclusivement à **Claude Code**, l'outil en ligne de commande. Pour l'application Claude bureau, se reporter à la section "Avertissement préalable" ci-dessus.

L'installation s'effectue via la commande :

```bash
claude plugin install <nom-du-plugin>@<source>
```

La source officielle Anthropic est `claude-plugins-official`. Tous les exemples ci-dessous utilisent cette source.

---

## 4. Les dix plugins principaux

### Plugin 1 — Frontend-Design

**Utilité**  
Ce plugin modifie la manière dont Claude génère des interfaces visuelles. Plutôt que de produire des mises en page génériques, il applique des principes de design avancés : typographie cinétique, ruptures de grille raisonnées, utilisation intentionnelle des espaces blancs. L'objectif est d'obtenir un premier rendu directionnellement juste, réduisant ainsi les itérations de conception.

**Cas d'usage typique**  
Conception de pages d'accueil, de composants d'interface, ou de prototypes visuels.

**Installation**
```bash
claude plugin install frontend-design@claude-plugins-official
```

---

### Plugin 2 — Superpowers

**Utilité**  
Ce plugin supprime les frictions d'interaction entre Claude et l'environnement système. Il permet à Claude de lire des fichiers de configuration, d'exécuter des commandes terminal (avec validation de l'utilisateur) et d'enchaîner des étapes de workflow sans intervention manuelle entre chacune.

**Cas d'usage typique**  
Automatisation de pipelines de déploiement : exécution séquentielle des phases lint, test, build, déploiement et notification, depuis un seul prompt.

**Installation**
```bash
claude plugin install superpowers@claude-plugins-official
```

---

### Plugin 3 — Context7 (par Upstash)

**Utilité**  
Ce plugin résout le problème de l'obsolescence des données d'entraînement. Il interroge en temps réel la documentation technique correspondant exactement à la version des bibliothèques utilisées dans le projet. Claude cesse de supposer et commence à citer des sources précises et vérifiables.

**Cas d'usage typique**  
Développement sur des frameworks récents (React 19, Next.js 15, etc.) où les API évoluent rapidement.

**Installation**
```bash
claude plugin install context7@claude-plugins-official
```

---

### Plugin 4 — Code Review

**Utilité**  
Ce plugin effectue une analyse approfondie du code soumis en pull request. Contrairement aux outils de lint classiques qui vérifient la syntaxe, Code Review évalue l'intention : le code est-il maintenable ? Passera-t-il à l'échelle ? Existe-t-il une approche plus simple ? Il propose des explications et des corrections directement exploitables.

**Commande avancée**  
`/review --strict` pour un audit centré sur la sécurité.

**Cas d'usage typique**  
Validation systématique avant fusion de branches dans un dépôt partagé.

**Installation**
```bash
claude plugin install code-review@claude-plugins-official
```

---

### Plugin 5 — Code Simplifier

**Utilité**  
Ce plugin réduit la complexité du code existant sans modifier son comportement. Il identifie et supprime le code mort, aplatit les abstractions inutiles, renomme les éléments peu clairs et réduit les dépendances. Le résultat est un code plus léger, plus lisible et plus rapide à maintenir.

**Cas d'usage typique**  
Assainissement de code hérité, préparation d'une refactorisation, ou réduction de la taille d'un bundle applicatif.

**Installation**
```bash
claude plugin install code-simplifier@claude-plugins-official
```

---

### Plugin 6 — Skill Creator

**Utilité**  
Ce plugin transforme des processus décrits en langage naturel en compétences réutilisables pour Claude. Les procédures internes d'une équipe — déploiements, conventions de nommage, processus qualité — deviennent des savoirs interrogeables, partageables et versionnables. Le savoir institutionnel sort des mémoires individuelles pour intégrer un référentiel commun.

**Cas d'usage typique**  
Capitalisation des bonnes pratiques d'équipe, réduction du temps d'intégration des nouveaux membres.

**Installation**
```bash
claude plugin install skill-creator@claude-plugins-official
```

---

### Plugin 7 — GitHub

**Utilité**  
Ce plugin donne à Claude une vision au niveau du dépôt, et non plus au niveau du fragment de code. Il peut rechercher dans les fichiers sources, lire les fichiers pertinents et proposer des corrections sous forme de pull requests préliminaires. Par défaut, il fonctionne en lecture seule ; toute action d'écriture requiert une validation explicite de l'utilisateur.

**Cas d'usage typique**  
Localisation rapide de la source d'un bug, analyse de l'impact d'une modification, rédaction de messages de commit.

**Installation**
```bash
claude plugin install github@claude-plugins-official
```

---

### Plugin 8 — Playwright MCP

**Utilité**  
Ce plugin permet à Claude de contrôler un navigateur réel pour exécuter des tests fonctionnels. L'utilisateur décrit le parcours utilisateur à tester en langage naturel, Claude l'exécute et vérifie les résultats. Il s'adapte aux modifications du DOM sans nécessiter de mise à jour des sélecteurs.

**Conseil pratique**  
Pour les flux nécessitant une authentification, se connecter manuellement une première fois suffit : Claude récupère ensuite les cookies de session.

**Cas d'usage typique**  
Automatisation des tests de recette, validation des parcours utilisateurs critiques.

**Installation**
```bash
claude plugin install playwright@claude-plugins-official
```

---

### Plugin 9 — Feature-Dev

**Utilité**  
Ce plugin orchestre le cycle complet de développement d'une fonctionnalité à partir d'une description en langage naturel. Il enchaîne automatiquement les étapes : analyse des besoins, proposition d'architecture, implémentation, tests et documentation. Il ne génère pas seulement du code, il livre un résultat complet.

**Commande de déclenchement**  
`/feature-dev <description de la fonctionnalité>`

**Cas d'usage typique**  
Prototypage rapide, développement en solo, ou ajout de fonctionnalités sur un projet existant.

**Installation**
```bash
claude plugin install feature-dev@claude-plugins-official
```

---

### Plugin 10 — CLAUDE.md Management

**Utilité**  
Ce plugin exploite les fichiers CLAUDE.md pour rendre persistantes les conventions d'un projet ou d'une équipe. Une fois ces conventions documentées, Claude les applique automatiquement dans chaque conversation suivante, sans que l'utilisateur ait besoin de les rappeler. Ces fichiers sont versionnables et partageables comme n'importe quel fichier du dépôt.

**Cas d'usage typique**  
Standardisation des pratiques au sein d'une équipe, mémorisation des préférences de formatage, de nommage ou d'architecture.

**Installation**
```bash
claude plugin install claude-md-management@claude-plugins-official
```

---

## 5. Recommandations d'installation par profil

**Pour un développeur**  
Commencer par : Code Review, GitHub, Context7, puis Frontend-Design (si conception d'interfaces) et Playwright MCP (si tests fonctionnels).

**Pour un travailleur de la connaissance (formateur, chargé de projet, administratif)**  
Commencer par : Superpowers, Skill Creator, CLAUDE.md Management.

**Pour un créateur de produit ou un fondateur**  
Commencer par : Feature-Dev, Frontend-Design, Code Simplifier, Skill Creator.

---

## 6. Données de référence sur l'écosystème (mai 2026)

| Indicateur | Valeur |
|---|---|
| Serveurs MCP disponibles | Plus de 1 000 |
| Plugin le plus installé (Frontend-Design) | 721 000+ installations |
| Total des installations de plugins | Plus de 8 millions |
| Agents IA supportant le protocole MCP | 18 |
| Connecteurs officiels Anthropic | Plus de 50 |

---

*Document rédigé dans le cadre de la formation "Maîtriser Claude et l'IA Agentique" — Pôle Formation UIMM-CVDL*
