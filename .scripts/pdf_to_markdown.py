#!/usr/bin/env python3
"""
Script utilitaire pour convertir un fichier PDF en Markdown
en utilisant pymupdf4llm
"""

import sys
import pymupdf4llm
from pathlib import Path


def pdf_to_markdown(pdf_path: str, output_path: str = None) -> str:
    """
    Convertit un PDF en Markdown
    
    Args:
        pdf_path: Chemin vers le fichier PDF
        output_path: Chemin de sortie pour le fichier .md (optionnel)
        
    Returns:
        Le contenu markdown
    """
    pdf_file = Path(pdf_path)
    
    if not pdf_file.exists():
        raise FileNotFoundError(f"Le fichier {pdf_path} n'existe pas")
    
    if not pdf_file.suffix.lower() == '.pdf':
        raise ValueError(f"Le fichier doit être un PDF")
    
    # Convertir en markdown
    print(f"Conversion de {pdf_file.name}...")
    md_text = pymupdf4llm.to_markdown(str(pdf_file))
    
    # Déterminer le chemin de sortie
    if output_path is None:
        output_path = pdf_file.with_suffix('.md')
    else:
        output_path = Path(output_path)
    
    # Sauvegarder le fichier markdown
    output_path.write_text(md_text, encoding='utf-8')
    print(f"✓ Fichier markdown créé : {output_path}")
    
    return md_text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_markdown.py <fichier.pdf> [fichier_sortie.md]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        pdf_to_markdown(pdf_path, output_path)
    except Exception as e:
        print(f"Erreur : {e}", file=sys.stderr)
        sys.exit(1)
