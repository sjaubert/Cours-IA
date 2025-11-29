import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(
    page_title="Analyse des Robots Industriels",
    page_icon="🤖",
    layout="wide"
)

# Titre principal
st.title("🤖 Analyse des Installations de Robots Industriels (2011-2023)")
st.markdown("""
Cette application présente une analyse interactive des données de l'International Federation of Robotics (IFR) 
concernant les installations annuelles de robots industriels.
""")

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("annual-industrial-robots-installed.csv")
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Le fichier 'annual-industrial-robots-installed.csv' est introuvable. Veuillez vérifier qu'il est dans le même dossier.")
    st.stop()

# Sidebar pour les filtres
st.sidebar.header("Filtres")

# Filtre Année
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
selected_years = st.sidebar.slider(
    "Sélectionnez la période",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Filtre Pays (Top 5 par défaut)
all_countries = sorted(df[df['Entity'] != 'World']['Entity'].unique())
default_countries = ['China', 'Germany', 'Japan', 'South Korea', 'United States']
# S'assurer que les pays par défaut sont dans la liste
default_countries = [c for c in default_countries if c in all_countries]

selected_countries = st.sidebar.multiselect(
    "Sélectionnez les pays",
    options=all_countries,
    default=default_countries
)

# Filtrage des données
df_filtered = df[
    (df['Year'] >= selected_years[0]) & 
    (df['Year'] <= selected_years[1])
]

# --- Section 1: Évolution Mondiale ---
st.header("1. Évolution Mondiale")
st.markdown("L'installation de robots industriels dans le monde a connu une croissance soutenue.")

df_world = df_filtered[df_filtered['Entity'] == 'World']

if not df_world.empty:
    fig_world = px.line(
        df_world, 
        x='Year', 
        y='Annual industrial robots installed',
        markers=True,
        title="Installations annuelles de robots dans le monde"
    )
    fig_world.update_layout(yaxis_title="Nombre de robots")
    st.plotly_chart(fig_world, use_container_width=True)
    
    st.info(f"""
    **Observation** : On observe une tendance haussière. 
    En {max_year}, le nombre d'installations a atteint {df_world[df_world['Year'] == max_year]['Annual industrial robots installed'].values[0]:,.0f}.
    """)
else:
    st.warning("Pas de données mondiales pour la période sélectionnée.")

# --- Section 2: Comparaison par Pays ---
st.header("2. Comparaison par Pays")
st.markdown("Comparaison de l'évolution des installations pour les pays sélectionnés.")

df_countries = df_filtered[df_filtered['Entity'].isin(selected_countries)]

if not df_countries.empty:
    fig_countries = px.line(
        df_countries,
        x='Year',
        y='Annual industrial robots installed',
        color='Entity',
        markers=True,
        title="Installations annuelles par pays"
    )
    fig_countries.update_layout(yaxis_title="Nombre de robots")
    st.plotly_chart(fig_countries, use_container_width=True)
    
    st.markdown("""
    *   **La Chine** montre généralement une croissance exponentielle.
    *   **Les autres pays** (Japon, Corée du Sud, USA, Allemagne) montrent une croissance plus modérée.
    """)
else:
    st.warning("Veuillez sélectionner au moins un pays.")

# --- Section 3: Parts de Marché Cumulées ---
st.header("3. Parts de Marché Cumulées")
st.markdown("Visualisation du volume total et de la part de chaque pays sélectionné.")

if not df_countries.empty:
    fig_area = px.area(
        df_countries,
        x='Year',
        y='Annual industrial robots installed',
        color='Entity',
        title="Évolution cumulée des installations (Aires empilées)"
    )
    fig_area.update_layout(yaxis_title="Nombre de robots (Cumulé)")
    st.plotly_chart(fig_area, use_container_width=True)
    
    st.markdown("Ce graphique permet de visualiser la dominance croissante de certains acteurs comme la Chine.")

# --- Section 4: Situation en 2023 (ou dernière année sélectionnée) ---
last_year = selected_years[1]
st.header(f"4. Situation en {last_year}")

df_last_year = df[
    (df['Year'] == last_year) & 
    (df['Entity'].isin(selected_countries))
].sort_values(by='Annual industrial robots installed', ascending=False)

if not df_last_year.empty:
    fig_bar = px.bar(
        df_last_year,
        x='Entity',
        y='Annual industrial robots installed',
        color='Entity',
        text='Annual industrial robots installed',
        title=f"Installations de robots en {last_year}"
    )
    fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig_bar.update_layout(yaxis_title="Nombre de robots", showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)
    
    top_country = df_last_year.iloc[0]
    st.success(f"**Leader en {last_year}** : {top_country['Entity']} avec {top_country['Annual industrial robots installed']:,} installations.")

# --- Conclusion ---
st.header("Conclusion")
st.markdown("""
L'analyse des données montre que la **Chine** est devenue un acteur incontournable de la robotisation industrielle, 
dépassant largement les autres puissances historiques.
""")

# Footer
st.markdown("---")
st.caption("Source des données : International Federation of Robotics (IFR) via AI Index Report (2025).")
