# Formation IA - Usages en Maintenance Industrielle

## 📚 Vue d'Ensemble

Cette formation propose **5 activités pédagogiques** pour initier des étudiants Bachelor en maintenance industrielle aux usages pratiques de l'IA dans leur métier.

---

## 🎯 Activités Disponibles

### ✅ Activité 1 : Analyse de Données GMAO et Reporting Décisionnel
**Durée** : 60 min | **Niveau** : Intermédiaire

Transformer des données brutes de GMAO (5000 interventions) en aide à la décision. Nettoyage de données, calcul MTBF/MTTR, diagramme de Pareto, rapport managérial.

📁 `A1_Analyse_Donnees_GMAO/`

---

### ✅ Activité 2 : Assistant Diagnostic de Pannes Multi-Sources
**Durée** : 45 min | **Niveau** : Débutant

Utiliser l'IA pour diagnostiquer des pannes en exploitant une base documentaire technique (manuels pompes, variateurs, pneumatique). 5 scénarios réalistes.

📁 `A2_Assistant_Diagnostic/`

---

### ✅ Activité 3 : Génération de Procédures de Sécurité et Consignation
**Durée** : 40 min | **Niveau** : Intermédiaire

Générer une procédure de consignation/déconsignation avec l'IA, puis la critiquer et corriger pour conformité aux normes (NFC 18-510). Développe l'esprit critique sur sujets de sécurité.

📁 `A3_Procedures_Securite/`

---

### ✅ Activité 4 : Planification Prédictive avec Analyse de Tendances
**Durée** : 50 min | **Niveau** : Avancé

Analyser 12 mois de relevés capteurs (température, vibration, courant) pour détecter les dérives, prédire les pannes et optimiser le planning de maintenance.

📁 `A4_Maintenance_Predictive/`

---

### ✅ Activité 5 : Documentation Technique Interactive et Formation
**Durée** : 35 min | **Niveau** : Débutant

Créer un guide de dépannage rapide (2 pages) pour nouveaux techniciens à partir d'un manuel technique complexe. Synthèse, vulgarisation, création de supports.

📁 `A5_Documentation_Technique/`

---

## 📊 Vue D'ensemble Pédagogique

| Activité | Durée | Niveau | Compétences Clés |
|----------|-------|--------|------------------|
| A1 - GMAO | 60 min | Intermédiaire | Analyse données, KPIs, visualisation |
| A2 - Diagnostic | 45 min | Débutant | Exploitation docs, raisonnement |
| A3 - Sécurité | 40 min | Intermédiaire | Esprit critique, normalisation |
| A4 - Prédictive | 50 min | Avancé | Séries temporelles, anticipation |
| A5 - Documentation | 35 min | Débutant | Synthèse, vulgarisation |

**Durée totale** : ~4 heures (½ journée de formation)

---

## 🎓 Objectifs Pédagogiques Transversaux

### Savoirs
- Comprendre les capacités et limites de l'IA
- Connaître les bonnes pratiques d'interaction (prompts efficaces)
- Ma îtriser les outils d'analyse de données industrielles

### Savoir-faire
- Utiliser l'IA comme assistant (pas oracle)
- Valider et critiquer les outputs IA
- Générer du code Python avec assistance
- Créer des documents techniques

### Savoir-être
- **Esprit critique** : Ne pas faire confiance aveuglément
- **Rigueur** : Vérification systématique (surtout sécurité)
- **Initiative** : Explorer, itérer avec l'IA
- **Communication** : Traduire le technique en managérial

---

## 💻 Prérequis Techniques

### Logiciels
- **Python 3.8+** (Activités 1 et 4)
- **Bibliothèques Python** : `pandas`, `matplotlib`, `numpy`
- **Accès Gemini** (toutes les activités)

### Installation Python
```bash
pip install pandas matplotlib numpy
```

Ou utiliser **Google Colab** (gratuit, dans le navigateur).

---

## 📁 Structure des Activités

Chaque activité contient :
- `README.md` : Guide de démarrage rapide
- `instructions_apprenant.md` : Instructions détaillées avec prompts suggérés
- `guide_formateur.md` : Guide pédagogique (objectifs, solutions, grille d'évaluation)
- Fichiers de données/documentation selon l'activité
- `exemple_solution/` (A1 uniquement) : Solution complète Python

---

## 🚀 Utilisation

### Pour le Formateur

1. **Préparez** votre environnement :
   - Testez les scripts Python (A1, A4)
   - Vérifiez l'accès Gemini pour tous
   - Imprimez ou partagez les `instructions_apprenant.md`

2. **Choisissez** vos activités (modulaire) :
   - Formation Express (2h) : A2 + A5
   - Formation Standard (4h) : Les 5 activités
   - Focus Data (3h) : A1 + A4

3. **Consultez** les `guide_formateur.md` pour :
   - Objectifs pédagogiques détaillés
   - Solutions attendues
   - Points de vigilance
   - Critères d'évaluation

### Pour l'Étudiant

1. **Ouvrez** le dossier de l'activité
2. **Lisez** le `README.md`
3. **Suivez** le `instructions_apprenant.md` pas à pas
4. **Utilisez** Gemini avec les prompts suggérés (adaptez-les!)
5. **Produisez** les livrables demandés

---

## 🎯 Progressivité

Les activités sont conçues pour être progressives :

**Débutant** (découverte) :
- A2 : Diagnostic assisté
- A5 : Documentation

**Intermédiaire** (maîtrise) :
- A1 : Analyse GMAO
- A3 : Procédures sécurité

**Avancé** (expertise) :
- A4 : Maintenance prédictive

---

## ⚠️ Messages Clés pour les Apprenants

### 1. L'IA est un **assistant**, pas un **oracle**
→ Toujours valider les résultats

### 2. Esprit critique **obligatoire** (surtout en sécurité)
→ Une erreur de procédure = risque d'accident

### 3. Itération et précision des prompts
→ Plus vous êtes précis, meilleure est la réponse

### 4. L'IA ne remplace pas la compétence métier
→ Elle accélère et aide, mais nécessite votre expertise

---

## 📞 Support et Ressources

### Pendant la Formation
- Guide formateur pour chaque activité
- Solutions types disponibles (à distribuer en fin d'activité)

### Après la Formation
- Scripts Python réutilisables
- Prompts Gemini adaptables à d'autres situations
- Méthodologies transposables sur équipements réels

---

## 🔄 Évolution Continue

Ces activités sont conçues pour évoluer :
- Utilisez vos **propres données GMAO** (A1)
- Créez vos **scénarios de pannes** (A2)
- Adaptez aux **équipements de votre école** (A3-A5)

---

## 📝 Fichiers Créés

**Total** : 5 activités complètes
- **40+ fichiers** pédagogiques
- **~600 lignes de code** Python
- **~8000 mots** de documentation
- **Prêt à l'emploi** dès maintenant

---

## ✨ Bon ne Formation !

Ces activités ont été conçues pour être **réalistes**, **pratiques** et **applicables** directement en milieu industriel.

**Objectif** : Former des techniciens lucides et critiques dans leur usage de l'IA.

---

*Formation créée pour Bachelor Maintenance Industrielle - UIMM CVDL*
