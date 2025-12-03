"""
Script de génération de données capteurs pour maintenance prédictive
Génère 12 mois de relevés horaires avec tendances et anomalies
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration
FICHIER_SORTIE = "releves_capteurs_12mois.csv"
MACHINE_ID = "PMP-042"

# Génération des timestamps (1 an, relevés toutes les heures)
date_debut = datetime(2024, 1, 1, 0, 0, 0)
nb_heures = 365 * 24  # 8760 heures
timestamps = [date_debut + timedelta(hours=i) for i in range(nb_heures)]

print(f"Génération de {nb_heures} relevés horaires...")

# Fonction pour simuler une tendance croissante (usure)
def tendance_lineaire(x, pente, offset, bruit):
    return offset + pente * x + np.random.normal(0, bruit, len(x))

# Fonction pour ajouter des cycles journaliers
def cycle_journalier(timestamps, amplitude):
    heures = np.array([t.hour for t in timestamps])
    return amplitude * np.sin(2 * np.pi * heures / 24)

# Génération des données

# Température (°C) : Augmente progressivement (usure roulement)
# Valeur normale : 50°C, augmente jusqu'à 75°C en fin d'année
x = np.arange(len(timestamps))
temperature_base = tendance_lineaire(x, pente=25/nb_heures, offset=50, bruit=2)
temperature = temperature_base + cycle_journalier(timestamps, amplitude=3)
temperature = np.clip(temperature, 30, 85)  # Limites physiques

# Vibration (mm/s RMS) : Augmente avec usure roulements
# Valeur normale : 2 mm/s, augmente jusqu'à 8 mm/s (inadmissible)
vibration_base = tendance_lineaire(x, pente=6/nb_heures, offset=2, bruit=0.3)
vibration = vibration_base + np.random.normal(0, 0.2, len(x))
vibration = np.clip(vibration, 1, 12)

# Courant moteur (A) : Augmente si frottements augmentent
# Valeur normale : 10A, augmente jusqu'à 13A
courant_base = tendance_lineaire(x, pente=3/nb_heures, offset=10, bruit=0.5)
courant = courant_base + cycle_journalier(timestamps, amplitude=0.3)
courant = np.clip(courant, 8, 15)

# Ajout d'anomalies ponctuelles
# Simuler 3 événements anormaux (pics)
anomalies_indices = random.sample(range(nb_heures), 3)
for idx in anomalies_indices:
    # Pic de température et vibration
    if idx < len(temperature):
        temperature[idx:idx+5] += np.random.uniform(8, 15)
        vibration[idx:idx+5] += np.random.uniform(2, 4)
        courant[idx:idx+5] += np.random.uniform(1, 2)

# Création du DataFrame
df = pd.DataFrame({
    'Timestamp': timestamps,
    'Machine_ID': MACHINE_ID,
    'Temperature_C': np.round(temperature, 1),
    'Vibration_mm_s': np.round(vibration, 2),
    'Courant_A': np.round(courant, 1)
})

# Sauvegarder
df.to_csv(FICHIER_SORTIE, index=False, encoding='utf-8')

print(f"\n✓ Fichier '{FICHIER_SORTIE}' créé avec succès !")
print(f"  Nombre de relevés : {len(df)}")
print(f"  Période : {df['Timestamp'].min()} à {df['Timestamp'].max()}")
print(f"\nCaractéristiques des données :")
print(f"  - Tendance croissante température : {temperature[0]:.1f}°C → {temperature[-1]:.1f}°C")
print(f"  - Tendance croissante vibration : {vibration[0]:.2f} mm/s → {vibration[-1]:.2f} mm/s")
print(f"  - Tendance croissante courant : {courant[0]:.1f}A → {courant[-1]:.1f}A")
print(f"  - {len(anomalies_indices)} anomalies ponctuelles insérées")
print(f"\n⚠️  Seuils d'alerte simulés :")
print(f"  - Température > 70°C : Attention")
print(f"  - Vibration > 7 mm/s : Inadmissible (ISO 10816)")
print(f"  - Courant > 12A : Surcharge")
