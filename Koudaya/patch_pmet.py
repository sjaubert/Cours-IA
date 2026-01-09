# Script helper pour injecter le code CSV dans pmet_app.py
import re

with open('pmet_app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Trouver la ligne avec "stats, graph_dir, excel_path, rich_excel_path = analyse_pmet.analyze_file(file_path, output_dir)"
# et insérer le code de conversion CSV avant

csv_conversion_code = """            
            # Check if file is CSV and convert if needed
            analysis_file = file_path
            if file_path.lower().endswith('.csv'):
                self.update_status("Conversion du fichier CSV en format Excel...")
                try:
                    # Convert CSV to Excel format
                    temp_excel = csv_parser.csv_to_compatible_format(file_path)
                    analysis_file = temp_excel
                    self.update_status("Conversion reussie. Analyse en cours...")
                except Exception as csv_error:
                    raise Exception(f"Erreur lors de la conversion CSV: {csv_error}")
            
"""

# Remplacer "analyse_pmet.analyze_file(file_path, output_dir)" par "analyse_pmet.analyze_file(analysis_file, output_dir)"
content = content.replace(
    '            # 1. Run Analysis\n            self.update_status("Generation des graphiques et rapport Excel...")\n            # Note: analyze_file returns (stats, graph_dir, excel_file, rich_excel_file)\n            stats, graph_dir, excel_path, rich_excel_path = analyse_pmet.analyze_file(file_path, output_dir)',
    csv_conversion_code + '            # 1. Run Analysis\n            self.update_status("Generation des graphiques et rapport Excel...")\n            # Note: analyze_file returns (stats, graph_dir, excel_file, rich_excel_file)\n            stats, graph_dir, excel_path, rich_excel_path = analyse_pmet.analyze_file(analysis_file, output_dir)'
)

with open('pmet_app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Modification appliquee!")
