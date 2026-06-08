# Specification — Script de detection d'anomalies capteurs (sortie attendue de la Session 1)

> Document produit en SESSION DE SPECIFICATION, puis transmis tel quel a une
> session d'implementation neuve (exercice 4). Il ne contient aucune trace de
> l'exploration : seulement le contrat agree.

## Objectif

Detecter, dans un releve de capteurs de la presse hydraulique PH-200, les points de
mesure anormaux (vibration, temperature, pression) afin d'alerter avant defaillance.

## Entree

Fichier CSV `data/releve_capteurs.csv`, colonnes :

- `horodatage` (ISO 8601)
- `vibration_mm_s` (flottant)
- `temperature_c` (flottant)
- `pression_bar` (flottant)

## Sortie

Un DataFrame des anomalies, colonnes : `horodatage`, `grandeur`, `valeur`, `seuil`,
`type` (haut / bas). Plus un PNG par grandeur dans `rapports/`.

## Regle de detection

Methode statistique simple : une mesure est anormale si elle s'ecarte de plus de
3 ecarts-types de la moyenne glissante sur 24 h. Seuils durs de securite a respecter
en priorite : temperature > 85 C, pression > 180 bar.

## Cas limites a traiter

- Trous de mesure (lignes manquantes) : ne pas interpoler, signaler.
- Valeurs negatives de pression : invalides, a ecarter et compter.
- Premiere fenetre de 24 h incomplete : pas d'alerte statistique, seuils durs seuls.

## Hors perimetre (non-goals)

- Pas de modele predictif ni de machine learning.
- Pas d'envoi d'alerte (mail, supervision) : seulement la detection.
