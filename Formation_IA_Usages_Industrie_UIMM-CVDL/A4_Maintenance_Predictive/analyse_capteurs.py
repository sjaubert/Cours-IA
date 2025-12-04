import pandas as pd
import matplotlib.pyplot as plt

# 1. Charger les données
fichier = "releves_capteurs_12mois.csv"
print(f"Chargement du fichier {fichier}...")
df = pd.read_csv(fichier)

# Conversion du timestamp
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# 2. Créer 3 graphiques
plt.figure(figsize=(15, 10))

# Température
plt.subplot(3, 1, 1)
plt.plot(df['Timestamp'], df['Temperature_C'], color='red', linewidth=0.5)
plt.title('Évolution de la Température (°C)')
plt.ylabel('Température (°C)')
plt.grid(True, alpha=0.3)

# Vibration
plt.subplot(3, 1, 2)
plt.plot(df['Timestamp'], df['Vibration_mm_s'], color='blue', linewidth=0.5)
plt.title('Évolution de la Vibration (mm/s)')
plt.ylabel('Vibration (mm/s)')
plt.grid(True, alpha=0.3)

# Courant
plt.subplot(3, 1, 3)
plt.plot(df['Timestamp'], df['Courant_A'], color='green', linewidth=0.5)
plt.title('Évolution du Courant (A)')
plt.ylabel('Courant (A)')
plt.xlabel('Date')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('analyse_capteurs.png')
print("Graphiques sauvegardés dans 'analyse_capteurs.png'")
plt.show()

# 3. Afficher les statistiques de base
print("\nStatistiques de base :")
cols = ['Temperature_C', 'Vibration_mm_s', 'Courant_A']
stats = df[cols].agg(['min', 'max', 'mean', 'std'])
print(stats)
