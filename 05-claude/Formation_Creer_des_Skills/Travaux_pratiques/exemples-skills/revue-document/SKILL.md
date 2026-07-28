---
name: revue-document
description: Relit un document et propose des corrections sans modifier les fichiers. À utiliser pour une revue, une relecture ou un contrôle qualité d'un document existant.
allowed-tools: Read, Grep, Glob
model: sonnet
---

# Revue de document (lecture seule)

Cette compétence sert à relire un document et à proposer des améliorations.
Elle ne doit jamais modifier de fichier : elle se limite à la lecture et au signalement.

## Procédure
1. Lire le document concerné.
2. Évaluer le document selon les critères qualité décrits dans
   `references/criteres-qualite.md`. Ne charger ce fichier que lorsqu'une revue
   est réellement demandée.
3. Restituer les remarques sous forme de liste : pour chaque point, indiquer
   l'emplacement (section ou ligne), le problème constaté et la correction suggérée.

## Garde-fous
- Ne proposer que des corrections justifiées.
- Ne pas réécrire le document à la place de l'auteur : suggérer, ne pas imposer.
- En cas de doute sur l'intention de l'auteur, poser la question plutôt que de trancher.
