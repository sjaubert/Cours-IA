---
title: "IA appliquée à l’industrie — Cas d’usage avec Gemini CLI (7h)"
author: "Pôle Formation UIMM Centre-Val de Loire — Formateur : S. JAUBERT"
date: "2025-10-25"
layout: default
---

<p align="center">
  <img src="assets/logo_uimm_placeholder.jpg" alt="Pôle Formation UIMM-CVDL" width="200"/>
</p>

# IA appliquée à l’industrie — Automatisation & MCP (7h)

## Objectifs pédagogiques
- Installer, mettre à jour et désinstaller **Gemini CLI** (Windows & macOS).
- Automatiser des tâches : **classement de PDF**, **rapports CSV**, **rédaction technique**.
- Vérifier et améliorer des **scripts**.
- Découvrir l’extension par **serveurs MCP**.

## Public & format
- Public : salariés/techniciens néophytes.
- Durée : **7h**. Pré-requis : savoir manipuler des dossiers/fichiers.

## Programme (7h)
**Matin** : Intro IA + Gemini CLI ; Activités 1–2.  
**Après-midi** : Activités 3–7 ; bonus MCP ; synthèse & plan d’action.

---

# Guide pratique — Gemini CLI

## Installation / Mise à jour / Désinstallation
### Windows (PowerShell)
```powershell
# Prérequis : Node.js (LTS)
npm install -g @google/gemini-cli
npm update -g @google/gemini-cli
npm uninstall -g @google/gemini-cli
gemini --version
```

### macOS (Terminal)
```bash
# Prérequis : Node.js (LTS)
sudo npm install -g @google/gemini-cli
sudo npm update -g @google/gemini-cli
sudo npm uninstall -g @google/gemini-cli
gemini --version
```

**Premier test :**
```bash
gemini "Donne trois idées d’automatisation utiles dans un atelier de production."
```

---

# Fiches Activités

## Activité 1 — Automatiser l’organisation de documents / factures (45 min)
**Objectif :** trier/renommer/ranger automatiquement des PDF par mois.  
**Matériel :** dossier `factures_incoming/` (20 PDF).  
**Étapes :**
1. Préparer le dossier de test.
2. Lancer la commande de tri et création de sous-dossiers.
3. Contrôler le résultat, corriger les exceptions.
**Prompt :**
```bash
gemini "Organise les PDF de factures_incoming/ dans des sous-dossiers mensuels selon la date de facture."
```
**Résultat :** arborescence propre, gain de temps.  
**Vigilance :** dates non extraites, doublons → **validation humaine**.

---

## Activité 2 — Générer automatiquement des rapports de petites analyses (45 min)
**Objectif :** produire un rapport synthétique à partir d’un `CSV`.  
**Étapes :**
1. Charger `maintenance_logs.csv`.
2. Demander un **rapport Markdown** avec indicateurs + recommandations.
3. Relire et ajuster.
**Prompt :**
```bash
gemini "Analyse maintenance_logs.csv et rédige un rapport : arrêts, causes, recommandations."
```
**Résultat :** rapport exploitable rapidement.  
**Vigilance :** confronter au terrain/données sources.

---

## Activité 3 — Aide à la rédaction de documentation/procédures (45 min)
**Objectif :** produire un mode opératoire clair et sûr.  
**Étapes :** lister EPI/risques ; demander un mode opératoire ; faire valider par un expert.  
**Prompt :**
```bash
gemini "Rédige une procédure pour le changement de filtre machine X, avec EPI et étapes numérotées."
```
**Résultat :** document prêt à valider.  
**Vigilance :** vocabulaire interne, pictos, photos.

---

## Activité 4 — Vérification de code simple / script industriel (45 min)
**Objectif :** détecter erreurs & améliorer robustesse.  
**Étapes :** analyser script fragile ; demander version améliorée ; comparer.  
**Prompt :**
```bash
gemini "Analyse log_extract.py : propose une version robuste avec logs et gestion d’erreurs."
```
**Résultat :** script plus fiable.  
**Vigilance :** **revue humaine** avant déploiement.

---

## Activité 5 — Brainstorming de nouveaux usages IA (30 min)
**Objectif :** identifier 2 idées réalisables en 1–2 jours par service.  
**Étapes :** travail par groupe (maintenance/qualité/RH/logistique), restitution, priorisation.  
**Résultat :** backlog d’expérimentations.

---

## Activité 6 — Analyse d’images et détection d’anomalies (45 min)
**Objectif :** découvrir l’IA visuelle pour qualité/maintenance.  
**Étapes :** comparer images normales/défectueuses ; décrire anomalies ; limites (éclairage, angle).  
**Prompt :**
```bash
gemini "Analyse image1.jpg et image2.jpg : signale les anomalies visibles."
```
**Résultat :** sensibilisation au contrôle visuel assisté.

---

## Activité 7 — Préparer un assistant IA interne (30 min)
**Objectif :** définir un persona d’assistant pour un service.  
**Étapes :** périmètre/ton/limites ; 10 questions fréquentes ; prompt système.  
**Prompt :**
```bash
gemini "Tu es un assistant sécurité atelier : réponds brièvement, cite la procédure interne RS-SEC."
```
**Résultat :** première spécification d’assistant.

---

# Bonus — Serveurs MCP (Model Context Protocol)

## À quoi ça sert ?
Étendre Gemini CLI avec des **outils/APIs** : navigation/test web (Playwright), cloud (Firebase), 3D (Blender), code (GitHub), etc.

## Exemple de configuration (extrait à adapter)
```json
"mcpServers": {
  "mcp-server-firecrawl": {
    "command": "npx",
    "args": ["-y", "firecrawl-mcp"],
    "env": { "FIRECRAWL_API_KEY": "fc-***" }
  },
  "context7": { "command": "npx", "args": ["-y", "@upstash/context7-mcp"] },
  "playwright": { "command": "npx", "args": ["@playwright/mcp@latest"] },
  "firebase": { "command": "npx", "args": ["-y", "firebase-tools@latest", "experimental:mcp"] },
  "blender": { "command": "uvx", "args": ["blender-mcp"] },
  "github": {
    "httpUrl": "https://api.githubcopilot.com/mcp/",
    "headers": { "Authorization": "ghp_***" },
    "timeout": 5000
  }
}
```

## Bonnes pratiques
- **Ne jamais exposer des clés** : utiliser des **variables d’environnement**.
- Commencer par un serveur simple (**playwright**), puis enrichir.
- Journaliser ce que fait l’IA, garder une **revue humaine**.

---

# Synthèse & plan d’action
- Chaque participant choisit **un cas d’usage** à tester sous 15 jours.
- Définir validation, métriques de gain, et plan de déploiement.

## Annexes
- Check-list, bibliographie, quiz (10 questions + corrigé).
