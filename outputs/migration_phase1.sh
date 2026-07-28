#!/usr/bin/env bash
#
# Cours-IA : migration phase 1 (gains sûrs, sans impact sur les liens du README).
# À lire avant de lancer. À exécuter depuis la racine du dépôt Cours-IA.
#
# Ce script :
#   1. crée un .gitignore correct
#   2. retire node_modules du suivi git
#   3. crée _archive et _interne
#   4. y range essais, scripts et fichiers de service (tous orphelins du README)
#
# Il ne touche à AUCUN contenu référencé dans le README. Les liens restent valides.
# La phase 2 (déplacement des domaines) est un autre script, à générer après validation.

set -u

# Garde-fou : on doit être à la racine du dépôt.
if [ ! -f "README.md" ] || [ ! -d ".git" ]; then
  echo "Erreur : lance ce script depuis la racine du dépôt Cours-IA (README.md et .git attendus)." >&2
  exit 1
fi

# Déplacement sûr : git mv si le fichier est suivi, sinon mv simple.
move() {
  local src="$1" dst="$2"
  if [ ! -e "$src" ]; then
    echo "  ignoré (absent) : $src"
    return
  fi
  mkdir -p "$(dirname "$dst")"
  if git ls-files --error-unmatch "$src" >/dev/null 2>&1; then
    git mv -k "$src" "$dst" && echo "  git mv : $src -> $dst"
  else
    mv "$src" "$dst" && echo "  mv     : $src -> $dst"
  fi
}

echo "== 1. .gitignore =="
cat > .gitignore <<'IGN'
# Dépendances régénérables
node_modules/
.venv/
__pycache__/
*.pyc

# Fichiers de travail
.Rhistory
*.tmp
extracted_text.txt
doc_content.json

# Dossier interne non publié (décommente si tu ne veux pas le publier)
# _interne/
IGN
git add .gitignore
echo "  .gitignore écrit."

echo "== 2. Retrait de node_modules du suivi git =="
if [ -d "00-Formation/prompt_flow_uimm/node_modules" ]; then
  git rm -r --cached "00-Formation/prompt_flow_uimm/node_modules" >/dev/null 2>&1 \
    && echo "  node_modules retiré du suivi (fichiers conservés sur le disque)." \
    || echo "  node_modules n'était pas suivi, rien à faire."
else
  echo "  dossier node_modules introuvable, rien à faire."
fi

echo "== 3. Dossiers cibles =="
mkdir -p _archive _interne
echo "  _archive et _interne prêts."

echo "== 4. Rangement des orphelins =="

# Coquille vide -> archive
move "Developper_applications_LLM_SDK_Vertex_AI" "_archive/vertex-ai-coquille-vide"

# Essais et sous-projets orphelins -> interne
move "app_Test"  "_interne/app_Test"
move "gemini_API" "_interne/gemini_API"
move "tasks"      "_interne/tasks"

# Scripts et sorties de travail à la racine -> interne
for f in organize_files.py fix_readme_encoding.py extract_doc.py extract_docx.py \
         chat_gemini.py verify_moves.py doc_content.json extracted_text.txt .Rhistory; do
  move "$f" "_interne/$f"
done

echo
echo "== Terminé. À faire à la main =="
echo "  - claude-usage/ : dépôt git tiers imbriqué. Ne pas le déplacer avec git mv."
echo "    Décide s'il reste (le sortir vers _interne à la main) ou s'il part ailleurs."
echo "  - streamlit_cheatsheet/ et espérance_vie/ : démos exploitables, destination à décider"
echo "    (_interne ou ressources/demos)."
echo "  - LiveBook/ et Accomplish/ : vrai contenu à exposer, traité en phase 2."
echo
echo "Relis avec 'git status', puis 'git commit' quand tu es satisfait."
