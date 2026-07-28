# Audit du dépôt Cours-IA et proposition de réorganisation

Auteur de l'audit : assistant de travail. Destinataire : S. Jaubert, Pôle Formation UIMM CVDL.
Date : 28 juillet 2026.

## 1. Ce que j'ai vérifié, et comment

J'ai contrôlé le README.md que tu m'as fourni, puis je l'ai confronté à l'arborescence réelle de ton dossier `Cours-IA` sur ton poste. Tous les constats ci-dessous sont ancrés sur des fichiers réellement présents ou réellement absents. Je n'ai pas deviné.

Pour l'obsolescence, tu as demandé un traitement aux signaux internes uniquement. Je ne recherche donc pas en ligne l'état actuel des outils. Je signale ce qui a l'air daté à partir du dépôt lui-même : nommage en version, dates anciennes, contenus qui font doublon avec du plus récent. Tout ce qui touche à l'obsolescence est une hypothèse à confirmer par toi, pas une affirmation.

Réserve technique : la lecture automatique de l'arborescence s'arrête à 2000 entrées, et ton dépôt en dépasse largement ce nombre. La cause est identifiée au point 3. J'ai vérifié un par un les dossiers qui posaient doute, donc les conclusions sur les liens sont fiables. En revanche, l'inventaire complet des sous-dossiers profonds n'est pas exhaustif.

## 2. Contrôle des liens

Le README contient 106 liens locaux, 19 URL vers ton site GitHub Pages, et 8 ancres de navigation interne.

Un seul lien est réellement cassé. Section 7, la ligne « Plan Formation IA - AFPI » pointe vers `00-Formation/Plan_Formation_IA_AFPI.html`. Ce fichier n'existe pas. Le dossier contient seulement `Plan_Formation_IA_AFPI.md` et `Plan_Formation_IA_AFPI.docx`. Correctif appliqué dans le README réécrit : le lien pointe vers la version `.md`, avec la version Word en complément.

Les 105 autres liens locaux résolvent. Lors du premier passage, quatre liens ressortaient comme manquants. C'étaient de faux négatifs dus à la limite de lecture des 2000 entrées. Je les ai vérifiés individuellement sur ton poste : les fichiers existent bien. Il s'agissait du cahier de TP « Créer des skills », des deux fichiers de la formation Skills dans `00-Formation/IA_Skills/Formation_Skills`, et du START-HERE du guide Cowork.

Les 19 URL GitHub Pages ont toutes leur fichier source présent en local. J'en ai testé deux en ligne : elles répondent. Le site est déployé.

Les 8 ancres de navigation sont valides. Les doubles tirets que l'on voit dans certaines ancres, par exemple `#1-comprendre-lia--fondamentaux-et-biais`, viennent des tirets cadratins présents dans tes titres : GitHub les retire et laisse une double espace, donc un double tiret. Les ancres fonctionnent, mais c'est un symptôme du point de style traité plus bas.

## 3. Problèmes de structure, factuels

### Un node_modules versionné

Le dossier `00-Formation/prompt_flow_uimm/` contient un `node_modules` complet, suivi par git. C'est ce qui fait exploser le nombre de fichiers du dépôt et bloque la lecture au-delà de 2000 entrées. Un `node_modules` ne doit jamais être versionné : il se régénère avec `npm install`. À exclure via `.gitignore`, puis à retirer du suivi git. Seuls les sources et le dossier `dist/` compilé ont besoin d'être présents pour que la page publiée fonctionne.

### Une racine encombrée

La racine du dépôt mélange les livrables pédagogiques et des fichiers de travail qui n'ont rien à y faire. J'y trouve des scripts de manipulation ponctuels (`organize_files.py`, `fix_readme_encoding.py`, `extract_doc.py`, `extract_docx.py`, `chat_gemini.py`, `verify_moves.py`), des sorties intermédiaires (`extracted_text.txt`, `doc_content.json`), un historique R (`.Rhistory`), un script batch d'imprimante (`vider_spooler_imprimante.bat`), et plusieurs PDF ou images de lecture personnelle (thèses, articles de recherche, `turing.jpg`, `Transformers Attention.jpg`). Aucun n'est référencé dans le README. Ils brouillent la lecture du dépôt et allongent chaque recherche.

### Des dossiers présents sur le disque mais absents du README

Onze dossiers de contenu existent sans figurer nulle part dans le README. Soit ce sont des ressources oubliées qui mériteraient d'être exposées, soit des expérimentations à archiver. Je ne me prononce pas sur leur contenu, je n'y suis pas entré. Voici la liste, avec ce que leur nom suggère, à confirmer par toi :

| Dossier orphelin | Le nom suggère | À décider |
|---|---|---|
| `Formation_IA_EspritCritique_UIMM-CVDL` | Une formation aboutie, cohérente avec le thème des biais | Exposer dans le README ? |
| `Developper_applications_LLM_SDK_Vertex_AI` | Un contenu technique avancé | Exposer ou archiver ? |
| `Nouveautes_Antigravity` | Un complément à la section Antigravity | Fusionner avec `antigravity/` ? |
| `LiveBook` | Incertain | À statuer |
| `Accomplish` | Incertain | À statuer |
| `tasks` | Fichiers de travail | Archiver ? |
| `app_Test` | Un test | Archiver |
| `gemini_API` | Un essai technique | Archiver |
| `claude-usage` | Suivi de consommation | Interne, hors publication |
| `streamlit_cheatsheet` | Un aide-mémoire | Exposer ou archiver ? |
| `espérance_vie` | Un jeu de données ou un exercice | À statuer |

### Un nommage incohérent

Le dépôt cumule plusieurs conventions qui coexistent sans règle. Des accents dans les noms de dossier (`Activités`), ce qui force un encodage `%C3%A9` fragile dans chaque lien. Un mélange français et anglais (`Formation_Agentic_Workspace`, `cours-claude-code-ia`). Des tirets et des underscores selon les cas. Des préfixes numériques hétérogènes (`00-Formation`, `00Exp`). Des suffixes de version (`Formation_V1`, `Plan_Formation_Claude_Skills_v2`). Résultat : impossible de deviner où ranger un nouveau contenu.

### Trois axes de classement en concurrence

Le point de fond. Ton contenu est rangé tantôt par thème (`Formation_V1`, biais), tantôt par outil (`CLAUDE`, `NoteBLM`, Gemini dans `IA-Education`), tantôt par public (`FC` pour Formation Continue). Ces trois logiques se croisent et se marchent dessus. C'est la vraie cause du sentiment d'anarchie, plus que les liens ou le nommage.

## 4. Signaux d'obsolescence, à confirmer par toi

Rien ici n'est une affirmation. Ce sont des indices internes au dépôt.

`Formation_V1`. Le suffixe « V1 », les dates de novembre 2025, et un contenu qui recouvre le prompt engineering (modules 3 et 4) déjà traité de façon plus récente en section 2 et dans la formation Prompt Maintenance de janvier 2026. Fort candidat à l'archivage, sous réserve que rien d'unique n'y subsiste.

Doublons de contenu. Le prompt engineering vit à trois endroits : la section 2, les modules 3 et 4 de `Formation_V1`, et `00-Formation/Formation_Prompt`. Les biais vivent en section 1, dans `00-Formation/Activites-Biais`, et probablement dans le dossier orphelin `Formation_IA_EspritCritique_UIMM-CVDL`. Les skills occupent une demi-douzaine d'entrées en section 5. Ce n'est pas forcément à supprimer, mais à consolider : une seule source de référence par thème, le reste en archive.

Suffixes de version. `Plan_Formation_Claude_Skills_v2.docx` implique un v1 quelque part. Deux plans de formation Skills, un Claude et un Gemini, coexistent. À vérifier lequel fait foi.

Ancienneté sur les tutoriels d'outils. Les tutoriels Gemini CLI datent de décembre 2025. Un tutoriel d'outil vieillit vite. Je ne peux pas dire s'ils sont encore exacts, tu as demandé de ne pas vérifier en ligne. À revoir en priorité si tu les rejoues en formation.

## 5. Proposition de réorganisation

### Principe directeur

Choisir un seul axe : le parcours d'apprentissage. On range par étape et par thème, pas par outil ni par public. Le public et l'outil deviennent des étiquettes dans le README, pas des dossiers. Un salarié qui découvre l'IA suit les numéros croissants ; un formateur qui cherche un contenu précis suit le thème.

### Règles de nommage

Un seul jeu de règles, sans exception. Minuscules, pas d'accents, tirets simples entre les mots, préfixe numérique à deux chiffres pour l'ordre. Jamais de suffixe de version dans un nom de dossier : la version vit dans git, pas dans le nom. Les dossiers techniques ou internes commencent par un underscore pour tomber en bas de liste.

### Arborescence cible proposée

```
Cours-IA/
├── README.md
├── 00-demarrer/            Initiation IA, carnet de prompts, cheat sheets d'entrée
├── 01-comprendre-ia/       Fondamentaux, biais, esprit critique, réseaux de neurones
├── 02-prompt-engineering/  Guides, ateliers d'une journée, prompt maintenance, PromptFlow
├── 03-outils-google/       Gemini CLI, Workspace MCP, Antigravity
├── 04-notebooklm/          Prise en main et formation 7H NotebookLM
├── 05-claude/              Claude Code, agents, skills, hooks, cowork, plugins
├── 06-ia-industrie/        Usages industrie, cas métiers, modules de sensibilisation
├── 07-ia-locale/           Souveraineté, Ollama, projet 00Exp
├── ressources/             Tableaux de bord, prompts, références transversales, lectures
├── _archive/               Contenus supersédés (Formation_V1, versions anciennes)
└── _interne/               Scripts, extractions, brouillons, suivi de consommation (git ignore)
```

Google et NotebookLM sont séparés car NotebookLM pèse assez lourd pour vivre seul. Si tu préfères, on les fusionne.

### Correspondance ancien vers nouveau

Table de migration, à valider avant tout déplacement. Elle ne prétend pas être complète, elle donne la logique.

| Actuel | Cible |
|---|---|
| `00-Formation/Initiation_IA`, cheat sheets | `00-demarrer/` |
| `Activités` (A1 à A4), `00-Formation/Activites-Biais`, `Formation_IA_EspritCritique_UIMM-CVDL` | `01-comprendre-ia/` |
| `Formation-Journee-PromptEngineering`, `00-Formation/Formation_Prompt`, `00-Formation/prompt_flow_uimm`, `IA-Education/Guide_Interactif_Prompt.html` | `02-prompt-engineering/` |
| `IA-Education` (Gemini), `Formation_Agentic_Workspace`, `antigravity`, `Nouveautes_Antigravity` | `03-outils-google/` |
| `NoteBLM` | `04-notebooklm/` |
| `CLAUDE`, `cours-claude-code-ia`, `ai-parameters-demo` | `05-claude/` |
| `Formation_IA_Usages_Industrie_UIMM-CVDL`, `FC`, `Formation_V1` (ce qui est unique), `cours_IA_industrie.docx` | `06-ia-industrie/` |
| `00Exp` | `07-ia-locale/` |
| Tableaux de bord, `Prompts&Ressources IA.md`, PDF de lecture | `ressources/` |
| `Formation_V1` (le reste), doublons supersédés | `_archive/` |
| Scripts racine, `claude-usage`, `app_Test`, `gemini_API`, sorties intermédiaires | `_interne/` |

### Le cas des accents

Renomme `Activités` en `01-comprendre-ia` ou tout autre nom sans accent. Cela supprime d'un coup l'encodage `%C3%A9` de tous les liens qui le traversent, et rend les URL lisibles.

### Le fichier .gitignore

Ajoute au minimum : `node_modules/`, `.venv/`, `.Rhistory`, `*.tmp`, et le dossier `_interne/` si tu ne veux pas le publier. Retire ensuite `node_modules` du suivi avec `git rm -r --cached 00-Formation/prompt_flow_uimm/node_modules`.

## 6. Plan de migration prudent

Ne déplace rien à la main dans l'explorateur, tu casserais les liens et l'historique git. Procède par étapes, une par jour si besoin.

D'abord, valide la table de correspondance et tranche le sort des onze dossiers orphelins. Ensuite, crée le `.gitignore` et sors `node_modules` du suivi : gain immédiat, aucun risque. Puis déplace les dossiers un thème à la fois, avec `git mv` pour conserver l'historique, et corrige les liens du README au fur et à mesure. Termine par un contrôle des liens sur le nouveau README avant de pousser. Je peux t'accompagner à chaque étape, ou générer le script `git mv` complet une fois la table validée.

## 7. Livré avec cet audit

Un README réécrit, prêt à remplacer l'actuel : lien AFPI réparé, tirets cadratins retirés partout, titres nettoyés, marqueurs « à réviser » posés sur les contenus que les signaux internes désignent, structure des huit sections conservée mais assainie. Les liens y pointent vers les chemins actuels, donc il fonctionne tel quel, avant toute migration. Quand tu déplaceras les dossiers, seuls les chemins changeront, pas l'ossature.
