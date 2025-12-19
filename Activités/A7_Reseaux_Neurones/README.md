# Module A7 : Introduction aux Réseaux de Neurones

## 📚 Vue d'Ensemble

Ce module pédagogique propose deux visualisations interactives pour comprendre le fonctionnement des réseaux de neurones, depuis les concepts de base jusqu'aux architectures multicouches.

## 🎯 Objectifs Pédagogiques

- Comprendre le principe de la régression linéaire
- Visualiser comment un modèle s'ajuste aux données
- Découvrir l'architecture des réseaux de neurones
- Explorer les surfaces de décision complexes
- Manipuler interactivement les paramètres d'un réseau

## 📁 Contenu du Module

### 1. Régression Linéaire Interactive (`1_regression_lineaire.html`)

**Cas d'étude industriel** : Relation entre température de traitement thermique et dureté du matériau

**Fonctionnalités** :
- 📍 Points de données déplaçables par glisser-déposer
- ➕ Ajout de nouveaux points par simple clic
- ❌ Suppression de points par double-clic
- 📈 Calcul automatique de la droite de régression (méthode des moindres carrés)
- 📊 Affichage de l'équation y = mx + b
- 🎯 Coefficient de détermination R² 
- 🔄 Bouton de réinitialisation

**Utilisation** :
1. Cliquez n'importe où sur le graphique pour ajouter un point
2. Glissez-déposez les points pour les déplacer
3. Double-cliquez sur un point pour le supprimer
4. Observez la droite s'ajuster automatiquement
5. Consultez les statistiques dans le panneau de droite

### 2. Réseau de Neurones avec Apprentissage Supervisé (`2_reseau_neurones.html`)

**Cas d'étude industriel** : Prédiction de la qualité (Y) en fonction de 3 paramètres de fabrication (V1, V2, V3)

**Fonctionnalités** :
- 📊 **Données d'entraînement** : 10 exemples réels affichés sur la surface 3D (points rouges)
- 🧠 **Apprentissage supervisé** : Entraînement par rétropropagation du gradient
- 📉 **Fonction de coût** : Erreur quadratique moyenne (MSE) avec graphique d'évolution
- ⚙️ **Architecture configurable** : Choix du nombre de couches (1-3) et neurones par couche (3-8)
- 🔗 **Visualisation du réseau** : Neurones colorés selon leur activation
- 🌐 **Surface 3D interactive** : Axes clairement labelisés (V1, V2, Y)
- 🎚️ **Test du réseau** : Trois variables d'entrée ajustables pour tester les prédictions
- 🎯 **Métriques en temps réel** : Nombre d'itérations et MSE

**Utilisation** :
1. Configurez l'architecture (nombre de couches et neurones)
2. Cliquez sur "Créer le Réseau" pour initialiser
3. Cliquez sur "Entraîner (100 itérations)" et observez l'erreur diminuer
4. Testez le réseau avec les sliders V1, V2, V3
5. Observez la surface 3D et les points d'entraînement

### 📚 Ressources Complémentaires

- **`Synthese_Architecture.md`** : Guide visuel rapide sur l'influence du nombre de couches et neurones
- **`Guide_Architecture_Reseaux.md`** : Explication détaillée du choix d'architecture (compromis biais-variance, règles de décision)


## 🚀 Prérequis Techniques

- Navigateur web moderne (Chrome, Firefox, Edge, Safari)
- JavaScript activé
- Connexion internet (pour charger Three.js pour la visualisation 3D)

## 💡 Conseils Pédagogiques

### Pour la Régression Linéaire :
- Commencez par observer le jeu de données initial
- Déplacez quelques points pour voir l'impact sur la droite
- Ajoutez des points aberrants pour voir comment ils affectent le modèle
- Comparez le R² avant et après ajout de points

### Pour le Réseau de Neurones :
- Commencez avec une architecture simple (1 couche, 4-5 neurones)
- Entraînez et notez la MSE finale
- Augmentez progressivement la complexité (nombre de couches, puis neurones)
- Observez l'évolution de la surface 3D avec différentes architectures
- Comparez le temps d'apprentissage et la précision finale
- Identifiez les signes de sur-apprentissage (MSE très faible mais surface chahutée)

## 🎓 Utilisation en Cours

### Séquence Suggérée :

1. **Introduction (10 min)** : Présentation des concepts théoriques
2. **Activité 1 (20 min)** : Exploration de la régression linéaire
3. **Pause et Discussion (10 min)** : Questions et observations
4. **Activité 2 (30 min)** : Découverte des réseaux de neurones
5. **Synthèse (15 min)** : Liens entre les deux activités

### Questions à Poser :

**Régression Linéaire** :
- Que se passe-t-il quand on ajoute un point très éloigné ?
- Comment interpréter un R² proche de 1 ? Proche de 0 ?
- Pourquoi utilise-t-on la méthode des moindres carrés ?

**Réseau de Neurones** :
- Pourquoi a-t-on besoin de couches cachées ?
- Comment les poids influencent-ils le résultat ?
- Quelle est la différence entre cette surface et une simple droite ?
- Que se passe-t-il quand on augmente le nombre de couches ?
- Comment savoir si le réseau est trop complexe pour les données ?
- Quelle architecture donne le meilleur compromis entre simplicité et précision ?

## 📧 Contact

**Pôle Formation UIMM CVDL**  
Module de formation sur l'Intelligence Artificielle

---

*Ces outils ont été développés pour faciliter l'apprentissage interactif des concepts d'IA dans un contexte industriel.*
