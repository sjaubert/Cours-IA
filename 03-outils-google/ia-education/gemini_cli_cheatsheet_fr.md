# Mon Aide-Mémoire Gemini CLI 

**Auteur :** S. Jaubert
**Publié le :** 24-09-2025


---


> **Commentaire :** L'objectif de cet aide-mémoire est de fournir un accès rapide aux commandes les plus utiles, en passant des bases aux fonctionnalités plus avancées.


---

## Aide-Mémoire Gemini CLI

### 🟢 NIVEAU 1 : COMMANDES DE BASE
> **Commentaire :** Les commandes essentielles pour bien démarrer avec Gemini CLI.

#### Installation et Démarrage
```bash
# Installer globalement
npm install -g @google/gemini-cli

# Exécuter sans installation permanente
npx @google/gemini-cli

# Lancer le CLI interactif
gemini

# Vérifier la version installée
gemini --version
```

#### Navigation de Base
> **Commentaire :** Commandes internes pour interagir avec le CLI.
```bash
# Informations sur la version
/about

# Afficher les commandes disponibles
/help

# Lister les outils disponibles
/tools

# Effacer la conversation actuelle
/clear

# Quitter le CLI (ou Ctrl+C)
/quit
```

#### Opérations de Fichiers de Base
> **Commentaire :** Gemini peut interagir avec le système de fichiers en utilisant des commandes spécifiques ou un langage naturel.
```bash
# Lire le contenu d'un dossier
ReadFolder

# Lire un seul fichier
ReadFile

# Lire plusieurs fichiers
ReadManyFiles

# Utiliser le langage naturel pour les opérations sur les fichiers
"Liste les fichiers dans le répertoire courant"
"Montre-moi le contenu de package.json"
"Trouve tous les fichiers HTML dans ce projet"
```

#### Outils de Base
```bash
# Lister les outils disponibles
/tools

# Afficher la description des outils
/tools desc

# Masquer la description des outils
/tools nodesc
```

#### Configuration de Base
```bash
# Changer le thème visuel
/theme

# Changer la méthode d'authentification
/auth

# Sélectionner un éditeur de code supporté
/editor
```

#### Commandes Shell de Base
```bash
# Exécuter une commande shell simple
shell ls
```

#### Raccourcis Clavier
> **Commentaire :** Gagnez du temps avec ces raccourcis essentiels.
- **Entrée :** Envoyer le message
- **Échap :** Annuler l'opération en cours
- **Ctrl+L :** Effacer l'écran
- **Ctrl+C (x2) :** Quitter l'application
- **Ctrl+T :** Afficher/Masquer la description des outils
- **Flèches Haut/Bas :** Naviguer dans l'historique des prompts
- **Alt+Gauche/Droite :** Se déplacer mot par mot

#### Dépannage et Astuces
```bash
# Voir les paramètres de confidentialité
/privacy

# Soumettre un rapport de bug
/bug

# Ouvrir la documentation officielle
/docs
```

### 🟡 NIVEAU 2 : COMMANDES INTERMÉDIAIRES
> **Commentaire :** Gestion de fichiers et personnalisation de base.

#### Gestion de Fichiers
> **Commentaire :** Le préfixe `@` est un moyen rapide de spécifier un chemin de fichier ou de dossier.
```bash
# Lire un dossier entier
/tools read_folder <répertoire>

# Lire le contenu du dossier de projet
@src/mon_projet/

# Lire un fichier spécifique
@chemin/vers/fichier.txt

# Gérer les espaces dans les chemins
@"Mes Documents/fichier.txt"
```

#### Gestion des Conversations
```bash
# Sauvegarder la conversation actuelle avec un tag
/chat save <tag>

# Reprendre une conversation sauvegardée
/chat resume <tag>

# Lister toutes les conversations sauvegardées
/chat list

# Compresser le contexte de la conversation en un résumé
/compress
```

#### Configuration du Modèle
> **Commentaire :** Changez de modèle Gemini à la volée pour adapter la vitesse et la capacité à vos besoins.
```bash
# Afficher le modèle actuel
--model

# Passer au modèle Flash (le plus rapide)
--model gemini-1.5-flash

# Passer au modèle Pro (le plus capable)
--model gemini-1.5-pro

# Passer à la dernière version du modèle Pro
--model gemini-1.5-pro-002
```

#### Gestion de la Mémoire
```bash
# Afficher le contexte mémoire actuel
/memory show

# Ajouter du texte à la mémoire
/memory add <texte>

# Recharger les fichiers GEMINI.md
/memory refresh
```

### 🟠 NIVEAU 3 : COMMANDES AVANCÉES
> **Commentaire :** Configuration, gestion du contexte et fonctionnalités puissantes.

#### Méthodes d'Exécution
> **Commentaire :** Le mode "YOLO" (`-y`) est très pratique pour les scripts en désactivant les demandes de confirmation.
```bash
# Exécuter un prompt directement depuis le terminal
gemini -p "votre prompt ici"

# Confirmer automatiquement toutes les actions (mode YOLO)
gemini -y

# Exécuter en mode sandbox (isolé)
gemini --sandbox

# Activer la création de points de contrôle (checkpointing)
gemini --checkpointing
```

#### Statistiques et Suivi
```bash
# Afficher les statistiques de la session
/stats

# Afficher les statistiques d'utilisation du modèle
/stats model

# Afficher les statistiques d'utilisation des outils
/stats tools
```

#### Intégration Shell
> **Commentaire :** Le préfixe `!` permet d'exécuter n'importe quelle commande shell sans quitter le CLI.
```bash
# Exécuter une commande shell
!<commande_shell>

# Exemple : lister les fichiers en détail
!ls -la

# Exemple : voir le statut git
!git status

# Activer/Désactiver le mode shell
!
```

#### Gestion du Contexte
> **Commentaire :** Fournissez facilement des fichiers ou des dossiers entiers comme contexte pour vos prompts.
```bash
# Inclure le contenu d'un fichier dans le prompt
@<chemin_vers_fichier>

# Inclure le contenu d'un répertoire
@<répertoire>

# Exemple : inclure le README
@README.md

# Ajouter un fichier spécifique au contexte
@src/monFichier.ts

# Ajouter un dossier entier au contexte
@dossier/
```

### 🔴 NIVEAU 4 : COMMANDES EXPERT
> **Commentaire :** Serveurs MCP, automatisation et intégrations avancées.

#### Gestion des Serveurs MCP
```bash
# Lister les serveurs MCP disponibles
/mcp list

# Afficher les descriptions détaillées des MCP
/mcp desc

# Masquer les descriptions des MCP
/mcp nodesc

# Afficher le schéma JSON complet
/mcp schema
```

#### Exécution Avancée
```bash
# Exécuter la dernière version via npx
npx @google/gemini-cli

# Exécuter directement depuis le dépôt GitHub
npx https://github.com/google-gemini/gemini-cli
```

#### Configuration du Sandbox
> **Commentaire :** Le mode sandbox isole l'exécution pour plus de sécurité.
```bash
# Activer le sandboxing (raccourci)
gemini -s

# Activer via une variable d'environnement
export GEMINI_SANDBOX=true

# Spécifier Docker comme sandbox
export GEMINI_SANDBOX=docker

# Spécifier Podman
export GEMINI_SANDBOX=podman

# Spécifier sandbox-exec (macOS)
export GEMINI_SANDBOX=sandbox-exec
```

#### Opérations de Fichiers Avancées
> **Commentaire :** Le filtrage conscient de Git ignore automatiquement les fichiers et dossiers non pertinents comme `node_modules`.
```bash
# Le filtrage Git ignore automatiquement :
# node_modules/, dist/, .env, .git/
# Peut être configuré via les paramètres fileFiltering
```

### 🔵 NIVEAU 5 : COMMANDES "POWER USER"
> **Commentaire :** Workflows et intégrations pour les utilisateurs très avancés.

#### Exécution Basée sur des Conteneurs
```bash
# Exemple avec Docker
docker run --rm -it us-docker.pkg.dev/gemini-code-dev/gemini-cli/sandbox:0.1.1
gemini --sandbox -y -p "votre prompt ici"
```

#### Mode Développement
```bash
# Démarrage avec rechargement à chaud (hot-reloading)
npm run start

# Lier le paquet local globalement pour le tester
npm link packages/cli
```

#### Variables d'Environnement
```bash
# Profil de sandbox permissif pour macOS
export SEATBELT_PROFILE=permissive-open

# Profil de sandbox strict pour macOS
export SEATBELT_PROFILE=restrictive-closed

# Forcer l'UID/GID de l'hôte
export SANDBOX_SET_UID_GID=true

# Activer le mode de débogage
export DEBUG=1
```

#### Points de Contrôle et Restauration
> **Commentaire :** Ne perdez jamais votre travail en restaurant une session précédente.
```bash
# Lister les points de contrôle disponibles
/restore

# Restaurer un point de contrôle spécifique
/restore <fichier_checkpoint>

# Exemple de restauration
/restore 2025-06-22T10-00-00_000Z-my-file.txt-write_file
```

### 🟣 NIVEAU 6 : COMMANDES MAÎTRE
> **Commentaire :** Automatisation avancée et workflows personnalisés.

#### Rapport de Bugs et Problèmes
```bash
# Créer une issue GitHub directement depuis le CLI
/bug "Description du problème"
```

#### Gestion des Extensions
```bash
# Les extensions sont chargées depuis :
# <workspace>/.gemini/extensions
# <home>/.gemini/extensions
```

#### Paramètres Avancés (settings.json)
> **Commentaire :** Personnalisez finement le comportement de Gemini CLI via ce fichier de configuration.
```json
{
  "sandbox": "docker",
  "checkpointing": { "enabled": true },
  "bugCommand": "commande personnalisée",
  "mcpServers": {
    "mon-serveur": {
      "command": "node mon-serveur.js"
    }
  }
}
```

---
