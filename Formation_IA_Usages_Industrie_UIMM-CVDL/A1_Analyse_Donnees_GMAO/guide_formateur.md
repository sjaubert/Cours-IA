# Guide Formateur - Activité 1 : Analyse de Données GMAO

## 📝 Fiche Activité

| Élément | Détail |
|---------|--------|
| **Titre** | Analyse de Données GMAO et Reporting Décisionnel |
| **Durée** | 60 minutes |
| **Niveau** | Intermédiaire (Bachelor Maintenance) |
| **Prérequis** | Notions de bases Excel, connaissance GMAO |
| **Modalités** | Individuel ou binôme |

---

## 🎯 Objectifs Pédagogiques

### Savoirs
- Comprendre les indicateurs MTBF et MTTR
- Connaître le principe du diagramme de Pareto (loi des 80/20)
- Identifier les limites des données brutes de GMAO

### Savoir-faire
- Utiliser l'IA pour nettoyer des données sales
- Générer du code Python avec assistance IA
- Produire des visualisations pertinentes
- Rédiger un rapport de synthèse managérial

### Savoir-être
- Développer un esprit critique face aux résultats de l'IA
- Adopter une démarche méthodique d'analyse
- Communiquer des résultats techniques à un public non technique

---

## 📅 Déroulé de Séance

### Phase 1 : Introduction (10 min)

**Présentation du contexte** :
- Importance de la donnée dans la maintenance moderne
- Problématique : les GMAO contiennent souvent des données inconsistantes
- Objectif : transformer des données brutes en aide à la décision

**Démonstration rapide** :
- Montrer le fichier CSV généré
- Pointer quelques exemples d'erreurs
- Expliquer l'impact sur les analyses

### Phase 2 : Travail Guidé (40 min)

Les étudiants suivent les instructions dans `instructions_apprenant.md`.

**Rôle du formateur** :
- Circuler dans la salle
- Aider au déblocage technique
- Vérifier la progression (checklists)
- Encourager l'itération avec l'IA

**Points de vigilance** :

1. **Étape Nettoyage** (15 min) :
   - Vérifier que les étudiants comprennent les transformations appliquées
   - S'assurer qu'ils ne font pas confiance aveuglément au code généré
   - Les inciter à tester sur un échantillon d'abord

2. **Étape Calculs** (15 min) :
   - Valider que les formules MTBF/MTTR sont correctes
   - Certains peuvent confondre temps total disponible et période d'observation
   - Rappeler les unités (heures, jours)

3. **Étape Visualisation** (10 min) :
   - Le diagramme de Pareto doit être lisible
   - Les axes doivent être correctement labellisés
   - La courbe cumulée doit atteindre 100%

### Phase 3 : Débrief Collectif (10 min)

**Questions à poser** :
1. Combien de machines représentent 80% des arrêts ? (attendu : 10-15 machines)
2. Quel est le MTTR moyen sur l'ensemble du parc ?
3. Avez-vous trouvé des erreurs dans le code généré par l'IA ?
4. Quelles recommandations proposez-vous ?

**Points clés à souligner** :
- L'IA accélère le travail mais nécessite validation
- Les indicateurs doivent être contextualisés (type d'industrie, criticité)
- Un bon rapport allie chiffres et interprétation métier

---

## 💡 Solutions et Attendus

### Données Générées

Le script `generer_donnees_gmao.py` produit :
- **5000 lignes** d'interventions
- **50 machines** différentes
- Environ **10% d'erreurs** de frappe
- **5% de données manquantes**
- Formats hétérogènes dans dates et durées

### Résultats Attendus

**Après nettoyage** :
- Format de date uniforme : YYYY-MM-DD
- Durées en heures décimales (float)
- Types de pannes normalisés (10 catégories)
- Noms techniciens cohérents

**Métriques typiques** (peuvent varier selon génération aléatoire) :
- MTTR moyen : 5-8 heures
- MTBF moyen : 30-60 jours
- Top 3 machines : 100-150h d'arrêt cumulé chacune
- Environ 10-12 machines pour 80% des arrêts

**Graphique Pareto** :
- Barres décroissantes de gauche à droite
- Courbe cumulée en S
- Ligne 80% qui intersecte vers la 10-15ème machine

### Script Python Exemple

Un script complet est fourni dans `exemple_solution/analyse_gmao_complete.py`.

Les étudiants **ne doivent pas y avoir accès pendant l'activité**. Utilisez-le pour :
- Vous préparer en amont
- Débloquer un étudiant complètement bloqué
- Comparer les approches en fin de séance

---

## ⚠️ Points de Vigilance

### Erreurs Fréquentes

1. **Confusion MTBF vs MTTR** :
   - MTBF = temps de fonctionnement / nombre de pannes
   - MTTR = temps de réparation / nombre de pannes
   - Bien distinguer "temps entre pannes" et "temps de réparation"

2. **Mauvais calcul du MTBF** :
   - Erreur : diviser par le nombre total d'interventions toutes machines confondues
   - Correct : calculer par machine individuellement

3. **Diagramme de Pareto incorrects** :
   - Oublier de trier les machines par ordre décroissant
   - Courbe cumulée qui dépasse 100% (erreur de calcul)
   - Absence de la ligne des 80%

4. **Confiance aveugle dans l'IA** :
   - Ne pas vérifier le code généré
   - Ne pas tester sur un échantillon
   - Accepter des résultats incohérents (ex: MTTR > 1000h)

### Adaptations Possibles

**Si trop difficile** :
- Fournir un fichier déjà partiellement nettoyé
- Donner le code de nettoyage, se concentrer sur l'analyse
- Travailler en binôme

**Si trop facile** :
- Demander des analyses complémentaires (par type de panne, par technicien)
- Ajouter une analyse temporelle (mois par mois)
- Calculer le coût estimé des arrêts
- Créer une carte de criticité (fréquence × gravité)

---

## 📊 Grille d'Évaluation Détaillée

### 1. Script Python Fonctionnel (30 points)

| Critère | Points |
|---------|--------|
| Le script s'exécute sans erreur | 10 |
| Utilisation correcte de pandas | 10 |
| Code commenté et structuré | 5 |
| Gestion des erreurs (try/except) | 5 |

### 2. Nettoyage des Données (20 points)

| Critère | Points |
|---------|--------|
| Normalisation des types de pannes | 5 |
| Unification des formats de dates | 5 |
| Conversion des durées en float | 5 |
| Traitement des données manquantes | 5 |

### 3. Calculs Corrects (20 points)

| Critère | Points |
|---------|--------|
| MTTR calculé correctement par machine | 7 |
| MTBF calculé correctement | 7 |
| Temps d'arrêt cumulé correct | 6 |

### 4. Visualisation (15 points)

| Critère | Points |
|---------|--------|
| Diagramme de Pareto correct (tri, axes) | 8 |
| Courbe cumulée cohérente | 4 |
| Présentation claire (titre, légendes) | 3 |

### 5. Rapport de Synthèse (15 points)

| Critère | Points |
|---------|--------|
| Structure professionnelle | 3 |
| Chiffres clés présents et corrects | 5 |
| Recommandations pertinentes | 5 |
| Qualité rédactionnelle | 2 |

**Barème** :
- 85-100 : Excellent
- 70-84 : Bien
- 55-69 : Satisfaisant
- < 55 : À revoir

---

## 🔄 Variantes de l'Activité

### Variante 1 : Focus Coûts
Ajouter une colonne "Coût Intervention" et analyser :
- Coût total de la non-disponibilité
- ROI d'un investissement de remplacement
- Budget maintenance prévisible

### Variante 2 : Analyse Prédictive Simple
À partir des données historiques :
- Identifier les machines avec tendance croissante de pannes
- Prédire le nombre d'interventions au T1 2025
- Suggérer un planning de maintenance préventive

### Variante 3 : Comparaison Multi-Sites
Générer des données pour 3 sites différents et comparer :
- Performances relatives (MTBF, MTTR)
- Bonnes pratiques à partager
- Benchmarking

---

## 📚 Ressources Complémentaires

### Pour le Formateur

**Documentation** :
- Norme NF EN 13306 (terminologie de maintenance)
- Méthode AMDEC (Analyse des Modes de Défaillance)
- Principes du TPM (Total Productive Maintenance)

**Outils** :
- Pandas Documentation : https://pandas.pydata.org/docs/
- Matplotlib Gallery : https://matplotlib.org/stable/gallery/
- Exemples Pareto : rechercher "pareto chart python"

### Pour les Étudiants

**Après la séance** :
- Fiche récapitulative MTBF/MTTR à distribuer
- Liste de ressources Python pour débutants
- Exemples de tableaux de bord GMAO réels (anonymisés)

---

## 💬 FAQ Formateur

**Q : Un étudiant n'a pas Python installé, que faire ?**  
R : Utiliser Google Colab (gratuit, dans le navigateur) ou installer Anaconda rapidement.

**Q : L'IA génère du code avec des bibliothèques non installées ?**  
R : Demander à l'IA de vérifier les imports et générer la commande `pip install`.

**Q : Les résultats varient d'un étudiant à l'autre ?**  
R : Normal, les données sont générées aléatoirement. L'important est la démarche, pas les chiffres exacts.

**Q : Un étudiant critique l'IA qui fait des erreurs ?**  
R : Excellent ! C'est justement l'objectif pédagogique : développer l'esprit critique.

**Q : Peut-on utiliser leurs vraies données GMAO en stage ?**  
R : Oui, si autorisé par l'entreprise et données anonymisées. Encore plus formateur !

---

## ✅ Checklist Préparation Séance

- [ ] Tester le script `generer_donnees_gmao.py`
- [ ] Vérifier que Python + pandas + matplotlib sont installés
- [ ] Préparer un exemple de fichier généré à montrer
- [ ] Imprimer les `instructions_apprenant.md` ou les partager numériquement
- [ ] Tester soi-même l'activité avec Gemini pour anticiper les blocages
- [ ] Préparer 2-3 prompts de secours pour débloquer les étudiants
- [ ] Prévoir un vidéoprojecteur pour le débrief (montrer des graphiques)

---

**Bonne séance ! 🎓**
