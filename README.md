# Cours d'Introduction à l'Intelligence Artificielle

## ![Logo UIMM](logo_uimm_placeholder.jpg) Pôle Formation UIMM CVDL : S. Jaubert

---

## Navigation rapide

| # | Thème | Public cible |
|---|---|---|
| [1](#1-comprendre-lia-fondamentaux-et-biais) | Comprendre l'IA, fondamentaux et biais | Tous |
| [2](#2-prompt-engineering) | Prompt engineering | Tous |
| [3](#3-gemini-cli-et-workspace-ia) | Gemini CLI et Workspace IA | Techniciens, formateurs |
| [4](#4-notebooklm) | NotebookLM | Formateurs, managers |
| [5](#5-claude-code-et-agents-ia) | Claude Code et agents IA | Utilisateurs avancés |
| [6](#6-ia-appliquée-à-lindustrie) | IA appliquée à l'industrie | Techniciens, opérateurs |
| [7](#7-ressources-et-outils) | Ressources et outils | Formateurs |
| [8](#8-ia-locale-et-souveraineté) | IA locale et souveraineté | Techniciens, formateurs |

---

## Légende des niveaux

- **Découverte** : aucun prérequis, première approche
- **Pratique** : bases en IA acquises, manipulation autonome des outils
- **Avancé** : expérience des outils IA agentiques requise

---

## 1. Comprendre l'IA, fondamentaux et biais

### Cours magistral & Support de référence actualisé (2026)

- [Introduction à l'Intelligence Artificielle (Promotion 2026)](https://sjaubert.github.io/Cours-IA/00-Formation/cours-introduction-ia-2026/index.html) | **Découverte à Avancé** | Web App & Support de formation | Support de cours complet en 4 modules : Histoire & cybernétique, Mathématiques des Transformers, Ruptures 2022-2026 (Multimodalité, Raisonnement, Systèmes agentiques & protocole MCP), Cadre réglementaire AI Act européen et Souveraineté industrielle <sub>*(créé en sept. 2026)*</sub>
  - [Diaporama PowerPoint 2026 harmonisé (81 slides, 4 modules)](00-Formation/cours-introduction-ia-2026/Diaporama_COURS_Introduction_IA_2026.pptx) | [Version PDF haute résolution](00-Formation/cours-introduction-ia-2026/Diaporama_COURS_Introduction_IA_2026.pdf) <sub>*(sept. 2026)*</sub>
  - [Version web interactive](00-Formation/cours-introduction-ia-2026/index.html) | [Conducteur pédagogique détaillé et sourcé](00-Formation/cours-introduction-ia-2026/plan_detaille_formation_ia_2026.md) <sub>*(sept. 2026)*</sub>
  - [Archive historique PPTX originale (66 slides)](00-Formation/Module%20Formation/Diaporama%20COURS%20Introduction%20IA.pptx) | [Archive PDF originale](00-Formation/Module%20Formation/Diaporama%20COURS%20Introduction%20IA.pdf) <sub>*(déc. 2025)*</sub>

### Démonstrations interactives

- [Les 7 Paramètres qui Contrôlent l'IA](https://sjaubert.github.io/Cours-IA/01-comprendre-ia/parametres-ia/index.html) | **Découverte** | HTML | Expérimentation en temps réel de Temperature, Top-P, Max Tokens et leur impact sur les réponses <sub>*(déc. 2025)*</sub>

- [Visualisation Réseaux de Neurones](01-comprendre-ia/activites/A7_Reseaux_Neurones/index.html) | **Pratique** | HTML | Deux simulateurs : régression linéaire interactive et réseau de neurones avec rétropropagation configurable <sub>*(déc. 2025)*</sub>
  - [Régression Linéaire Interactive](01-comprendre-ia/activites/A7_Reseaux_Neurones/1_regression_lineaire.html) | Manipulation de points et calcul de droite de régression <sub>*(déc. 2025)*</sub>
  - [Réseau de Neurones avec Apprentissage Supervisé](01-comprendre-ia/activites/A7_Reseaux_Neurones/2_reseau_neurones.html) | Architecture configurable <sub>*(déc. 2025)*</sub>
  - [Guide d'utilisation pédagogique](01-comprendre-ia/activites/A7_Reseaux_Neurones/README.md) | [Synthèse Architecture](01-comprendre-ia/activites/A7_Reseaux_Neurones/Synthese_Architecture.md) | [Guide complet](01-comprendre-ia/activites/A7_Reseaux_Neurones/Guide_Architecture_Reseaux.md) <sub>*(déc. 2025)*</sub>

### Activités sur les biais et les limites de l'IA

Formation interactive en 6 activités (biais cognitifs, première impression, sélection, confirmation, culturels, jeu de rôle) :

- [Formation Intelligence Artificielle : Les Biais](https://sjaubert.github.io/Cours-IA/01-comprendre-ia/activites-biais/index.html) | **Découverte** | HTML | Point d'entrée avec guide formateur et support apprenant <sub>*(déc. 2025)*</sub>
- [Métacognition et Biais dans le Prompting](00-Formation/Module%20Formation/MÉTACOGNITION%20ET%20BIAIS%20DANS%20LE%20PROMPTING.docx) | **Pratique** | DOCX | Identifier les mécanismes cognitifs (ancrage, confirmation, cadrage) et appliquer des protocoles de dé-biaisage dans le prompting <sub>*(déc. 2025)*</sub>

Activités autonomes (approche par cas) :

- [A1 : Illusion de Vérité](01-comprendre-ia/activites/A1_illusion_verite/instructions_apprenant.md) | **Découverte** | MD | L'IA génère des textes crédibles contenant des erreurs factuelles <sub>*(nov. 2025)*</sub>
- [A2 : Biais de Confirmation](01-comprendre-ia/activites/A2_Biais_Confirmation/) | **Découverte** | MD | L'IA argumente des points de vue opposés selon le contexte <sub>*(nov. 2025)*</sub>
- [A3 : Biais Culturel](01-comprendre-ia/activites/A3_Biais_Culturel/) | **Découverte** | MD | Les LLMs reflètent les biais culturels de leurs données d'entraînement <sub>*(nov. 2025)*</sub>
- [A4 : Illusion de Raisonnement](01-comprendre-ia/activites/A4_Illusion_raisonnement/) | **Découverte** | MD | L'IA ne raisonne pas au sens humain : corrélations statistiques vs. logique <sub>*(nov. 2025)*</sub>

---

## 2. Prompt engineering

### Guides de référence

- [Guide Interactif Art du Prompt](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/Guide_Interactif_Prompt.html) | **Découverte** | HTML | Introduction structurée aux principes du prompting efficace <sub>*(déc. 2025)*</sub>
- [Maîtriser l'Art du Prompt Engineering](00-Formation/Maîtriser%20l'Art%20du%20Prompt%20Engineering%20.docx) | **Pratique** | DOCX | Synthèse complète des principes, techniques avancées et meilleures pratiques de conception d'instructions pour LLM <sub>*(nov. 2025)*</sub>
- [Cas d'usage : Démonstration de Puissance & Effet de Levier Cognitif](00-Formation/CAS%20D'USAGE%20%20DÉMONSTRATION%20DE%20PUISSANCE%20EFFET%20DE%20LEVIER%20COGNITIF.docx) | **Avancé** | DOCX | Analyse financière & stratégique assistée par RAG, extraction de données multi-sources et synthèse de notes confidentielles <sub>*(nov. 2025)*</sub>

- [PromptFlow UIMM Studio](https://sjaubert.github.io/Cours-IA/02-prompt-engineering/promptflow/dist/index.html) | **Pratique** | App Web | Outil de création pédagogique pour concevoir des séquences de prompts <sub>*(déc. 2025)*</sub>

### Ateliers de formation

- [Formation Journée Prompt Engineering](02-prompt-engineering/formation-journee/README.md) | **Pratique** | MD + HTML | Programme d'une journée avec 3 ateliers complets <sub>*(déc. 2025)*</sub>
  - [Atelier 1 : Les 6 Piliers](02-prompt-engineering/formation-journee/Atelier1_6Piliers.html) | [Corrigés formateur](02-prompt-engineering/formation-journee/Atelier1_Corriges_Formateur.md)
  - [Atelier 2 : Exercices Pratiques](02-prompt-engineering/formation-journee/Atelier2_Exercices_Pratiques.html) | [Corrigés formateur](02-prompt-engineering/formation-journee/Atelier2_Corriges_Formateur.md)
  - [Atelier 3 : Techniques Avancées](02-prompt-engineering/formation-journee/Atelier3_Techniques_Avancees.html) | [Corrigés formateur](02-prompt-engineering/formation-journee/Atelier3_Corriges_Formateur.md)

- [Formation Prompt Engineering : Maintenance Industrielle](02-prompt-engineering/formation-prompt/Formation_Prompt_Maintenance_Etudiants.html) | **Pratique** | HTML | 4h pour étudiants Bachelor Maintenance : cas d'usage réalistes, travaux de groupe, sensibilisation aux biais <sub>*(jan. 2026)*</sub>
  - [Guide Formateur](02-prompt-engineering/formation-prompt/Formation_Prompt_Maintenance_Guide_Formateur.md)

---

## 3. Gemini CLI et Workspace IA

### Installation et configuration

- [Installation Gemini CLI](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/Gemin-cli_V2.html) | **Pratique** | HTML | Procédure d'installation pas à pas <sub>*(déc. 2025)*</sub>
- [Installation MCP Workspace](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/gemini-cli_workspace.html) | **Pratique** | HTML | Configuration de l'environnement MCP pour Google Workspace <sub>*(déc. 2025)*</sub>
- <a href="https://sjaubert.github.io/Cours-IA/03-outils-google/agentic-workspace/gemini_cli_workspace.html" target="_blank">Gemini CLI Extension pour Google Workspace</a> : **Pratique** | HTML | Intégration Gemini dans l'écosystème Google <sub>*(déc. 2025)*</sub>
- [Antigravity : Guide d'installation](https://sjaubert.github.io/Cours-IA/03-outils-google/antigravity/guide_antigravity.html) | **Pratique** | HTML | Installation et prise en main d'Antigravity <sub>*(déc. 2025)*</sub>

### Tutoriels

- [Astuces Gemini CLI](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/astuce_geminiCLI.html) | **Pratique** | HTML | Raccourcis et commandes utiles au quotidien <sub>*(déc. 2025)*</sub>
- [Tutoriel Google Apps Script](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/tutoriel_google_appsscript.html) | **Pratique** | HTML | Automatisation de Google Workspace via Apps Script <sub>*(déc. 2025)*</sub>
- [Tutoriel Sécurité Gemini](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/tutoriel-gemini-secure.html) | **Pratique** | HTML | Bonnes pratiques de sécurité et confidentialité <sub>*(déc. 2025)*</sub>
- [Tutoriel Automatisation Workspace](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/Tutoriel_Automatisation_Workspace.html) | **Pratique** | HTML | Workflows automatisés dans Google Workspace <sub>*(déc. 2025)*</sub>
- [Tutoriel Automatisation Agentique](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/Agentic_Automation_Tutorial.html) | **Avancé** | HTML | Conception d'agents IA autonomes avec Gemini CLI <sub>*(déc. 2025)*</sub>
- [Antigravity : Tutoriel avancé](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/antigravity_tutorial.html) | **Avancé** | HTML | Fonctionnalités avancées d'Antigravity <sub>*(déc. 2025)*</sub>

### Parcours de formation complets

- <a href="https://sjaubert.github.io/Cours-IA/03-outils-google/agentic-workspace/guide_formation_ia.html" target="_blank">Guide Formation IA & Productivité : Gemini CLI & MCP</a> : **Avancé** | HTML | Programme structuré d'adoption de Gemini CLI en contexte professionnel <sub>*(nov. 2025)*</sub>
- [Formation Agentic Workspace](03-outils-google/agentic-workspace/index.html) | **Avancé** | HTML | Parcours complet avec exercices et corrigés par module <sub>*(nov. 2025)*</sub>
- [Navigation Tutoriels Gemini CLI & MCP](https://sjaubert.github.io/Cours-IA/03-outils-google/agentic-workspace/tutoriels_gemini_mcp.html) | **Avancé** | HTML | Guide de navigation entre les ressources Gemini CLI et MCP <sub>*(déc. 2025)*</sub>

---

## 4. NotebookLM

### Prise en main

- [Présentation NotebookLM](04-notebooklm/index.html) | **Découverte** | HTML | Introduction interactive : principes, cas d'usage, interface <sub>*(jan. 2026)*</sub>
- [TP Prise en main : Presse Hydraulique](04-notebooklm/scenario_tp_notebooklm.html) | **Pratique** | HTML | Cas concret industrie : analyser la documentation d'une presse hydraulique <sub>*(jan. 2026)*</sub>

### Formation structurée 7H

- [Parcours complet : Formation 7H](04-notebooklm/Formation_7H/parcours_formation.html) | **Pratique** | HTML | 5 shifts cognitifs progressifs pour maîtriser NotebookLM <sub>*(fév. 2026)*</sub>
  - [Module 1 : Comprendre NotebookLM](04-notebooklm/Formation_7H/M1_comprendre_nblm.html) | *L'espace clos : la qualité vient des sources* <sub>*(fév. 2026)*</sub>
  - [Module 2 : L'art de questionner](04-notebooklm/Formation_7H/M2_art_questionner.html) | *Contraindre la question pour augmenter sa puissance* <sub>*(fév. 2026)*</sub>
  - [Module 3 : Vérifier et citer](04-notebooklm/Formation_7H/M3_verifier_citer.html) | *L'IA hallucine, la citation ancre* <sub>*(fév. 2026)*</sub>
  - [Module 4 : Produire en boucle créative](04-notebooklm/Formation_7H/M4_produire_boucler.html) | *Itérer, reformater, exporter* <sub>*(fév. 2026)*</sub>
  - [Module 5 : Penser avec NotebookLM](04-notebooklm/Formation_7H/M5_penser_avec_nblm.html) | *Les méta-patterns, l'outil de pensée durable* <sub>*(fév. 2026)*</sub>
  - [Guide Formateur](04-notebooklm/Formation_7H/guide_formateur.html) | [Fiches Activités Imprimables](04-notebooklm/Formation_7H/fiches_activites.html) <sub>*(fév. 2026)*</sub>

---

## 5. Claude Code et agents IA

### Maîtriser Claude : Formations structurées

- [Maitrise de l'IA : Formation 7H (Cadre & Fondements)](05-claude/Formation_CLAUDE/Formation_Maitrise_IA_7H.html) | **Découverte** | HTML | Journée complète basée sur le programme *AI Fluency* d'Anthropic : cadre 4D (Délégation, Description, Discernement, Diligence), 3 modes d'interaction, fonctionnement de l'IA générative, 10 vidéos ressources, 4 ateliers pratiques et projet fil rouge : public salariés tous niveaux <sub>*(juin 2026)*</sub>

- [Syllabus : Maîtriser Claude (4 blocs)](05-claude/Formation_Maitriser_Claude/plan_de_formation.html) | **Pratique** | HTML | Plan d'ingénierie pédagogique restructuré pour salariés : formateurs, administratifs, ingénieurs <sub>*(avr. 2026)*</sub>
- [Livret Pratique : Maîtriser Claude](05-claude/Formation_Maitriser_Claude/Livret_Pratique.html) | **Pratique** | HTML | Manuel apprenant : exercices pas à pas, fichiers Markdown (identité, contraintes), prompts contre les hallucinations <sub>*(avr. 2026)*</sub>
- [Construire un agent IA avec Claude : Plan de formation](05-claude/formation-agent-ia/plan_formation_agent_claude.html) | **Avancé** | HTML | Parcours 6 semaines en 4 étapes progressives : agent mono-outil, tests mesurables, multi-outils + mémoire, affinage et mise en production : cas d'usage RH, administratif, comptabilité <sub>*(mai 2026)*</sub>
  - [Semaine 1 : Découvrir les agents IA avec Claude.ai](05-claude/formation-agent-ia/semaine1.html) | Guide formateur + fiche apprenant + activités · Niveau A · 2h30
  - [Semaine 2 : Premier agent HTML avec recherche web](05-claude/formation-agent-ia/semaine2.html) | Clé API, prompt système, web_search · Niveau B · 2h30
  - [Semaine 3 : Mesurer et améliorer la qualité](05-claude/formation-agent-ia/semaine3.html) | Grille 5 critères, scénarios de test, OODA · 2×1h
  - [Semaine 4 : Connecter Drive et Agenda via MCP](05-claude/formation-agent-ia/semaine4.html) | MCP Google, workflows multi-outils · 1h30
  - [Semaine 5 : Gmail, mémoire et workflows automatisés](05-claude/formation-agent-ia/semaine5.html) | MCP Gmail, mémoire conversationnelle · 1h30
  - [Semaine 6 : Évaluation finale et mise en production](05-claude/formation-agent-ia/semaine6.html) | Bilan scores, catalogue erreurs, checklist production · 2×1h

### Claude Code : Architecture et écosystème

- [Masterclass Claude Code & Workflow](05-claude/cours-claude-code-workflow/index.html) | **Avancé** | HTML | 12 modules : CLAUDE.md, mémoire persistante, hiérarchie de contexte, Skills, Hooks, permissions, workflow quotidien <sub>*(avr. 2026)*</sub>
  - [Version Markdown](05-claude/cours-claude-code-workflow/cours_claude_code_workflow.md)

- [Formation IA Avancée : Maîtriser l'Écosystème Claude Code (14H)](05-claude/cours-claude-code-ia/README.md) | **Avancé** | MD | 6 modules, base sur l'analyse de 15 dépôts GitHub, public industrie tous profils <sub>*(mai 2026)*</sub>
  - [Module 1 : Introduction à l'IA Agentique](05-claude/cours-claude-code-ia/01-introduction-ia-agentique.md) | *De l'assistant à l'agent : contexte, enjeux, paradigme (1h30)* <sub>*(mai 2026)*</sub>
  - [Module 2 : Concepts Fondamentaux](05-claude/cours-claude-code-ia/02-concepts-fondamentaux.md) | *Glossaire illustré, architecture d'un agent (2h)* <sub>*(mai 2026)*</sub>
  - [Module 3 : Les 15 Ressources GitHub](05-claude/cours-claude-code-ia/03-ressources-github.md) | *Analyse détaillée des dépôts de référence (3h)* <sub>*(mai 2026)*</sub>
  - [Module 4 : Cas d'Usage Métier](05-claude/cours-claude-code-ia/04-cas-usage-metiers.md) | *Scénarios concrets par profil professionnel (3h)* <sub>*(mai 2026)*</sub>
  - [Module 5 : Méthodologies Pratiques](05-claude/cours-claude-code-ia/05-methodologies-pratiques.md) | *Workflows, TDD agentique, bonnes pratiques (2h)* <sub>*(mai 2026)*</sub>
  - [Module 6 : Guide de Démarrage](05-claude/cours-claude-code-ia/06-guide-demarrage.md) | *Feuille de route personnalisée, exercices (2h)* <sub>*(mai 2026)*</sub>

- [Guide débutants Claude Code](05-claude/guide-claude-code-debutants/guide-complet.md) | **Pratique** | MD | Prise en main progressive de Claude Code pour non-développeurs <sub>*(mai 2026)*</sub>

### Workflows avancés

- [TP : Workflows avancés Claude Code : maîtriser le contexte](05-claude/TP_Workflow_Avance_Claude_Code/README.md) | **Avancé** | MD | Demi-journée (3h30), ancrage industrie/maintenance : hooks vs CLAUDE.md, sous-agents et isolation de contexte, séparation spec/implémentation, /compact et /clear, Skills de convention, migration fan-out, git worktree. Dépôt fil rouge manipulable + corrigés formateur <sub>*(juin 2026)*</sub>
  - [Fiche apprenant : 8 exercices](05-claude/TP_Workflow_Avance_Claude_Code/fiche_apprenant.md) | [Guide formateur](05-claude/TP_Workflow_Avance_Claude_Code/guide_formateur.md)

### Plugins et MCP

- [Fiche procédurale : Les plugins Claude](05-claude/Fiche_Procedurale_Plugins_Claude.md) | **Pratique** | MD | Types de plugins (MCP, Skills, Commands, Hooks), installation dans Claude Code et l'application bureau, dix plugins principaux avec cas d'usage, recommandations par profil <sub>*(mai 2026)*</sub>

### Aide-mémoire opérationnel

- [Cheat Sheet : Claude Code en pratique](05-claude/cheat-sheet-claude-code-pratique.html) | **Découverte** | HTML + PDF | Aide-mémoire vulgarisé pour public non technique : trouver le bon outil avec `find-skills` (décrire le résultat, lire le nombre d'installations) et les 13 astuces bash essentielles (format débutant/pro avec cas d'usage et glossaire des symboles) <sub>*(juin 2026)*</sub>
  - [Version PDF imprimable](05-claude/cheat-sheet-claude-code-pratique.pdf)

### Skills

Note : plusieurs supports Skills coexistent ci-dessous. Désigne une source de référence unique et archive le reste.

- [Formation : Créer des skills pour Claude (1 jour)](05-claude/Formation_Creer_des_Skills/LISEZMOI.md) | **Pratique** | DOCX + PDF | Journée 7h autonome (aucune vidéo requise), public mixte non-développeurs et techniques : 6 modules, livret stagiaire, support formateur, cahier de 4 TP guidés + corrigés et compétences SKILL.md d'exemple : Claude Code et application bureau <sub>*(juin 2026)*</sub>
  - [Support formateur](05-claude/Formation_Creer_des_Skills/Support_formateur_Creer_des_Skills.docx) | [Livret stagiaire](05-claude/Formation_Creer_des_Skills/Livret_stagiaire_Creer_des_Skills.docx) | [Cahier de TP](05-claude/Formation_Creer_des_Skills/Travaux_pratiques/Cahier_TP_Creer_des_Skills.docx)

- [Formation Agents et Skills IA : Programme 2 jours](05-claude/skills/Formation_Skills/Plan_Formation_Skills.md) | **Avancé** | MD | Transformer des utilisateurs occasionnels en experts de l'automatisation : installation, diagnostic amnésie LLMs, ateliers par métiers, paramétrage d'agents personnalisés <sub>*(mars 2026)*</sub>
  - [Guide Apprenant : Skills](05-claude/skills/Formation_Skills/Guide_Apprenant_Skills.md) <sub>*(mars 2026)*</sub>

- [Cours Interactif Skills Claude Code](05-claude/cours-skills-claude.html) | **Avancé** | HTML | Cours structuré sur la création et l'usage des Skills dans Claude Code <sub>*(mai 2026)*</sub>

- [Guide de référence : Claude Code Skills](05-claude/Claude%20Code%20Skills.docx) | **Avancé** | DOCX | Document de référence complet sur les Skills <sub>*(mai 2026)*</sub>
- [Plan Formation Skills Claude (v3)](05-claude/Plan_Formation_Claude_Skills_v3.docx) | **Avancé** | DOCX | Programme pédagogique révisé (version formateur) <sub>*(mai 2026)*</sub>
- [Plan Formation Skills Gemini](05-claude/Plan_Formation_GEMINI_Skills.docx) | **Avancé** | DOCX | Équivalent pour l'écosystème Gemini CLI <sub>*(mai 2026)*</sub>

### Hooks

- [Guide complet : Claude Code Hooks](05-claude/A%20Complete%20Guide%20to%20Claude%20Code%20Hooks.docx) | **Avancé** | DOCX | Référence exhaustive : syntaxe, cas d'usage, sécurité, exemples <sub>*(mai 2026)*</sub>
- [Plan Formation Claude Hooks](05-claude/Plan_Formation_Claude_Hooks_v2.docx) | **Avancé** | DOCX | Programme de formation pédagogique sur les Hooks <sub>*(mai 2026)*</sub>

### Cowork (délégation et automatisation)

- [Guide Cowork : 12 leçons + 7 scénarios](05-claude/cowork-complete-guide/cowork-complete-guide/START-HERE.md) | **Avancé** | MD | Du premier contact avec Cowork jusqu'à l'IA comme employé autonome : délégation, organisation, recherche, création documentaire, automatisation navigateur <sub>*(avr. 2026)*</sub>
- [Guide Cowork](05-claude/guide_cowork.docx) | **Avancé** | DOCX | Version condensée du guide Cowork <sub>*(avr. 2026)*</sub>

### Documents de référence

- [Guide Claude Code CLI](05-claude/guide_claude_code_CLI.docx) | **Pratique** | DOCX | Référence complète des commandes Claude Code en ligne de commande <sub>*(avr. 2026)*</sub>
- [Formation Claude Code](05-claude/Formation_Claude_Code.docx) | **Avancé** | DOCX | Support de formation générale Claude Code <sub>*(avr. 2026)*</sub>

---

## 6. IA appliquée à l'industrie

### Formation IA Usages Industrie UIMM-CVDL

Six activités guidées pour techniciens et opérateurs, avec guides formateurs et corrigés :

- [Vue d'ensemble : Formation IA Industrie](06-ia-industrie/usages-industrie/README.md) | **Pratique** | MD | Présentation de la démarche et des 6 activités <sub>*(déc. 2025)*</sub>

  - [A1 : Analyse de Données GMAO](06-ia-industrie/usages-industrie/A1_Analyse_Donnees_GMAO/README.md) | **Pratique** | MD + Python | Exploiter des données d'interventions GMAO (CSV) avec l'IA pour identifier les équipements critiques <sub>*(déc. 2025)*</sub>
  - [A2 : Assistant Diagnostic](06-ia-industrie/usages-industrie/A2_Assistant_Diagnostic/README.md) | **Pratique** | MD | Construire un assistant de diagnostic panne à partir de bases de connaissances (pneumatique, variateurs, pompes) <sub>*(déc. 2025)*</sub>
  - [A3 : Rédaction de Procédures Sécurité](06-ia-industrie/usages-industrie/A3_Procedures_Securite/README.md) | **Pratique** | MD | Utiliser l'IA pour générer et valider des procédures d'intervention en sécurité <sub>*(déc. 2025)*</sub>
  - [A4 : Maintenance Prédictive](06-ia-industrie/usages-industrie/A4_Maintenance_Predictive/README.md) | **Avancé** | MD + Python | Analyse de relevés capteurs sur 12 mois, détection d'anomalies, esprit critique face aux résultats IA <sub>*(déc. 2025)*</sub>
  - [A5 : Documentation Technique](06-ia-industrie/usages-industrie/A5_Documentation_Technique/README.md) | **Pratique** | MD | Générer de la documentation technique structurée à partir d'un manuel de variateur <sub>*(déc. 2025)*</sub>
  - [A6 : Diagnostic Panne Intermittente](06-ia-industrie/usages-industrie/A6_Diagnostic_Panne_Intermittente/instructions_apprenant.md) | **Avancé** | MD | Analyser des logs de convoyeur pour diagnostiquer une panne intermittente complexe <sub>*(déc. 2025)*</sub>

### Activités transversales

- [A5 : IA Rédactrice de Rapports](06-ia-industrie/A5_IA_Redactrice_de_rapports/) | **Pratique** | MD | Analyser des données CSV et générer un rapport de synthèse structuré <sub>*(nov. 2025)*</sub>
- [A6 : Futur du Développement avec l'IA](01-comprendre-ia/activites/A6_Futur_Dev_IA/index.html) | **Découverte** | HTML | Explorer l'impact de l'IA sur les métiers du développement <sub>*(nov. 2025)*</sub>

### Contenus archivés

Les huit modules HTML de la version 1 (novembre 2025) ont été déplacés dans `_archive/Formation_V1`. Ils recoupaient le prompt engineering des sections 2 et 6. À rouvrir seulement si besoin.

### Cas d'usage professionnels (Formation Continue)

Cinq scénarios clés en main pour animer des ateliers en Formation Continue :

- [Cas 1 : Finance](06-ia-industrie/cas-usage-formation-continue/Cas_Usage_1_Finance/Guide_Activite.md) | Analyse d'un rapport annuel, extraction de KPIs <sub>*(nov. 2025)*</sub>
- [Cas 2 : Pédagogie](06-ia-industrie/cas-usage-formation-continue/Cas_Usage_2_Pedagogie/Guide_Activite_Pedagogie.md) | Exploitation d'un programme de formation et d'un référentiel RNCP <sub>*(nov. 2025)*</sub>
- [Cas 3 : Transformation Digitale](06-ia-industrie/cas-usage-formation-continue/Cas_Usage_3_Transformation/Guide_Activite_Transformation.md) | Conduite du changement et accompagnement managérial <sub>*(nov. 2025)*</sub>
- [Cas 4 : RH](06-ia-industrie/cas-usage-formation-continue/Cas_Usage_4_RH/Guide_Activite_RH.md) | Analyse de fiches de poste, recrutement assisté par IA <sub>*(nov. 2025)*</sub>
- [Cas 5 : Data](06-ia-industrie/cas-usage-formation-continue/Cas_Usage_5_Data/Guide_Activite_Data.md) | Analyse de données industrielles (robots installés) <sub>*(nov. 2025)*</sub>

### Support de cours

- [Cours IA pour l'Industrie](06-ia-industrie/cours_IA_industrie.docx) | **Pratique** | DOCX | Support complet destiné aux salariés et techniciens : maintenance, qualité, production, documentation technique <sub>*(mai 2026)*</sub>

---

## 7. Ressources et outils

### Tableaux de bord et suivi pédagogique

- [Tableau de Bord : Formation IA](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/Tableau_de_Bord_Interactif_Formation_IA.html) | HTML | Suivi interactif de la progression des apprenants <sub>*(déc. 2025)*</sub>
- [Ateliers Pratiques Gemini CLI](https://sjaubert.github.io/Cours-IA/03-outils-google/ia-education/Ateliers_Pratiques.html) | HTML | Banque d'exercices pratiques pour animer une session <sub>*(déc. 2025)*</sub>

### Premiers pas (entrée en formation)

- [Initiation IA 7H](00-demarrer/initiation-ia/Initiation_IA_7H.md) | **Découverte** | MD | Programme complet d'une journée d'initiation à l'IA, tous publics <sub>*(avr. 2026)*</sub>
- [Carnet de Prompts IA](00-demarrer/initiation-ia/Carnet_de_prompts_IA.md) | **Découverte** | MD | Recueil de prompts commentés pour débuter en autonomie <sub>*(avr. 2026)*</sub>
- [Plan Formation IA : AFPI](ressources/offres-et-dispositifs/Plan_Formation_IA_AFPI.md) | MD | Dispositif de formation IA adapté au contexte AFPI. [Version Word](ressources/offres-et-dispositifs/Plan_Formation_IA_AFPI.docx) <sub>*(avr. 2026)*</sub>
- [Proposition d'animation et cahier des charges](ressources/offres-et-dispositifs/Proposition_Formation_IA_CahierDesCharges.html) | HTML | Programme 2 jours, public mixte industrie, outils Gemini/Claude/Antigravity/NotebookLM : cahier des charges équipements et abonnements, scénarios cloud et Ollama local <sub>*(mai 2026)*</sub>
  - [Version Word (.docx)](ressources/offres-et-dispositifs/Proposition_Formation_IA_CahierDesCharges.docx)

### Références et documents transversaux

- [Prompts & Ressources IA](ressources/Prompts_et_Ressources_IA.md) | MD | Compilation de ressources et prompts utiles, classés par usage <sub>*(nov. 2025)*</sub>
- [Cheat Sheet IA](00-demarrer/cheat_sheet.md) | MD | Aide-mémoire synthétique : commandes, paramètres, bonnes pratiques <sub>*(mars 2026)*</sub>

---

## 8. IA locale et souveraineté

### Déployer une IA 100% locale (projet expérimental 00Exp)

Apprendre l'IA en mettant les mains dans la machine : faire tourner un modèle sur son poste, sans réseau, comprendre ce qui se passe et l'enseigner.

- [Feuille de route : IA locale pas à pas](https://sjaubert.github.io/Cours-IA/07-ia-locale/ia-locale-pas-a-pas/index.html) | **Pratique** | HTML | Matériel recommandé, Ollama et ses alternatives, modèles open source (Gemma 3, Qwen Coder, Llama 3.2), 3 paliers progressifs (démo pédagogique, assistant de code dans VS Code avec Continue, agent autonome avec Goose), cas d'usage et défis étudiants, enjeux de souveraineté, sécurité et écologie <sub>*(juin 2026)*</sub>
  - [Version Markdown](07-ia-locale/ia-locale-pas-a-pas/Feuille_de_route_IA_locale.md) | [Export imprimable](07-ia-locale/ia-locale-pas-a-pas/Feuille_de_route_IA_locale.html)
  - Fichiers d'exemple pour les démos d'agent : [dossier bac_a_sable](07-ia-locale/ia-locale-pas-a-pas/bac_a_sable/)

---

## Notes techniques

- Navigateur recommandé : Chrome, Firefox, Edge ou Safari (version récente)
- JavaScript requis pour toutes les activités interactives
- Les fichiers DOCX s'ouvrent avec Microsoft Word ou LibreOffice
- Les fichiers MD s'affichent directement sur GitHub ou via un éditeur Markdown

---

## Contact

**Pôle Formation UIMM CVDL**
Formateur : S. Jaubert
Formation sur l'Intelligence Artificielle et ses applications industrielles

---

*Dernière mise à jour : 12 septembre 2026. Actualisation du cours magistral d'introduction à l'IA (promotion 2026 : support interactif Web, conducteur pédagogique sourcé, intégration des ruptures agentiques et du cadre réglementaire AI Act).*
