# Les 7 Paramètres qui Contrôlent l'IA

Application web interactive pour comprendre et expérimenter avec les 7 paramètres qui influencent les réponses de l'intelligence artificielle.

**Pôle Formation UIMM-CVDL**

## Description

Cette application pédagogique permet d'explorer en temps réel comment les différents paramètres (Temperature, Top-P, Max Tokens, etc.) affectent les réponses générées par les modèles de langage comme Gemini.

## Fonctionnalités

- **7 paramètres interactifs** avec sliders et explications détaillées
- **Intégration API Gemini** pour tester en temps réel
- **Configurations prédéfinies** (Factuel, Équilibré, Créatif, Code, JSON)
- **Interface moderne** avec design sombre et animations fluides
- **Guide de référence rapide** pour une utilisation optimale
- **Entièrement en français** sans emojis

## Les 7 Paramètres

1. **Max Tokens** - Contrôleur de longueur
2. **Temperature** - Cadran de créativité
3. **Top-P** - Filtre de qualité
4. **Top-K** - Limiteur de candidats
5. **Frequency Penalty** - Tueur de répétitions
6. **Presence Penalty** - Moteur de nouveauté
7. **Stop Sequences** - Frein d'urgence

## Installation

Aucune installation requise ! Ouvrez simplement `index.html` dans votre navigateur.

```bash
# Cloner ou télécharger le projet
cd ai-parameters-demo

# Ouvrir dans le navigateur
start index.html  # Windows
open index.html   # macOS
xdg-open index.html  # Linux
```

## Utilisation

1. **Obtenir une clé API Gemini**
   - Visitez [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Créez une clé API gratuite
   - Copiez-la

2. **Utiliser l'application**
   - Ouvrez `index.html` dans votre navigateur
   - Collez votre clé API dans le champ prévu
   - Entrez un prompt
   - Choisissez un preset ou ajustez les paramètres manuellement
   - Cliquez sur "Générer la Réponse"

3. **Expérimenter**
   - Essayez différents presets
   - Modifiez un paramètre à la fois
   - Observez l'impact sur les réponses
   - Utilisez "Copier la Configuration" pour sauvegarder vos réglages

## Structure du Projet

```
ai-parameters-demo/
├── index.html          # Structure HTML de l'application
├── style.css           # Styles et design moderne
├── app.js              # Logique JavaScript et API Gemini
├── assets/
│   └── logo_uimm.jpg   # Logo UIMM-CVDL
└── README.md           # Ce fichier
```

## Technologies Utilisées

- **HTML5** - Structure sémantique
- **CSS3** - Design moderne avec glassmorphism
- **JavaScript (Vanilla)** - Pas de framework, code léger
- **Google Fonts** - Typographie Inter
- **Gemini API** - Génération de texte

## Presets Disponibles

### Factuel/Technique

- Temperature: 0.2
- Top-P: 0.9
- Penalties: 0.0
- **Usage**: Code, extraction de données, traduction

### Équilibré

- Temperature: 0.7
- Top-P: 0.9
- Frequency Penalty: 0.2
- **Usage**: Conversation générale, explications

### Créatif

- Temperature: 1.2
- Top-P: 0.95
- Frequency Penalty: 0.7
- Presence Penalty: 0.4
- **Usage**: Écriture créative, brainstorming

### Code

- Temperature: 0.2
- Stop Sequences: ```
- **Usage**: Génération de code

### JSON

- Temperature: 0.0
- Stop Sequences: }
- **Usage**: Extraction de données structurées

## Avertissements

- **Coûts API**: L'utilisation de l'API Gemini peut entraîner des frais selon votre quota
- **Clé API**: Votre clé est stockée uniquement dans votre navigateur (sessionStorage)
- **Données**: Aucune donnée n'est envoyée à un serveur tiers

## Support

Pour toute question ou problème, contactez le Pôle Formation UIMM-CVDL.

## Licence

© 2025 Pôle Formation UIMM-CVDL - Tous droits réservés

---

**Note**: Cette application est destinée à des fins pédagogiques pour comprendre le fonctionnement des paramètres de l'IA.
