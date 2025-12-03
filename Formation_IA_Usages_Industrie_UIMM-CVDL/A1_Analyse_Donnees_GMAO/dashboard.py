import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re

# Page config
st.set_page_config(page_title="Rapport Maintenance GMAO", layout="wide")

st.title("📊 Rapport de Synthèse Maintenance 2024")

# --- DATA LOADING & CLEANING ---

def parse_duration(duration_str):
    """
    Parses duration strings in various formats:
    - "11.75" (float)
    - "29h45" (hours and minutes)
    - "9:00" (hours:minutes)
    - "0 hours 45 min" (text)
    Returns duration in hours (float).
    """
    if pd.isna(duration_str) or duration_str == '' or duration_str == '-':
        return 0.0
    
    duration_str = str(duration_str).strip().lower().replace(',', '.')
    
    try:
        # Format: Float (e.g., "11.75")
        return float(duration_str)
    except ValueError:
        pass

    # Format: "29h45" or "1h15"
    match_h = re.match(r'(\d+)h(\d*)', duration_str)
    if match_h:
        hours = float(match_h.group(1))
        minutes = float(match_h.group(2)) if match_h.group(2) else 0
        return hours + minutes / 60.0

    # Format: "9:00"
    match_colon = re.match(r'(\d+):(\d+)', duration_str)
    if match_colon:
        hours = float(match_colon.group(1))
        minutes = float(match_colon.group(2))
        return hours + minutes / 60.0

    # Format: "0 hours 45 min" or "13 hours 45 min"
    match_text = re.search(r'(\d+)\s*heure[s]?\s*(\d*)\s*min', duration_str)
    if match_text:
        hours = float(match_text.group(1))
        minutes = float(match_text.group(2)) if match_text.group(2) else 0
        return hours + minutes / 60.0
        
    # Format: "45 min" (without hours)
    match_min = re.search(r'(\d+)\s*min', duration_str)
    if match_min:
         return float(match_min.group(1)) / 60.0

    return 0.0

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    
    # 1. Clean Dates
    # Handle mixed formats like "2024-09-04", "26-01-2024", "03.02.2024"
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    
    # 2. Clean Durations
    df['Duree_Arret_h_Clean'] = df['Duree_Arret_h'].apply(parse_duration)
    
    # 3. Clean Failure Types
    df['Type_Panne'] = df['Type_Panne'].fillna('Inconnu').str.title().str.strip()
    
    return df

FILE_PATH = "interventions_2024.csv"

try:
    df = load_data(FILE_PATH)
    st.success(f"Données chargées avec succès : {len(df)} interventions.")
except FileNotFoundError:
    st.error(f"Fichier non trouvé : {FILE_PATH}")
    st.stop()

# Show raw data (optional, expandable)
with st.expander("Voir les données brutes (5 premières lignes)"):
    st.dataframe(df.head())

# --- METRICS CALCULATION ---

# Group by Machine
machine_stats = df.groupby('ID_Machine').agg(
    Nombre_Interventions=('ID_Intervention', 'count'),
    Temps_Arret_Total=('Duree_Arret_h_Clean', 'sum')
).reset_index()

# Constants
HOURS_IN_YEAR = 365 * 24

# Calculate MTTR (Mean Time To Repair) -> Average downtime per intervention
machine_stats['MTTR (h)'] = machine_stats['Temps_Arret_Total'] / machine_stats['Nombre_Interventions']

# Calculate MTBF (Mean Time Between Failures)
# Formula: (Total Time - Total Downtime) / Number of Failures
# Result in Days for readability (as requested)
machine_stats['MTBF (jours)'] = ((HOURS_IN_YEAR - machine_stats['Temps_Arret_Total']) / machine_stats['Nombre_Interventions']) / 24

# Sort by Total Downtime (Descending)
machine_stats = machine_stats.sort_values(by='Temps_Arret_Total', ascending=False)

# --- DASHBOARD LAYOUT ---

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🏆 Top 10 Machines les plus critiques (Temps d'arrêt)")
    top_10 = machine_stats.head(10)
    st.dataframe(top_10.style.format({
        'Temps_Arret_Total': '{:.2f}',
        'MTTR (h)': '{:.2f}',
        'MTBF (jours)': '{:.2f}'
    }))

with col2:
    st.subheader("📈 Indicateurs Globaux")
    total_downtime = machine_stats['Temps_Arret_Total'].sum()
    total_interventions = machine_stats['Nombre_Interventions'].sum()
    avg_mttr = total_downtime / total_interventions
    
    st.metric("Temps d'arrêt total (h)", f"{total_downtime:.2f}")
    st.metric("Nombre d'interventions", f"{total_interventions}")
    st.metric("MTTR Moyen Global (h)", f"{avg_mttr:.2f}")

# --- PARETO ANALYSIS ---

st.markdown("---")
st.subheader("📊 Analyse de Pareto : Règle des 80/20")

# Calculate cumulative percentage
machine_stats['Cum_Downtime'] = machine_stats['Temps_Arret_Total'].cumsum()
total_downtime_all = machine_stats['Temps_Arret_Total'].sum()
machine_stats['Cum_Percent'] = (machine_stats['Cum_Downtime'] / total_downtime_all) * 100

# Create Pareto Chart
fig = go.Figure()

# Bar chart (Downtime)
fig.add_trace(go.Bar(
    x=machine_stats['ID_Machine'],
    y=machine_stats['Temps_Arret_Total'],
    name='Temps d\'arrêt (h)',
    marker_color='indianred'
))

# Line chart (Cumulative %)
fig.add_trace(go.Scatter(
    x=machine_stats['ID_Machine'],
    y=machine_stats['Cum_Percent'],
    name='Pourcentage Cumulé (%)',
    yaxis='y2',
    mode='lines+markers',
    marker_color='blue'
))

# 80% Line
fig.add_shape(
    type="line",
    x0=0,
    y0=80,
    x1=len(machine_stats),
    y1=80,
    yref="y2",
    line=dict(color="green", width=2, dash="dash"),
)

fig.update_layout(
    title='Pareto des Temps d\'Arrêt par Machine',
    xaxis_title='Machine',
    yaxis=dict(title='Temps d\'arrêt (h)'),
    yaxis2=dict(
        title='Pourcentage Cumulé (%)',
        overlaying='y',
        side='right',
        range=[0, 105]
    ),
    legend=dict(x=0.8, y=1.1)
)

st.plotly_chart(fig, use_container_width=True)

# --- INSIGHTS ---

# Identify machines contributing to 80% of downtime
critical_machines = machine_stats[machine_stats['Cum_Percent'] <= 80]
num_critical = len(critical_machines)
total_machines = len(machine_stats)
percent_critical = (num_critical / total_machines) * 100

st.info(f"💡 **Insight** : {num_critical} machines (soit {percent_critical:.1f}% du parc) représentent environ 80% du temps d'arrêt total.")

# Failure types for critical machines
st.subheader("🔍 Types de pannes fréquents sur les machines critiques")
critical_ids = critical_machines['ID_Machine'].tolist()
critical_data = df[df['ID_Machine'].isin(critical_ids)]

failure_counts = critical_data['Type_Panne'].value_counts().reset_index()
failure_counts.columns = ['Type de Panne', 'Nombre']

fig_pie = px.pie(failure_counts, values='Nombre', names='Type de Panne', title='Répartition des pannes sur les machines critiques')
st.plotly_chart(fig_pie)
