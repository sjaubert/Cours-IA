# Table de migration validée, dépôt Cours-IA

Validation faite le 28 juillet 2026, par inspection réelle des dossiers, pas sur les noms. Chaque destination ci-dessous repose sur le contenu vu. Ce qui n'a pas pu être tranché est marqué « à décider ».

## Ce que l'inspection a changé par rapport à la table initiale

Trois dossiers que j'avais rangés en bloc se répartissent en fait sur plusieurs domaines. `IA-Education` contient à la fois des tutoriels Gemini, des guides de prompt, des tableaux de bord et un guide esprit critique. `00-Formation` est un fourre-tout qui touche cinq domaines. `Activités` mélange biais, industrie et fichiers de service. Les découper au fichier près était nécessaire.

Découvertes à valeur pédagogique, aujourd'hui invisibles dans le README. `Accomplish` est une formation Ollama complète, par métier, avec guide d'installation, corrigés formateur, fiches stagiaires et politique d'utilisation. À exposer. `LiveBook/LB_AI` est une méthode aboutie, la « Méthode LiveBook UIMM v1.1 », avec glossaire, questions, tensions et carte mentale, construite sur un article source. À exposer aussi, mais elle traîne 16 Mo de binaires (un PDF de 9,8 Mo, une image de 6 Mo).

Points durs à traiter à part. `Developper_applications_LLM_SDK_Vertex_AI` ne contient qu'un `Intro.html` de 1,5 Ko : une coquille vide, à archiver ou supprimer. `claude-usage` est un dépôt git tiers complet, avec son propre `.git`, `Dockerfile`, `cli.py` : ce n'est pas ton contenu, et un `git mv` dessus est risqué. À sortir à la main.

Doublons confirmés. `IA-Education/Gemin-cli V2.html` et `IA-Education/Gemin-cli_V2.html` sont deux copies (espace contre underscore) ; le README pointe la version avec espace. `Integrating_File_Search_with_Gemini_CLI_Extension.html` existe dans `Formation_V1` et dans `Activités`. `CLAUDE/` contient trois versions de `Plan_Formation_Claude_Skills` (v1, v2, v3) et deux de `Plan_Formation_Claude_Hooks` (v1, v2). Garde une source de référence, archive le reste.

## Arborescence cible

```
Cours-IA/
├── 00-demarrer
├── 01-comprendre-ia
├── 02-prompt-engineering
├── 03-outils-google
├── 04-notebooklm
├── 05-claude
├── 06-ia-industrie
├── 07-ia-locale
├── ressources
├── _archive        (contenus supersédés ou vides)
└── _interne        (scripts, essais, outils tiers, hors publication, git ignore)
```

## Déplacements de dossiers entiers, sans ambiguïté

Ces dossiers vont à un seul endroit. Ils sont sûrs.

| Dossier actuel | Destination |
|---|---|
| `00Exp` | `07-ia-locale/ia-locale-pas-a-pas` |
| `Accomplish` | `07-ia-locale/ollama-par-metier` (à exposer) |
| `NoteBLM` | `04-notebooklm` |
| `ai-parameters-demo` | `01-comprendre-ia/parametres-ia` |
| `antigravity` | `03-outils-google/antigravity` |
| `Nouveautes_Antigravity` | `03-outils-google/antigravity-nouveautes` |
| `cours-claude-code-ia` | `05-claude/cours-claude-code-ia` |
| `Formation-Journee-PromptEngineering` | `02-prompt-engineering/formation-journee` |
| `Formation_Agentic_Workspace` | `03-outils-google/agentic-workspace` |
| `Formation_IA_Usages_Industrie_UIMM-CVDL` | `06-ia-industrie/usages-industrie` |
| `Formation_IA_EspritCritique_UIMM-CVDL` | `01-comprendre-ia/esprit-critique` |
| `FC` | `06-ia-industrie/cas-usage-formation-continue` |
| `Formation_V1` | `_archive/Formation_V1` |
| `Developper_applications_LLM_SDK_Vertex_AI` | `_archive/vertex-ai-coquille-vide` |

Remarque : `Formation_IA_EspritCritique` ne contient qu'un guide formateur. Il existe un guide esprit critique voisin dans `IA-Education`. Vérifie s'ils font doublon avant de les séparer.

## Dossiers à découper au fichier près

### IA-Education, éclaté

| Contenu | Destination |
|---|---|
| `Guide_Interactif_Prompt.html`, `art_prompt.html`, `temperature.html` | `02-prompt-engineering` |
| Tous les tutoriels Gemini et Workspace (`Gemin-cli_V2.html`, `gemini-cli_workspace.html`, `astuce_geminiCLI.html`, `tutoriel_google_appsscript.html`, `tutoriel-gemini-secure.html`, `Tutoriel_Automatisation_Workspace.html`, `Agentic_Automation_Tutorial.html`, `antigravity_tutorial.html`, `Tutoriel_Gemini_Workspace.html`, `Tutoriel_Google_Workspace.html`, `google_credentials_setup.html`, `gemini_cli_cheatsheet_fr.md`, `transcription-article-gemini-cli.md`, `Guide_Formateur_UsagesGemini_UIMM.md`) | `03-outils-google` |
| `Tableau_de_Bord_Interactif_Formation_IA.html`, `Ateliers_Pratiques.html`, `Synthese_Formation_IA.html`, `Teacher_AI_Competency_Ecosystem.pptx`, PDF et images | `ressources` |
| `Guide_Formateur_EspritCritique_UIMM.md` | `01-comprendre-ia` |
| `Gemin-cli V2.html` (doublon avec espace) | à supprimer après vérification |

### 00-Formation, éclaté

| Contenu | Destination |
|---|---|
| `Initiation_IA/`, `cheat_sheet.md`, `Fiche_Apprenant_Carnet_de_Prompts.docx`, `Fiche_Apprenant_CheatSheet_Prompt.docx` | `00-demarrer` |
| `Activites-Biais/`, `Ressources Biais/` | `01-comprendre-ia` |
| `Formation_Prompt/`, `Formation_Prompt_Entreprise.*`, `prompt_flow_uimm/`, `The 7 Secret Knobs...docx`, `The Perfect Prompt...docx` | `02-prompt-engineering` |
| `NotebookLM De l'Analyse...md` | `04-notebooklm` |
| `IA_Skills/` | `05-claude/skills` |
| `Plan_Formation_IA_AFPI.*`, `Proposition_Formation_IA_CahierDesCharges.*` | `ressources/offres-et-dispositifs` |
| `Shreyas_Naphad.md`, docx divers | `ressources/lectures` |
| `generer_supports.py` | `_interne` |

Rappel : `prompt_flow_uimm/` doit perdre son `node_modules` avant tout déplacement (voir le script phase 1).

### Activités, éclaté

| Contenu | Destination |
|---|---|
| `A1_illusion_vérité`, `A2_Biais_Confirmation`, `A3_Biais_Culturel`, `A4_Illusion_raisonnement`, `A6_Futur_Dev_IA`, `A7_Reseaux_Neurones` | `01-comprendre-ia` |
| `A5 IA Rédactrice de rapports` | `06-ia-industrie` |
| `meta-commandes.md`, `Exemples meta-commandes.docx` | `ressources` |
| `A0_organisation_documents`, `GEMINI.md`, `settings.json`, `info_projet.txt` | `_interne` |
| `Integrating_File_Search...html` (doublon) | à supprimer après vérification |

### CLAUDE, à consolider

Le gros va dans `05-claude`. Mais le dossier accumule des doublons et des versions. Avant de déplacer, envoie dans `_archive` : `Plan_Formation_Claude_Skills.docx` et `_v2.docx` (garde `_v3`), `Plan_Formation_Claude_Hooks.docx` (garde `_v2`), `CLAUDE_26052026.md` (copie datée). Envoie dans `_interne` : `.Rhistory`, `.claude`. Le reste, sous-dossiers de formation compris, va dans `05-claude`.

## Essais, outils et fichiers de service, vers _interne

Aucun n'est référencé dans le README, donc les déplacer ne casse aucun lien.

| Élément | Destination | Note |
|---|---|---|
| `app_Test/`, `gemini_API/`, `tasks/` | `_interne` | essais |
| `streamlit_cheatsheet/`, `espérance_vie/` | `_interne` ou `ressources/demos` | à décider : ce sont des démos exploitables |
| `claude-usage/` | `_interne` | dépôt git tiers, à sortir à la main, pas avec git mv |
| Scripts racine (`organize_files.py`, `fix_readme_encoding.py`, `extract_doc.py`, `extract_docx.py`, `chat_gemini.py`, `verify_moves.py`), `doc_content.json`, `extracted_text.txt`, `.Rhistory` | `_interne` | fichiers de travail |
| PDF et notes de lecture racine (thèses, articles, `turing.jpg`, `Transformers Attention.jpg`, `Cours_IA_v2_illustre.pptx`, `resume_competences.md`) | `ressources/lectures` | matière de fond |

## Deux points laissés à ta décision

`LiveBook/LB_AI`. Vrai contenu, la Méthode LiveBook UIMM. Destination logique : `ressources/methode-livebook`, ou `04-notebooklm` si tu la rattaches à cette démarche. Mais elle contient 16 Mo de binaires lourds. Décide si tu les gardes dans le dépôt ou si tu les sors.

`espérance_vie` et `streamlit_cheatsheet`. Ce sont des démos utilisables en formation, pas de simples brouillons. Soit tu les exposes dans `ressources/demos`, soit tu les mets en `_interne`. À toi.

## Effet sur le README

Une fois les dossiers déplacés, tous les liens du README changent de chemin. C'est attendu. Le `README_propose.md` que je t'ai livré correspond à l'état avant migration. Quand tu auras déplacé les dossiers, je régénère un README aligné sur la nouvelle arborescence. Ne fais pas les deux dans le désordre.

## Ce que je te propose comme suite

Le script `migration_phase1.sh` livré avec ce document fait uniquement les gains sûrs, sans toucher au contenu référencé dans le README : il crée le `.gitignore`, retire `node_modules` du suivi git, crée `_archive` et `_interne`, et y range les essais, outils et fichiers de service. Zéro risque sur les liens.

La phase 2, le déplacement des domaines et le découpage des dossiers éclatés, je te la génère en script `git mv` complet dès que tu me confirmes cette table, en particulier les deux points laissés à ta décision. Je fournirai le README réaligné dans la foulée.
