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

### 2. Réseau de Neurones et Surface 3D (`2_reseau_neurones.html`)

**Architecture** : Réseau avec 3 entrées, 2 couches cachées, 1 sortie

**Fonctionnalités** :
- 🔗 Visualisation de l'architecture du réseau
- 🎨 Neurones colorés selon leur activation
- 🌐 Surface 3D interactive (rotation avec la souris)
- 🎚️ Trois variables d'entrée ajustables (V1, V2, V3)
- 📊 Calcul en temps réel de la sortie Y
- 🎲 Bouton pour générer des entrées aléatoires
- 🔄 Bouton de réinitialisation

**Utilisation** :
1. Ajustez les curseurs V1, V2 et V3 pour modifier les entrées
2. Observez comment le réseau calcule la sortie Y
3. Regardez les neurones s'activer dans l'architecture
4. Explorez la surface 3D en la faisant pivoter avec la souris
5. Testez différentes combinaisons avec le bouton "Aléatoire"

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
- Observez d'abord l'architecture avec les valeurs par défaut
- Modifiez une seule variable à la fois pour comprendre son impact
- Explorez la surface 3D sous différents angles
- Notez comment les couches cachées transforment les données

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

## 📧 Contact

**Pôle Formation UIMM CVDL**  
Module de formation sur l'Intelligence Artificielle

---

*Ces outils ont été développés pour faciliter l'apprentissage interactif des concepts d'IA dans un contexte industriel.*
