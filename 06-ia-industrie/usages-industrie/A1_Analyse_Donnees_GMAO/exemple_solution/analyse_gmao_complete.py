"""
Solution complète de l'activité : Analyse de Données GMAO
Ce script illustre une approche complète de l'analyse
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Configuration
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

print("="*60)
print("ANALYSE DES DONNÉES GMAO - 2024")
print("="*60)

# ==============================================================================
# ÉTAPE 1 : CHARGEMENT ET NETTOYAGE DES DONNÉES
# ==============================================================================

print("\n[1/5] Chargement des données...")
try:
    df = pd.read_csv('interventions_2024.csv', encoding='utf-8')
    print(f"✓ {len(df)} interventions chargées")
except FileNotFoundError:
    print("❌ Erreur : fichier 'interventions_2024.csv' non trouvé")
    print("Exécutez d'abord : python generer_donnees_gmao.py")
    exit(1)

print(f"\nAperçu des données brutes :")
print(df.head())
print(f"\nTypes de données :")
print(df.dtypes)

print("\n[2/5] Nettoyage des données...")

# 1. Normalisation des dates
def nettoyer_date(date_str):
    """Convertit différents formats de dates en datetime"""
    if pd.isna(date_str):
        return pd.NaT

    formats = [
        "%Y-%m-%d",      # 2024-01-15
        "%d/%m/%Y",      # 15/01/2024
        "%d-%m-%Y",      # 15-01-2024
        "%d.%m.%Y",      # 15.01.2024
    ]

    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except:
            continue

    return pd.NaT

df['Date'] = df['Date'].apply(nettoyer_date)
print(f"✓ Dates normalisées : {df['Date'].notna().sum()} valeurs valides")

# 2. Normalisation des durées (conversion en heures décimales)
def nettoyer_duree(duree_str):
    """Convertit différents formats de durées en heures (float)"""
    if pd.isna(duree_str):
        return np.nan

    duree_str = str(duree_str).strip()

    # Format : "3h30" ou "3h00"
    if 'h' in duree_str:
        parts = duree_str.split('h')
        heures = float(parts[0])
        minutes = float(parts[1]) if len(parts) > 1 and parts[1] else 0
        return heures + minutes / 60

    # Format : "3:30"
    if ':' in duree_str:
        parts = duree_str.split(':')
        heures = float(parts[0])
        minutes = float(parts[1]) if len(parts) > 1 else 0
        return heures + minutes / 60

    # Format : "3.5" ou "3"
    try:
        return float(duree_str)
    except:
        return np.nan

df['Duree_Arret_h'] = df['Duree_Arret_h'].apply(nettoyer_duree)
print(f"✓ Durées normalisées : {df['Duree_Arret_h'].notna().sum()} valeurs valides")

# 3. Normalisation des types de pannes
dictionnaire_pannes = {
    "panne mecanique": "Panne Mécanique",
    "mecanique": "Panne Mécanique",
    "panne electrique": "Panne Électrique",
    "electrique": "Panne Électrique",
    "panne pneumatique": "Panne Pneumatique",
    "pneumatique": "Panne Pneumatique",
    "panne hydraulique": "Panne Hydraulique",
    "hydraulique": "Panne Hydraulique",
    "def. lubrification": "Défaut Lubrification",
    "defaut lubrification": "Défaut Lubrification",
    "surchauffe": "Surchauffe",
    "vibration anormale": "Vibrations Anormales",
    "vibrations anormales": "Vibrations Anormales",
    "fuite": "Fuite",
    "fuites": "Fuite",
    "defaut capteur": "Défaut Capteur",
    "défaut capteur": "Défaut Capteur",
    "usure normale": "Usure Normale",
}

def normaliser_type_panne(type_panne):
    """Normalise le type de panne"""
    if pd.isna(type_panne):
        return "Non renseigné"

    type_clean = type_panne.lower().strip()
    return dictionnaire_pannes.get(type_clean, type_panne)

df['Type_Panne'] = df['Type_Panne'].apply(normaliser_type_panne)
print(f"✓ Types de pannes normalisés : {df['Type_Panne'].nunique()} catégories")

# 4. Normalisation des noms de techniciens
def normaliser_technicien(nom):
    """Unifie les variations de noms de techniciens"""
    if pd.isna(nom):
        return "Non assigné"

    # Supprimer les abréviations (M., S., etc.)
    nom = nom.replace("M. ", "").replace("S.", "Sophie").replace("A. ", "Alexandre ")
    nom = nom.replace("T.", "Thomas ").replace("N.", "Nicolas ").replace("I. ", "Isabelle ")

    # Normaliser les casses
    if nom.isupper():
        # Si tout en majuscules, supposer que c'est un nom de famille
        noms_complets = {
            "DUPONT": "Martin Dupont",
            "PETIT": "Alexandre Petit",
            "RODRIGUEZ": "Pierre Rodriguez",
            "SIMON": "Marie Simon",
        }
        return noms_complets.get(nom, nom.title())

    if nom.islower():
        return nom.title()

    # Corriger les accents manquants connus
    if "Celine" in nom:
        return "Céline Lefebvre"

    return nom

df['Technicien'] = df['Technicien'].apply(normaliser_technicien)
print(f"✓ Techniciens normalisés : {df['Technicien'].nunique()} techniciens")

# 5. Gérer les valeurs manquantes
df_avant = len(df)
df = df.dropna(subset=['Date', 'ID_Machine', 'Duree_Arret_h'])
print(f"✓ Lignes avec données manquantes critiques supprimées : {df_avant - len(df)}")

# Sauvegarder les données nettoyées
df.to_csv('interventions_2024_clean.csv', index=False, encoding='utf-8')
print(f"\n✓ Données nettoyées sauvegardées : 'interventions_2024_clean.csv'")
print(f"  Lignes conservées : {len(df)}/{df_avant}")

# ==============================================================================
# ÉTAPE 2 : CALCUL DES INDICATEURS PAR MACHINE
# ==============================================================================

print("\n[3/5] Calcul des indicateurs de maintenance...")

# Grouper par machine
stats_machines = df.groupby('ID_Machine').agg({
    'ID_Intervention': 'count',  # Nombre d'interventions
    'Duree_Arret_h': ['sum', 'mean']  # Temps total et moyen
}).reset_index()

stats_machines.columns = ['ID_Machine', 'Nb_Interventions', 'Temps_Arret_Total_h', 'MTTR_h']

# Calcul du MTBF (en jours)
# MTBF = Temps disponible / Nombre de pannes
# Hypothèse : 365 jours disponibles dans l'année
JOURS_ANNEE = 365

stats_machines['MTBF_jours'] = JOURS_ANNEE / stats_machines['Nb_Interventions']

# Trier par temps d'arrêt total décroissant
stats_machines = stats_machines.sort_values('Temps_Arret_Total_h', ascending=False)

# Calculer le pourcentage cumulé
stats_machines['Temps_Cumul_h'] = stats_machines['Temps_Arret_Total_h'].cumsum()
temps_total = stats_machines['Temps_Arret_Total_h'].sum()
stats_machines['Pct_Cumul'] = (stats_machines['Temps_Cumul_h'] / temps_total) * 100

print(f"\n✓ Statistiques calculées pour {len(stats_machines)} machines")
print(f"\nTop 10 des machines les plus critiques :")
print(stats_machines.head(10).to_string(index=False))

# Identifier le seuil 80%
machines_80 = stats_machines[stats_machines['Pct_Cumul'] <= 80]
print(f"\n📊 Analyse de Pareto :")
print(f"   {len(machines_80)} machines représentent 80% du temps d'arrêt total")
print(f"   Soit {len(machines_80)/len(stats_machines)*100:.1f}% du parc")

# Moyennes globales
print(f"\n📈 Indicateurs moyens sur l'ensemble du parc :")
print(f"   MTTR moyen : {stats_machines['MTTR_h'].mean():.2f} heures")
print(f"   MTBF moyen : {stats_machines['MTBF_jours'].mean():.1f} jours")
print(f"   Temps d'arrêt total : {temps_total:.0f} heures")

# Sauvegarder les statistiques
stats_machines.to_csv('statistiques_machines.csv', index=False, encoding='utf-8')
print(f"\n✓ Statistiques sauvegardées : 'statistiques_machines.csv'")

# ==============================================================================
# ÉTAPE 3 : DIAGRAMME DE PARETO
# ==============================================================================

print("\n[4/5] Génération du diagramme de Pareto...")

fig, ax1 = plt.subplots(figsize=(14, 7))

# Barres : temps d'arrêt par machine
x = range(len(stats_machines))
ax1.bar(x, stats_machines['Temps_Arret_Total_h'], color='steelblue', alpha=0.7)
ax1.set_xlabel('Machines (triées par criticité)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Temps d\'arrêt cumulé (heures)', fontsize=12, fontweight='bold', color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')
ax1.set_xticks([])  # Masquer les noms de machines (trop nombreux)

# Courbe : pourcentage cumulé
ax2 = ax1.twinx()
ax2.plot(x, stats_machines['Pct_Cumul'], color='red', marker='o', linewidth=2, markersize=4)
ax2.set_ylabel('Pourcentage cumulé (%)', fontsize=12, fontweight='bold', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(0, 105)

# Ligne des 80%
ax2.axhline(y=80, color='green', linestyle='--', linewidth=2, label='Seuil 80%')
ax2.legend(loc='lower right')

# Titre
plt.title('Diagramme de Pareto - Temps d\'arrêt par machine (2024)',
          fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('pareto_machines.png', dpi=300, bbox_inches='tight')
print(f"✓ Graphique sauvegardé : 'pareto_machines.png'")
plt.close()

# ==============================================================================
# ÉTAPE 4 : ANALYSES COMPLÉMENTAIRES
# ==============================================================================

print("\n[5/5] Analyses complémentaires...")

# Analyse par type de panne
pannes_par_type = df.groupby('Type_Panne').agg({
    'ID_Intervention': 'count',
    'Duree_Arret_h': 'sum'
}).reset_index()
pannes_par_type.columns = ['Type_Panne', 'Nb_Pannes', 'Temps_Total_h']
pannes_par_type = pannes_par_type.sort_values('Temps_Total_h', ascending=False)

print(f"\n📋 Répartition par type de panne :")
print(pannes_par_type.to_string(index=False))

# Visualisation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Camembert : nombre de pannes
ax1.pie(pannes_par_type['Nb_Pannes'], labels=pannes_par_type['Type_Panne'],
        autopct='%1.1f%%', startangle=90)
ax1.set_title('Répartition du nombre de pannes par type', fontweight='bold')

# Barres : temps d'arrêt
ax2.barh(pannes_par_type['Type_Panne'], pannes_par_type['Temps_Total_h'], color='coral')
ax2.set_xlabel('Temps d\'arrêt total (heures)', fontweight='bold')
ax2.set_title('Temps d\'arrêt cumulé par type de panne', fontweight='bold')

plt.tight_layout()
plt.savefig('analyse_types_pannes.png', dpi=300, bbox_inches='tight')
print(f"✓ Graphique sauvegardé : 'analyse_types_pannes.png'")
plt.close()

# ==============================================================================
# ÉTAPE 5 : GÉNÉRATION DU RAPPORT DE SYNTHÈSE
# ==============================================================================

print("\nGénération du rapport de synthèse...')

# Identifier le top 3
top_3 = stats_machines.head(3)

# Estimation du coût (500€/h d'arrêt)
COUT_HEURE_ARRET = 500
cout_total = temps_total * COUT_HEURE_ARRET

rapport = f"""# Rapport d'Analyse GMAO - Année 2024

## Synthèse Exécutive

Analyse réalisée sur **{len(df)} interventions** de maintenance enregistrées en 2024 sur un parc de **{len(stats_machines)} machines**.

**Temps d'arrêt total** : {temps_total:.0f} heures
**Coût estimé** : {cout_total:,.0f} € (base 500€/h)

---

## Indicateurs Clés de Performance

| Indicateur | Valeur | Benchmark Industrie |
|------------|--------|---------------------|
| **MTTR moyen** | {stats_machines['MTTR_h'].mean():.2f} h | 4-6 h (Bon) |
| **MTBF moyen** | {stats_machines['MTBF_jours'].mean():.1f} jours | 45-60 jours (Standard) |
| **Disponibilité estimée** | {(1 - temps_total / (JOURS_ANNEE * 24 * len(stats_machines))) * 100:.2f}% | > 95% (Cible) |

---

## Top 3 des Machines Critiques

### 🔴 1. {top_3.iloc[0]['ID_Machine']}
- **Temps d'arrêt total** : {top_3.iloc[0]['Temps_Arret_Total_h']:.1f} heures ({top_3.iloc[0]['Temps_Arret_Total_h']/temps_total*100:.1f}% du total)
- **Nombre d'interventions** : {top_3.iloc[0]['Nb_Interventions']:.0f}
- **MTTR** : {top_3.iloc[0]['MTTR_h']:.2f} heures
- **MTBF** : {top_3.iloc[0]['MTBF_jours']:.1f} jours
- **Coût estimé** : {top_3.iloc[0]['Temps_Arret_Total_h'] * COUT_HEURE_ARRET:,.0f} €

### 🟠 2. {top_3.iloc[1]['ID_Machine']}
- **Temps d'arrêt total** : {top_3.iloc[1]['Temps_Arret_Total_h']:.1f} heures ({top_3.iloc[1]['Temps_Arret_Total_h']/temps_total*100:.1f}% du total)
- **Nombre d'interventions** : {top_3.iloc[1]['Nb_Interventions']:.0f}
- **MTTR** : {top_3.iloc[1]['MTTR_h']:.2f} heures
- **MTBF** : {top_3.iloc[1]['MTBF_jours']:.1f} jours
- **Coût estimé** : {top_3.iloc[1]['Temps_Arret_Total_h'] * COUT_HEURE_ARRET:,.0f} €

### 🟡 3. {top_3.iloc[2]['ID_Machine']}
- **Temps d'arrêt total** : {top_3.iloc[2]['Temps_Arret_Total_h']:.1f} heures ({top_3.iloc[2]['Temps_Arret_Total_h']/temps_total*100:.1f}% du total)
- **Nombre d'interventions** : {top_3.iloc[2]['Nb_Interventions']:.0f}
- **MTTR** : {top_3.iloc[2]['MTTR_h']:.2f} heures
- **MTBF** : {top_3.iloc[2]['MTBF_jours']:.1f} jours
- **Coût estimé** : {top_3.iloc[2]['Temps_Arret_Total_h'] * COUT_HEURE_ARRET:,.0f} €

---

## Analyse de Pareto

**{len(machines_80)} machines** ({len(machines_80)/len(stats_machines)*100:.0f}% du parc) concentrent **80% du temps d'arrêt total**.

Ce constat valide la loi des 80/20 : un petit nombre de machines génère la majorité des problèmes.

*(Voir graphique : pareto_machines.png)*

---

## Types de Pannes Dominants

| Type de panne | Occurrences | Temps total (h) | % du total |
|---------------|-------------|-----------------|------------|
"""

for _, row in pannes_par_type.head(5).iterrows():
    rapport += f"| {row['Type_Panne']} | {row['Nb_Pannes']:.0f} | {row['Temps_Total_h']:.1f} | {row['Temps_Total_h']/temps_total*100:.1f}% |\n"

rapport += f"""
---

## Recommandations

### 🔧 Court Terme (0-3 mois)

1. **Renforcer la maintenance préventive** sur les {len(machines_80)} machines critiques
   - Réduire les intervalles de contrôle
   - Augmenter la fréquence de lubrification
   - Prévoir des inspections thermographiques

2. **Audit technique** des 3 machines les plus critiques
   - Évaluer l'état réel (usure, vétusté)
   - Identifier les causes racines des pannes répétitives

### 💰 Moyen Terme (3-12 mois)

3. **Investissement de remplacement** pour la machine {top_3.iloc[0]['ID_Machine']}
   - Coût estimé : ~80 000€ (équipement neuf)
   - ROI : < 18 mois au vu du coût actuel des arrêts
   - Alternative : retrofit ou modernisation partielle

4. **Formation des techniciens** :
   - Réduire le MTTR moyen de 10% (cible : {stats_machines['MTTR_h'].mean() * 0.9:.2f}h)
   - Focus sur les pannes récurrentes ({pannes_par_type.iloc[0]['Type_Panne']})

### 📊 Long Terme (1-3 ans)

5. **Déploiement de capteurs IoT** sur les machines critiques
   - Maintenance prédictive via analyse de vibrations, température
   - Anticipation des pannes avant arrêt production

6. **Optimisation du stock de pièces** :
   - Analyser les pièces les plus changées
   - Adapter le stock de sécurité

---

## Gains Attendus

| Action | Gain estimé | Investissement |
|--------|-------------|----------------|
| Maintenance préventive renforcée | -15% temps d'arrêt | 20 k€/an (heures tech) |
| Remplacement machine {top_3.iloc[0]['ID_Machine']} | -{top_3.iloc[0]['Temps_Arret_Total_h']/temps_total*70:.0f}% des arrêts de cette machine | 80 k€ |
| Formation techniciens | -10% MTTR | 15 k€ |
| **Total sur 2025** | **-{temps_total * 0.20:.0f} h d'arrêt évités** | **{(20+80+15):,.0f} k€** |

**ROI estimé** : Économie de {temps_total * 0.20 * COUT_HEURE_ARRET:,.0f} € pour {115:,.0f} k€ investis = **récupération en 6 mois**

---

## Annexes

- `statistiques_machines.csv` : Données détaillées par machine
- `pareto_machines.png` : Diagramme de Pareto
- `analyse_types_pannes.png` : Répartition des types de pannes

---

*Rapport généré automatiquement le {datetime.now().strftime("%d/%m/%Y à %H:%M")}*
"""

# Sauvegarder le rapport
with open('rapport_synthese_gmao_2024.md', 'w', encoding='utf-8') as f:
    f.write(rapport)

print(f"✓ Rapport sauvegardé : 'rapport_synthese_gmao_2024.md'")

print("\n" + "="*60)
print("✅ ANALYSE TERMINÉE AVEC SUCCÈS")
print("="*60)
print("\nFichiers générés :")
print("  - interventions_2024_clean.csv")
print("  - statistiques_machines.csv")
print("  - pareto_machines.png")
print("  - analyse_types_pannes.png")
print("  - rapport_synthese_gmao_2024.md")
print("\nOuvrez 'rapport_synthese_gmao_2024.md' pour consulter la synthèse complète.")
