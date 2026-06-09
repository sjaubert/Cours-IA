![Logo UIMM](../logo_uimm_placeholder.jpg)

**Pôle Formation UIMM - CVDL**
*Formateur : S. JAUBERT*

---

# Cheatsheet Streamlit visuelle

Voir la **tête réelle** de chaque composant Streamlit (le rendu), pas seulement son API.
Chaque composant est rendu en vrai, avec son code juste en dessous.

## Pourquoi

Un LLM connaît l'API (`st.columns` existe) mais pas le rendu (3 colonnes vs 4,
un `expander` ouvert, une sidebar surchargée). Cette app sert de **référence visuelle**
à garder ouverte à côté du LLM, et le **guide de prompt** cadre vos demandes pour
éviter les allers-retours de mise en page.

## Installation

```bash
cd streamlit_cheatsheet
pip install -r requirements.txt
```

## Lancement

```bash
streamlit run cheatsheet_app.py
```

L'app s'ouvre dans le navigateur (http://localhost:8501). Naviguez par catégorie
dans la barre latérale.

## Contenu (10 pages)

| Page | Couverture |
|------|------------|
| Introduction | Vue d'ensemble, version Streamlit détectée |
| Mise en page & conteneurs | columns (3/4/ratios/gap), tabs, expander, container scrollable, popover, form, sidebar |
| Texte & écriture | title/header, markdown, write, caption, code, latex, divider, badges |
| Widgets de saisie | button, checkbox, toggle, radio, selectbox, multiselect, slider, date/time, color, file, pills, segmented_control, feedback |
| Données & tableaux | dataframe, column_config, data_editor, table, metric, json |
| Graphiques | line/area/bar/scatter, map, altair |
| Média | image, audio, video, logo, camera_input |
| Statut & flux | alertes, progress, status, toast, balloons, spinner |
| Chat & IA | chat_message, chat_input, write_stream |
| Guide prompt LLM | rend `GUIDE_PROMPT_LLM.md` : méthode pour décrire le rendu à un LLM + prompt-modèle |

Le guide est aussi disponible en fichier autonome [`GUIDE_PROMPT_LLM.md`](GUIDE_PROMPT_LLM.md)
(à coller directement dans vos prompts). L'app et le fichier partagent la même source.

## Notes

- Les composants récents (`st.pills`, `st.segmented_control`, `st.feedback`) exigent
  une version Streamlit récente. S'ils manquent, l'encadré affiche un message au lieu
  de planter (garde-fou `try/except`).
- Graphiques optionnels (`plotly`, `matplotlib`, `graphviz`, `pydeck`) non requis :
  ajoutez les paquets correspondants si besoin.

---

**Pôle Formation UIMM - CVDL** | *Formateur : S. JAUBERT*
