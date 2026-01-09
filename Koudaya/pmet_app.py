import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
import webbrowser
import threading

# Import our backend modules
try:
    import analyse_pmet
    import generate_report
    import csv_parser  # Support for direct CSV processing
except ImportError as e:
    messagebox.showerror("Erreur", f"Modules manquants : {e}\nVérifiez que analyse_pmet.py, generate_report.py et csv_parser.py sont dans le même dossier.")
    sys.exit(1)

class PmetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SATEBA - Analyse PMET")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        
        # Colors
        self.bg_color = "#0A0F1D"
        self.fg_color = "#F0F2F5"
        self.accent_color = "#FFD700" 
        self.btn_color = "#1E293B"
        
        self.root.configure(bg=self.bg_color)
        
        # UI Elements
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(pady=30)
        
        title_label = tk.Label(header_frame, text="SATEBA", font=("Helvetica", 24, "bold"), 
                               bg=self.bg_color, fg=self.fg_color)
        title_label.pack()
        
        subtitle_label = tk.Label(header_frame, text="Analyseur de Données PMET", font=("Helvetica", 14), 
                                  bg=self.bg_color, fg=self.accent_color)
        subtitle_label.pack()

        # Main Content
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(pady=20, expand=True)

        self.instruction_label = tk.Label(main_frame, text="Sélectionnez un fichier Excel (.xlsx) ou CSV (.csv) contenant les mesures",
                                          bg=self.bg_color, fg="#8E9AAF", font=("Arial", 10))
        self.instruction_label.pack(pady=10)

        # File Selection Button
        self.select_btn = tk.Button(main_frame, text="Ouvrir un Fichier (Excel/CSV)", 
                                    command=self.select_file,
                                    bg=self.accent_color, fg="#000000",
                                    font=("Arial", 12, "bold"),
                                    padx=20, pady=10, borderwidth=0, cursor="hand2")
        self.select_btn.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(main_frame, text="", bg=self.bg_color, fg=self.fg_color)
        self.status_label.pack(pady=20)
        
        # Result Actions (Hidden initially)
        self.action_frame = tk.Frame(main_frame, bg=self.bg_color)
        
        self.open_report_btn = tk.Button(self.action_frame, text="Voir le Rapport (Excel)", 
                                         command=self.open_excel_report,
                                         bg=self.btn_color, fg=self.fg_color,
                                         font=("Arial", 11), padx=15, pady=8, borderwidth=0)
        self.open_report_btn.pack(side=tk.LEFT, padx=10)
        
        self.open_folder_btn = tk.Button(self.action_frame, text="Ouvrir le Dossier", 
                                         command=self.open_folder,
                                         bg=self.btn_color, fg=self.fg_color,
                                         font=("Arial", 11), padx=15, pady=8, borderwidth=0)
        self.open_folder_btn.pack(side=tk.LEFT, padx=10)

        # Footer
        footer_label = tk.Label(self.root, text="v1.0 | SATEBA France | by Mohamed Koudaya", 
                                bg=self.bg_color, fg="#475569", font=("Arial", 8))
        footer_label.pack(side=tk.BOTTOM, pady=10)

    def select_file(self):
        # Utiliser le dossier utilisateur par défaut
        initial_dir = os.path.expanduser("~")
        
        file_path = filedialog.askopenfilename(
            initialdir=initial_dir,
            title="Sélectionner le fichier (Excel ou CSV Keyence)",
            filetypes=[("Fichiers supportés", "*.xlsx *.csv"),
                      ("Fichiers Excel", "*.xlsx"), 
                      ("Fichiers CSV", "*.csv"),
                      ("Tous les fichiers", "*.*")]
        )
        
        if file_path:
            self.run_analysis(file_path)

    def run_analysis(self, file_path):
        # Disable button
        self.select_btn.config(state=tk.DISABLED, text="Analyse en cours...")
        self.status_label.config(text="Traitement des données...", fg=self.accent_color)
        self.action_frame.pack_forget()
        
        # Threading to keep UI responsive
        thread = threading.Thread(target=self._process_analysis, args=(file_path,))
        thread.start()

    def _process_analysis(self, file_path):
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

            self.excel_report_path = excel_path
            self.rich_excel_report_path = rich_excel_path
            
            # 2. Generate Report
            self.update_status("Finalisation...")
            self.report_path = generate_report.generate_html_report(stats, output_dir)
            
            # Success
            self.root.after(0, self.on_success)
            
        except Exception as e:
            self.root.after(0, lambda: self.on_error(str(e)))

    def update_status(self, message):
        self.root.after(0, lambda: self.status_label.config(text=message))

    def on_success(self):
        self.select_btn.config(state=tk.NORMAL, text="Analyser un autre fichier")
        self.status_label.config(text="Analyse terminée avec succès !", fg="#4ADE80")
        
        # Reset action frame
        for widget in self.action_frame.winfo_children():
            widget.destroy()
            
        self.open_report_btn = tk.Button(self.action_frame, text="Voir Rapport Web", 
                                         command=self.open_web_report,
                                         bg=self.btn_color, fg=self.fg_color,
                                         font=("Arial", 11), padx=15, pady=8, borderwidth=0)
        self.open_report_btn.pack(side=tk.LEFT, padx=10)
        
        self.open_rich_btn = tk.Button(self.action_frame, text="Rapport Excel (Editable)", 
                                         command=self.open_rich_excel_report,
                                         bg="#217346", fg="white", # Excel Green
                                         font=("Arial", 11, "bold"), padx=15, pady=8, borderwidth=0)
        self.open_rich_btn.pack(side=tk.LEFT, padx=10)
        
        self.open_folder_btn = tk.Button(self.action_frame, text="Ouvrir Dossier", 
                                         command=self.open_folder,
                                         bg=self.btn_color, fg=self.fg_color,
                                         font=("Arial", 11), padx=15, pady=8, borderwidth=0)
        self.open_folder_btn.pack(side=tk.LEFT, padx=10)

        self.action_frame.pack(pady=10)
        
        # Auto-open Web report
        self.open_web_report()

    def on_error(self, error_msg):
        self.select_btn.config(state=tk.NORMAL, text="Ouvrir un Fichier Excel")
        self.status_label.config(text=f"Erreur : {error_msg}", fg="#F87171")
        messagebox.showerror("Erreur d'analyse", f"Une erreur est survenue :\n{error_msg}")

    def open_web_report(self):
        if hasattr(self, 'report_path') and self.report_path:
             webbrowser.open('file://' + self.report_path)

    def open_excel_report(self):
        # Legacy simple report
        if hasattr(self, 'excel_report_path') and self.excel_report_path and os.path.exists(self.excel_report_path):
            try:
                os.startfile(self.excel_report_path)
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier Excel:\n{e}")

    def open_rich_excel_report(self):
        if hasattr(self, 'rich_excel_report_path') and self.rich_excel_report_path and os.path.exists(self.rich_excel_report_path):
            try:
                os.startfile(self.rich_excel_report_path)
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier Excel Complet:\n{e}")
        else:
            messagebox.showwarning("Attention", "Le rapport Excel complet n'est pas disponible.")

    def open_folder(self):
        output_dir = os.path.dirname(os.path.abspath(__file__))
        os.startfile(output_dir)

if __name__ == "__main__":
    root = tk.Tk()
    app = PmetApp(root)
    root.mainloop()
