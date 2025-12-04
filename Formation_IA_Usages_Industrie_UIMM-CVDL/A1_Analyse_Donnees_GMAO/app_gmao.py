import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

# Configuration de la page
st.set_page_config(page_title="Analyse GMAO 2024", layout="wide")

st.title("📊 Tableau de Bord Analyse GMAO 2024")
st.markdown("Analyse des interventions de maintenance et aide à la décision.")

# --- FONCTIONS DE NETTOYAGE ---

def clean_duration(val):
    """Nettoie et convertit la durée en heures (float)."""
    if pd.isna(val) or val == '' or val == '-':
        return np.nan
    
    val = str(val).strip().lower()
    val = val.replace(',', '.')
    
    # Cas "33.0.25" -> "33.25" (typo spécifique)
    if re.match(r'^\d+\.0\.\d+$', val):
        parts = val.split('.')
        return float(f"{parts[0]}.{parts[2]}")

    # Cas "41h45", "13 heures 30 min"
    if 'h' in val or 'heure' in val:
        val = val.replace('heures', 'h').replace('heure', 'h').replace('min', '').strip()
        parts = val.split('h')
        hours = float(parts[0]) if parts[0] else 0
        minutes = float(parts[1]) if len(parts) > 1 and parts[1] else 0
        return hours + minutes / 60.0
    
    # Cas "9:45"
    if ':' in val:
        parts = val.split(':')
        return float(parts[0]) + float(parts[1]) / 60.0
    
    try:
        return float(val)
    except ValueError:
        return np.nan

def clean_technician(name):
    """Normalise les noms des techniciens."""
    if pd.isna(name) or name in ['-', 'N/A', 'Aucune', '']:
        return "Non Spécifié"
    
    name = str(name).strip().title()
    
    # Mapping des alias connus
    mapping = {
        "M. Dupont": "Martin Dupont",
        "A. Petit": "Alexandre Petit",
        "S.Bernard": "Sophie Bernard",
        "I. Garcia": "Isabelle Garcia",
        "T.Laurent": "Thomas Laurent",
        "N.Michel": "Nicolas Michel",
        "Rodriguez": "Pierre Rodriguez" # Assumption based on other entries
    }
    
    return mapping.get(name, name)

def clean_failure_type(val):
    """Normalise les types de panne."""
    if pd.isna(val):
        return "Non Spécifié"
    val = str(val).strip().title()
    val = val.replace('Mecanique', 'Mécanique').replace('Electrique', 'Électrique').replace('Def.', 'Défaut')
    return val

@st.cache_data
def load_data():
    file_path = "interventions_2024.csv"
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"Fichier {file_path} introuvable. Veuillez générer les données d'abord.")
        return pd.DataFrame()

    # 1. Nettoyage des Dates
    # On essaie de convertir avec dayfirst=True pour gérer le format DD/MM/YYYY prédominant en France
    # errors='coerce' va transformer les formats inconnus en NaT
    df['Date_Clean'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    
    # 2. Nettoyage des Durées
    df['Duree_Heures'] = df['Duree_Arret_h'].apply(clean_duration)
    
    # 3. Nettoyage Techniciens
    df['Technicien_Clean'] = df['Technicien'].apply(clean_technician)
    
    # 4. Nettoyage Types de Panne
    df['Type_Panne_Clean'] = df['Type_Panne'].apply(clean_failure_type)
    
    # Suppression des lignes avec Date ou Durée invalides pour l'analyse
    df_clean = df.dropna(subset=['Date_Clean', 'Duree_Heures'])
    
    return df_clean

# --- CHARGEMENT DES DONNÉES ---
df = load_data()

if df.empty:
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filtres")

# Filtre Date
min_date = df['Date_Clean'].min()
max_date = df['Date_Clean'].max()
date_range = st.sidebar.date_input(
    "Plage de dates",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filtre Machine
machines = sorted(df['ID_Machine'].unique())
selected_machines = st.sidebar.multiselect("ID Machine", machines, default=machines)

# Filtre Type de Panne
pannes = sorted(df['Type_Panne_Clean'].unique())
selected_pannes = st.sidebar.multiselect("Type de Panne", pannes, default=pannes)

# Filtre Technicien
techs = sorted(df['Technicien_Clean'].unique())
selected_techs = st.sidebar.multiselect("Technicien", techs, default=techs)

# --- APPLICATION DES FILTRES ---
mask = (
    (df['Date_Clean'].dt.date >= date_range[0]) &
    (df['Date_Clean'].dt.date <= date_range[1]) &
    (df['ID_Machine'].isin(selected_machines)) &
    (df['Type_Panne_Clean'].isin(selected_pannes)) &
    (df['Technicien_Clean'].isin(selected_techs))
)
df_filtered = df[mask]

st.markdown(f"**{len(df_filtered)}** interventions affichées sur {len(df)} totales.")

# --- KPI ---
col1, col2, col3, col4 = st.columns(4)
total_arret = df_filtered['Duree_Heures'].sum()
cout_horaire = 500
cout_total = total_arret * cout_horaire
mttr = df_filtered['Duree_Heures'].mean()

col1.metric("Nombre d'Interventions", len(df_filtered))
col2.metric("Temps d'Arrêt Total", f"{total_arret:.1f} h")
col3.metric("Coût Estimé (500€/h)", f"{cout_total:,.0f} €")
col4.metric("MTTR Moyen", f"{mttr:.2f} h")

st.markdown("---")

# --- GRAPHIQUES ---

col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("Pareto des Machines (Temps d'Arrêt)")
    # Group by Machine and sum duration
    machine_stats = df_filtered.groupby('ID_Machine')['Duree_Heures'].sum().sort_values(ascending=False)
    
    # Pareto calculation
    pareto_df = pd.DataFrame({'Duree': machine_stats})
    pareto_df['Cumul'] = pareto_df['Duree'].cumsum()
    pareto_df['Pourcentage_Cumul'] = 100 * pareto_df['Cumul'] / pareto_df['Duree'].sum()
    
    # Plot
    fig, ax1 = plt.subplots()
    ax1.bar(pareto_df.index, pareto_df['Duree'], color='C0')
    ax1.set_ylabel("Temps d'arrêt (h)", color='C0')
    ax1.tick_params(axis='y', labelcolor='C0')
    plt.xticks(rotation=45, ha='right')
    
    ax2 = ax1.twinx()
    ax2.plot(pareto_df.index, pareto_df['Pourcentage_Cumul'], color='C1', marker='o', ms=4)
    ax2.set_ylabel("Pourcentage Cumulé (%)", color='C1')
    ax2.tick_params(axis='y', labelcolor='C1')
    ax2.axhline(80, color='r', linestyle='--', alpha=0.5)
    
    st.pyplot(fig)

with col_g2:
    st.subheader("Répartition par Type de Panne")
    panne_counts = df_filtered['Type_Panne_Clean'].value_counts()
    st.bar_chart(panne_counts)

# --- ANALYSE TECHNICIENS ---
st.subheader("Performance Techniciens")
tech_stats = df_filtered.groupby('Technicien_Clean').agg(
    Interventions=('ID_Intervention', 'count'),
    Duree_Totale=('Duree_Heures', 'sum'),
    Duree_Moyenne=('Duree_Heures', 'mean')
).sort_values('Interventions', ascending=False)
st.dataframe(tech_stats)

# --- DONNÉES BRUTES ---
with st.expander("Voir les données brutes filtrées"):
    st.dataframe(df_filtered[['ID_Intervention', 'Date', 'ID_Machine', 'Type_Panne', 'Duree_Arret_h', 'Technicien', 'Pieces_Changees', 'Duree_Heures', 'Type_Panne_Clean', 'Technicien_Clean']])
