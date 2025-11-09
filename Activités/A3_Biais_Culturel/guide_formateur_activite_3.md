# Guide Formateur - Activité 3 : Le Biais Culturel et Linguistique

**Objectif Pédagogique :** Démontrer par l'expérience que les LLMs ne sont pas "neutres". Ils reflètent la culture, la langue et les valeurs (souvent occidentales, individualistes) de leur corpus d'entraînement.

**Durée :** 20-30 minutes

**Fichiers à fournir aux stagiaires :**
1.  `1_prompt_generique.bat`
2.  `2_prompt_specifique.bat`
3.  `instructions_apprenant.md`

---

### Le Moteur de l'Activité : Les Prompts de Comparaison

Les stagiaires n'ont pas besoin de voir ces prompts, ils sont cachés dans les fichiers `.bat`.

#### Prompt 1 (Générique)
* **Contenu (dans `1_prompt_generique.bat`) :**
    ```
    (Set "GEMINI_PROMPT=Décris une scène de réussite professionnelle typique en environ 150 mots. Ton style doit être inspirant et universel.")
    ```
* **Objectif :** Obtenir la vision "par défaut" du modèle de ce qu'est la réussite.

#### Prompt 2 (Spécifique)
* **Contenu (dans `2_prompt_specifique.bat`) :**
    ```
    (Set "GEMINI_PROMPT=Décris une scène de réussite professionnelle selon une perspective rurale ou axée sur la communauté (par opposition à une réussite individuelle en entreprise). Rédige environ 150 mots.")
    ```
* **Objectif :** Forcer le modèle à changer son "angle culturel" et à activer un autre ensemble de valeurs.

---

### Déroulé pour le Formateur

1.  **Mise en place (5 min) :**
    * Expliquez l'activité : "Nous allons maintenant explorer la 'personnalité' de l'IA. Nous allons lui poser une question sur un concept universel, la réussite, de deux manières différentes. Votre mission est d'être des analystes culturels."
2.  **Phase 1 - Générique (10 min) :**
    * Les stagiaires lancent `1_prompt_generique.bat`.
    * Ils lisent `sortie_generique.txt` en binômes.
    * Animer la discussion sur ce premier texte.
3.  **Phase 2 - Spécifique (10 min) :**
    * Les stagiaires lancent `2_prompt_specifique.bat`.
    * Ils lisent `sortie_specifique.txt` et le comparent au premier texte.
    * Animer la discussion comparative.

### Clés pour le Débriefing Collectif

**Analyse du Texte 1 (Générique) :**
* *Attendu :* Une scène de promotion individuelle, un bonus financier, un grand bureau ("corner office"), le fait de "battre" la concurrence, la reconnaissance par un supérieur.
* **Questions à poser :**
    * "Quelles valeurs voyez-vous ici ?" (Individualisme, compétition, argent, hiérarchie).
    * "De quelle culture ces marqueurs de réussite vous semblent-ils les plus proches ?" (Occidentale, "corporate" américaine).
    * "Est-ce que cela représente la *seule* forme de réussite professionnelle ?"

**Analyse du Texte 2 (Spécifique) et Comparaison :**
* *Attendu :* Une scène de réussite d'une récolte, la pérennité de l'exploitation familiale, la reconnaissance par les pairs (la communauté), la fierté du travail bien fait, l'équilibre de vie.
* **Questions à poser :**
    * "Quelles sont les valeurs dans ce second texte ?" (Collectif, durabilité, savoir-faire, équilibre).
    * "Pourquoi l'IA n'a-t-elle pas proposé cela la première fois ?" (Parce que le prompt "typique" active les schémas les plus fréquents dans son corpus, qui est majoritairement américain).

### Message Clé

> **L’IA n’est pas neutre : elle parle avec la voix du monde qui l’a formée.**
>
> Ce n'est pas un "bug", c'est une caractéristique fondamentale. Elle reflète la culture dominante de ses données d'entraînement.
>
> **Notre rôle, en tant que professionnels et ingénieurs, n'est pas de subir ce biais, mais de le savoir et de le corriger.** Nous devons lui injecter notre propre diversité intellectuelle, notre culture d'entreprise, et nos valeurs (ex: sécurité, collectif, qualité long terme) par des prompts précis, des rôles et du contexte (RAG).