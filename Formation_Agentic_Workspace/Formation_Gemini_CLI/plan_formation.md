# Formation : Maîtriser l'IA Agentique avec Gemini CLI (Programmation Morphique)

**Public cible :** Salariés d'entreprise (Développeurs, Chefs de Projet, Analystes de Données, Ingénieurs)
**Durée estimée :** 1 journée (ou 4 modules de 2h)
**Prérequis :** Notions de base en utilisation de la ligne de commande (CLI) et compréhension des concepts IA généraux.

---

## Objectif de la formation
Cette formation vise à faire passer les participants du statut d'utilisateur d'interfaces conversationnelles (ChatGPT, Gemini Web) à celui d'**opérateurs de systèmes IA autonomes** (Agents CLI). 
En s'appuyant sur les principes de la **Programmation Morphique** (adaptés à **Gemini CLI**), les participants apprendront à utiliser le langage naturel comme un code versionnable, réutilisable et abstrait pour automatiser des processus métier complexes de bout en bout (End-to-End Autonomy).

---

## Sommaire de la Formation

*   [Module 1 : Le Langage Naturel comme Code (Morphabilité & Abstraction)](#module-1)
*   [Module 2 : L'Environnement de Travail Agentique (Cohérence & Reproductibilité)](#module-2)
*   [Module 3 : L'Art de la Délégation et des Sous-Agents (Récursivité & Complexité Morphique)](#module-3)
*   [Module 4 : Le Cycle de Travail et l'Autonomie de Bout en Bout](#module-4)

---

<a id="module-1"></a>
## Module 1 : Le Langage Naturel comme Code (Principes 1 & 2)

**Concept Clé :** *L'anglais (ou le français) est maintenant du code.* Les instructions ne sont plus de simples "prompts" éphémères, mais des spécifications (Morphic Code) que l'IA peut adapter (Morphing) à chaque exécution.

### 1.1 La Morphabilité (Principe 1)
*   **Théorie :** Comment une même instruction de base (ex: un *Skill* Gemini) peut être modifiée à la volée sans altérer le fichier d'origine.
*   **Cas pratique Gemini CLI :**
    *   *Scénario :* On possède un skill `seo-audit`.
    *   *Exécution standard :* On demande à Gemini d'exécuter l'audit complet.
    *   *Morphing :* L'utilisateur tape : *"Exécute le skill `seo-audit` sur la page d'accueil, mais concentre-toi uniquement sur les balises d'accessibilité (ARIA) en ignorant le reste."*
    *   *Résultat :* Gemini adapte l'exécution du skill sans modifier le fichier `SKILL.md`.

### 1.2 L'Abstraction (Principe 2)
*   **Théorie :** Transformer une tâche manuelle complexe et itérative en une compétence réutilisable (un *Skill*).
*   **Cas pratique Gemini CLI :**
    *   *Scénario :* Analyser un fichier de logs d'erreurs mensuel (processus en 10 étapes : tri, nettoyage, synthèse, formatage Markdown).
    *   *Action :* Créer un fichier `log-analyzer/SKILL.md`.
    *   *Exercice :* Les participants rédigent ce *Skill* en langage naturel décrivant précisément le workflow. Ils créent ainsi une "fonction" invocable à volonté par Gemini CLI.

---

<a id="module-2"></a>
## Module 2 : L'Environnement de Travail Agentique (Principes 4 & 5)

**Concept Clé :** Un agent IA ne vaut que par le contexte qu'on lui donne. Le système doit être robuste aux plantages (Crash-resilience) et ne jamais s'écarter de ses instructions (Consistency drift).

### 2.1 L'Ingénierie du Contexte & Reproductibilité (Principe 5)
*   **Théorie :** La règle du "Zéro perte de contexte". Si le terminal plante, l'agent doit pouvoir reprendre son travail en moins de 2 minutes.
*   **Cas pratique Gemini CLI :**
    *   *Le fichier `GEMINI.md` :* Comprendre le *System-Wide Context*. Ce fichier charge les règles universelles de l'entreprise (ex: "Toujours utiliser le logo UIMM sur les PDF générés", "Ton professionnel").
    *   *Le dossier `tasks/` :* Les participants apprennent à imposer à Gemini la création de plans d'actions concrets (`todo.md`) et de journaux de progression (`lessons.md`).
    *   *Exercice :* Fermer brutalement le terminal de Gemini CLI en pleine tâche. Le rouvrir et taper : *"Où en étions-nous selon le `todo.md` ?"* et constater la reprise immédiate.

### 2.2 La Cohérence Interne (Principe 4)
*   **Théorie :** Maintenir l'écosystème sain. Éviter les contradictions entre plusieurs fichiers de contexte ou plusieurs *Skills*.
*   **Cas pratique Gemini CLI :**
    *   *Scénario :* Le projet possède 20 *skills*. Certains sont obsolètes.
    *   *Exercice :* Utiliser un skill d'audit (ex: `skill-sentinel` évoqué précédemment) pour scanner le propre dossier `.gemini/skills/` de l'apprenant et identifier les redondances ou la "dette technique" des prompts.

---

<a id="module-3"></a>
## Module 3 : Délégation et Sous-Agents (Principes 3 & 6)

**Concept Clé :** Construire des workflows capables d'appeler d'autres workflows. Résoudre le problème du "Context Window" en déléguant les tâches massives.

### 3.1 La Récursivité (Principe 3)
*   **Théorie :** Empiler les commandes. Un processus de haut niveau fait appel à des processus de bas niveau.
*   **Cas pratique Gemini CLI :**
    *   *Scénario :* Déployer une application.
    *   *Workflow :* Un prompt maître demande à l'agent de "Générer la Release". L'agent comprend qu'il doit, dans l'ordre, activer les sous-compétences : `run-tests` puis `build-feature` puis `deploy-staging`.

### 3.2 Complexité Morphique & Efficacité des Tokens (Principe 6 & 8)
*   **Théorie :** "Trop d'instructions tuent l'instruction". Comment éviter que l'IA "oublie" des étapes.
*   **Cas pratique Gemini CLI :**
    *   *Le sous-agent `generalist` :* Les participants apprennent à ne pas demander à l'agent principal de lire 50 fichiers. 
    *   *Exercice :* Demander à Gemini : *"Délègue l'exploration du répertoire `src/` au sous-agent `codebase_investigator` pour dresser une carte de l'architecture, et reviens vers moi avec la synthèse uniquement."*

---

<a id="module-4"></a>
## Module 4 : Le Cycle de Travail et Autonomie E2E (Principe 7)

**Concept Clé :** Adopter la posture d'un "Manager de Produit" face à son "Ingénieur Logiciel IA".

### 4.1 Le Cycle : Entrée -> Planification -> Exécution -> Apprentissage
*   **Théorie :** La méthode de travail rigoureuse pour interagir avec un agent de manière asynchrone (Plan -> Act -> Validate).
*   **Cas pratique Gemini CLI :**
    *   *Étape 1 (Entrée) :* Fournir un objectif clair (ex: "Générer un script Python pour analyser les ventes Q3 et sortir un graphique").
    *   *Étape 2 (Planification) :* Forcer l'outil `enter_plan_mode`. L'agent rédige sa stratégie. L'utilisateur valide ou corrige.
    *   *Étape 3 (Exécution) :* L'agent exécute les commandes shell, installe les dépendances et code. Il a l'interdiction de dire "J'ai fini" sans avoir exécuté le script et prouvé qu'il marche (Validation rigoureuse).
    *   *Étape 4 (Apprentissage) :* Mettre à jour `tasks/lessons.md` si une erreur inattendue (ex: dépendance `pandas` manquante) a été rencontrée.

### 4.2 L'Autonomie de Bout en Bout (E2E)
*   **Théorie :** Savoir évaluer la capacité de son système. Si l'agent réussit sans intervention (one-shot), le niveau de complexité E2E est atteint.
*   **Exercice final :** Chaque participant choisit un processus métier qui lui prend habituellement 2 heures. Il doit concevoir le contexte (`GEMINI.md`) et le *Skill* nécessaires pour que Gemini CLI réalise cette tâche de bout en bout, en moins de 10 minutes.

---

## 📂 Organisation des Ressources

L'ensemble du matériel de cette formation est stocké dans ce répertoire :
`Formation_Agentic_Workspace/Formation_Gemini_CLI/`

Ce dossier contiendra :
*   `plan_formation.md` (Ce document)
*   `exercices/` (Dossier contenant des templates de fichiers `todo.md`, `GEMINI.md` et des exemples de `SKILL.md` à faire évoluer par les stagiaires).
*   `TP_Final/` (Dossier contenant les corrigés types des cas pratiques métiers).
