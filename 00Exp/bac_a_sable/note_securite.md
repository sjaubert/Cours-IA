# Sécurité d'une IA locale

Le local supprime le risque de fuite réseau, mais pas tous les risques.

Points de vigilance :

- Ne jamais laisser une clé API en clair dans un fichier versionné. En local pur, on n'en a pas, c'est un avantage.
- Un agent qui agit sur les fichiers peut écraser ou supprimer. Travailler dans un dossier dédié (bac à sable).
- Lire ce que l'agent propose avant de valider une action destructrice.
- Faire une sauvegarde ou un commit Git avant une tâche qui modifie des fichiers existants.
