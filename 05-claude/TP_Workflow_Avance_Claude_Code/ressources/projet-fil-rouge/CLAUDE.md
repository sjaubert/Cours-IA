# CLAUDE.md — Projet GMAO Maintenance (version a degraisser)

> Ce fichier est volontairement TROP LONG. Exercice 2 : le ramener a une page ecran
> en deplacant le contexte profond vers des fichiers compagnons dans memory/.

## Presentation du projet

Ce depot regroupe les scripts d'analyse des donnees de GMAO (Gestion de Maintenance
Assistee par Ordinateur) et les procedures d'intervention de l'atelier. Il est utilise
par l'equipe maintenance pour exploiter les exports d'interventions, detecter les
equipements critiques et generer des procedures securisees. Le projet existe depuis
2024 et a connu trois reorganisations successives de son arborescence, ce qui explique
la coexistence d'anciens et de nouveaux formats de fichiers.

## Historique detaille des versions

En 2024, les donnees etaient stockees en fichiers Excel. En 2025, migration vers des
exports CSV avec separateur point-virgule. Depuis 2026, le separateur est la virgule et
l'encodage est UTF-8. Les anciens fichiers Excel sont conserves dans archives/ pour
reference mais ne doivent plus etre utilises. Cette section change rarement et n'aide
pas Claude au quotidien.

## Conventions de code Python

Les scripts utilisent pandas. Indentation 4 espaces. Noms de variables en francais.
Les fonctions d'analyse retournent toujours un DataFrame. Les graphiques sont generes
avec matplotlib et sauvegardes en PNG dans rapports/. Toujours fermer les figures avec
plt.close() pour eviter les fuites memoire lors des traitements par lots.

## Conventions de redaction des procedures

Chaque procedure suit une structure en cinq rubriques : pre-requis securite,
consignation, mode operatoire, verification, remise en service. Le vocabulaire est
imperatif a l'infinitif. Les valeurs chiffrees portent toujours leur unite et leur
tolerance. (Note formateur : ce bloc fait doublon avec le Skill procedures-securite.)

## Liste exhaustive des equipements de l'atelier

Presse hydraulique PH-200, convoyeur CV-12, compresseur CP-04, variateur VAR-08,
pompe doseuse PD-03, robot de soudure RB-15, four de traitement FT-01, ligne
d'assemblage LA-02... (liste de reference, consultee une fois par trimestre).

## Regles de securite generales

Toute intervention sur energie consignee. EPI obligatoires selon la zone. Habilitation
electrique B2V pour les interventions sur armoire. Ces regles detaillees gagneraient a
vivre dans un fichier dedie plutot que dans le CLAUDE.md charge a chaque session.

## Procedure de deploiement des rapports

Les rapports generes sont deposes chaque vendredi sur le serveur partage. Nommage :
AAAA-MM-JJ_rapport_maintenance.pdf. Cette information n'a change le comportement de
Claude aucune fois cette semaine.

## Instructions de compactage

(Vide pour l'instant — a completer en exercice 5.)
