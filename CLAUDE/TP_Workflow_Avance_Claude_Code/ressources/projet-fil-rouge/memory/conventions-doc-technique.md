# Conventions de documentation technique (fichier compagnon)

> Charge a la demande par Claude quand le sujet le justifie, et non a chaque session.
> Reference depuis CLAUDE.md par : voir memory/conventions-doc-technique.md

## Formats de fichiers GMAO

- Exports posterieurs a 2026 : CSV, separateur virgule, encodage UTF-8.
- Exports 2025 : CSV, separateur point-virgule (a convertir avant traitement).
- Fichiers Excel 2024 : archives uniquement, ne pas exploiter.

## Conventions Python

- pandas pour la manipulation de donnees ; indentation 4 espaces.
- Noms de variables en francais ; fonctions d'analyse renvoyant un DataFrame.
- Graphiques matplotlib en PNG dans rapports/ ; toujours plt.close() en traitement par lots.

## Nommage des livrables

- Rapports : AAAA-MM-JJ_rapport_maintenance.pdf, deposes le vendredi sur le serveur partage.
