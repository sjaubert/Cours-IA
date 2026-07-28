"""
Cheatsheet Streamlit visuelle — auto-démo.

But : voir la TÊTE réelle de chaque composant Streamlit (le rendu),
pas seulement son API. Chaque composant est rendu en vrai, avec son
code juste en dessous.

Lancement :
    streamlit run cheatsheet_app.py

Auteur : assistant BTS ATI — Pole Formation UIMM CVDL
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, time
from pathlib import Path

st.set_page_config(
    page_title="Cheatsheet Streamlit visuelle",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def demo(name, code, render, note=""):
    """Affiche un composant rendu en vrai + son code juste en dessous.

    name   : nom affiché (ex. "st.columns")
    code   : snippet montré dans le bloc de code
    render : fonction sans argument qui exécute le rendu live
    note   : courte indication sur le rendu / l'usage
    """
    with st.container(border=True):
        st.markdown(f"**`{name}`**" + (f"  —  {note}" if note else ""))
        try:
            render()
        except Exception as exc:  # garde-fou : dépendance absente, etc.
            st.info(f"Rendu indisponible ici : {exc}")
        st.code(code, language="python")


@st.cache_data
def sample_df():
    rng = np.random.default_rng(42)
    return pd.DataFrame(
        {
            "Poste": [f"P{i}" for i in range(1, 9)],
            "TRS": rng.integers(60, 95, 8),
            "Rebuts": rng.integers(0, 12, 8),
            "Dispo": rng.random(8).round(2),
        }
    )


@st.cache_data
def chart_df():
    rng = np.random.default_rng(7)
    return pd.DataFrame(rng.standard_normal((20, 3)).cumsum(axis=0),
                        columns=["Ligne A", "Ligne B", "Ligne C"])


# --------------------------------------------------------------------------- #
# Sections
# --------------------------------------------------------------------------- #
def page_intro():
    st.title("Cheatsheet Streamlit visuelle")
    st.caption(
        "Voir le rendu réel de chaque composant — pas seulement son API. "
        "Naviguez par catégorie dans la barre latérale."
    )
    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Catégories", "9")
    c2.metric("Composants démontrés", "70+")
    c3.metric("Version Streamlit", st.__version__)
    st.divider()
    st.markdown(
        """
        **Comment l'utiliser**

        - Chaque encadré rend le composant *en vrai*, avec son code juste en dessous.
        - Comparez visuellement les variantes (3 vs 4 colonnes, `gap`, `border`, `expander`).
        - Page **Guide prompt LLM** : comment décrire ce rendu à un LLM pour éviter
          les allers-retours de mise en page.
        """
    )


def page_layout():
    st.header("Mise en page & conteneurs")
    st.caption("Le coeur des allers-retours : voir l'impact réel de chaque structure.")

    def r_cols3():
        a, b, c = st.columns(3)
        a.metric("TRS", "78 %")
        b.metric("Dispo", "0.92")
        c.metric("Rebuts", "4")
    demo("st.columns(3)",
         'a, b, c = st.columns(3)\na.metric("TRS", "78 %")\nb.metric("Dispo", "0.92")\nc.metric("Rebuts", "4")',
         r_cols3, "3 colonnes égales : aéré, lisible pour des KPIs")

    def r_cols4():
        cols = st.columns(4)
        for i, col in enumerate(cols, 1):
            col.metric(f"Poste {i}", f"{70 + i*4} %")
    demo("st.columns(4)",
         'cols = st.columns(4)\nfor i, col in enumerate(cols, 1):\n    col.metric(f"Poste {i}", f"{70 + i*4} %")',
         r_cols4, "4 colonnes : plus dense, chaque bloc rétrécit")

    def r_cols_ratio():
        left, right = st.columns([3, 1])
        left.write("Zone principale (poids 3)")
        right.button("Action", key="ratio_btn")
    demo("st.columns([3, 1])",
         'left, right = st.columns([3, 1])\nleft.write("Zone principale (poids 3)")\nright.button("Action")',
         r_cols_ratio, "Ratios : largeurs proportionnelles (3 fois plus large)")

    def r_cols_gap():
        a, b, c = st.columns(3, gap="large", vertical_alignment="center")
        a.button("A", key="g_a")
        b.button("B plus haut\n\net multiligne", key="g_b")
        c.button("C", key="g_c")
    demo("st.columns(..., gap, vertical_alignment)",
         'a, b, c = st.columns(3, gap="large", vertical_alignment="center")',
         r_cols_gap, "gap='large' espace ; vertical_alignment aligne en hauteur")

    def r_tabs():
        t1, t2, t3 = st.tabs(["Mesure", "Analyse", "Contrôle"])
        t1.write("Contenu onglet Mesure")
        t2.write("Contenu onglet Analyse")
        t3.write("Contenu onglet Contrôle")
    demo("st.tabs",
         't1, t2, t3 = st.tabs(["Mesure", "Analyse", "Contrôle"])\nt1.write("Contenu onglet Mesure")',
         r_tabs, "Onglets horizontaux : un seul visible à la fois")

    def r_expander():
        with st.expander("Voir le détail du calcul TRS", expanded=False):
            st.write("TRS = Disponibilité × Performance × Qualité")
            st.latex(r"TRS = D \times P \times Q")
    demo("st.expander",
         'with st.expander("Voir le détail", expanded=False):\n    st.write("...")',
         r_expander, "Replié par défaut : cache le détail, déplie au clic")

    def r_container():
        with st.container(border=True):
            st.write("Bloc encadré (border=True)")
            st.write("Regroupe visuellement des éléments")
    demo("st.container(border=True)",
         'with st.container(border=True):\n    st.write("Bloc encadré")',
         r_container, "Cadre léger pour regrouper sans onglet ni expander")

    def r_container_scroll():
        with st.container(height=140, border=True):
            for i in range(12):
                st.write(f"Ligne {i+1} — contenu défilant")
    demo("st.container(height=140)",
         'with st.container(height=140, border=True):\n    for i in range(12):\n        st.write(f"Ligne {i+1}")',
         r_container_scroll, "height fixe : zone scrollable interne")

    def r_popover():
        with st.popover("Ouvrir le filtre"):
            st.checkbox("Inclure FC", key="pop_fc")
            st.checkbox("Inclure apprentissage", key="pop_app")
    demo("st.popover",
         'with st.popover("Ouvrir le filtre"):\n    st.checkbox("Inclure FC")',
         r_popover, "Bouton qui ouvre un petit panneau flottant au clic")

    def r_form():
        with st.form("demo_form"):
            st.text_input("Nom du poste", key="form_nom")
            st.slider("Cadence", 0, 100, 50, key="form_cad")
            st.form_submit_button("Valider")
    demo("st.form + st.form_submit_button",
         'with st.form("f"):\n    st.text_input("Nom")\n    st.form_submit_button("Valider")',
         r_form, "Regroupe des saisies : exécution seulement à la validation")

    st.subheader("Barre latérale (sidebar)")
    st.info(
        "La barre latérale de gauche **est** un `st.sidebar`. "
        "Tout `st.sidebar.xxx` ou `with st.sidebar:` s'y range. "
        "Règle d'or : navigation + filtres globaux uniquement, sinon elle se surcharge."
    )
    st.code(
        'with st.sidebar:\n    st.radio("Page", [...])\n    st.selectbox("Atelier", [...])',
        language="python",
    )


def page_text():
    st.header("Texte & écriture")

    demo("st.title / header / subheader",
         'st.title("Titre")\nst.header("En-tête")\nst.subheader("Sous-titre")',
         lambda: (st.title("Titre"), st.header("En-tête"), st.subheader("Sous-titre")),
         "Hiérarchie de titres : tailles décroissantes")

    demo("st.markdown",
         'st.markdown("**Gras**, *italique*, `code`, [lien](https://streamlit.io)")',
         lambda: st.markdown("**Gras**, *italique*, `code`, [lien](https://streamlit.io)"),
         "Markdown complet")

    demo("st.write",
         'st.write("Texte", 42, {"clé": "valeur"})',
         lambda: st.write("Texte", 42, {"clé": "valeur"}),
         "Couteau suisse : s'adapte au type passé")

    demo("st.caption",
         'st.caption("Légende discrète, gris clair")',
         lambda: st.caption("Légende discrète, gris clair"),
         "Petit texte secondaire")

    demo("st.code",
         'st.code("for i in range(3):\\n    print(i)", language="python")',
         lambda: st.code("for i in range(3):\n    print(i)", language="python"),
         "Bloc de code avec coloration + bouton copier")

    demo("st.latex",
         r'st.latex(r"\sigma = \sqrt{\frac{1}{n}\sum (x_i-\bar x)^2}")',
         lambda: st.latex(r"\sigma = \sqrt{\frac{1}{n}\sum (x_i-\bar x)^2}"),
         "Formule mathématique (utile MSP / écart-type)")

    demo("st.divider",
         'st.divider()',
         lambda: (st.write("Avant"), st.divider(), st.write("Après")),
         "Trait de séparation horizontal")

    def r_badge():
        st.markdown(":blue-badge[Lean] :green-badge[Validé] :red-badge[Bloquant]")
    demo("badges Markdown (:color-badge[...])",
         'st.markdown(":blue-badge[Lean] :green-badge[Validé]")',
         r_badge, "Étiquettes colorées inline (Streamlit récent)")


def page_widgets():
    st.header("Widgets de saisie")

    demo("st.button",
         'st.button("Lancer l\'analyse")',
         lambda: st.button("Lancer l'analyse", key="w_btn"),
         "Bouton standard, renvoie True le run où on clique")

    demo("st.download_button",
         'st.download_button("Télécharger CSV", data="a,b\\n1,2", file_name="x.csv")',
         lambda: st.download_button("Télécharger CSV", data="a,b\n1,2",
                                    file_name="x.csv", key="w_dl"),
         "Déclenche un téléchargement de fichier")

    demo("st.link_button",
         'st.link_button("Doc Streamlit", "https://docs.streamlit.io")',
         lambda: st.link_button("Doc Streamlit", "https://docs.streamlit.io"),
         "Bouton qui ouvre une URL")

    demo("st.checkbox / st.toggle",
         'st.checkbox("Inclure FC")\nst.toggle("Mode sombre")',
         lambda: (st.checkbox("Inclure FC", key="w_cb"),
                  st.toggle("Mode sombre", key="w_tg")),
         "Case à cocher vs interrupteur (même logique booléenne)")

    demo("st.radio",
         'st.radio("Voie", ["Apprentissage", "FC"], horizontal=True)',
         lambda: st.radio("Voie", ["Apprentissage", "FC"], horizontal=True, key="w_radio"),
         "Choix unique exclusif ; horizontal=True pour gagner de la hauteur")

    demo("st.selectbox",
         'st.selectbox("Bloc", ["BC01", "BC02", "BC03"])',
         lambda: st.selectbox("Bloc", ["BC01", "BC02", "BC03"], key="w_sel"),
         "Menu déroulant, choix unique")

    demo("st.multiselect",
         'st.multiselect("Capacités", ["C1", "C2", "C3", "C4"])',
         lambda: st.multiselect("Capacités", ["C1", "C2", "C3", "C4"], key="w_multi"),
         "Choix multiple sous forme d'étiquettes")

    demo("st.slider",
         'st.slider("Cadence", 0, 100, 50)',
         lambda: st.slider("Cadence", 0, 100, 50, key="w_slider"),
         "Curseur numérique")

    demo("st.select_slider",
         'st.select_slider("Gravité", ["Faible", "Moyenne", "Élevée"])',
         lambda: st.select_slider("Gravité", options=["Faible", "Moyenne", "Élevée"], key="w_ssl"),
         "Curseur sur valeurs discrètes / textuelles")

    demo("st.text_input / st.text_area",
         'st.text_input("Référence")\nst.text_area("Commentaire")',
         lambda: (st.text_input("Référence", key="w_ti"),
                  st.text_area("Commentaire", key="w_ta")),
         "Saisie courte vs multiligne")

    demo("st.number_input",
         'st.number_input("Effectif", min_value=0, max_value=30, value=12)',
         lambda: st.number_input("Effectif", min_value=0, max_value=30, value=12, key="w_num"),
         "Saisie numérique avec +/-")

    demo("st.date_input / st.time_input",
         'st.date_input("Date", value=date.today())\nst.time_input("Heure", time(8, 30))',
         lambda: (st.date_input("Date", value=date.today(), key="w_date"),
                  st.time_input("Heure", value=time(8, 30), key="w_time")),
         "Sélecteurs date et heure")

    demo("st.color_picker",
         'st.color_picker("Couleur thème", "#0E5AA7")',
         lambda: st.color_picker("Couleur thème", "#0E5AA7", key="w_color"),
         "Pastille ouvrant un nuancier")

    demo("st.file_uploader",
         'st.file_uploader("Importer un CSV", type=["csv"])',
         lambda: st.file_uploader("Importer un CSV", type=["csv"], key="w_file"),
         "Zone de dépôt / parcourir un fichier")

    # Widgets récents (guardés)
    def r_pills():
        st.pills("Outils Lean", ["5S", "SMED", "Kanban", "Kaizen"],
                 selection_mode="multi", key="w_pills")
    demo("st.pills (récent)",
         'st.pills("Outils Lean", ["5S","SMED","Kanban"], selection_mode="multi")',
         r_pills, "Étiquettes cliquables ; alternative compacte au multiselect")

    def r_seg():
        st.segmented_control("Vue", ["Jour", "Semaine", "Mois"], key="w_seg")
    demo("st.segmented_control (récent)",
         'st.segmented_control("Vue", ["Jour", "Semaine", "Mois"])',
         r_seg, "Boutons segmentés type interrupteur multi-position")

    def r_feedback():
        st.feedback("stars", key="w_feedback")
    demo("st.feedback (récent)",
         'st.feedback("stars")  # ou "thumbs"',
         r_feedback, "Notation par étoiles ou pouce")


def page_data():
    st.header("Données & tableaux")
    df = sample_df()

    demo("st.dataframe",
         'st.dataframe(df, use_container_width=True)',
         lambda: st.dataframe(df, use_container_width=True),
         "Tableau interactif : tri par colonne, redimensionnable")

    demo("st.dataframe + column_config",
         'st.dataframe(df, column_config={\n'
         '  "TRS": st.column_config.ProgressColumn("TRS", min_value=0, max_value=100)})',
         lambda: st.dataframe(
             df,
             column_config={
                 "TRS": st.column_config.ProgressColumn("TRS", format="%d %%",
                                                        min_value=0, max_value=100),
                 "Dispo": st.column_config.NumberColumn("Dispo", format="%.2f"),
             },
             use_container_width=True,
         ),
         "column_config : barres de progression, formats, etc.")

    demo("st.data_editor",
         'st.data_editor(df, num_rows="dynamic")',
         lambda: st.data_editor(df, num_rows="dynamic", key="d_editor",
                                use_container_width=True),
         "Tableau ÉDITABLE : l'utilisateur modifie les cellules")

    demo("st.table",
         'st.table(df.head(3))',
         lambda: st.table(df.head(3)),
         "Tableau statique (pas d'interaction, tout affiché)")

    demo("st.metric",
         'st.metric("TRS ligne 1", "78 %", delta="+3 %")',
         lambda: st.metric("TRS ligne 1", "78 %", delta="+3 %"),
         "KPI avec valeur + variation colorée")

    demo("st.json",
         'st.json({"bloc": "BC01", "capacites": ["C1", "C2"]})',
         lambda: st.json({"bloc": "BC01", "capacites": ["C1", "C2"]}),
         "Affichage JSON repliable")


def page_charts():
    st.header("Graphiques")
    df = chart_df()

    demo("st.line_chart",
         'st.line_chart(df)',
         lambda: st.line_chart(df), "Courbes (natif, rapide)")

    demo("st.area_chart",
         'st.area_chart(df)',
         lambda: st.area_chart(df), "Aires empilées")

    demo("st.bar_chart",
         'st.bar_chart(df)',
         lambda: st.bar_chart(df), "Barres (natif)")

    demo("st.scatter_chart",
         'st.scatter_chart(df, x="Ligne A", y="Ligne B")',
         lambda: st.scatter_chart(df, x="Ligne A", y="Ligne B"), "Nuage de points")

    def r_map():
        rng = np.random.default_rng(1)
        pts = pd.DataFrame(rng.standard_normal((100, 2)) / [50, 50] + [47.9, 1.9],
                           columns=["lat", "lon"])
        st.map(pts)
    demo("st.map",
         'st.map(df_latlon)  # colonnes lat / lon',
         r_map, "Carte avec points géolocalisés")

    def r_altair():
        import altair as alt
        long = df.reset_index().melt("index", var_name="Ligne", value_name="Valeur")
        chart = alt.Chart(long).mark_line().encode(
            x="index", y="Valeur", color="Ligne")
        st.altair_chart(chart, use_container_width=True)
    demo("st.altair_chart",
         'chart = alt.Chart(df).mark_line().encode(...)\nst.altair_chart(chart)',
         r_altair, "Altair (livré avec Streamlit) : contrôle fin")

    st.info(
        "Graphiques optionnels (dépendances séparées) : "
        "`st.plotly_chart` (plotly), `st.pyplot` (matplotlib), "
        "`st.graphviz_chart` (graphviz), `st.pydeck_chart` (cartes 3D)."
    )


def page_media():
    st.header("Média")

    demo("st.image",
         'st.image("https://placehold.co/600x200?text=Image", caption="Légende")',
         lambda: st.image("https://placehold.co/600x200?text=Streamlit",
                          caption="Légende", use_container_width=True),
         "Image depuis URL, chemin local ou tableau numpy")

    st.info(
        "`st.audio(bytes/url)` et `st.video(url)` affichent un lecteur intégré. "
        "`st.logo(image)` place un logo en haut de la sidebar (branding UIMM, par ex.)."
    )
    st.code(
        'st.audio("son.mp3")\nst.video("https://...mp4")\nst.logo("logo_uimm.jpg")',
        language="python",
    )

    demo("st.camera_input",
         'st.camera_input("Prendre une photo")',
         lambda: st.camera_input("Prendre une photo", key="cam"),
         "Capture via webcam (demande l'autorisation navigateur)")


def page_status():
    st.header("Statut, feedback & flux")

    def r_alerts():
        st.success("Succès : opération validée")
        st.info("Info : pensez à enregistrer")
        st.warning("Attention : plafond U7 à 100 h")
        st.error("Erreur : champ manquant")
    demo("st.success / info / warning / error",
         'st.success("...")\nst.info("...")\nst.warning("...")\nst.error("...")',
         r_alerts, "Bandeaux colorés selon la gravité")

    def r_progress():
        st.progress(0.65, text="Avancement 65 %")
    demo("st.progress",
         'st.progress(0.65, text="Avancement 65 %")',
         r_progress, "Barre de progression")

    def r_status():
        with st.status("Traitement en cours...", expanded=True) as s:
            st.write("Étape 1 : lecture")
            st.write("Étape 2 : calcul")
            s.update(label="Terminé", state="complete")
    demo("st.status",
         'with st.status("Traitement...") as s:\n    st.write("Étape 1")\n    s.update(state="complete")',
         r_status, "Conteneur de progression multi-étapes repliable")

    def r_toast_balloons():
        if st.button("Déclencher toast + ballons", key="st_toast"):
            st.toast("Notification éphémère !", icon=":material/check_circle:")
            st.balloons()
    demo("st.toast / st.balloons / st.snow",
         'st.toast("Message", icon=":material/check_circle:")\nst.balloons()\nst.snow()',
         r_toast_balloons, "Notifications et animations ponctuelles")

    def r_spinner():
        st.write("`with st.spinner(...)` affiche un loader pendant un calcul long.")
    demo("st.spinner",
         'with st.spinner("Calcul en cours..."):\n    long_task()',
         r_spinner, "Indicateur d'attente pendant un bloc de code")


def page_chat():
    st.header("Chat & IA")
    st.caption("Briques pour une interface conversationnelle.")

    def r_chat():
        with st.chat_message("user"):
            st.write("Quel est le TRS cible ?")
        with st.chat_message("assistant"):
            st.write("La cible usuelle est 85 % en production de série.")
    demo("st.chat_message",
         'with st.chat_message("user"):\n    st.write("...")\nwith st.chat_message("assistant"):\n    st.write("...")',
         r_chat, "Bulles de conversation avec avatar rôle")

    st.info(
        "`st.chat_input('Votre message')` ancre une barre de saisie en bas de page. "
        "`st.write_stream(generator)` affiche une réponse token par token (effet machine à écrire)."
    )
    st.code(
        'prompt = st.chat_input("Votre message")\nst.write_stream(reponse_streamee())',
        language="python",
    )


def page_guide():
    """Rend le guide depuis GUIDE_PROMPT_LLM.md (source unique)."""
    from pathlib import Path

    guide_path = Path(__file__).with_name("GUIDE_PROMPT_LLM.md")
    try:
        st.markdown(guide_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        st.warning(f"Fichier introuvable : {guide_path.name}")


# --------------------------------------------------------------------------- #
# Navigation
# --------------------------------------------------------------------------- #
PAGES = {
    "Introduction": page_intro,
    "Mise en page & conteneurs": page_layout,
    "Texte & écriture": page_text,
    "Widgets de saisie": page_widgets,
    "Données & tableaux": page_data,
    "Graphiques": page_charts,
    "Média": page_media,
    "Statut & flux": page_status,
    "Chat & IA": page_chat,
    "Guide prompt LLM": page_guide,
}

logo_path = Path(__file__).parent.parent / "logo_uimm_placeholder.jpg"

with st.sidebar:
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
    st.markdown("**Pôle Formation UIMM - CVDL**")
    st.markdown("*Formateur : S. JAUBERT*")
    st.divider()
    st.title("Cheatsheet Streamlit")
    st.caption("Voir le rendu, pas seulement l'API")
    choix = st.radio("Catégorie", list(PAGES.keys()), label_visibility="collapsed")
    st.divider()
    st.caption(f"Streamlit {st.__version__}")

PAGES[choix]()

st.divider()
st.caption("Pôle Formation UIMM - CVDL | Formateur : S. JAUBERT")
