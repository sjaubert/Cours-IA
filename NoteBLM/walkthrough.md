# Déploiement du Serveur MCP NotebookLM : Walkthrough

Le serveur MCP NotebookLM a été installé et configuré avec succès dans l'environnement virtuel. Les problèmes courants d'authentification sous Windows et de coupure de communication avec le client MCP ont été résolus. Voici un résumé des actions effectuées et des instructions pour l'utilisation :

## 1. Modifications Apportées

- **Installation d'Environnement :** Création d'un environnement Python virtualisé avec `uv` dans le répertoire `NoteBLM\env_mcp` dédié. Installation de `notebooklm-mcp-server`.
- **Patch de Sécurité Chrome :** Modification du fichier interne `auth_cli.py` pour scanner de multiples chemins d'installation Windows incluant `C:\Program Files (x86)` et `%LOCALAPPDATA%`, prévenant ainsi l'erreur "Chrome introuvable".
- **Protocol Guard :** Création du fichier `run_mcp.py`, qui enveloppe l'exécutable du serveur. Il analyse le flux de sortie (`stdout`) pour s'assurer que seuls les paquets JSON valides sont transmis au client AI, redirigeant tous les autres messages de log de la console vers le flux d'erreur standard (`stderr`).
- **Script d'Authentification (`auth_mcp.py`) :** Un script robuste conçu pour arrêter systématiquement (via `taskkill`) tous les processus Google Chrome existants (et éviter le blocage du port de débogage 9222), puis lancer une interface d'authentification propre pour `notebooklm-mcp-auth`.
- **Exemple de Configuration MCP :** Le fichier `mcp_config_example.json` montre comment intégrer `run_mcp.py` dans la configuration existante de votre client Agent MCP.
- **Script de Validation (`test_notebooklm.py`) :** Un mini-programme python pour certifier que l'infrastructure de tokens fonctionne et que les carnets de notes NotebookLM peuvent être récupérés par l'IA.

## 2. Instructions d'Utilisation

L'ensemble des fichiers réside dans `d:\projets\Cours-IA\NoteBLM`.

### Étape A : S'authentifier auprès de Google

1. Exécutez le script d'authentification en tant qu'administrateur ou dans un terminal classique :

   ```bash
   python d:\projets\Cours-IA\NoteBLM\auth_mcp.py
   ```

2. Cela va arrêter tout Chrome ouvert afin de libérer le port 9222.
3. Une nouvelle fenêtre Chrome s'ouvrira.
4. **Connectez-vous** à votre compte Google via cette fenêtre. La fenêtre se fermera automatiquement une fois les jetons de sécurité validés et extraits.

### Étape B : Vérification du Bon Fonctionnement

Lancez le script de test pour vous assurer que tout s'est bien déroulé.

```bash
python d:\projets\Cours-IA\NoteBLM\test_notebooklm.py
```

Si le script liste les noms de vos carnets de notes NotebookLM, la configuration est un succès. En cas d'"Authentification expirée", il suffira de relancer l'étape A.

### Étape C : Configuration du Client MCP (Antigravity/Claude)

Ouvrez le fichier de configuration de votre client IA (généralement `mcp.json` ou `claude_desktop_config.json`) et ajoutez le serveur comme indiqué dans `mcp_config_example.json` :

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "python",
      "args": [
        "-u",
        "d:\\projets\\Cours-IA\\NoteBLM\\run_mcp.py"
      ]
    }
  }
}
```

N'oubliez pas de redémarrer le client IA pour que le serveur prenne effet. Vous pouvez désormais discuter avec votre agent IA et lui demander de consulter vos documents stockés sur NotebookLM.
