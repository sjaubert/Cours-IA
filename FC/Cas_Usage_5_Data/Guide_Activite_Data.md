# Guide d'Activité : Codage & Analyse de Données (Code Interpreter)

## Contexte du Scénario
Vous êtes assistant commercial. Votre manager vous envoie un fichier Excel "brut" contenant les ventes du mois de janvier. Il vous demande une analyse rapide pour la réunion de demain.
Problème : Le fichier est "sale" (erreurs de saisie, formats de dates mélangés, doublons) et vous ne maîtrisez pas Python.
Heureusement, vous avez l'IA avec son module "Code Interpreter" (ou Analyse de Données Avancée).

## Objectifs Pédagogiques
*   Utiliser l'IA pour nettoyer un jeu de données sans écrire de code.
*   Comprendre comment l'IA écrit et exécute du Python pour analyser des données.
*   Générer des visualisations (graphiques) interactives ou statiques.

---

## Partie 1 : Instructions pour l'Apprenant

### Étape 1 : Audit et Nettoyage des Données
1.  Ouvrez votre interface de chat avec l'IA (assurez-vous que le mode "Code Interpreter" ou upload de fichier est actif).
2.  Uploadez le fichier `Ventes_2024_Brut.csv`.
3.  **Prompt suggéré** :
    > "Agis comme un Data Analyst expert. Analyse ce fichier CSV. Identifie toutes les anomalies (valeurs manquantes, doublons, formats de dates incohérents, fautes de frappe). Ensuite, nettoie le fichier et dis-moi ce que tu as corrigé."

### Étape 2 : Analyse Exploratoire
1.  Demandez des statistiques descriptives.
2.  **Prompt suggéré** :
    > "Maintenant que le fichier est propre, fais-moi une analyse des ventes.
    > 1. Quel est le chiffre d'affaires total ?
    > 2. Quel est le produit le plus vendu (en volume et en valeur) ?
    > 3. Qui est le meilleur vendeur ?"

### Étape 3 : Visualisation (Data Viz)
1.  Demandez des graphiques.
2.  **Prompt suggéré** :
    > "Génère deux graphiques pour illustrer ces résultats :
    > 1. Un diagramme en barres (Bar chart) des ventes par Vendeur.
    > 2. Une courbe d'évolution (Line chart) des ventes jour par jour sur le mois de janvier.
    > Affiche les graphiques ici."

---

## Partie 2 : Guide pour le Formateur (Solutions)

### Les "Pièges" du fichier (Ce que l'IA doit corriger)
*   **Dates** : Mélange de formats `DD/MM/YYYY` et `YYYY-MM-DD`. L'IA doit tout standardiser.
*   **Typos** : "Laptpo Pro" au lieu de "Laptop Pro". Si non corrigé, cela crée deux catégories de produits faussant les stats.
*   **Doublons** : La ligne du "07/01/2024" (Casque Audio) apparaît deux fois.
*   **Valeurs manquantes** : Il manque le montant pour une vente de Sophie (05/01) et le nom du vendeur pour une vente de Pierre (18/01). L'IA doit proposer une stratégie (supprimer la ligne ou imputer une valeur).

### Point de vigilance
*   **Vérification du code** : Si possible, montrez aux apprenants qu'ils peuvent cliquer sur "Voir le code" (selon l'outil) pour voir le script Python généré par l'IA. C'est une preuve de transparence.
*   **Hallucination vs Calcul** : Expliquez que contrairement à un LLM classique qui "devine" le mot suivant, ici l'IA "calcule" vraiment via Python. Le risque d'hallucination sur les chiffres est quasi nul, mais le risque d'erreur de logique dans le code existe.
