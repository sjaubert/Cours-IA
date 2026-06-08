#!/usr/bin/env bash
# Hook PostToolUse : controle qualite apres chaque edition d'une procedure.
# Verifie que tout fichier docs/procedure_*.md contient les rubriques
# obligatoires d'une procedure d'intervention securisee.
#
# Sort en code 2 si une rubrique manque, pour signaler le probleme a l'agent.

set -euo pipefail

INPUT="$(cat)"
FICHIER="$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // empty')"

# Ne controle que les procedures
case "$FICHIER" in
  *docs/procedure_*.md) ;;
  *) exit 0 ;;
esac

[ -f "$FICHIER" ] || exit 0

RUBRIQUES=("Pre-requis securite" "Consignation" "Mode operatoire" "Verification" "Remise en service")
MANQUANTES=()

for r in "${RUBRIQUES[@]}"; do
  grep -qi "$r" "$FICHIER" || MANQUANTES+=("$r")
done

if [ "${#MANQUANTES[@]}" -gt 0 ]; then
  echo "Procedure incomplete : rubriques manquantes -> ${MANQUANTES[*]}" >&2
  exit 2
fi

exit 0
