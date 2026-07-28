![Logo UIMM](../logo_uimm_placeholder.jpg)

**Pôle Formation UIMM - CVDL**
*Formateur : S. JAUBERT*

---

# Guide : décrire le rendu Streamlit à un LLM

Couper court aux 3 allers-retours de mise en page.

Le LLM connaît l'API, pas le **rendu**. Donnez-lui le rendu dans le prompt.

---

## 1. Décrivez la grille, pas seulement les composants

Au lieu de « mets ça en colonnes », précisez la structure :

> Layout en 3 zones : sidebar (filtres : bloc, voie, période) ;
> bande de 4 `st.metric` en haut (`st.columns(4)`) ;
> dessous, `st.columns([2, 1])` avec un `st.line_chart` à gauche et un
> `st.dataframe` à droite.

---

## 2. Donnez les contraintes de densité

- « 4 colonnes max, sinon chaque bloc devient illisible »
- « pas plus de 3 filtres dans la sidebar »
- « détails secondaires dans un `st.expander` replié »

---

## 3. Nommez les pièges de rendu connus

- `st.columns` ne s'imbrique qu'à un niveau : pas de colonnes dans des colonnes profondes.
- Widgets dupliqués : exiger une `key` unique pour chaque widget.
- `use_container_width=True` pour que graphiques et tableaux remplissent la zone.
- Un `st.metric` par colonne, sinon ils s'empilent.

---

## 4. Fournissez une maquette ASCII

Une grille texte vaut mieux qu'un paragraphe :

```
+----------+-------------------------------+
| SIDEBAR  |  [KPI][KPI][KPI][KPI]         |
| - bloc   |  +-------------+-----------+   |
| - voie   |  |  line_chart | dataframe |   |
| - période|  +-------------+-----------+   |
+----------+-------------------------------+
```

---

## 5. Imposez le squelette attendu

> Structure le code ainsi : `st.set_page_config(layout="wide")`, puis une
> fonction par section, sidebar pour les filtres, et chaque widget avec une `key`.

---

## Prompt-modèle réutilisable

> Construis un dashboard Streamlit. Layout `wide`. Sidebar : [filtres].
> Haut : `st.columns(N)` de `st.metric` pour [KPIs]. Corps : `st.columns([…])`
> avec [graphique] et [tableau], tous en `use_container_width=True`.
> Détails dans des `st.expander` repliés. Une `key` unique par widget.
> Contraintes : max 4 colonnes, max 3 filtres sidebar. Voici la maquette ASCII : […].

---

**Astuce** : gardez l'app cheatsheet ouverte à côté du LLM. Quand le rendu vous
déplaît, retrouvez le composant adéquat et nommez-le explicitement dans le prompt.

---

**Pôle Formation UIMM - CVDL** | *Formateur : S. JAUBERT*
