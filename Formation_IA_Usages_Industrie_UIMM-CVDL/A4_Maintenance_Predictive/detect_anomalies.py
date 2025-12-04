import pandas as pd
import matplotlib.pyplot as plt

# 1. Charger les données
fichier = "releves_capteurs_12mois.csv"
print(f"Chargement du fichier {fichier}...")
try:
    df = pd.read_csv(fichier)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
except FileNotFoundError:
    print(f"Erreur : Le fichier {fichier} est introuvable.")
    exit()

# Colonnes à analyser
colonnes = ['Temperature_C', 'Vibration_mm_s', 'Courant_A']

# Dictionnaire pour stocker les anomalies
anomalies_dict = {}

# Configuration des graphiques
plt.figure(figsize=(15, 12))

for i, col in enumerate(colonnes):
    # 2. Calculer moyenne et écart-type
    moyenne = df[col].mean()
    ecart_type = df[col].std()
    seuil = moyenne + 2 * ecart_type

    print(f"\n--- Analyse de {col} ---")
    print(f"Moyenne : {moyenne:.2f}")
    print(f"Écart-type : {ecart_type:.2f}")
    print(f"Seuil d'anomalie (> moy + 2*std) : {seuil:.2f}")

    # 3. Identifier les anomalies
    anomalies = df[df[col] > seuil]
    anomalies_dict[col] = anomalies

    # 4. Lister les timestamps
    if not anomalies.empty:
        print(f"Anomalies détectées ({len(anomalies)}) :")
        for index, row in anomalies.iterrows():
            print(f"  - {row['Timestamp']} : {row[col]:.2f}")
    else:
        print("Aucune anomalie détectée.")

    # 5. Afficher sur les graphiques
    plt.subplot(3, 1, i + 1)
    plt.plot(df['Timestamp'], df[col], label='Données normales', color='blue', linewidth=0.5)
    
    # Mettre en évidence les anomalies
    if not anomalies.empty:
        plt.scatter(anomalies['Timestamp'], anomalies[col], color='red', label='Anomalies', zorder=5)

    plt.title(f'Détection d\'anomalies : {col}')
    plt.ylabel(col)
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.xlabel('Date')
plt.tight_layout()
plt.savefig('anomalies_detected.png')
print("\nGraphique sauvegardé sous 'anomalies_detected.png'")
# plt.show() # Commenté pour éviter de bloquer l'exécution si pas d'interface graphique
