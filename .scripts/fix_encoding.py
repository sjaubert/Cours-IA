"""
Reconstruit CLAUDE.md proprement depuis CLAUDE/claude.md.
Supprime les delimiteurs de blocs de code si presents.
Ecrit en UTF-8 sans BOM avec LF final.
"""
import pathlib

# Lire le contenu source (celui qui a l'air correct)
source = pathlib.Path("CLAUDE/claude.md")
dest = pathlib.Path("CLAUDE.md")

content = source.read_text(encoding="utf-8")
lines = content.splitlines()

# Supprimer les delimiteurs de bloc de code (```) au debut et a la fin
if lines and lines[0].strip().startswith("```"):
    lines = lines[1:]
if lines and lines[-1].strip() == "```":
    lines = lines[:-1]

content = "\n".join(lines).rstrip() + "\n"

# Verifier que ca commence bien par du Markdown
if not content.strip().startswith("#"):
    print("[WARN] Le contenu ne commence pas par un titre Markdown !")
    print("Debut:", repr(content[:100]))
else:
    print("[OK] Contenu Markdown valide.")

# Ecrire en UTF-8 sans BOM
dest.write_bytes(content.encode("utf-8"))
print(f"[OK] {dest} reecrit en UTF-8 sans BOM.")
print("Apercu:", content[:200])
