# Script pour corriger pmet_app.py avec le code CSV
import re

print("Lecture de pmet_app.py...")
with open('pmet_app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Trouver la ligne qui contient "def _process_analysis"
start_idx = None
for i, line in enumerate(lines):
    if 'def _process_analysis(self, file_path):' in line:
        start_idx = i
        print(f"Trouve _process_analysis a la ligne {i+1}")
        break

if start_idx is None:
    print("ERREUR: _process_analysis non trouve!")
    exit(1)

# Nouveau code a inserer
new_code = """    def _process_analysis(self, file_path):
        try:
            output_dir = os.path.dirname(os.path.abspath(__file__))
            
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
            
            # 1. Run Analysis
            self.update_status("Generation des graphiques et rapport Excel...")
            # Note: analyze_file returns (stats, graph_dir, excel_file, rich_excel_file)
            stats, graph_dir, excel_path, rich_excel_path = analyse_pmet.analyze_file(analysis_file, output_dir)
"""

# Trouver la fin de la methode (jusqu'a la ligne avec self.excel_report_path)
end_idx = None
for i in range(start_idx + 1, min(start_idx + 20, len(lines))):
    if 'self.excel_report_path = excel_path' in lines[i]:
        end_idx = i
        print(f"Trouve la fin a la ligne {i+1}")
        break

if end_idx is None:
    print("ERREUR: fin de methode non trouvee!")
    exit(1)

# Remplacer les lignes
new_lines = lines[:start_idx] + [new_code + '\n'] + lines[end_idx:]

print("Ecriture du fichier corrige...")
with open('pmet_app.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("[OK] Fichier corrige avec succes!")
print("Verification...")
with open('pmet_app.py', 'r', encoding='utf-8') as f:
    content = f.read()
    if 'analysis_file' in content:
        print("[OK] Variable 'analysis_file' trouvee dans le code")
    else:
        print("[ERREUR] Variable 'analysis_file' non trouvee!")
