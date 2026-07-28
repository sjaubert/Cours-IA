# Corrigé Module 1 : Skill d'Analyse (SKILL.md)

Voici une implémentation possible d'un skill (Morphic Code) pour l'analyse de logs.

```markdown
# log-analyzer

## Description
Analyse un fichier CSV de logs pour en extraire et résumer les erreurs principales (CRITICAL et ERROR) dans un rapport Markdown.

## Workflow
1. Lire le fichier CSV spécifié en paramètre d'entrée. S'il n'est pas spécifié, chercher le dernier fichier `.csv` dans le dossier courant.
2. Nettoyer les données : supprimer les lignes vides ou illisibles.
3. Filtrer les données : ne conserver que les lignes contenant "ERROR" ou "CRITICAL".
4. Trier ces erreurs par ordre de fréquence d'apparition (si possible) ou par gravité.
5. Générer un résumé textuel des problèmes rencontrés.
6. Construire un tableau Markdown avec les 5 erreurs les plus fréquentes (ou pertinentes).

## Output
Générer et sauvegarder le rapport final dans un fichier nommé `rapport_erreurs.md` à la racine du projet.

```

### Bonus : La Morphabilité

**La commande (le prompt) :** 
*"Exécute le skill `log-analyzer` sur les logs d'aujourd'hui, mais modifie les étapes 3 et 6 : filtre **uniquement** sur les erreurs contenant 'Timeout' et au lieu du fichier par défaut, sauvegarde le résultat dans `rapport_timeout.md`."*

**L'intérêt :** L'agent exécutera les étapes 1, 2, 4 et 5 telles qu'écrites dans le fichier `SKILL.md`, mais remplacera les directives de filtres et d'enregistrement sans que nous ayons besoin de dupliquer ou de réécrire le fichier original. C'est la programmation morphique !
