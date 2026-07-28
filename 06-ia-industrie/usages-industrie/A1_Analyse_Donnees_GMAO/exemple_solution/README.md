# 📚 Solution Exemple - Activité 1

## ⚠️ Attention Formateur

Ce dossier contient la **solution complète** de l'activité.

**Ne pas distribuer aux étudiants pendant l'activité !**

## 📄 Contenu

### `analyse_gmao_complete.py`

Script Python complet illustrant une approche professionnelle de l'analyse GMAO.

**Fonctionnalités** :
- ✅ Nettoyage automatisé des données sales
- ✅ Calcul des KPIs (MTBF, MTTR)
- ✅ Génération du diagramme de Pareto
- ✅ Analyses complémentaires (par type de panne)
- ✅ Génération automatique du rapport de synthèse

**Exécution** :
```bash
# Pré-requis : données générées
python ../generer_donnees_gmao.py

# Lancer l'analyse complète
python analyse_gmao_complete.py
```

**Sortie attendue** :
```
[1/5] Chargement des données...
[2/5] Nettoyage des données...
[3/5] Calcul des indicateurs de maintenance...
[4/5] Génération du diagramme de Pareto...
[5/5] Analyses complémentaires...
✅ ANALYSE TERMINÉE AVEC SUCCÈS
```

**Fichiers produits** :
- `interventions_2024_clean.csv` : données nettoyées
- `statistiques_machines.csv` : métriques par machine
- `pareto_machines.png` : diagramme de Pareto
- `analyse_types_pannes.png` : visualisations complémentaires
- `rapport_synthese_gmao_2024.md` : rapport final

## 🎯 Usage Pédagogique

### 1. Préparation du formateur
Exécutez le script en amont pour :
- Vérifier que l'environnement fonctionne
- Anticiper les résultats attendus
- Préparer le débrief

### 2. Pendant l'activité
Utilisez ce script pour :
- **Débloquer un étudiant** complètement bloqué (montrer un extrait, pas tout)
- **Vérifier une approche** : comparer avec ce que l'étudiant a produit
- **Gérer le timing** : si manque de temps, fournir une partie du code

**Exemples d'extraits à montrer** :
- Fonction `nettoyer_date()` si bloqué sur les formats
- Calcul du MTBF si confusion avec MTTR
- Structure du diagramme de Pareto

### 3. Débrief final
Projetez :
- Le diagramme de Pareto généré
- Le tableau des top 10 machines
- Des extraits du rapport de synthèse

Comparez avec les productions étudiantes :
- Approches différentes (toutes valides si correctes)
- Erreurs fréquentes identifiées
- Points d'amélioration

## 💡 Variantes

Le script peut être adapté pour :
- Modifier les seuils (ex: Pareto à 70% ou 90%)
- Ajouter d'autres visualisations
- Intégrer des analyses prédictives simples
- Générer un rapport PDF (via markdown → pandoc)

## 📝 Notes

- Le script est **surcommenté** volontairement pour être pédagogique
- Les étudiants peuvent avoir des approches différentes (ex: utiliser seaborn au lieu de matplotlib)
- L'important est la démarche, pas le code identique

---

**Ce code est un guide, pas la seule bonne réponse !**
