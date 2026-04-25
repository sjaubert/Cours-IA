---
output:
  word_document: default
  html_document: default
---
# Plan de Formation : Intelligence Artificielle (IA)
## Pôle Formation UIMM - CVDL | Formateur : S. JAUBERT
### Programme V3.0 — 2 jours (14 heures) — Version validée 22/04/2026

---

> [!IMPORTANT]
> Ce plan est construit à partir de la **Fiche AFPI V3.0** (maj 18-fév.-26) et s'appuie exclusivement sur les ressources pédagogiques **déjà produites** dans le dépôt `Cours-IA`. Chaque séquence est liée à un ou plusieurs fichiers sources existants.

> [!NOTE]
> **Arbitrages validés :** Public mixte (tous secteurs) — Outils retenus : **NotebookLM + Antigravity** (pas Gemini CLI, raisons de coût) — Activités Biais : **1 + 4 + 6** — Supports imprimés DOCX générés dans `00-Formation/`.

---

## Vue d'ensemble

| Élément | Détail |
|---|---|
| **Durée totale** | 2 jours — 14 heures effectives |
| **Public** | **Mixte** : techniciens, managers, RH, fonctions support, pédagogues — sans prérequis |
| **Prérequis** | Aucun |
| **Outils utilisés** | **NotebookLM** (RAG documentaire) + **Antigravity** (agent IA) + LLM au choix (Gemini/ChatGPT) |
| **Livrable stagiaire** | Attestation de capacités + Carnet de prompts personnalisé |
| **Modalité** | Présentiel — 1 poste informatique par stagiaire |
| **Méthode** | Participative, démonstrative, alternance théorie/pratique |

---

## Objectifs de la formation (Fiche AFPI)

A l'issue des 2 jours, les bénéficiaires seront capables de :

1. **Comprendre** les principes fondamentaux de l'IA et ses implications industrielles
2. **Analyser** l'impact de l'IA sur les métiers techniques et l'organisation du travail
3. **Utiliser** des outils basés sur l'IA dans leur pratique professionnelle
4. **Intégrer** l'IA dans une démarche de veille et d'amélioration continue

---

## JOUR 1 — Comprendre et Explorer l'IA (7h)

### 08h30 - 09h00 | Accueil et cadrage (30 min)

**Contenu :**
- Présentation du Pôle Formation UIMM-CVDL et du formateur
- Tour de table : attentes, représentations et niveau de connaissance des participants
- Brise-glace : "Qu'est-ce que l'IA pour vous ?" — recueil des représentations initiales

**Ressource formateur :**
- `00-Formation/Diaporama COURS Introduction IA.pptx` — Slides d'introduction générales

---

### 09h00 - 10h30 | MODULE 1 : Comprendre les fondamentaux de l'IA (1h30)

**Objectifs spécifiques :**
- Clarifier les notions liées à l'IA
- Distinguer IA / Machine Learning / Deep Learning / Programmation traditionnelle
- Démystifier les représentations (science-fiction vs réalité)

**Contenu théorique :**

1. **Qu'est-ce que l'IA ?** — Définition, histoire, grandes étapes (des pionniers à aujourd'hui)
2. **Arbre des IA** — IA symbolique vs IA apprenante ; ML supervisé, non supervisé, par renforcement
3. **Deep Learning** — Réseaux de neurones, analogie biologique, pourquoi cela "fonctionne" avec les données massives
4. **Programmation traditionnelle vs ML** — Le renversement de paradigme : "on programme les règles" vs "on apprend les règles"
5. **Données : le nerf de la guerre** — "Garbage in, garbage out", features, entraînement vs test, overfitting

**Ressources à mobiliser :**
- `00-Formation/Diaporama COURS Introduction IA.pptx` — Slides Modules 1 et 2
- `Formation_V1/Module1_Introduction_IA_Generative_Enjeux_Industriels.html` — Support HTML interactif
- `Activités/A7_Reseaux_Neurones/` — Illustration réseaux de neurones (`reseau_neurones.png`, `surface-reseau_neurones.png`)
- PDF de référence formateur : `00-Formation/IA_Histoire_Convergence.pdf`

**Activité pratique (20 min) — "Le Tri Intégral" :**
- Étude de cas papier : tableau de données comportant des aberrations (profils, factures)
- Les participants identifient quelles colonnes (features) pourraient induire un biais
- *Source :* `00-Formation/Initiation_IA/Initiation_IA_7H.md` — Module 2

---

### 10h30 - 10h45 | Pause (15 min)

---

### 10h45 - 12h15 | MODULE 2 : Explorer les IA génératives (1h30)

**Objectifs spécifiques :**
- Comprendre le fonctionnement d'un LLM
- Prendre en main un LLM de manière guidée
- Découvrir les différentes IA génératives selon les métiers (texte, image, audio, code)

**Contenu théorique :**

1. **Qu'est-ce qu'un LLM ?** — Tokens, prédiction probabiliste, fenêtre de contexte
2. **Le Transformer** — Architecture "Attention is all you need" (vulgarisation)
3. **5 concepts clés pour être dans le Top 10% :**
   - Les Tokens (le vrai langage de l'IA)
   - La Fenêtre de Contexte (la mémoire à court terme)
   - La Température (précision vs créativité)
   - L'Hallucination (pourquoi l'IA "invente")
   - Le RAG (connecter l'IA à ses propres documents)
4. **Panorama des outils** — ChatGPT, Gemini, Claude, Copilot, DALL-E, Midjourney, Runway...

**Ressources à mobiliser :**
- `00-Formation/qu est ce qu un LLM.pdf` — Explication accessible du fonctionnement LLM
- `Formation_V1/Module1_Introduction_IA_Generative_Enjeux_Industriels.html`
- `IA-Education/temperature.html` — Démo interactive du paramètre température
- `IA-Education/Gemin-cli_V2.html` — Interface de démonstration
- PDF approfondissement formateur : `00-Formation/13 - LLM.pdf`

**Démonstration en direct (30 min) — "Prise en main guidée d'un LLM" :**
- Connexion sur **Gemini** (compte Google) ou **ChatGPT** (compte gratuit suffisant)
- Comparaison : même question avec et sans contexte (Atelier 1 du Carnet)
- Réglage de la température par le texte (Atelier 2 du Carnet)
- Test de l'hallucination : Atelier 3 du Carnet (le 'traité de Neuville-sur-Vance')
- *Support apprenant imprimé :* `00-Formation/Fiche_Apprenant_Carnet_de_Prompts.docx`

---

### 12h15 - 13h15 | Pause déjeuner (1h)

---

### 13h15 - 14h45 | MODULE 3 : Maîtriser le Prompt Engineering (1h30)

**Objectifs spécifiques :**
- S'approprier les principes du prompt engineering
- Utiliser les techniques de base et avancées
- Tester et prendre en main avec des cas concrets

**Contenu théorique :**

1. **Qu'est-ce qu'un prompt ?** — Anatomie d'un bon prompt (Rôle, Contexte, Tâche, Format, Contraintes)
2. **Techniques de base :**
   - Zéro-shot, Few-shot, Chain-of-Thought
   - Les méta-commandes (Act as, Step by step, Format JSON...)
3. **Les 7 paramètres secrets** — Temperature, Top-P, Max Tokens, Stop sequence...
4. **Prompt Engineering pour l'industrie** — Cas d'usage maintenance, qualité, documentation technique

**Ressources à mobiliser :**
- `00-Formation/Formation_Prompt/Formation_Prompt_Maintenance_Guide_Formateur.md` — Guide complet formateur pour prompt maintenance
- `00-Formation/Formation_Prompt/Formation_Prompt_Maintenance_Etudiants.html` — Support apprenant HTML interactif
- `IA-Education/art_prompt.html` — Guide interactif de l'art du prompt
- `IA-Education/Guide_Interactif_Prompt.html` — Exercices guidés interactifs
- `00-Formation/Formation_Prompt_Entreprise.md` — Mise en situation entreprise
- `Activités/meta-commandes.md` + `Activités/Exemples meta-commandes.docx`
- PDF formateur : `00-Formation/Le Prompt Engineering pour Manager.pdf`
- Cheat sheet : `00-Formation/cheat_sheet.md`

**Ateliers pratiques progressifs (45 min) :**

*Atelier 1 — Les 6 Piliers du prompt (20 min) :*
- `Formation-Journee-PromptEngineering/Atelier1_6Piliers.html`
- Guide corrigé formateur : `Formation-Journee-PromptEngineering/Atelier1_Corriges_Formateur.md`

*Atelier 2 — Exercices pratiques (15 min) :*
- `Formation-Journee-PromptEngineering/Atelier2_Exercices_Pratiques.html`
- Corrigé : `Formation-Journee-PromptEngineering/Atelier2_Corriges_Formateur.md`

---

### 14h45 - 15h00 | Pause (15 min)

---

### 15h00 - 16h30 | Suite MODULE 3 : Action — Présenter une IA générative au choix (1h30)

**Activité finale Jour 1 — "Pitch IA" (travail en binôme) :**

Chaque binôme choisit une IA générative parmi une liste proposée (selon leur métier ou intérêt) et prépare une présentation de 5 minutes répondant à :
- Que fait cet outil ?
- Comment l'utiliser (démonstration live) ?
- Quel cas d'usage dans mon métier ?
- Quelle limite principale ?

**Liste d'outils suggérés :**
- Gemini / ChatGPT / Claude (texte)
- NotebookLM (synthèse documentaire)
- DALL-E / Midjourney (image)
- Copilot (code / bureautique)
- ElevenLabs (voix)

**Ressources de support pour les binômes :**
- `FC/CAS D'USAGE DÉMONSTRATION DE PUISSANCE EFFET DE LEVIER COGNITIF.pdf`
- `FC/Cas_Usage_1_Finance/`, `Cas_Usage_2_Pedagogie/`, `Cas_Usage_3_Transformation/`, `Cas_Usage_4_RH/`, `Cas_Usage_5_Data/`
- `00-Formation/Identifier les bons cas d'usage.pdf`

**Restitution et débriefing :**
- Chaque binôme présente (5 min)
- Discussion collective : similarités, différences, complémentarités des outils

---

### 16h30 - 17h00 | Bilan Jour 1 (30 min)

- Quiz rapide de consolidation (5 questions clés du jour)
- Tour de table : 1 chose apprise, 1 question qui reste
- Annonce du programme Jour 2

---

## JOUR 2 — Identifier les Limites et Intégrer l'IA (7h)

### 08h30 - 09h00 | Rappel et mise en route (30 min)

- Rappel des notions clés du Jour 1 (quiz express)
- Recueil des questions des participants suite à la nuit de "digestion"
- Présentation des objectifs du Jour 2

---

### 09h00 - 10h30 | MODULE 4 (partie 1) : Identifier les limites et les pièges de l'IA (1h30)

**Objectifs spécifiques :**
- Identifier les biais algorithmiques et leur origine
- Reconnaître les limites techniques et éthiques de l'IA
- Adopter une posture d'esprit critique face aux sorties d'un LLM

**Contenu théorique :**

1. **Les biais de l'IA — Anatomie :**
   - Biais dans les données d'entraînement
   - Biais de sélection, de confirmation, culturels
   - Biais de l'utilisateur dans le prompting (métacognition)
2. **L'hallucination — Mécanismes et détection :**
   - Pourquoi l'IA ne "sait" pas qu'elle se trompe
   - Techniques de vérification (cross-checking, sourcing)
3. **Limites techniques :**
   - Coupure de connaissance (knowledge cutoff)
   - Absence de mémoire persistante
   - Coûts computationnels et empreinte environnementale
4. **Enjeux éthiques et légaux :**
   - Données personnelles et RGPD
   - Droits d'auteur et propriété intellectuelle
   - IA Act européen (grandes lignes)
5. **L'illusion du raisonnement :** prédire ≠ comprendre

**Ressources à mobiliser :**
- `00-Formation/Activites-Biais/index.html` — Portail des 6 activités biais
- `00-Formation/Activites-Biais/guide_formateur.html` — Guide formateur complet
- `00-Formation/Activites-Biais/support_projection.html` — Support de projection
- `00-Formation/Activites-Biais/Architecture of AI Bias and Human Lucidity.pdf`
- Vidéo : `00-Formation/Activites-Biais/L_Anatomie_des_Biais.mp4`
- `Formation_IA_EspritCritique_UIMM-CVDL/Diaporama_UIMM_EspritCritique.pptx`
- `Formation_IA_EspritCritique_UIMM-CVDL/Guide_Formateur_UIMM_EspritCritique.docx`
- PDF formateur : `IA-Education/Discernement et Esprit Critique_ IA Génératives.pdf`

**Ateliers Biais (45 min — au choix selon le groupe) :**

| Activité | Fichier | Thème |
|---|---|---|
| Activité 1 | `activite1_biais_cognitifs.html` | Biais cognitifs fondamentaux |
| Activité 2 | `activite2_premiere_impression.html` | Effet de halo / première impression |
| Activité 3 | `activite3_biais_selection.html` | Biais de sélection |
| Activité 4 | `activite4_biais_confirmation.html` | Biais de confirmation |
| Activité 5 | `activite5_biais_culturels.html` | Biais culturels |
| Activité 6 | `activite6_jeu_role.html` | Jeu de rôle — Prise de décision |

**Recommandation :** Activités 1 + 4 + 6 pour une session de 45 min

---

### 10h30 - 10h45 | Pause (15 min)

---

### 10h45 - 12h15 | MODULE 4 (partie 2) : Faire face aux évolutions rapides (1h30)

**Objectifs spécifiques :**
- Comprendre la trajectoire d'évolution de l'IA (agents, RAG, IA multimodale)
- Identifier les usages émergents dans l'industrie
- Construire une posture de veille active

**Contenu théorique :**

1. **L'IA Agentique — La révolution en cours :**
   - Différence chatbot vs agent
   - L'agent planifie, utilise des outils, exécute
   - Le standard MCP (Model Context Protocol)
2. **Usages industriels concrets :**
   - Maintenance prédictive et GMAO augmentée
   - Assistant de diagnostic technique
   - Génération de procédures de sécurité
   - Documentation technique automatisée
3. **Outils de veille IA — Stratégie :**
   - NotebookLM comme assistant de veille
   - Newsletters, podcasts, GitHub Trending
   - Réflexe "test & learn" permanent

**Ressources à mobiliser :**
- `Formation_Agentic_Workspace/index.html` — Portail formation agentic workspace
- `Formation_Agentic_Workspace/guide_formation_ia.html`
- `IA-Education/Agentic_Automation_Tutorial.html`
- `Formation_IA_Usages_Industrie_UIMM-CVDL/Guide_Formateur_UIMM_UsagesGemini.docx`
- Cas d'usage **adaptés au public mixte** :
  - Industrie/maintenance : `A1_Analyse_Donnees_GMAO/`, `A2_Assistant_Diagnostic/`, `A4_Maintenance_Predictive/`
  - RH / Formation : `FC/Cas_Usage_4_RH/`, `FC/Cas_Usage_2_Pedagogie/`
  - Finance / Data : `FC/Cas_Usage_1_Finance/`, `FC/Cas_Usage_5_Data/`
- `IA-Education/Tableau_de_Bord_Interactif_Formation_IA.html` — Tableau de bord synthèse

**Démonstration NotebookLM (30 min) — outil phare de la formation :**
- Chaque participant importe UN document de son choix (notice, procédure, rapport, cours...)
- L'IA répond aux questions en citant les sources exactes : zéro hallucination
- Génération d'un FAQ, d'une fiche de révision ou d'un podcast audio sur son propre document
- Découverte d'**Antigravity** : démo live d'un agent qui planifie et exécute une tâche multi-étapes
- *Guide formateur :* `00-Formation/NotebookLM De l'Analyse de Documents à la Création de Valeur Stratégique.md`
- *Tutoriel Antigravity :* `IA-Education/antigravity_tutorial.html`

---

### 12h15 - 13h15 | Pause déjeuner (1h)

---

### 13h15 - 14h30 | Atelier de synthèse — Techniques avancées et mise en situation (1h15)

**Atelier 3 — Techniques avancées de prompting (45 min) :**
- `Formation-Journee-PromptEngineering/Atelier3_Techniques_Avancees.html`
- Corrigé formateur : `Formation-Journee-PromptEngineering/Atelier3_Corriges_Formateur.md`
- Thèmes : Chain-of-Thought, Few-Shot avancé, Roleplay structuré, prompts système
- *Support apprenant :* `00-Formation/Fiche_Apprenant_CheatSheet_Prompt.docx` (distribué ici)

**Mise en situation métier (30 min) — "Mon cas d'usage" (public mixte) :**
- Chaque participant choisit SON contexte professionnel (technicien, RH, formateur, manager...)
- Il formule un prompt adapté à sa réalité quotidienne
- Test sur NotebookLM OU en LLM direct, selon la nature du besoin
- Itération collective : le groupe améliore le prompt ensemble
- Référence cas d'usage : `FC/CAS D'USAGE DÉMONSTRATION DE PUISSANCE EFFET DE LEVIER COGNITIF.pdf`

---

### 14h30 - 14h45 | Pause (15 min)

---

### 14h45 - 16h15 | MODULE COMPLEMENTAIRE : NotebookLM avancé + Antigravity + Veille (1h30)

**Objectifs :**
- Approfondir NotebookLM (fonctionnalités avancées, usage collectif)
- Découvrir Antigravity comme agent de productivité au quotidien
- Construire une routine de veille IA personnalisée (gratuite)

**Contenu :**

1. **NotebookLM avancé :**
   - Partage de notebooks en équipe
   - Génération de podcasts audio pour ses documents internes
   - Cas concrets : notice technique, rapport de réunion, référentiel RH
2. **Antigravity — l'agent IA :**
   - Démo : rédaction automatisée, synthèse multi-documents, tâches enchaînées
   - Différence agent vs chatbot : l'agent planifie et exécute
3. **Google Workspace + IA (sans coût supplémentaire) :**
   - Gemini dans Gmail, Docs, Sheets (compte existant)
4. **Routine de veille IA — les 3 réflexes :**
   - Tester 1 outil nouveau par semaine
   - Maintenir son carnet de prompts (distribué en début de J1)
   - Sources recommandées : newsletters, podcasts IA francophones

**Ressources :**
- `IA-Education/antigravity_tutorial.html` — Tutoriel Antigravity pas à pas
- `IA-Education/Agentic_Automation_Tutorial.html`
- `IA-Education/Tutoriel_Google_Workspace.html`
- `IA-Education/Tutoriel_Gemini_Workspace.html`
- `Formation_Agentic_Workspace/guide_formation_ia.html`
- Guide NotebookLM : `00-Formation/NotebookLM De l'Analyse de Documents à la Création de Valeur Stratégique.md`

---

### 16h15 - 17h00 | Synthèse, évaluation et clôture (45 min)

**Quiz final — Validation des acquis (20 min) :**
- 15 questions couvrant les 4 modules
- Format mixte : QCM, Vrai/Faux, association terminologie
- *Source :* `Formation_IA_Usages_Industrie_UIMM-CVDL/Quiz_UsagesGemini.pdf` + `Formation_IA_EspritCritique_UIMM-CVDL/Quiz_EspritCritique.pdf`

**Bilan collectif (15 min) :**
- Tour de table : 1 outil que je vais utiliser dès demain
- 1 engagement concret noté sur fiche individuelle

**Remise des documents (10 min) :**
- Attestation de capacités
- **Carnet de prompts** personnalisé (complété pendant la formation) — `Fiche_Apprenant_Carnet_de_Prompts.docx`
- **Cheat Sheet Prompt Engineering** — `Fiche_Apprenant_CheatSheet_Prompt.docx`
- Ressources de veille recommandées
- Fiche synthèse : `IA-Education/Synthese_Formation_IA.html`

---

## Carte des Ressources par Module

| Module | Type | Fichier / Ressource |
|---|---|---|
| **M1 - Fondamentaux** | Cours | `Diaporama COURS Introduction IA.pptx` |
| **M1 - Fondamentaux** | HTML interactif | `Formation_V1/Module1_Introduction_IA.html` |
| **M1 - Fondamentaux** | Activite | `Initiation_IA/Initiation_IA_7H.md` (Le Tri Integral) |
| **M1 - Fondamentaux** | Visuels | `Activites/A7_Reseaux_Neurones/` (PNG reseaux) |
| **M1 - Fondamentaux** | Lecture formateur | `00-Formation/IA_Histoire_Convergence.pdf` |
| **M2 - IA Generatives** | Cours | `00-Formation/qu est ce qu un LLM.pdf` |
| **M2 - IA Generatives** | Demo interactive | `IA-Education/temperature.html` |
| **M2 - IA Generatives** | Demonstration | `IA-Education/Gemin-cli_V2.html` |
| **M2 - IA Generatives** | Carnet de prompts | `Initiation_IA/Carnet_de_prompts_IA.md` |
| **M2 - IA Generatives** | Lecture formateur | `00-Formation/13 - LLM.pdf` |
| **M3 - Prompt Engineering** | Guide formateur | `Formation_Prompt/Formation_Prompt_Maintenance_Guide_Formateur.md` |
| **M3 - Prompt Engineering** | Support apprenant | `Formation_Prompt/Formation_Prompt_Maintenance_Etudiants.html` |
| **M3 - Prompt Engineering** | Ateliers | `Formation-Journee-PromptEngineering/Atelier1,2,3_*.html` |
| **M3 - Prompt Engineering** | Corriges | `Formation-Journee-PromptEngineering/Atelier1,2,3_Corriges_Formateur.md` |
| **M3 - Prompt Engineering** | Cheat sheet | `00-Formation/cheat_sheet.md` |
| **M3 - Prompt Engineering** | Cas d'usage | `FC/Cas_Usage_1,2,3,4,5/` |
| **M4 - Limites et Enjeux** | Portail biais | `Activites-Biais/index.html` + `guide_formateur.html` |
| **M4 - Limites et Enjeux** | Activites biais | `Activites-Biais/activite1,4,6.html` |
| **M4 - Limites et Enjeux** | Video | `Activites-Biais/L_Anatomie_des_Biais.mp4` |
| **M4 - Limites et Enjeux** | Esprit critique | `Formation_IA_EspritCritique_UIMM-CVDL/` (PPTX + Guide + Quiz) |
| **M4 - Limites et Enjeux** | Usages industrie | `Formation_IA_Usages_Industrie_UIMM-CVDL/A1...A6/` |
| **M4 - Limites et Enjeux** | NotebookLM guide | `00-Formation/NotebookLM De l'Analyse...Valeur_Strategique.md` |

---

## Matrice de conformité — Fiche AFPI

| Exigence AFPI | Couverture dans ce plan | Ressource |
|---|---|---|
| Clarifier notions IA | Module 1 complet | Diaporama Intro + Formation_V1 |
| Découvrir l'IA | Module 1 + Module 2 Jour 1 | qu_est_ce_qu_un_LLM.pdf |
| Expliquer concepts ML/DL | Module 1 (1h30) | IA_Histoire_Convergence + A7_Reseaux |
| ML vs programmation | Module 1 — comparaison paradigmes | Diaporama |
| Utiliser IA génératives | Module 2 + Démonstration live | Carnet_de_prompts |
| Prendre en main LLM | Démonstration guidée Jour 1 | Gemini / ChatGPT direct |
| IA selon métier | FC/Cas_Usage + Formation_IA_Usages_Industrie | A1...A6 industrie |
| Prompt engineering | Module 3 complet (2h30) | Ateliers 1, 2, 3 |
| Techniques avancées | Atelier 3 Jour 2 | Atelier3_Techniques_Avancees.html |
| Présenter une IA (Action) | "Pitch IA" Jour 1 fin de journée | Cas_Usage FC |
| Limites et pièges | Module 4 partie 1 + Activités Biais | activite1...6.html |
| Face aux évolutions | Module 4 partie 2 + NotebookLM | Agentic_Automation + usages |
| Méthode participative | Ateliers, débriefing, tour de table | Tous ateliers |
| Alternance théorie/pratique | Toutes séquences (ratio ~40%/60%) | Structure du plan |
| Suivi et bilan | Quiz final + tour de table J2 | Quiz UIMM + Synthese_Formation |

---

## Arbitrages valides (22/04/2026)

| Point | Decision |
|---|---|
| Public | **Mixte** — cas d'usage adaptes selon les metiers en salle |
| Outils retenus | **NotebookLM + Antigravity** — Gemini CLI retire (cout) |
| Activites Biais | **1 + 4 + 6** (45 min au total) |
| LLM en salle | Gemini (compte Google) ou ChatGPT gratuit — au choix du formateur |
| Supports imprimes | **2 DOCX generes** dans `00-Formation/` |

## Supports imprimes disponibles

- [Fiche_Apprenant_Carnet_de_Prompts.docx](file:///c:/Users/s.jaubert/projets/Cours-IA/00-Formation/Fiche_Apprenant_Carnet_de_Prompts.docx) — Distribue en debut de J1
- [Fiche_Apprenant_CheatSheet_Prompt.docx](file:///c:/Users/s.jaubert/projets/Cours-IA/00-Formation/Fiche_Apprenant_CheatSheet_Prompt.docx) — Distribue au debut de J2 Atelier 3

## Point de vigilance restant

> [!NOTE]
> **Consigne a envoyer aux participants AVANT la formation** (email ou convocation) :
>
> "Pour l'atelier pratique du Jour 2, merci d'apporter sur votre poste un fichier PDF ou Word que vous utilisez dans votre travail. Par exemple :
> - une procedure ou instruction de travail
> - un compte-rendu de reunion
> - une fiche produit ou notice technique
> - un reglement interieur ou une note RH
> - un programme de formation ou un referentiel de competences
> - un rapport d'audit ou un bilan d'activite
> - une fiche de poste
>
> Ce document ne sera utilise que par vous, sur votre propre poste. Il restera confidentiel."

---

*Pôle Formation UIMM - CVDL | S. JAUBERT | Plan généré le 22 avril 2026*
