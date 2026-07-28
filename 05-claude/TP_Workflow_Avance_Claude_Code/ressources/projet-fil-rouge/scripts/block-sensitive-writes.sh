#!/usr/bin/env bash
# Hook PreToolUse : bloque toute ecriture sur des fichiers sensibles.
# Contexte industriel : exports GMAO bruts et configuration automate
# ne doivent jamais etre modifies par l'agent.
#
# Claude Code transmet l'appel d'outil au format JSON sur stdin.
# Le script lit le chemin cible et sort en code 2 pour BLOQUER l'action.
# Tout autre code (0) laisse l'action se poursuivre.

set -euo pipefail

INPUT="$(cat)"
FICHIER="$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // empty')"

# Motifs interdits. Les motifs de dossier tolerent un chemin relatif.
MOTIFS_INTERDITS='(\.env$|\.env\.|(^|/)secrets/|(^|/)data/gmao_brut/|credentials|automate_config)'

if printf '%s' "$FICHIER" | grep -Eq "$MOTIFS_INTERDITS"; then
  echo "Ecriture refusee : $FICHIER est un fichier protege (donnees ou secrets)." >&2
  exit 2
fi

exit 0
