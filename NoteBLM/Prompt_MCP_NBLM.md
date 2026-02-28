```
"Agis comme un ingénieur de systèmes expert en Windows et en protocoles MCP. Votre objectif est d'installer et de configurer le serveur MCP de NotebookLM en garantissant une connexion aveugle contre les erreurs communes. 
Suivez ce plan technique:

"1. Installation et mise à jour de l'environnement :Installez notebooklm-mcp-server à l'aide de pip. 
IMPORTANT (Correction du chemin d'accès à Chrome sous Windows) : Avant de continuer, localisez le fichier 
auth_cli.py 
dans le répertoire site-packages de la bibliothèque. Modifiez le code source afin qu'il recherche chrome.exe non seulement dans C:\Program Files, mais aussi dans C:\Program Files (x86) et %LOCALAPPDATA%. Ceci est essentiel pour éviter les échecs d'authentification au lancement sous Windows. 
2. Créez un wrapper de communication (Protocol Guard) :Créez un script Python nommé run_mcp.py qui servira d'interface à l'exécutable notebooklm-mcp. 
Ce script doit filtrer la sortie standard (stdout) : il ne doit transmettre que les lignes au format JSON valide. Toute sortie non JSON (bannières, avertissements ou texte brut) doit être redirigée vers la sortie d'erreur standard (stderr). Cette étape est indispensable pour éviter que le client MCP ne se déconnecte en raison d'erreurs de « données de fin invalides ». 
3. Configuration MCP :Configurez le fichier mcp_config.json de l'outil d'IA (par exemple, Antigravity, Claude Desktop ou Gemini) en ajoutant l'entrée du serveur notebooklm. 
Utilisez la commande : python -u [CHEMIN_VERS_LE_SCRIPT_WRAPPER]. 
4. Système d'authentification automatisé :Créez un flux de travail ou un script d'automatisation qui : 
arrête en toute sécurité les processus Chrome existants si nécessaire ; 
lance Chrome avec l'option `--remote-debugging-port=9222` ; 
exécute la commande `notebooklm-mcp-auth`. 
Cela garantit que l'agent peut capturer les jetons sans problème, sans conflit de port ni de chemin. 
5. Vérification du succès :Créez un script de vérification nommé test_notebooklm.py. Ce script doit importer l'interface NotebookLMClient depuis la bibliothèque installée et tenter d'exécuter la fonction list_notebooks(). 
La tâche est considérée comme terminée uniquement lorsque la liste des carnets de l'utilisateur est récupérée et affichée. En cas d'erreur « Authentification expirée », fournissez des instructions claires à l'utilisateur pour renouveler son authentification.
```
