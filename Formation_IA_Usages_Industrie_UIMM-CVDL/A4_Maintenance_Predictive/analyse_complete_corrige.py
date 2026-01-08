"""
Analyse Complète - Activité A4 : Maintenance Prédictive
Corrigé complet pour les étudiants Bachelor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import base64
from io import BytesIO

# Configuration matplotlib pour des graphiques professionnels
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Seuils critiques
SEUILS = {
    'Temperature_C': 75,
    'Vibration_mm_s': 7.1,
    'Courant_A': 13
}

def load_data(filepath):
    """Charge les données et prépare le DataFrame"""
    df = pd.read_csv(filepath)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.sort_values('Timestamp')
    return df

def get_statistics(df):
    """Calcule les statistiques descriptives"""
    stats = {}
    for col in ['Temperature_C', 'Vibration_mm_s', 'Courant_A']:
        stats[col] = {
            'min': df[col].min(),
            'max': df[col].max(),
            'mean': df[col].mean(),
            'std': df[col].std(),
            'median': df[col].median()
        }
    return stats

def plot_evolution(df):
    """Crée les 3 graphiques d'évolution"""
    fig, axes = plt.subplots(3, 1, figsize=(14, 10))
    
    params = [
        ('Temperature_C', 'Température (°C)', 'red', SEUILS['Temperature_C']),
        ('Vibration_mm_s', 'Vibration (mm/s)', 'blue', SEUILS['Vibration_mm_s']),
        ('Courant_A', 'Courant (A)', 'green', SEUILS['Courant_A'])
    ]
    
    for ax, (col, title, color, seuil) in zip(axes, params):
        ax.plot(df['Timestamp'], df[col], color=color, alpha=0.6, linewidth=0.8)
        ax.axhline(y=seuil, color='darkred', linestyle='--', linewidth=2, 
                   label=f'Seuil critique: {seuil}')
        ax.set_ylabel(title, fontsize=12, fontweight='bold')
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)
    
    axes[2].set_xlabel('Date', fontsize=12, fontweight='bold')
    axes[0].set_title('Évolution des Paramètres sur 12 Mois - PMP-042', 
                      fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    # Convert to base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=120, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()
    
    return image_base64

def calculate_trends(df):
    """Calcule les régressions linéaires et projections"""
    results = {}
    
    # Création d'un index numérique pour la régression
    df['days_since_start'] = (df['Timestamp'] - df['Timestamp'].min()).dt.total_seconds() / (24*3600)
    
    for col in ['Temperature_C', 'Vibration_mm_s', 'Courant_A']:
        X = df['days_since_start'].values
        y = df[col].values
        
        # Régression linéaire avec numpy
        coefficients = np.polyfit(X, y, 1)  # degré 1 = linéaire
        slope = coefficients[0]
        intercept = coefficients[1]
        
        # Prédiction
        y_pred = slope * X + intercept
        
        # Calcul R²
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        
        # Valeur actuelle et pente
        current_value = df[col].iloc[-1]
        slope_per_day = slope
        slope_per_month = slope_per_day * 30
        
        # Projection jusqu'au seuil
        seuil = SEUILS[col]
        if slope_per_day > 0:
            days_to_threshold = (seuil - current_value) / slope_per_day
            date_threshold = df['Timestamp'].iloc[-1] + timedelta(days=days_to_threshold)
        else:
            days_to_threshold = None
            date_threshold = None
        
        results[col] = {
            'current_value': current_value,
            'slope_per_month': slope_per_month,
            'r2': r2,
            'days_to_threshold': days_to_threshold,
            'date_threshold': date_threshold,
            'y_pred': y_pred
        }
    
    return results, df

def plot_trends(df, trends):
    """Crée les graphiques de tendances avec projections"""
    fig, axes = plt.subplots(3, 1, figsize=(14, 10))
    
    params = [
        ('Temperature_C', 'Température (°C)', 'red'),
        ('Vibration_mm_s', 'Vibration (mm/s)', 'blue'),
        ('Courant_A', 'Courant (A)', 'green')
    ]
    
    for ax, (col, title, color) in zip(axes, params):
        # Données réelles
        ax.scatter(df['Timestamp'], df[col], alpha=0.3, s=5, color=color, label='Mesures')
        
        # Tendance
        ax.plot(df['Timestamp'], trends[col]['y_pred'], 
                color='darkred', linewidth=2, label='Tendance linéaire')
        
        # Seuil
        ax.axhline(y=SEUILS[col], color='orange', linestyle='--', linewidth=2,
                   label=f'Seuil: {SEUILS[col]}')
        
        # Projection si applicable
        if trends[col]['date_threshold'] is not None:
            ax.axvline(x=trends[col]['date_threshold'], color='purple', 
                      linestyle=':', linewidth=2, alpha=0.7,
                      label=f"Dépassement prévu: {trends[col]['date_threshold'].strftime('%Y-%m-%d')}")
        
        ax.set_ylabel(title, fontsize=12, fontweight='bold')
        ax.legend(loc='upper left', fontsize=9)
        ax.grid(True, alpha=0.3)
        
        # R² dans le titre
        ax.text(0.98, 0.95, f"R² = {trends[col]['r2']:.3f}", 
                transform=ax.transAxes, ha='right', va='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    axes[2].set_xlabel('Date', fontsize=12, fontweight='bold')
    axes[0].set_title('Analyse de Tendances et Projections - PMP-042', 
                      fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=120, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()
    
    return image_base64

def detect_anomalies(df):
    """Détecte les anomalies (moyenne + 2σ)"""
    anomalies = {}
    
    for col in ['Temperature_C', 'Vibration_mm_s', 'Courant_A']:
        mean = df[col].mean()
        std = df[col].std()
        threshold = mean + 2 * std
        
        anomaly_mask = df[col] > threshold
        anomaly_data = df[anomaly_mask][['Timestamp', col]].copy()
        
        anomalies[col] = {
            'threshold': threshold,
            'count': len(anomaly_data),
            'data': anomaly_data
        }
    
    return anomalies

def plot_anomalies(df, anomalies):
    """Visualise les anomalies"""
    fig, axes = plt.subplots(3, 1, figsize=(14, 10))
    
    params = [
        ('Temperature_C', 'Température (°C)', 'red'),
        ('Vibration_mm_s', 'Vibration (mm/s)', 'blue'),
        ('Courant_A', 'Courant (A)', 'green')
    ]
    
    for ax, (col, title, color) in zip(axes, params):
        # Données normales
        ax.plot(df['Timestamp'], df[col], color=color, alpha=0.5, linewidth=0.8)
        
        # Seuil anomalie
        ax.axhline(y=anomalies[col]['threshold'], color='orange', 
                   linestyle='--', linewidth=2, 
                   label=f"Seuil anomalie (μ+2σ): {anomalies[col]['threshold']:.2f}")
        
        # Anomalies
        if len(anomalies[col]['data']) > 0:
            ax.scatter(anomalies[col]['data']['Timestamp'], 
                      anomalies[col]['data'][col],
                      color='red', s=50, marker='x', linewidths=2,
                      label=f"Anomalies ({anomalies[col]['count']})",
                      zorder=5)
        
        ax.set_ylabel(title, fontsize=12, fontweight='bold')
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)
    
    axes[2].set_xlabel('Date', fontsize=12, fontweight='bold')
    axes[0].set_title('Détection d\'Anomalies (Moyenne + 2σ) - PMP-042', 
                      fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=120, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()
    
    return image_base64

def analyze_correlations(df, anomalies):
    """Analyse les corrélations entre les paramètres pendant les anomalies"""
    # Trouver les timestamps communs d'anomalies
    timestamps_temp = set(anomalies['Temperature_C']['data']['Timestamp'])
    timestamps_vib = set(anomalies['Vibration_mm_s']['data']['Timestamp'])
    timestamps_cur = set(anomalies['Courant_A']['data']['Timestamp'])
    
    # Anomalies simultanées
    simultaneous = timestamps_temp & timestamps_vib & timestamps_cur
    
    # Corrélation globale
    corr_matrix = df[['Temperature_C', 'Vibration_mm_s', 'Courant_A']].corr()
    
    return {
        'simultaneous_count': len(simultaneous),
        'correlation_matrix': corr_matrix,
        'temp_vib_corr': corr_matrix.loc['Temperature_C', 'Vibration_mm_s'],
        'temp_cur_corr': corr_matrix.loc['Temperature_C', 'Courant_A'],
        'vib_cur_corr': corr_matrix.loc['Vibration_mm_s', 'Courant_A']
    }

def main():
    """Fonction principale"""
    filepath = 'releves_capteurs_12mois.csv'
    
    print("Chargement des données...")
    df = load_data(filepath)
    
    print("Calcul des statistiques...")
    stats = get_statistics(df)
    
    print("Génération des graphiques d'évolution...")
    plot_evolution_img = plot_evolution(df)
    
    print("Calcul des tendances...")
    trends, df = calculate_trends(df)
    
    print("Génération des graphiques de tendances...")
    plot_trends_img = plot_trends(df, trends)
    
    print("Détection des anomalies...")
    anomalies = detect_anomalies(df)
    
    print("Génération des graphiques d'anomalies...")
    plot_anomalies_img = plot_anomalies(df, anomalies)
    
    print("Analyse des corrélations...")
    correlations = analyze_correlations(df, anomalies)
    
    # Retourner tous les résultats
    return {
        'stats': stats,
        'trends': trends,
        'anomalies': anomalies,
        'correlations': correlations,
        'images': {
            'evolution': plot_evolution_img,
            'trends': plot_trends_img,
            'anomalies': plot_anomalies_img
        },
        'last_date': df['Timestamp'].iloc[-1]
    }

if __name__ == '__main__':
    results = main()
    print("\nAnalyse terminée!")
    print(f"\nDernière mesure: {results['last_date'].strftime('%Y-%m-%d')}")
    print("\nStatistiques:")
    for param, data in results['stats'].items():
        print(f"\n{param}:")
        print(f"  Min: {data['min']:.2f}, Max: {data['max']:.2f}")
        print(f"  Moyenne: {data['mean']:.2f}, Écart-type: {data['std']:.2f}")
