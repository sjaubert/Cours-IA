# Activité 4 : Planification Prédictive

## 📋 Contexte

Vous gérez la maintenance d'une pompe équipée de capteurs (température, vibration, courant). Vous disposez de 12 mois de relevés horaires. Utilisez l'IA pour analyser les données, détecter les dérives et planifier la maintenance préventive.

## ⏱️ Durée : 50 min

---

## Étape 1 : Génération des Données (5 min)

Vérifiez le fichier `releves_capteurs_12mois.csv`.

---

## Étape 2 : Analyse avec Gemini (30 min)

### Prompt 1 : Chargement et Visualisation

```
J'ai un fichier CSV "releves_capteurs_12mois.csv" avec des relevés horaires sur 1 an.

Colonnes : Timestamp, Machine_ID, Temperature_C, Vibration_mm_s, Courant_A

Peux-tu générer du code Python (pandas + matplotlib) pour :
1. Charger les données
2. Créer 3 graphiques (un par paramètre) montrant l'évolution sur l'année
3. Afficher les statistiques de base (min, max, moyenne, écart-type)
```

### Prompt 2 : Détection de Tendances

```
Analyse les tendances sur l'année :

1. Y a-t-il une tendance croissante ou décroissante pour chaque paramètre ?
2. Calcule la régression linéaire pour chaque capteur
3. Si la tendance se poursuit, quand les seuils critiques seront-ils atteints ?

Seuils critiques :
- Température > 75°C
- Vibration > 7,1 mm/s (ISO 10816 - Inadmissible)
- Courant > 13A

Génère le code Python pour visualiser ces tendances + projections.
```

### Prompt 3 : Détection d'Anomalies

```
Détecte les anomalies ponctuelles (pics inhabituels) :

1. Identifie les valeurs qui dépassent la moyenne + 2× écart-type
2. Liste les timestamps de ces anomalies
3. Affiche-les sur les graphiques

Que peuvent signifier ces pics (corrélation entre les capteurs) ?
```

### Prompt 4 : Recommandations Maintenance

```
Sur la base de cette analyse :

1. Quel est le diagnostic probable ? (usure roulement, désalignement, etc.)
2. Quand recommandes-tu une intervention préventive ?
3. Quels paramètres surveiller en priorité ?
4. Quelle fréquence de contrôle recommandes-tu d'ici l'intervention ?
```

---

## Étape 3 : Planning de Maintenance (15 min)

Créez un document de synthèse :

```markdown
# PLAN DE MAINTENANCE PRÉDICTIVE - PMP-042

## État Actuel (Fin de l'analyse)

- **Température** : [Valeur actuelle]°C (Tendance : +X°C/mois)
- **Vibration** : [Valeur] mm/s (Tendance : +X mm/s/mois)
- **Courant** : [Valeur]A (Tendance : +XA/mois)

## Diagnostic Probable

[Cause identifiée par analyse IA]

## Prévision de Dépassement Seuils

| Paramètre | Seuil Critique | Date Prévue Dépassement |
|-----------|----------------|-------------------------|
| Température | 75°C | [Date] |
| Vibration | 7,1 mm/s | [Date] |
| Courant | 13A | [Date] |

## Recommandations

### Action Immédiate
- [Action corrective si nécessaire]

### Intervention Planifiée
**Date recommandée** : [Date, avant dépassement seuil]  
**Type** : [Remplacement roulement / Alignement / ...]  
**Durée estimée** : [Heures]

### Surveillance Renforcée
- Fréquence contrôle : [Hebdomadaire / Bihebdomadaire]
- Paramètre prioritaire : [Vibration / Température]
- Seuil d'alerte anticipé : [Valeur]

## Gain Espéré

- Éviter un arrêt non planifié
- Coût arrêt production évité : [Estimation]
- Optimisation : Intervention planifiée en période creuse
```

---

## 📊 Critères d'Évaluation

| Critère | Points |
|---------|--------|
| **Analyse** : Tendances identifiées correctement | 30% |
| **Prédiction** : Dates de dépassement seuils pertinentes | 25% |
| **Diagnostic** : Cause probable cohérente | 20% |
| **Planning** : Recommandations justifiées | 25% |

---

## 💡 Conseils

1. **Visualisez d'abord** : Les graphiques révèlent beaucoup
2. **Corrélez les paramètres** : Souvent, plusieurs évoluent ensemble
3. **Seuils ISO** : Vibration basée sur ISO 10816 (standard)
4. **Anticipez** : Planifier 1-2 mois avant seuil critique

---

**Bonne analyse prédictive ! 📈**
