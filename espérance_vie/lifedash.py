import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page en mode large
st.set_page_config(layout="wide")

# Titre principal de l'application
st.title("Explorateur d'Espérance de Vie")

# Barre latérale avec les instructions
with st.sidebar:
    st.header("Instructions")
    st.write("""
    Cette application vous permet d'explorer les données sur l'espérance de vie à la naissance à travers le monde et le temps.

    1.  **Sélectionnez les entités :** Choisissez un ou plusieurs pays, groupes de pays ou zones géographiques dans le menu déroulant.
    2.  **Choisissez une période :** Utilisez le curseur pour définir l'intervalle d'années que vous souhaitez visualiser.
    3.  **Mode d'affichage :**
        *   **Regroupé :** Affiche toutes les courbes sur un seul graphique pour comparer facilement les tendances.
        *   **Individuel :** Affiche un graphique distinct pour chaque entité sélectionnée.
    """)

# Fonction pour charger et mettre en cache les données
@st.cache_data
def load_data():
    """Charge, nettoie et prépare les données sur l'espérance de vie."""
    try:
        df = pd.read_csv("Long-run life expectancy at birth - Sheet1.csv")
        # Renommer les colonnes pour une manipulation plus aisée
        df.rename(columns={
            "country": "Country",
            "year": "Year",
            "life_expectancy_at_birth": "LifeExpectancy"
        }, inplace=True)
        # Supprimer les lignes avec des données manquantes pour la visualisation
        df.dropna(subset=["Country", "Year", "LifeExpectancy"], inplace=True)
        return df
    except FileNotFoundError:
        # Affiche un message d'erreur si le fichier n'est pas trouvé
        st.error("Fichier de données 'Long-run life expectancy at birth - Sheet1.csv' introuvable.")
        st.info("Veuillez vous assurer que le fichier CSV se trouve dans le même répertoire que l'application.")
        return pd.DataFrame() # Retourne un DataFrame vide pour éviter d'autres erreurs

# Chargement des données
data = load_data()

# Ne poursuit que si les données ont été chargées avec succès
if not data.empty:
    # Création des contrôles dans la fenêtre principale
    
    # Obtenir la liste unique des pays/entités
    entity_list = sorted(data["Country"].unique())
    
    # Zones géographiques présélectionnées
    default_selections = ["World", "Americas", "Asia", "Europe"]
    
    # Contrôle de sélection multiple pour les pays/entités
    selected_entities = st.multiselect(
        "Choisissez les pays, groupes de pays ou zones géographiques :",
        options=entity_list,
        default=default_selections
    )

    # Obtenir les années min et max pour le curseur
    min_year, max_year = int(data["Year"].min()), int(data["Year"].max())
    
    # Contrôle de curseur pour la période
    selected_years = st.slider(
        "Sélectionnez une période :",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    # Contrôle radio pour le mode d'affichage
    display_mode = st.radio(
        "Choisissez le mode d'affichage :",
        options=["Regroupé", "Individuel"],
        horizontal=True
    )

    # Filtrage des données en fonction des sélections de l'utilisateur
    if selected_entities:
        filtered_data = data[
            (data["Country"].isin(selected_entities)) &
            (data["Year"] >= selected_years[0]) &
            (data["Year"] <= selected_years[1])
        ]

        st.markdown("---") # Ligne de séparation

        if not filtered_data.empty:
            # Logique d'affichage des graphiques
            if display_mode == "Regroupé":
                st.subheader("Graphique regroupé")
                fig = px.line(
                    filtered_data,
                    x="Year",
                    y="LifeExpectancy",
                    color="Country",
                    title="Évolution de l'espérance de vie",
                    labels={"Year": "Année", "LifeExpectancy": "Espérance de vie (années)", "Country": "Entité"}
                )
                fig.update_layout(legend_title_text='Entités sélectionnées')
                st.plotly_chart(fig, use_container_width=True)

            elif display_mode == "Individuel":
                st.subheader("Graphiques individuels")
                
                # Définir le nombre de colonnes
                max_cols = 4
                
                # Créer une grille de colonnes
                cols = st.columns(max_cols)
                
                # Itérer sur chaque entité sélectionnée pour créer un graphique
                for i, entity in enumerate(selected_entities):
                    entity_data = filtered_data[filtered_data["Country"] == entity]
                    
                    if not entity_data.empty:
                        # Placer chaque graphique dans une colonne
                        with cols[i % max_cols]:
                            fig = px.line(
                                entity_data,
                                x="Year",
                                y="LifeExpectancy",
                                title=entity,
                                labels={"Year": "Année", "LifeExpectancy": "Espérance de vie"}
                            )
                            # Masquer la légende pour les graphiques individuels pour plus de clarté
                            fig.update_layout(showlegend=False)
                            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Aucune donnée disponible pour les sélections actuelles.")
    else:
        st.info("Veuillez sélectionner au moins une entité pour afficher les données.")
