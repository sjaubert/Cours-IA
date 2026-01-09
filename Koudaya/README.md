# SATEBA - Analyseur PMET

Application d'analyse de données PMET pour fichiers Excel et CSV Keyence.

## 📋 Prérequis

- **Windows** (7, 10, 11)
- **Python 3.8 ou supérieur** ([Télécharger Python](https://www.python.org/downloads/))

## 🚀 Installation sur un nouveau PC

### Étape 1 : Copier les fichiers

Copiez le dossier complet `Koudaya` sur le nouveau PC (par exemple dans `C:\Programmes\SATEBA\`)

### Étape 2 : Installer les dépendances

**Double-cliquez sur** `INSTALLER.bat`

Ce script va :

- Vérifier que Python est installé
- Installer automatiquement toutes les bibliothèques nécessaires
- Vous indiquer si tout s'est bien passé

### Étape 3 : Lancer l'application

**Double-cliquez sur** `LANCER_APPLICATION.bat`

L'interface graphique s'ouvre et vous pouvez commencer à analyser vos fichiers !

## 📦 Contenu du dossier

### Fichiers principaux

| Fichier | Description |
|---------|-------------|
| `INSTALLER.bat` | Script d'installation des dépendances |
| `LANCER_APPLICATION.bat` | Lance l'application |
| `pmet_app.py` | Interface graphique |
| `analyse_pmet.py` | Moteur d'analyse |
| `csv_parser.py` | Convertisseur CSV Keyence |
| `generate_report.py` | Générateur de rapports HTML |
| `requirements.txt` | Liste des dépendances Python |

### Dossiers de sortie

| Dossier | Description |
|---------|-------------|
| `graphiques/` | Graphiques PNG générés |
| `summary/` | Rapports HTML interactifs |

## 🔧 Dépendances Python

L'application nécessite les bibliothèques suivantes :

- `pandas` >= 2.0.0 - Manipulation de données
- `matplotlib` >= 3.7.0 - Génération de graphiques
- `openpyxl` >= 3.1.0 - Lecture/écriture Excel
- `numpy` >= 1.24.0 - Calculs numériques

Ces dépendances sont installées automatiquement par `INSTALLER.bat`.

## 📖 Utilisation

### Analyser un fichier Excel

1. Lancer `LANCER_APPLICATION.bat`
2. Cliquer sur **"Ouvrir un Fichier (Excel/CSV)"**
3. Sélectionner votre fichier `.xlsx`
4. Attendre la génération des rapports
5. Le rapport HTML s'ouvre automatiquement

### Analyser un fichier CSV Keyence

1. Lancer `LANCER_APPLICATION.bat`
2. Cliquer sur **"Ouvrir un Fichier (Excel/CSV)"**
3. Sélectionner votre fichier `.csv`
4. L'application convertit automatiquement le CSV en format Excel
5. Les rapports sont générés normalement

### Consulter les rapports

**Rapport Web (recommandé)** :

- Ouvre automatiquement dans votre navigateur
- Fichier : `summary/index.html`
- Interface moderne avec graphiques interactifs

**Rapport Excel simple** :

- Fichier : `Rapport_Analyse_PMET_Simple.xlsx`
- Tableau récapitulatif des statistiques

**Rapport Excel complet** :

- Fichier : `Rapport_Complet_PMET.xlsx`
- Graphiques natifs Excel éditables
- Données brutes incluses

## ⚠️ Résolution de problèmes

### "Python n'est pas installé"

**Solution** : Installer Python depuis [python.org](https://www.python.org/downloads/)

- ⚠️ **Important** : Cocher "Add Python to PATH" pendant l'installation

### "Dépendances manquantes"

**Solution** : Exécuter `INSTALLER.bat`

### "Permission denied" sur fichier Excel

**Solution** : Fermez le fichier `Rapport_Complet_PMET.xlsx` s'il est ouvert dans Excel

### L'application ne se lance pas

**Vérifications** :

1. Python est bien installé : ouvrir cmd et taper `python --version`
2. Les dépendances sont installées : exécuter `INSTALLER.bat`
3. Tous les fichiers `.py` sont présents dans le dossier

## 📂 Déploiement sur plusieurs PC

### Option 1 : Copie manuelle

1. Copier le dossier complet `Koudaya`
2. Sur chaque nouveau PC, exécuter `INSTALLER.bat`

### Option 2 : Avec Python déjà configuré

Si Python et les bibliothèques sont déjà installés système :

- Seul le dossier `Koudaya` est nécessaire
- Lancer directement `LANCER_APPLICATION.bat`

### Fichiers essentiels à copier

```
Koudaya/
├── INSTALLER.bat              ← Script d'installation
├── LANCER_APPLICATION.bat     ← Lanceur
├── requirements.txt           ← Liste des dépendances
├── pmet_app.py               ← Application principale
├── analyse_pmet.py           ← Moteur d'analyse
├── csv_parser.py             ← Convertisseur CSV
├── generate_report.py        ← Générateur HTML
├── summary/                  ← Templates HTML/CSS
│   ├── style.css
│   └── [autres fichiers]
└── bg_train.png              ← Image de fond (optionnel)
```

## 🔄 Mise à jour

Pour mettre à jour sur un PC déjà configuré :

1. Remplacer les fichiers `.py` par les nouvelles versions
2. Vérifier `requirements.txt` pour de nouvelles dépendances
3. Si nécessaire, ré-exécuter `INSTALLER.bat`

## 📞 Support

Pour toute question ou problème :

- Vérifier que Python 3.8+ est installé
- Vérifier que toutes les bibliothèques sont installées (`INSTALLER.bat`)
- Consulter les messages d'erreur affichés

## 📄 Licence

Application développée pour SATEBA France - Usage interne

---

**Version** : 1.1 (avec support CSV direct)  
**Dernière mise à jour** : Janvier 2026
