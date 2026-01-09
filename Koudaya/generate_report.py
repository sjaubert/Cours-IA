import json
import os
import shutil
from datetime import datetime

# Common paths and constants
# (Ces chemins par défaut seront écrasés si on appelle la fonction avec des arguments)
DEFAULT_ROOT_DIR = os.getcwd()

def format_number(value):
    """Format numbers nicely"""
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)

def get_status_class(percentage, threshold=10):
    """Return styling class based on value"""
    is_good = percentage < threshold
    return "status-good" if is_good else "status-bad"

def generate_html_report(stats_data, output_dir):
    """
    Génère le rapport HTML à partir des données statistiques fournies.
    
    Args:
        stats_data (dict): Dictionnaire contenant les stats ('P' et 'G')
        output_dir (str): Dossier racine où générer le rapport (contenant 'summary' et 'graphiques')
    """
    
    summary_dir = os.path.join(output_dir, 'summary')
    assets_dir = os.path.join(summary_dir, 'assets')
    graph_dir = os.path.join(output_dir, 'graphiques')
    output_html = os.path.join(summary_dir, 'index.html')
    
    # 1. Setup Assets
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    
    # Copier les graphiques vers assets
    if os.path.exists(graph_dir):
        for filename in os.listdir(graph_dir):
            if filename.endswith('.png'):
                src = os.path.join(graph_dir, filename)
                dst = os.path.join(assets_dir, filename)
                try:
                    shutil.copy2(src, dst)
                except Exception as e:
                    print(f"Warning: Could not copy {filename}: {e}")

    # Copy background image if exists in root
    bg_src = os.path.join(output_dir, "bg_train.png")
    bg_dst = os.path.join(assets_dir, "bg_train.png")
    if os.path.exists(bg_src):
        try:
            shutil.copy2(bg_src, bg_dst)
        except Exception as e:
                print(f"Warning: Could not copy background image: {e}")

    # 2. Extract Stats
    p_stats = stats_data.get('P', {})
    g_stats = stats_data.get('G', {})
    timestamp = p_stats.get('timestamp', datetime.now().strftime("%d/%m/%Y %H:%M"))

    # 3. Generate HTML Content
    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SATEBA France - Rapport d'Analyse PMET</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Outfit:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="logo-container">
            <h1>SATEBA <span>France</span></h1>
            <div class="rail-accent"></div>
        </div>
        <p style="text-align: center; color: var(--text-muted); margin-top: 1rem;">
            Rapport d'Analyse Automatisé • {timestamp}
        </p>
    </header>

    <main>
        
        <!-- P PMET SECTION -->
        <section class="intro">
            <h2>Analyse P PMET</h2>
            <p>Synthèse des mesures pour les profils de type P (Limite < 80mm)</p>
        </section>

        <div class="grid">
            <article class="card">
                <div class="card-number">M</div>
                <h3>Volume Analysé</h3>
                <div class="stat-value">{p_stats.get('total_moules', 0)}</div>
                <div class="stat-label">Moules Totaux</div>
            </article>

            <article class="card">
                <div class="card-number">%</div>
                <h3>Non-Conformité</h3>
                <div class="stat-value {get_status_class(p_stats.get('taux_non_conformite', 0))}">
                    {format_number(p_stats.get('taux_non_conformite', 0))}%
                </div>
                <div class="stat-label">Taux de Rejet</div>
            </article>

            <article class="card">
                <div class="card-number">Ø</div>
                <h3>Moyenne Globale</h3>
                <div class="stat-value">{format_number(p_stats.get('moyenne_globale', 0))}</div>
                <div class="stat-label">Millimètres</div>
            </article>
        </div>

        <div class="graph-section">
            <h3 style="color: var(--brand-yellow); margin-bottom: 1rem;">Courbes de Tendance P PMET</h3>
            <div class="graph-container">
                <img src="assets/P_PMET_tendances.png" alt="Graphiques P PMET">
            </div>
        </div>

        <div style="margin: 4rem 0; text-align: center;"><div class="rail-accent" style="width: 100px; opacity: 0.5;"></div></div>

        <!-- G PMET SECTION -->
        <section class="intro">
            <h2>Analyse G PMET</h2>
            <p>Synthèse des mesures pour les profils de type G (Limite < 130mm)</p>
        </section>

        <div class="grid">
            <article class="card">
                <div class="card-number">M</div>
                <h3>Volume Analysé</h3>
                <div class="stat-value">{g_stats.get('total_moules', 0)}</div>
                <div class="stat-label">Moules Totaux</div>
            </article>

            <article class="card">
                <div class="card-number">%</div>
                <h3>Non-Conformité</h3>
                <div class="stat-value {get_status_class(g_stats.get('taux_non_conformite', 0))}">
                    {format_number(g_stats.get('taux_non_conformite', 0))}%
                </div>
                <div class="stat-label">Taux de Rejet</div>
            </article>

            <article class="card">
                <div class="card-number">Ø</div>
                <h3>Moyenne Globale</h3>
                <div class="stat-value">{format_number(g_stats.get('moyenne_globale', 0))}</div>
                <div class="stat-label">Millimètres</div>
            </article>
        </div>

         <div class="graph-section">
            <h3 style="color: var(--brand-yellow); margin-bottom: 1rem;">Courbes de Tendance G PMET</h3>
            <div class="graph-container">
                <img src="assets/G_PMET_tendances.png" alt="Graphiques G PMET">
            </div>
        </div>

    </main>

    <footer>
        <div class="signature">
            <div class="railway-icon">
                <div class="rail-line"></div>
                <div class="sleeper"></div>
                <div class="sleeper"></div>
                <div class="sleeper"></div>
                <div class="rail-line"></div>
            </div>
            <p>SATEBA France | Rapport Généré Automatiquement</p>
        </div>
    </footer>
</body>
</html>
"""
    
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Rapport HTML généré: {output_html}")
    return output_html

def main():
    # Backward compatibility for running directly
    print("Mode manuel : Lecture de stats.json...")
    stats_file = os.path.join('summary', 'stats.json')
    if os.path.exists(stats_file):
        with open(stats_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        generate_html_report(data, os.getcwd())
    else:
        print("Fichier stats.json introuvable.")

if __name__ == "__main__":
    main()
