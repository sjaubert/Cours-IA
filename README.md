# Cours d'Introduction à l'Intelligence Artificielle

## ![Logo UIMM](logo_uimm_placeholder.jpg) Pôle Formation UIMM CVDL — S. Jaubert

---

## Navigation rapide

| # | Thème | Public cible |
|---|---|---|
| [1](#1-comprendre-lia--fondamentaux-et-biais) | Comprendre l'IA — Fondamentaux et biais | Tous |
| [2](#2-prompt-engineering) | Prompt Engineering | Tous |
| [3](#3-gemini-cli--workspace-ia) | Gemini CLI & Workspace IA | Techniciens, formateurs |
| [4](#4-notebooklm) | NotebookLM | Formateurs, managers |
| [5](#5-claude-code--agents-ia) | Claude Code & Agents IA | Utilisateurs avancés |
| [6](#6-ia-appliquée-à-lindustrie) | IA appliquée à l'industrie | Techniciens, opérateurs |
| [7](#7-ressources--outils) | Ressources & Outils | Formateurs |

---

## Légende des niveaux

- **Découverte** — aucun prérequis, première approche
- **Pratique** — bases en IA acquises, manipulation autonome des outils
- **Avancé** — expérience des outils IA agentiques requise

---

## 1. Comprendre l'IA — Fondamentaux et Biais

### Démonstrations interactives

- [Les 7 Paramètres qui Contrôlent l'IA](https://sjaubert.github.io/Cours-IA/ai-parameters-demo/index.html) — **Découverte** | HTML | Expérimentation en temps réel de Temperature, Top-P, Max Tokens et leur impact sur les réponses <sub>*(déc. 2025)*</sub>

- [Visualisation Réseaux de Neurones](Activités/A7_Reseaux_Neurones/index.html) — **Pratique** | HTML | Deux simulateurs : régression linéaire interactive et réseau de neurones avec rétropropagation configurable <sub>*(déc. 2025)*</sub>
  - [Régression Linéaire Interactive](Activités/A7_Reseaux_Neurones/1_regression_lineaire.html) — Manipulation de points et calcul de droite de régression
  - [Réseau de Neurones avec Apprentissage Supervisé](Activités/A7_Reseaux_Neurones/2_reseau_neurones.html) — Architecture configurable
  - [Guide d'utilisation pédagogique](Activités/A7_Reseaux_Neurones/README.md) | [Synthèse Architecture](Activités/A7_Reseaux_Neurones/Synthese_Architecture.md) | [Guide complet](Activités/A7_Reseaux_Neurones/Guide_Architecture_Reseaux.md)

### Activités sur les biais et les limites de l'IA

Formation interactive en 6 activités (biais cognitifs, première impression, sélection, confirmation, culturels, jeu de rôle) :

- [Formation Intelligence Artificielle : Les Biais](https://sjaubert.github.io/Cours-IA/00-Formation/Activites-Biais/index.html) — **Découverte** | HTML | Point d'entrée avec guide formateur et support apprenant <sub>*(déc. 2025)*</sub>

Activités autonomes (approche par cas) :

- [A1 — Illusion de Vérité](Activit%C3%A9s/A1_illusion_v%C3%A9rit%C3%A9/instructions_apprenant.md) — **Découverte** | MD | L'IA génère des textes crédibles contenant des erreurs factuelles <sub>*(nov. 2025)*</sub>
- [A2 — Biais de Confirmation](Activit%C3%A9s/A2_Biais_Confirmation/) — **Découverte** | MD | L'IA argumente des points de vue opposés selon le contexte <sub>*(nov. 2025)*</sub>
- [A3 — Biais Culturel](Activit%C3%A9s/A3_Biais_Culturel/) — **Découverte** | MD | Les LLMs reflètent les biais culturels de leurs données d'entraînement <sub>*(nov. 2025)*</sub>
- [A4 — Illusion de Raisonnement](Activit%C3%A9s/A4_Illusion_raisonnement/) — **Découverte** | MD | L'IA ne raisonne pas au sens humain : corrélations statistiques vs. logique <sub>*(nov. 2025)*</sub>

---

## 2. Prompt Engineering

### Guides de référence

- [Guide Interactif Art du Prompt](https://sjaubert.github.io/Cours-IA/IA-Education/Guide_Interactif_Prompt.html) — **Découverte** | HTML | Introduction structurée aux principes du prompting efficace <sub>*(déc. 2025)*</sub>

- [PromptFlow UIMM Studio](https://sjaubert.github.io/Cours-IA/00-Formation/prompt_flow_uimm/dist/index.html) — **Pratique** | App Web | Outil de création pédagogique pour concevoir des séquences de prompts <sub>*(déc. 2025)*</sub>

### Ateliers de formation

- [Formation Journée Prompt Engineering](Formation-Journee-PromptEngineering/README.md) — **Pratique** | MD + HTML | Programme d'une journée avec 3 ateliers complets <sub>*(déc. 2025)*</sub>
  - [Atelier 1 — Les 6 Piliers](Formation-Journee-PromptEngineering/Atelier1_6Piliers.html) | [Corrigés formateur](Formation-Journee-PromptEngineering/Atelier1_Corriges_Formateur.md)
  - [Atelier 2 — Exercices Pratiques](Formation-Journee-PromptEngineering/Atelier2_Exercices_Pratiques.html) | [Corrigés formateur](Formation-Journee-PromptEngineering/Atelier2_Corriges_Formateur.md)
  - [Atelier 3 — Techniques Avancées](Formation-Journee-PromptEngineering/Atelier3_Techniques_Avancees.html) | [Corrigés formateur](Formation-Journee-PromptEngineering/Atelier3_Corriges_Formateur.md)

- [Formation Prompt Engineering — Maintenance Industrielle](00-Formation/Formation_Prompt/Formation_Prompt_Maintenance_Etudiants.html) — **Pratique** | HTML | 4h pour étudiants Bachelor Maintenance : cas d'usage réalistes, travaux de groupe, sensibilisation aux biais <sub>*(jan. 2026)*</sub>
  - [Guide Formateur](00-Formation/Formation_Prompt/Formation_Prompt_Maintenance_Guide_Formateur.md)

---

## 3. Gemini CLI & Workspace IA

### Installation et configuration

- [Installation Gemini CLI](https://sjaubert.github.io/Cours-IA/IA-Education/Gemin-cli%20V2.html) — **Pratique** | HTML | Procédure d'installation pas à pas <sub>*(déc. 2025)*</sub>
- [Installation MCP Workspace](https://sjaubert.github.io/Cours-IA/IA-Education/gemini-cli_workspace.html) — **Pratique** | HTML | Configuration de l'environnement MCP pour Google Workspace <sub>*(déc. 2025)*</sub>
- <a href="https://sjaubert.github.io/Cours-IA/Formation_Agentic_Workspace/gemini_cli_workspace.html" target="_blank">Gemini CLI Extension pour Google Workspace</a> — **Pratique** | HTML | Intégration Gemini dans l'écosystème Google <sub>*(déc. 2025)*</sub>
- [Antigravity — Guide d'installation](https://sjaubert.github.io/Cours-IA/antigravity/guide_antigravity.html) — **Pratique** | HTML | Installation et prise en main d'Antigravity <sub>*(déc. 2025)*</sub>

### Tutoriels

- [Astuces Gemini CLI](https://sjaubert.github.io/Cours-IA/IA-Education/astuce_geminiCLI.html) — **Pratique** | HTML | Raccourcis et commandes utiles au quotidien <sub>*(déc. 2025)*</sub>
- [Tutoriel Google Apps Script](https://sjaubert.github.io/Cours-IA/IA-Education/tutoriel_google_appsscript.html) — **Pratique** | HTML | Automatisation de Google Workspace via Apps Script <sub>*(déc. 2025)*</sub>
- [Tutoriel Sécurité Gemini](https://sjaubert.github.io/Cours-IA/IA-Education/tutoriel-gemini-secure.html) — **Pratique** | HTML | Bonnes pratiques de sécurité et confidentialité <sub>*(déc. 2025)*</sub>
- [Tutoriel Automatisation Workspace](https://sjaubert.github.io/Cours-IA/IA-Education/Tutoriel_Automatisation_Workspace.html) — **Pratique** | HTML | Workflows automatisés dans Google Workspace <sub>*(déc. 2025)*</sub>
- [Tutoriel Automatisation Agentique](https://sjaubert.github.io/Cours-IA/IA-Education/Agentic_Automation_Tutorial.html) — **Avancé** | HTML | Conception d'agents IA autonomes avec Gemini CLI <sub>*(déc. 2025)*</sub>
- [Antigravity — Tutoriel avancé](https://sjaubert.github.io/Cours-IA/IA-Education/antigravity_tutorial.html) — **Avancé** | HTML | Fonctionnalités avancées d'Antigravity <sub>*(déc. 2025)*</sub>

### Parcours de formation complets

- <a href="https://sjaubert.github.io/Cours-IA/Formation_Agentic_Workspace/guide_formation_ia.html" target="_blank">Guide Formation IA & Productivité — Gemini CLI & MCP</a> — **Avancé** | HTML | Programme structuré d'adoption de Gemini CLI en contexte professionnel <sub>*(nov. 2025)*</sub>
- [Formation Agentic Workspace](Formation_Agentic_Workspace/index.html) — **Avancé** | HTML | Parcours complet avec exercices et corrigés par module <sub>*(nov. 2025)*</sub>
- [Navigation Tutoriels Gemini CLI & MCP](https://sjaubert.github.io/Cours-IA/Formation_Agentic_Workspace/tutoriels_gemini_mcp.html) — **Avancé** | HTML | Guide de navigation entre les ressources Gemini CLI et MCP <sub>*(déc. 2025)*</sub>

---

## 4. NotebookLM

### Prise en main

- [Présentation NotebookLM](NoteBLM/index.html) — **Découverte** | HTML | Introduction interactive : principes, cas d'usage, interface <sub>*(jan. 2026)*</sub>
- [TP Prise en main — Presse Hydraulique](NoteBLM/scenario_tp_notebooklm.html) — **Pratique** | HTML | Cas concret industrie : analyser la documentation d'une presse hydraulique <sub>*(jan. 2026)*</sub>

### Formation structurée 7H

- [Parcours complet — Formation 7H](NoteBLM/Formation_7H/parcours_formation.html) — **Pratique** | HTML | 5 shifts cognitifs progressifs pour maîtriser NotebookLM <sub>*(fév. 2026)*</sub>
  - [Module 1 — Comprendre NotebookLM](NoteBLM/Formation_7H/M1_comprendre_nblm.html) — *L'espace clos : la qualité vient des sources* <sub>*(fév. 2026)*</sub>
  - [Module 2 — L'art de questionner](NoteBLM/Formation_7H/M2_art_questionner.html) — *Contraindre la question pour augmenter sa puissance* <sub>*(fév. 2026)*</sub>
  - [Module 3 — Vérifier et citer](NoteBLM/Formation_7H/M3_verifier_citer.html) — *L'IA hallucine, la citation ancre* <sub>*(fév. 2026)*</sub>
  - [Module 4 — Produire en boucle créative](NoteBLM/Formation_7H/M4_produire_boucler.html) — *Itérer, reformater, exporter* <sub>*(fév. 2026)*</sub>
  - [Module 5 — Penser avec NotebookLM](NoteBLM/Formation_7H/M5_penser_avec_nblm.html) — *Les méta-patterns, l'outil de pensée durable* <sub>*(fév. 2026)*</sub>
  - [Guide Formateur](NoteBLM/Formation_7H/guide_formateur.html) | [Fiches Activités Imprimables](NoteBLM/Formation_7H/fiches_activites.html) <sub>*(fév. 2026)*</sub>

---

## 5. Claude Code & Agents IA

### Maîtriser Claude — Formations structurées

- [Syllabus — Maîtriser Claude (4 blocs)](CLAUDE/Formation_Maitriser_Claude/plan_de_formation.html) — **Pratique** | HTML | Plan d'ingénierie pédagogique restructuré pour salariés : formateurs, administratifs, ingénieurs <sub>*(avr. 2026)*</sub>
- [Livret Pratique — Maîtriser Claude](CLAUDE/Formation_Maitriser_Claude/Livret_Pratique.html) — **Pratique** | HTML | Manuel apprenant : exercices pas à pas, fichiers Markdown (identité, contraintes), prompts contre les hallucinations <sub>*(avr. 2026)*</sub>
- [Construire un agent IA avec Claude — Plan de formation](CLAUDE/formation-agent-ia/plan_formation_agent_claude.html) — **Avancé** | HTML | Parcours 6 semaines en 4 étapes progressives : agent mono-outil, tests mesurables, multi-outils + mémoire, affinage et mise en production — cas d'usage RH, administratif, comptabilité <sub>*(mai 2026)*</sub>
  - [Semaine 1 — Découvrir les agents IA avec Claude.ai](CLAUDE/formation-agent-ia/semaine1.html) — Guide formateur + fiche apprenant + activités · Niveau A · 2h30
  - [Semaine 2 — Premier agent HTML avec recherche web](CLAUDE/formation-agent-ia/semaine2.html) — Clé API, prompt système, web_search · Niveau B · 2h30
  - [Semaine 3 — Mesurer et améliorer la qualité](CLAUDE/formation-agent-ia/semaine3.html) — Grille 5 critères, scénarios de test, OODA · 2×1h
  - [Semaine 4 — Connecter Drive et Agenda via MCP](CLAUDE/formation-agent-ia/semaine4.html) — MCP Google, workflows multi-outils · 1h30
  - [Semaine 5 — Gmail, mémoire et workflows automatisés](CLAUDE/formation-agent-ia/semaine5.html) — MCP Gmail, mémoire conversationnelle · 1h30
  - [Semaine 6 — Évaluation finale et mise en production](CLAUDE/formation-agent-ia/semaine6.html) — Bilan scores, catalogue erreurs, checklist production · 2×1h

### Claude Code — Architecture et écosystème

- [Masterclass Claude Code & Workflow](CLAUDE/cours-claude-code-workflow/index.html) — **Avancé** | HTML | 12 modules : CLAUDE.md, mémoire persistante, hiérarchie de contexte, Skills, Hooks, permissions, workflow quotidien <sub>*(avr. 2026)*</sub>
  - [Version Markdown](CLAUDE/cours-claude-code-workflow/cours_claude_code_workflow.md)

- [Formation IA Avancée — Maîtriser l'Écosystème Claude Code (14H)](cours-claude-code-ia/README.md) — **Avancé** | MD | 6 modules, base sur l'analyse de 15 dépôts GitHub, public industrie tous profils <sub>*(mai 2026)*</sub>
  - [Module 1 — Introduction à l'IA Agentique](cours-claude-code-ia/01-introduction-ia-agentique.md) — *De l'assistant à l'agent : contexte, enjeux, paradigme (1h30)* <sub>*(mai 2026)*</sub>
  - [Module 2 — Concepts Fondamentaux](cours-claude-code-ia/02-concepts-fondamentaux.md) — *Glossaire illustré, architecture d'un agent (2h)* <sub>*(mai 2026)*</sub>
  - [Module 3 — Les 15 Ressources GitHub](cours-claude-code-ia/03-ressources-github.md) — *Analyse détaillée des dépôts de référence (3h)* <sub>*(mai 2026)*</sub>
  - [Module 4 — Cas d'Usage Métier](cours-claude-code-ia/04-cas-usage-metiers.md) — *Scénarios concrets par profil professionnel (3h)* <sub>*(mai 2026)*</sub>
  - [Module 5 — Méthodologies Pratiques](cours-claude-code-ia/05-methodologies-pratiques.md) — *Workflows, TDD agentique, bonnes pratiques (2h)* <sub>*(mai 2026)*</sub>
  - [Module 6 — Guide de Démarrage](cours-claude-code-ia/06-guide-demarrage.md) — *Feuille de route personnalisée, exercices (2h)* <sub>*(mai 2026)*</sub>

- [Guide débutants Claude Code](CLAUDE/guide-claude-code-debutants/guide-complet.md) — **Pratique** | MD | Prise en main progressive de Claude Code pour non-développeurs <sub>*(mai 2026)*</sub>

### Plugins et MCP

- [Fiche procédurale — Les plugins Claude](CLAUDE/Fiche_Procedurale_Plugins_Claude.md) — **Pratique** | MD | Types de plugins (MCP, Skills, Commands, Hooks), installation dans Claude Code et l'application bureau, dix plugins principaux avec cas d'usage, recommandations par profil <sub>*(mai 2026)*</sub>

### Skills

- [Formation Agents et Skills IA — Programme 2 jours](00-Formation/IA_Skills/Formation_Skills/Plan_Formation_Skills.md) — **Avancé** | MD | Transformer des utilisateurs occasionnels en experts de l'automatisation : installation, diagnostic amnésie LLMs, ateliers par métiers, paramétrage d'agents personnalisés <sub>*(mars 2026)*</sub>
  - [Guide Apprenant — Skills](00-Formation/IA_Skills/Formation_Skills/Guide_Apprenant_Skills.md) <sub>*(mars 2026)*</sub>

- [Cours Interactif Skills Claude Code](CLAUDE/cours-skills-claude.html) — **Avancé** | HTML | Cours structuré sur la création et l'usage des Skills dans Claude Code <sub>*(mai 2026)*</sub>

- [Guide de référence — Claude Code Skills](CLAUDE/Claude%20Code%20Skills.docx) — **Avancé** | DOCX | Document de référence complet sur les Skills
- [Plan Formation Skills Claude v2](CLAUDE/Plan_Formation_Claude_Skills_v2.docx) — **Avancé** | DOCX | Programme pédagogique révisé (version formateur)
- [Plan Formation Skills Gemini](CLAUDE/Plan_Formation_GEMINI_Skills.docx) — **Avancé** | DOCX | Équivalent pour l'écosystème Gemini CLI

### Hooks

- [Guide complet — Claude Code Hooks](CLAUDE/A%20Complete%20Guide%20to%20Claude%20Code%20Hooks.docx) — **Avancé** | DOCX | Référence exhaustive : syntaxe, cas d'usage, sécurité, exemples
- [Plan Formation Claude Hooks](CLAUDE/Plan_Formation_Claude_Hooks.docx) — **Avancé** | DOCX | Programme de formation pédagogique sur les Hooks

### Cowork (délégation et automatisation)

- [Guide Cowork — 12 leçons + 7 scénarios](CLAUDE/cowork-complete-guide/cowork-complete-guide/START-HERE.md) — **Avancé** | MD | Du premier contact avec Cowork jusqu'à l'IA comme employé autonome : délégation, organisation, recherche, création documentaire, automatisation navigateur <sub>*(avr. 2026)*</sub>
- [Guide Cowork](CLAUDE/guide_cowork.docx) — **Avancé** | DOCX | Version condensée du guide Cowork

### Documents de référence

- [Guide Claude Code CLI](CLAUDE/guide_claude_code_CLI.docx) — **Pratique** | DOCX | Référence complète des commandes Claude Code en ligne de commande
- [Formation Claude Code](CLAUDE/Formation_Claude_Code.docx) — **Avancé** | DOCX | Support de formation générale Claude Code

---

## 6. IA Appliquée à l'Industrie

### Formation IA Usages Industrie UIMM-CVDL

Six activités guidées pour techniciens et opérateurs, avec guides formateurs et corrigés :

- [Vue d'ensemble — Formation IA Industrie](Formation_IA_Usages_Industrie_UIMM-CVDL/README.md) — **Pratique** | MD | Présentation de la démarche et des 6 activités <sub>*(déc. 2025)*</sub>

  - [A1 — Analyse de Données GMAO](Formation_IA_Usages_Industrie_UIMM-CVDL/A1_Analyse_Donnees_GMAO/README.md) — **Pratique** | MD + Python | Exploiter des données d'interventions GMAO (CSV) avec l'IA pour identifier les équipements critiques <sub>*(déc. 2025)*</sub>
  - [A2 — Assistant Diagnostic](Formation_IA_Usages_Industrie_UIMM-CVDL/A2_Assistant_Diagnostic/README.md) — **Pratique** | MD | Construire un assistant de diagnostic panne à partir de bases de connaissances (pneumatique, variateurs, pompes) <sub>*(déc. 2025)*</sub>
  - [A3 — Rédaction de Procédures Sécurité](Formation_IA_Usages_Industrie_UIMM-CVDL/A3_Procedures_Securite/README.md) — **Pratique** | MD | Utiliser l'IA pour générer et valider des procédures d'intervention en sécurité <sub>*(déc. 2025)*</sub>
  - [A4 — Maintenance Prédictive](Formation_IA_Usages_Industrie_UIMM-CVDL/A4_Maintenance_Predictive/README.md) — **Avancé** | MD + Python | Analyse de relevés capteurs sur 12 mois, détection d'anomalies, esprit critique face aux résultats IA <sub>*(déc. 2025)*</sub>
  - [A5 — Documentation Technique](Formation_IA_Usages_Industrie_UIMM-CVDL/A5_Documentation_Technique/README.md) — **Pratique** | MD | Générer de la documentation technique structurée à partir d'un manuel de variateur <sub>*(déc. 2025)*</sub>
  - [A6 — Diagnostic Panne Intermittente](Formation_IA_Usages_Industrie_UIMM-CVDL/A6_Diagnostic_Panne_Intermittente/instructions_apprenant.md) — **Avancé** | MD | Analyser des logs de convoyeur pour diagnostiquer une panne intermittente complexe <sub>*(déc. 2025)*</sub>

### Activités transversales

- [A5 — IA Rédactrice de Rapports](Activit%C3%A9s/A5%20IA%20R%C3%A9dactrice%20de%20rapports/) — **Pratique** | MD | Analyser des données CSV et générer un rapport de synthèse structuré <sub>*(nov. 2025)*</sub>
- [A6 — Futur du Développement avec l'IA](Activit%C3%A9s/A6_Futur_Dev_IA/index.html) — **Découverte** | HTML | Explorer l'impact de l'IA sur les métiers du développement <sub>*(nov. 2025)*</sub>

### Formation Modules HTML — Version 1 (8 modules)

Séquence complète de sensibilisation, du contexte à la feuille de route :

- [Module 1 — Introduction à l'IA Générative et Enjeux Industriels](Formation_V1/Module1_Introduction_IA_Generative_Enjeux_Industriels.html) — **Découverte** <sub>*(nov. 2025)*</sub>
- [Module 2 — Risques, Éthique et Confidentialité](Formation_V1/Module_2_Risques_Ethique_Confidentialite.html) — **Découverte** <sub>*(nov. 2025)*</sub>
- [Module 3 — Principes du Prompt Engineering](Formation_V1/Module_3_Le_C%C5%93ur_Competence_Principes_Prompt_Engineering.html) — **Pratique** <sub>*(nov. 2025)*</sub>
- [Module 4 — Techniques Avancées de Prompting](Formation_V1/Module_4_Techniques_Avancees_Prompting.html) — **Pratique** <sub>*(nov. 2025)*</sub>
- [Module 5 — Atelier Cas d'Usage Métiers](Formation_V1/Module_5_Atelier_Cas_Usage_Metiers.html) — **Pratique** <sub>*(nov. 2025)*</sub>
- [Module 6 — Stratégie Entreprise — Les 7 Leçons de l'Adoption](Formation_V1/Module_6_Strategie_Entreprise-Les_7_Lecons_de_Adoption.html) — **Avancé** <sub>*(nov. 2025)*</sub>
- [Module 7 — IA Avancée, Workflows et Agents Autonomes](Formation_V1/Module_7_IA_Avancee_Workflows_Agents_Autonomes.html) — **Avancé** <sub>*(nov. 2025)*</sub>
- [Module 8 — Synthèse et Feuille de Route](Formation_V1/Module_8_Synthese_Feuille_de_Route.html) — **Avancé** <sub>*(nov. 2025)*</sub>

### Cas d'usage professionnels (Formation Continue)

Cinq scénarios clés en main pour animer des ateliers en Formation Continue :

- [Cas 1 — Finance](FC/Cas_Usage_1_Finance/Guide_Activite.md) — Analyse d'un rapport annuel, extraction de KPIs <sub>*(nov. 2025)*</sub>
- [Cas 2 — Pédagogie](FC/Cas_Usage_2_Pedagogie/Guide_Activite_Pedagogie.md) — Exploitation d'un programme de formation et d'un référentiel RNCP <sub>*(nov. 2025)*</sub>
- [Cas 3 — Transformation Digitale](FC/Cas_Usage_3_Transformation/Guide_Activite_Transformation.md) — Conduite du changement et accompagnement managérial <sub>*(nov. 2025)*</sub>
- [Cas 4 — RH](FC/Cas_Usage_4_RH/Guide_Activite_RH.md) — Analyse de fiches de poste, recrutement assisté par IA <sub>*(nov. 2025)*</sub>
- [Cas 5 — Data](FC/Cas_Usage_5_Data/Guide_Activite_Data.md) — Analyse de données industrielles (robots installés) <sub>*(nov. 2025)*</sub>

### Support de cours

- [Cours IA pour l'Industrie](cours_IA_industrie.docx) — **Pratique** | DOCX | Support complet destiné aux salariés et techniciens : maintenance, qualité, production, documentation technique <sub>*(mai 2026)*</sub>

---

## 7. Ressources & Outils

### Tableaux de bord et suivi pédagogique

- [Tableau de Bord — Formation IA](https://sjaubert.github.io/Cours-IA/IA-Education/Tableau_de_Bord_Interactif_Formation_IA.html) — HTML | Suivi interactif de la progression des apprenants <sub>*(déc. 2025)*</sub>
- [Ateliers Pratiques Gemini CLI](https://sjaubert.github.io/Cours-IA/IA-Education/Ateliers_Pratiques.html) — HTML | Banque d'exercices pratiques pour animer une session <sub>*(déc. 2025)*</sub>

### Premiers pas (entrée en formation)

- [Initiation IA 7H](00-Formation/Initiation_IA/Initiation_IA_7H.md) — **Découverte** | MD | Programme complet d'une journée d'initiation à l'IA, tous publics <sub>*(avr. 2026)*</sub>
- [Carnet de Prompts IA](00-Formation/Initiation_IA/Carnet_de_prompts_IA.md) — **Découverte** | MD | Recueil de prompts commentés pour débuter en autonomie <sub>*(avr. 2026)*</sub>
- [Plan Formation IA — AFPI](00-Formation/Plan_Formation_IA_AFPI.md) — MD | Dispositif de formation IA adapté au contexte AFPI <sub>*(avr. 2026)*</sub>
- [Proposition d'animation et cahier des charges](00-Formation/Proposition_Formation_IA_CahierDesCharges.html) — HTML | Programme 2 jours, public mixte industrie, outils Gemini/Claude/Antigravity/NotebookLM — cahier des charges équipements et abonnements, scénarios cloud et Ollama local <sub>*(mai 2026)*</sub>
  - [Version Word (.docx)](00-Formation/Proposition_Formation_IA_CahierDesCharges.docx)

### Références et documents transversaux

- [Prompts & Ressources IA](Prompts%26Ressources%20IA.md) — MD | Compilation de ressources et prompts utiles, classés par usage <sub>*(nov. 2025)*</sub>
- [Cheat Sheet IA](00-Formation/cheat_sheet.md) — MD | Aide-mémoire synthétique : commandes, paramètres, bonnes pratiques <sub>*(mars 2026)*</sub>

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

*Dernière mise à jour : Mai 2026*
