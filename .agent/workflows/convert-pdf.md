---
description: Convertir un PDF en Markdown pour lecture
---

# Conversion PDF vers Markdown

Quand tu as besoin de lire un fichier PDF et que tes outils habituels ne fonctionnent pas bien, utilise le script de conversion avec `pymupdf4llm`.

## Prérequis

- `pymupdf4llm` doit être installé : `pip install pymupdf4llm`
- Le script utilitaire se trouve dans `.scripts/pdf_to_markdown.py`

## Utilisation

// turbo
1. Convertir un PDF en markdown :
```bash
python .scripts/pdf_to_markdown.py "chemin/vers/fichier.pdf"
```

2. Le fichier markdown sera créé automatiquement avec le même nom que le PDF (extension `.md`)

3. Tu peux ensuite lire le fichier markdown avec `view_file` ou d'autres outils

## Exemple

```bash
python .scripts/pdf_to_markdown.py "IA/Module Formation/IA_Démystifiée_Des_Concepts_Aux_Applications.pdf"
```

Cela créera : `IA/Module Formation/IA_Démystifiée_Des_Concepts_Aux_Applications.md`

## Notes

- Utilise cet outil **uniquement quand nécessaire** (pas de conversion en masse)
- Le script gère automatiquement l'encodage UTF-8
- Si le PDF est volumineux, la conversion peut prendre quelques secondes
