import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# Configuration
FILE_PATH = 'releves_capteurs_12mois.csv'
THRESHOLDS = {
    'Temperature_C': 75.0,
    'Vibration_mm_s': 7.1,
    'Courant_A': 13.0
}

def analyze_trends(file_path):
    print(f"Chargement des données depuis {file_path}...")
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
        return

    # Conversion du timestamp
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Conversion en nombres pour la régression (jours depuis le début)
    start_date = df['Timestamp'].min()
    df['Days'] = (df['Timestamp'] - start_date).dt.total_seconds() / (24 * 3600)

    # Préparation des graphiques
    fig, axes = plt.subplots(3, 1, figsize=(12, 15), sharex=True)
    plt.subplots_adjust(hspace=0.4)
    
    results = []

    for i, (col, threshold) in enumerate(THRESHOLDS.items()):
        ax = axes[i]
        
        # Données
        X = df['Days'].values
        y = df[col].values
        
        # Régression linéaire (y = ax + b)
        slope, intercept = np.polyfit(X, y, 1)
        
        # Tendance
        trend = "Croissante" if slope > 0 else "Décroissante"
        
        # Projection
        date_depassement = None
        days_to_threshold = None
        
        if slope > 0 and intercept < threshold:
            # Seuil atteint quand ax + b = threshold => x = (threshold - b) / a
            days_to_threshold = (threshold - intercept) / slope
            date_depassement = start_date + pd.Timedelta(days=days_to_threshold)
        
        # Sauvegarde des résultats
        results.append({
            'Paramètre': col,
            'Tendance': trend,
            'Pente': slope,
            'Seuil': threshold,
            'Date prévisionnelle dépassement': date_depassement
        })

        # --- Visualisation ---
        
        # Nuage de points (données réelles) - on en affiche un sous-ensemble pour la lisibilité si trop de points
        ax.scatter(df['Timestamp'], y, alpha=0.3, s=1, label='Données réelles', color='gray')
        
        # Ligne de régression (étendue pour montrer le futur si dépassement prévu)
        max_days = X.max()
        if days_to_threshold and days_to_threshold > max_days:
            max_days = days_to_threshold * 1.1 # Étendre un peu après le seuil
            
        X_plot = np.linspace(0, max_days, 100)
        y_plot = slope * X_plot + intercept
        dates_plot = [start_date + pd.Timedelta(days=d) for d in X_plot]
        
        ax.plot(dates_plot, y_plot, color='red', linewidth=2, label=f'Tendance (pente={slope:.4f})')
        
        # Ligne de seuil
        ax.axhline(y=threshold, color='orange', linestyle='--', linewidth=2, label=f'Seuil ({threshold})')
        
        # Marqueur dépassement
        if date_depassement:
            ax.axvline(x=date_depassement, color='purple', linestyle=':', label='Dépassement prévu')
            ax.text(date_depassement, threshold, f' {date_depassement.strftime("%Y-%m-%d")}', color='purple', fontweight='bold')

        ax.set_title(f'Analyse : {col}')
        ax.set_ylabel(col)
        ax.legend()
        ax.grid(True, alpha=0.3)

    # Formatage de l'axe X (dates)
    axes[-1].set_xlabel('Date')
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    axes[-1].xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45)
    
    print("\n--- RÉSULTATS DE L'ANALYSE ---")
    for res in results:
        print(f"\nParamètre : {res['Paramètre']}")
        print(f"  - Tendance : {res['Tendance']} (pente: {res['Pente']:.5f})")
        if res['Date prévisionnelle dépassement']:
            print(f"  - ⚠️ SEUIL CRITIQUE ({res['Seuil']}) sera atteint le : {res['Date prévisionnelle dépassement'].strftime('%Y-%m-%d')}")
        else:
            print(f"  - Pas de dépassement prévu dans un futur proche (ou tendance décroissante).")

    plt.suptitle('Analyse Prédictive des Capteurs', fontsize=16)
    plt.show()

if __name__ == "__main__":
    analyze_trends(FILE_PATH)
