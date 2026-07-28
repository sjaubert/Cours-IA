#!/usr/bin/env bash
#
# Cours-IA : migration phase 2 (restructuration en domaines).
# À lancer APRÈS migration_phase1.sh, depuis la racine du dépôt, dans git bash.
# À relire avant exécution. Fais-le sur une branche : git checkout -b reorg
#
# Principe : on ne déplace que des unités autonomes (sous-dossiers, documents isolés).
# IA-Education part en bloc pour ne pas casser les liens relatifs de ses pages HTML.
# Après ce script, lance 'git status', vérifie, puis demande le README réaligné.

set -u

if [ ! -f "README.md" ] || [ ! -d ".git" ]; then
  echo "Erreur : lance ce script depuis la racine du dépôt Cours-IA." >&2
  exit 1
fi

# Déplacement sûr : git mv si suivi, sinon mv. Ignore ce qui est absent.
move() {
  local src="$1" dst="$2"
  if [ ! -e "$src" ]; then echo "  absent, ignoré : $src"; return; fi
  mkdir -p "$(dirname "$dst")"
  if [ -n "$(git ls-files "$src" 2>/dev/null)" ]; then
    git mv -k "$src" "$dst" && echo "  git mv : $src -> $dst"
  else
    mv "$src" "$dst" && echo "  mv     : $src -> $dst"
  fi
}

echo "== Création des domaines =="
mkdir -p 00-demarrer 01-comprendre-ia 02-prompt-engineering 03-outils-google \
         06-ia-industrie 07-ia-locale \
         ressources/demos ressources/lectures ressources/offres-et-dispositifs \
         _archive/versions-anciennes _archive/doublons-a-verifier

echo "== Renommage des dossiers qui deviennent un domaine =="
# Ces cibles ne doivent pas déjà exister : ce sont des renommages.
[ -d NoteBLM ] && git mv NoteBLM 04-notebooklm && echo "  NoteBLM -> 04-notebooklm"
[ -d CLAUDE ]  && git mv CLAUDE 05-claude    && echo "  CLAUDE -> 05-claude"

echo "== Dossiers autonomes vers leur domaine =="
move "00Exp"                                   "07-ia-locale/ia-locale-pas-a-pas"
move "Accomplish"                              "07-ia-locale/ollama-par-metier"
move "ai-parameters-demo"                       "01-comprendre-ia/parametres-ia"
move "antigravity"                              "03-outils-google/antigravity"
move "Nouveautes_Antigravity"                   "03-outils-google/antigravity-nouveautes"
move "Formation_Agentic_Workspace"              "03-outils-google/agentic-workspace"
move "IA-Education"                             "03-outils-google/ia-education"
move "Formation-Journee-PromptEngineering"      "02-prompt-engineering/formation-journee"
move "Formation_IA_Usages_Industrie_UIMM-CVDL"  "06-ia-industrie/usages-industrie"
move "Formation_IA_EspritCritique_UIMM-CVDL"    "01-comprendre-ia/esprit-critique"
move "FC"                                        "06-ia-industrie/cas-usage-formation-continue"
move "cours-claude-code-ia"                     "05-claude/cours-claude-code-ia"
move "cours_IA_industrie.docx"                  "06-ia-industrie/cours_IA_industrie.docx"
move "streamlit_cheatsheet"                     "ressources/demos/streamlit-cheatsheet"
move "espérance_vie"                            "ressources/demos/esperance-vie"

echo "== Contenus supersédés vers _archive =="
move "Formation_V1"                             "_archive/Formation_V1"
move "Developper_applications_LLM_SDK_Vertex_AI" "_archive/vertex-ai-coquille-vide"

echo "== 00-Formation, sous-dossiers et documents isolés =="
move "00-Formation/Initiation_IA"                       "00-demarrer/initiation-ia"
move "00-Formation/cheat_sheet.md"                      "00-demarrer/cheat_sheet.md"
move "00-Formation/Fiche_Apprenant_Carnet_de_Prompts.docx" "00-demarrer/Fiche_Apprenant_Carnet_de_Prompts.docx"
move "00-Formation/Fiche_Apprenant_CheatSheet_Prompt.docx" "00-demarrer/Fiche_Apprenant_CheatSheet_Prompt.docx"
move "00-Formation/Activites-Biais"                     "01-comprendre-ia/activites-biais"
move "00-Formation/Ressources Biais"                    "01-comprendre-ia/ressources-biais"
move "00-Formation/Formation_Prompt"                    "02-prompt-engineering/formation-prompt"
move "00-Formation/prompt_flow_uimm"                    "02-prompt-engineering/promptflow"
move "00-Formation/Formation_Prompt_Entreprise.docx"    "02-prompt-engineering/Formation_Prompt_Entreprise.docx"
move "00-Formation/Formation_Prompt_Entreprise.md"      "02-prompt-engineering/Formation_Prompt_Entreprise.md"
move "00-Formation/The 7 Secret Knobs That Control Every AI Response.docx" "02-prompt-engineering/The_7_Secret_Knobs.docx"
move "00-Formation/The Perfect Prompt  A Prompt Engineering Cheat Sheet.docx" "02-prompt-engineering/The_Perfect_Prompt_Cheat_Sheet.docx"
move "00-Formation/IA_Skills"                           "05-claude/skills"
move "00-Formation/NotebookLM De l'Analyse de Documents à la Création de Valeur Stratégique.md" "04-notebooklm/NotebookLM_Analyse_Documents_Valeur_Strategique.md"
move "00-Formation/Plan_Formation_IA_AFPI.docx"         "ressources/offres-et-dispositifs/Plan_Formation_IA_AFPI.docx"
move "00-Formation/Plan_Formation_IA_AFPI.md"           "ressources/offres-et-dispositifs/Plan_Formation_IA_AFPI.md"
move "00-Formation/Proposition_Formation_IA_CahierDesCharges.docx" "ressources/offres-et-dispositifs/Proposition_Formation_IA_CahierDesCharges.docx"
move "00-Formation/Proposition_Formation_IA_CahierDesCharges.html" "ressources/offres-et-dispositifs/Proposition_Formation_IA_CahierDesCharges.html"
move "00-Formation/Shreyas_Naphad.md"                   "ressources/lectures/Shreyas_Naphad.md"
move "00-Formation/IA_Essentiel_prompt.jpg"             "ressources/lectures/IA_Essentiel_prompt.jpg"
move "00-Formation/generer_supports.py"                 "_interne/generer_supports.py"

echo "== Activités, sous-dossiers et fichiers =="
move "Activités/A1_illusion_vérité"        "01-comprendre-ia/activites/A1_illusion_verite"
move "Activités/A2_Biais_Confirmation"     "01-comprendre-ia/activites/A2_Biais_Confirmation"
move "Activités/A3_Biais_Culturel"         "01-comprendre-ia/activites/A3_Biais_Culturel"
move "Activités/A4_Illusion_raisonnement"  "01-comprendre-ia/activites/A4_Illusion_raisonnement"
move "Activités/A6_Futur_Dev_IA"           "01-comprendre-ia/activites/A6_Futur_Dev_IA"
move "Activités/A7_Reseaux_Neurones"       "01-comprendre-ia/activites/A7_Reseaux_Neurones"
move "Activités/reseau_neurones.png"       "01-comprendre-ia/activites/reseau_neurones.png"
move "Activités/surface-reseau_neurones.png" "01-comprendre-ia/activites/surface-reseau_neurones.png"
move "Activités/A5 IA Rédactrice de rapports" "06-ia-industrie/A5_IA_Redactrice_de_rapports"
move "Activités/meta-commandes.md"         "ressources/meta-commandes.md"
move "Activités/Exemples meta-commandes .docx" "ressources/Exemples_meta-commandes.docx"
move "Activités/A0_organisation_documents" "_interne/A0_organisation_documents"
move "Activités/GEMINI.md"                 "_interne/Activites_GEMINI.md"
move "Activités/settings.json"             "_interne/Activites_settings.json"
move "Activités/info_projet.txt"           "_interne/Activites_info_projet.txt"
move "Activités/Integrating_File_Search_with_Gemini_CLI_Extension.html" "_archive/doublons-a-verifier/Integrating_File_Search_Activites.html"
move "Activités/Former à l’IA, c’est d’abord former à la lucidité.docx" "01-comprendre-ia/Former_a_l_IA_former_a_la_lucidite.docx"

echo "== CLAUDE : versions et doublons hors 05-claude =="
move "05-claude/Plan_Formation_Claude_Skills.docx"    "_archive/versions-anciennes/Plan_Formation_Claude_Skills_v1.docx"
move "05-claude/Plan_Formation_Claude_Skills_v2.docx" "_archive/versions-anciennes/Plan_Formation_Claude_Skills_v2.docx"
move "05-claude/Plan_Formation_Claude_Hooks.docx"     "_archive/versions-anciennes/Plan_Formation_Claude_Hooks_v1.docx"
move "05-claude/CLAUDE_26052026.md"                   "_archive/versions-anciennes/CLAUDE_26052026.md"
move "05-claude/.Rhistory"                            "_interne/CLAUDE_Rhistory"

echo "== Doublon Gemin-cli (garde la version underscore, archive celle avec espace) =="
move "03-outils-google/ia-education/Gemin-cli V2.html" "_archive/doublons-a-verifier/Gemin-cli_V2_avec_espace.html"

echo "== Lectures de fond à la racine vers ressources/lectures =="
for f in "202606_Infox_version_web.pdf" "A_Definition_of_AGI.md" \
         "IA _ quand ChatGPT vous fait surestimer tous vos talents !.pdf" \
         "Ingé.pdf" "Souverain_2024_These.pdf" "When Does LeJEPA Learn a World Model_.pdf" \
         "Integrating Google Antigravity Unlocking the Google Workspace Extension for Gemini CL.docx" \
         "Synthèse - Pensées sur l'IA.md" "Transformers Attention.jpg" "turing.jpg" \
         "Cours_IA_v2_illustre.pptx" "resume_competences.md"; do
  move "$f" "ressources/lectures/$f"
done
move "Prompts&Ressources IA.md" "ressources/Prompts_et_Ressources_IA.md"

echo "== LiveBook : retiré du suivi git, conservé sur le disque =="
if [ -d LiveBook ]; then
  git rm -r --cached LiveBook >/dev/null 2>&1 && echo "  LiveBook retiré du suivi (toujours présent sur le disque)."
  grep -qxF "LiveBook/" .gitignore 2>/dev/null || printf "\n# Contenu jugé inutile, gardé hors dépôt\nLiveBook/\n" >> .gitignore
fi

echo "== Nettoyage des dossiers sources vides =="
for d in "00-Formation" "Activités"; do
  [ -d "$d" ] && rmdir "$d" 2>/dev/null && echo "  $d supprimé (vide)" || { [ -d "$d" ] && echo "  $d n'est pas vide, à vérifier à la main"; }
done

echo
echo "== Terminé =="
echo "Vérifie avec : git status"
echo "Puis ouvre quelques pages HTML déplacées pour confirmer que leurs images s'affichent."
echo "Quand l'arborescence te convient, demande le README réaligné : il sera généré sur"
echo "la structure réelle, pas sur une prédiction."
echo "Rappel : le dossier 05-claude/.claude et claude-usage/ n'ont pas été touchés."
