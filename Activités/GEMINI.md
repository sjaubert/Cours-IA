# Contexte du Projet : Activités Pédagogiques sur l'IA

Ce répertoire contient une série d'activités pédagogiques conçues pour explorer les caractéristiques, les biais et les capacités des modèles de langage (LLMs) comme Gemini. Chaque dossier `A*` représente une activité autonome avec ses propres instructions et scripts.

## Objectif Général

L'objectif de ces activités est de former les participants à interagir avec l'IA de manière lucide et critique. Les exercices sont conçus pour révéler des aspects fondamentaux des LLMs, tels que :

*   La génération de contenu plausible mais potentiellement inexact.
*   La sensibilité au contexte et au "biais de confirmation".
*   Les biais culturels inhérents aux données d'entraînement.
*   La différence entre le raisonnement sémantique humain et la prédiction statistique de l'IA.
*   L'utilisation de l'IA pour des tâches d'analyse et de synthèse de données.

## Structure du Répertoire

*   `A0_organisation_documents/` : Contient des scripts pour générer des fichiers d'exemple, probablement pour une activité de tri ou de classification.
*   `A1_illusion_vérité/` : Une activité pour démontrer que l'IA peut générer des textes très crédibles qui contiennent des erreurs factuelles.
*   `A2_Biais_Confirmation/` : Une activité montrant comment l'IA peut être amenée à argumenter des points de vue opposés en fonction du contexte fourni.
*   `A3_Biais_Culturel/` : Une activité qui illustre comment les LLMs reflètent les biais culturels de leurs données d'entraînement.
*   `A4_Illusion_raisonnement/` : Une activité conçue pour montrer que l'IA ne "raisonne" pas au sens humain, mais effectue des corrélations statistiques.
*   `A5_IA_Rédactrice_de_rapports/` : Une activité pratique sur l'utilisation de l'IA pour analyser des données (un fichier CSV de logs de maintenance) et générer un rapport de synthèse.

## Utilisation

Chaque activité est conçue pour être lancée via les scripts `.bat` qu'elle contient. Les instructions pour les participants se trouvent généralement dans un fichier `instructions_apprenant.md` et des guides pour le formateur peuvent être présents (`guide_formateur_*.md`).

Les interactions avec l'IA se font via la CLI Gemini, en utilisant les prompts et les contextes définis dans les fichiers de chaque activité.
