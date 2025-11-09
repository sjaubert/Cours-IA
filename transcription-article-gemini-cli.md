# Optimisation de la Création de Contenu : Un Guide pour Utiliser Gemini CLI, le Serveur MCP et VSCode

## Résumé
Ce guide explore un flux de travail puissant pour générer des articles et d'autres contenus en intégrant Gemini CLI, un serveur MCP (Model Context Protocol), et Visual Studio Code (VSCode). Découvrez comment tirer parti de cette combinaison pour une création, modification et distribution de contenu efficaces et contextuelles, avec des exemples pratiques et des prompts.

## Introduction
L'intégration de Gemini CLI avec Visual Studio Code (VSCode) crée un environnement hautement efficace et contextuel pour les développeurs comme pour les rédacteurs. Cette configuration permet à Gemini CLI, alimenté par l'IA, d'accéder à l'espace de travail de VSCode, le rendant conscient des fichiers ouverts et du texte sélectionné pour fournir des suggestions pertinentes et ciblées. Une fonctionnalité clé est la comparaison (diffing) native dans l'éditeur, qui permet une révision et une modification côte à côte des changements générés par l'IA avant leur acceptation, offrant un plus grand contrôle sur le résultat final.

Lorsqu'un serveur MCP est ajouté à cet environnement, les capacités s'étendent bien au-delà de la simple génération de texte. Le serveur MCP agit comme un pont, permettant à l'agent IA d'interagir avec des outils externes et des sources de données, telles que des bases de données, des API ou des logiciels de gestion de projet, directement depuis la ligne de commande. Cela transforme la configuration en un puissant flux de travail agentique où Gemini CLI peut non seulement suggérer du contenu, mais aussi exécuter des tâches concrètes comme lancer des tests, créer des tickets (issues) ou récupérer des données en direct.

La polyvalence de cet environnement intégré a des implications significatives au-delà du codage. Les mêmes fonctionnalités qui rationalisent le développement de logiciels peuvent être appliquées avec force à la création d'articles et de documents de recherche. Par exemple, la capacité de Gemini CLI à comprendre des informations complexes peut être utilisée pour expliquer des concepts complexes pour un article technique. Sa capacité de génération de contenu, ancrée par les résultats web en temps réel de la recherche Google, peut aider à rédiger des sections, à résumer des recherches et à surmonter le syndrome de la page blanche. Cet article explorera l'application pratique de la combinaison de Gemini CLI, VSCode et d'un serveur MCP pour révolutionner le processus d'écriture et de recherche.

## Configuration
1.  **Installer VSCode**
    Vous pouvez trouver la documentation officielle et les instructions d'installation sur [https://code.visualstudio.com](https://code.visualstudio.com).

2.  **Intégrer Gemini CLI avec VSCode**
    Pour des instructions détaillées sur la configuration de Gemini CLI avec VSCode, veuillez vous référer à l'article de blog officiel : [Gemini CLI + VS Code: Native diffing, context-aware workflows, and more](https://developers.googleblog.com/en/gemini-cli-vs-code-native-diffing-context-aware-workflows/).

3.  **Installer le serveur MCP**
    Cet article utilise un serveur MCP spécifique. Pour les instructions complètes de configuration et d'utilisation, veuillez vous référer au dépôt : [ToolsForMCPServer - Usage](https://github.com/tanaikech/ToolsForMCPServer?tab=readme-ov-file#usage).

## Applications Pratiques
Pour tester les scénarios suivants, veuillez ouvrir VSCode et le terminal intégré, puis exécutez Gemini CLI dans le terminal.

### 1. Générer un Article à Partir de Zéro
Vous pouvez générer un article complet sur un sujet donné en fournissant un prompt structuré.

**Prompt :**
*(Note : Le prompt est conservé en anglais car il s'agit d'une entrée directe pour l'outil.)*
```
The goal is to create an article on automation using Google Apps Script.

## Article Rules
1. The article's structure must include a Title, Abstract, Introduction, Discussion, Summary, and References.
2. For the References section, include the titles and the authors of the examples you find.
3. Include relevant, generated images to illustrate concepts. Add thumbnail links to the suitable position of the article in markdown format. Get the thumbnail link of the file on Google Drive using a tool, publicly_share_file_on_google_drive.

## Article Creation Steps
To create the article, follow these steps while adhering to the above rules:
1. Conduct Google searches to understand Google Apps Script.
2. Use Google searches to find real-world examples of automation using Google Apps Script. These examples can also include combinations with generative AI, such as Gemini, and AI agents like the Gemini CLI.
3. Suggest three new scenarios for automation using Google Apps Script. For each scenario, include both the advantages and disadvantages.
4. Write the article in Markdown format.
5. Save the article to a markdown file named `@sampleText1.md`.
```
En exécutant ce prompt, Gemini CLI effectuera les recherches nécessaires et générera l'article.

Le processus utilisera les outils suivants :
*   `Google Search`
*   `generate_image_on_google_drive` (depuis le serveur MCP)
*   `publicly_share_file_on_google_drive` (depuis le serveur MCP)

Le fichier Markdown généré sera sauvegardé dans votre espace de travail.

### 2. Modifier un Article Existant
Gemini CLI peut également être utilisé pour éditer et affiner des articles existants.

**Prompt :**
*(Note : Le prompt est conservé en anglais.)*
```
Here, the previously generated article is modified within VSCode.

Your mission is as follows.
1. Read and understand an article of @sampleText1.md
2. Summarize the abstract section within 30 words.
3. Replace it.
```
Les modifications peuvent être examinées en utilisant la vue "diff" dans VSCode avant de les accepter.

### 3. Demander des Retours par E-mail
Vous pouvez automatiser le processus de partage de votre article et de demande de retours.

**Prompt :**
*(Note : Le prompt est conservé en anglais.)*
```
Send the article as an email.

The goal and mission are as follows.

## Goal
Request the feedback on the generated article of @sampleText1.md to Tanaike (tanaike @hotmail.com) using email.

## Mission
1. Convert @sampleText1.md to Google Docs.
2. Convert Google Docs to PDF.
3. Create the email body by considering the goal.
4. Send an email with the email body by attaching the PDF file to Tanaike.
```
Ce processus utilise les outils suivants du serveur MCP :
*   `create_google_docs_from_markdown_on_google_drive`
*   `convert_mimetype_of_file_on_google_drive`
*   `auto_new_draft_creation_Gmail`
*   `send_mails_Gmail`

L'e-mail suivant sera envoyé avec l'article en pièce jointe PDF :

> Cher Tanaike,
>
> J'espère que vous allez bien.
>
> J'ai récemment rédigé un article intitulé "Libérer l'Efficacité : L'Automatisation avec Google Apps Script" et j'apprécierais grandement vos précieux retours à ce sujet. Votre expertise en Google Apps Script est très respectée, et vos éclairages seraient incroyablement utiles pour affiner ce travail.
>
> J'ai joint l'article au format PDF pour votre commodité.
>
> N'hésitez pas à me faire savoir si vous avez des questions ou si vous avez besoin de plus d'informations.
>
> Merci pour votre temps et votre considération.
>
> Cordialement,

Pour les prompts fréquemment utilisés comme celui-ci, vous pouvez les sauvegarder pour une réutilisation facile.

### 4. Créer une Présentation à Partir d'un Article
Transformez votre article en présentation avec un simple prompt.

**Prompt :**
*(Note : Le prompt est conservé en anglais.)*
```
Your mission is as follows.
1. Convert @sampleText1.md to Google Docs.
2. Create a presentation with Google Slides using the converted Google Docs as the description of the presentation. The author's name is Tanaike. The presentation title matches the title of the Markdown file. The presentation time is 5 minutes.
```
Les outils suivants du serveur MCP sont utilisés :
*   `create_google_docs_from_markdown_on_google_drive`
*   `generate_presentation_with_google_slides`

La présentation résultante sera créée dans votre Google Slides.

Les articles générés, convertis en Google Docs et Google Slides, peuvent également être automatiquement soumis à un site public en développant un outil sur le serveur MCP.

### 5. Créer des Graphiques à Partir de Données
Si vous avez des points de données, vous pouvez facilement créer des graphiques.

**Prompt :**
*(Note : Le prompt est conservé en anglais.)*
```
Your mission is as follows.
1. Create a new Google Spreadsheet.
2. Put the following CSV data into the 1st sheet on the Google Spreadsheet.
<csvData>
head1,head2
-1.00,0.01
-0.97,0.01
-0.93,0.02
-0.90,0.03
-0.87,0.03
-0.83,0.04
-0.80,0.06
-0.77,0.07
-0.73,0.09
-0.70,0.11
-0.67,0.14
-0.63,0.16
-0.60,0.20
-0.57,0.24
-0.53,0.28
-0.50,0.32
-0.47,0.38
-0.43,0.43
-0.40,0.49
-0.37,0.55
-0.33,0.61
-0.30,0.67
-0.27,0.73
-0.23,0.78
-0.20,0.84
-0.17,0.88
-0.13,0.92
-0.10,0.96
-0.07,0.98
-0.03,1.00
0.00,1.00
0.03,1.00
0.07,0.98
0.10,0.96
0.13,0.92
0.17,0.88
0.20,0.84
0.23,0.78
0.27,0.73
0.30,0.67
0.33,0.61
0.37,0.55
0.40,0.49
0.43,0.43
0.47,0.38
0.50,0.32
0.53,0.28
0.57,0.24
0.60,0.20
0.63,0.16
0.67,0.14
0.70,0.11
0.73,0.09
0.77,0.07
0.80,0.06
0.83,0.04
0.87,0.03
0.90,0.03
0.93,0.02
0.97,0.01
1.00,0.01
</csvData>
3. Create a line chart in the same sheet as the data sheet using the inserted data. In this case, the sheet ID is 0. Don't create the chart in another sheet.
```
Cette tâche utilise les outils suivants du serveur MCP :
*   `create_file_to_google_drive`
*   `put_values_to_google_sheets`
*   `explanation_create_chart_by_google_sheets_api`
*   `create_chart_on_google_sheets`

Pour utiliser ce graphique dans un document Google, vous pouvez utiliser le prompt suivant :

**Prompt :**
*(Note : Le prompt est conservé en anglais.)*
```
Your mission is as follows.
1. A sample chart of normal distribution is in the Google Spreadsheet (Spreadsheet ID is `{spreadsheetId}`). Convert the chart as an image file.
2. Create the text for understanding the normal distribution by including the chart.
3. Create the text as a Google Document.
```
Les outils du serveur MCP utilisés sont :
*   `get_charts_on_google_sheets`
*   `create_charts_as_image_on_google_sheets`
*   `GoogleSearch`
*   `create_file_to_google_drive`
*   `create_document_body_in_google_docs`

Le document Google résultant inclura le graphique et une explication.

### 6. Générer des Graphiques à Partir d'Images
Que faire si vous n'avez qu'une image d'un graphique et non les données sous-jacentes ? Bien sûr, l'image du graphique peut être directement utilisée avec l'article et le document.

Comme autre approche, on considère la méthode de détection des points de données à partir de l'image du graphique en utilisant l'IA générative. Voici quelques exemples.

**Cas 1**
L'image du graphique d'exemple provient de la Fig. 4 de cet article.

**Prompt :**
*(Note : Le prompt est conservé en anglais.)*
```
This goal is to duplicate a chart created as an image to a chart on Google Sheets. To achieve this goal, your mission is as follows.
1. Carefully understand the image chart @sampleChart1.png and detect accurately all data points in the chart by confirming the x-axis and y-axis. To correctly duplicate the image chart using the data, a large number of data points is required, and also, the gaps between each data point do not need to be the same.
2. Show the retrieved data in the console as a table.
3. Create a new Google Spreadsheet and put the data into 1st sheet of the Spreadsheet.
4. Create a chart with the data in the same sheet as the data in Google Sheets using the batchUpdate method of the Sheets API.
```
Les outils suivants du serveur MCP sont utilisés :
*   `create_file_to_google_drive`
*   `put_values_to_google_sheets`
*   `explanation_create_chart_by_google_sheets_api`
*   `manage_google_sheets_using_sheets_api` (Dans certains cas, l'outil `create_chart_on_google_sheets` peut également être utilisé).

**Cas 2**
L'image du graphique d'exemple provient de la Fig. 3 de cet article.

**Prompt :**
*(Note : Le prompt est conservé en anglais.)*
```
This goal is to duplicate a chart created as an image to a chart on Google Sheets. To achieve this goal, your mission is as follows.
1. Carefully understand the image chart @sampleChart2.png and detect accurately all data points in the chart by confirming the x-axis and y-axis. To correctly duplicate the image chart using the data, a large number of data points is required, and also, the gaps between each data point do not need to be the same.
2. Show the retrieved data in the console as a table.
3. Create a new Google Spreadsheet and put the data into 1st sheet of the Spreadsheet.
4. Create a chart with the data in the same sheet as the data in Google Sheets using the batchUpdate method of the Sheets API.
```
Les outils suivants du serveur MCP sont utilisés :
*   `create_file_to_google_drive`
*   `put_values_to_google_sheets`
*   `explanation_create_chart_by_google_sheets_api`
*   `manage_google_sheets_using_sheets_api` (Dans certains cas, l'outil `create_chart_on_google_sheets` peut également être utilisé).

Dans ce cas, les points de données détectés n'étaient pas parfaitement identiques à l'image du graphique original. On pense qu'avec l'affinement des prompts et les futures mises à jour de Gemini, des résultats plus précis pourront être obtenus.

## Résumé
Ce guide a démontré un flux de travail complet pour la création et la gestion de contenu en utilisant une combinaison d'outils puissants. Voici les points clés à retenir :

*   **Environnement Intégré** : La combinaison de Gemini CLI, VSCode et d'un serveur MCP crée un environnement fluide et puissant pour une variété de tâches.
*   **Génération et Modification de Contenu** : Vous pouvez générer des articles entiers à partir de zéro et modifier ceux existants avec des prompts simples en langage naturel.
*   **Automatisation des Tâches** : Au-delà du texte, cette configuration permet l'automatisation de tâches telles que l'envoi d'e-mails, la création de présentations et la génération de graphiques.
*   **Visualisation de Données** : Vous pouvez créer des graphiques à partir de données brutes et d'images de graphiques existantes, rationalisant le processus de visualisation des données.
*   **Extensibilité** : L'utilisation d'un serveur MCP permet l'intégration d'outils personnalisés, rendant les possibilités d'automatisation presque illimitées.