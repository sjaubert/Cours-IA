![Logo Pôle Formation UIMM-CVDL](../../logo_uimm_placeholder.jpg)

# Pôle Formation UIMM-CVDL

---

# CONDUCTEUR - Formation "Intelligence Artificielle (IA)" - 2 Jours

## Présentation

Ce conducteur assemble deux formations déjà existantes et éprouvées pour couvrir l'intégralité du programme officiel publié sur le site du Pôle Formation UIMM-CVDL (formation "Intelligence Artificielle (IA)", 2 jours, 4 modules) :

- **Jour 1** = [00-demarrer/initiation-ia/Initiation_IA_7H.md](../../00-demarrer/initiation-ia/Initiation_IA_7H.md), restructuré pour intégrer un nouveau bloc Deep Learning
- **Jour 2** = [02-prompt-engineering/formation-journee/](../../02-prompt-engineering/formation-journee/README.md), Ateliers 1 à 3 inchangés, complétés par deux nouveaux ateliers (4 et 5)

Ce document ne remplace pas les guides détaillés existants : il sert de fil conducteur qui indique, module par module, quel guide utiliser et à quel moment.

---

## Correspondance Programme Officiel / Contenu Existant

| Module officiel (site Pôle Formation) | Couverture assurée par | Où |
|---|---|---|
| **Module 1** - Comprendre les fondamentaux de l'IA | Fondations du Machine Learning + nouveau bloc Deep Learning | Jour 1, 11h15-12h30 (restructuré) |
| **Module 2** - Explorer les IA génératives | L'IA Générative et ses 5 Piliers (tokens, fenêtre de contexte, température, hallucination, RAG) | Jour 1, 9h30-11h00 |
| **Module 3** - Maîtriser le prompt engineering | 6 Piliers du prompt + Exercices pratiques + Techniques avancées + Cas d'usage métier (usages concrets) | Jour 2, 9h15-15h30 (Ateliers 1 à 4) |
| **Module 4** - Identifier les limites et les enjeux de l'IA | Approche critique (hallucinations, biais de confirmation, biais culturel, itération) + en renfort : "Évaluer l'IA" du Jour 1 (piège de l'accuracy) | Jour 2, 15h45-16h45 (Atelier 5) + Jour 1, 13h30-14h45 |

**Valeur ajoutée hors périmètre officiel** (contenu existant conservé mais non demandé par le programme officiel) : le Module 4 du Jour 1, "Productivité et Outils (IA Agentique)" - agents, MCP, NotebookLM - reste dans le déroulé actuel. Il enrichit la formation mais peut être coupé si le temps manque, sans affaiblir la couverture des 4 modules officiels.

---

## JOUR 1 - D'après [Initiation_IA_7H.md](../../00-demarrer/initiation-ia/Initiation_IA_7H.md)

| Horaire | Contenu | Statut |
|---|---|---|
| 09:00 - 09:30 | Accueil et Introduction | Inchangé |
| 09:30 - 11:00 | Module 1 : L'IA Générative et ses 5 Piliers (Tokens, Fenêtre de Contexte, Température, Hallucination, RAG) + activité "Le Carnet de Prompts" | Inchangé |
| 11:00 - 11:15 | Pause | Inchangé |
| 11:15 - 12:30 | Module 2 : Fondations du Machine Learning + activité "Le Tri Intégral" | **Restructuré** (voir ci-dessous) |
| 12:30 - 13:30 | Déjeuner | Inchangé |
| 13:30 - 14:45 | Module 3 : Évaluer l'IA et la Connecter au Monde (accuracy, précision/rappel, API) + activité "Le Serveur Numérique" | Inchangé |
| 14:45 - 16:00 | Module 4 : Productivité et Outils - IA Agentique (Agent vs Chatbot, MCP, NotebookLM, Antigravity) + activité "Le Manager Agentique" | Inchangé - bonus hors périmètre officiel |
| 16:00 - 16:15 | Pause | Inchangé |
| 16:15 - 17:00 | Module 5 : Synthèse & Validation des Acquis (12 termes clés, quiz 10 questions, clôture) | Inchangé |

### Proposition de Restructuration - Module 2 (11h15-12h30, durée inchangée : 1h15)

Le script original de [Initiation_IA_7H.md](../../00-demarrer/initiation-ia/Initiation_IA_7H.md) ne détaille pas de sous-minutage à l'intérieur de ce module (théorie + activité "Le Tri Intégral" présentées comme un seul bloc de 1h15). Ce qui suit est **une proposition de découpage**, pas un contenu déjà chronométré dans le document source :

| Séquence | Durée proposée | Contenu |
|---|---|---|
| Théorie ML | 15 min | Donnée reine, Features, Train/Test, Overfitting/Underfitting, Prédire ≠ Comprendre (inchangé) |
| Activité "Le Tri Intégral" | 20 min | Inchangée |
| **NOUVEAU** - Deep Learning compact | 35 min | Voir ci-dessous |
| Transition / questions | 5 min | |
| **Total** | **75 min** | Durée du module inchangée (1h15) |

### Nouveau Bloc : Deep Learning Compact (35 min)

Source : [01-comprendre-ia/activites/A7_Reseaux_Neurones/](../../01-comprendre-ia/activites/A7_Reseaux_Neurones/README.md) (régression linéaire interactive + réseau de neurones configurable).

La séquence suggérée dans le README de ce module dure 85 minutes (Introduction 10 + Activité régression 20 + Pause/discussion 10 + Activité réseau de neurones 30 + Synthèse 15). Pour tenir dans les 35 minutes disponibles ici, voici une version compacte proposée :

| Étape | Durée | Détail |
|---|---|---|
| Présentation rapide | 5 min | De la droite de régression à la couche de neurones |
| [1_regression_lineaire.html](../../01-comprendre-ia/activites/A7_Reseaux_Neurones/1_regression_lineaire.html) | 10 min | Manipulation express du cas dureté/température, lecture du R² |
| [2_reseau_neurones.html](../../01-comprendre-ia/activites/A7_Reseaux_Neurones/2_reseau_neurones.html) | 15 min | Architecture à 1 couche, entraînement, test avec les sliders V1/V2/V3 |
| Mini-synthèse | 5 min | Pourquoi ajouter des couches, lien avec le Machine Learning vu juste avant |

Cette version compacte sacrifie l'exploration libre des architectures à 2-3 couches et le temps de manipulation étendu de la régression, réservés à la version complète de 85 minutes si ce module est animé seul, hors du conducteur 2 jours.

---

## JOUR 2 - D'après [formation-journee/](../../02-prompt-engineering/formation-journee/README.md)

Le programme original de cette journée (voir [formation-journee/README.md](../../02-prompt-engineering/formation-journee/README.md)) est découpé en durées de contenu ("Matinée 3h30", "Après-midi 3h30") sans horaires d'horloge ni pauses explicites. Le tableau ci-dessous propose des horaires complets, calés sur le rythme du Jour 1 :

| Horaire | Contenu | Statut |
|---|---|---|
| 09:00 - 09:15 | Accueil, lien avec le Jour 1 | **Nouveau** (non chronométré dans les guides existants) |
| 09:15 - 10:15 | Atelier 1 : Les 6 Piliers d'un Prompt Parfait | Inchangé |
| 10:15 - 11:15 | Atelier 2 : Exercices Pratiques | Inchangé |
| 11:15 - 11:30 | Pause | **Nouveau** (absente du programme original) |
| 11:30 - 13:00 | Atelier 3 : Techniques Avancées | Inchangé |
| 13:00 - 14:00 | Déjeuner | **Nouveau** (absent du programme original) |
| 14:00 - 15:30 | Atelier 4 : Cas d'Usage Métier | **Nouveau** (créé dans le cadre de cette mission) |
| 15:30 - 15:45 | Pause | **Nouveau** |
| 15:45 - 16:45 | Atelier 5 : Approche Critique | **Nouveau** (créé dans le cadre de cette mission) |

Fichiers du Jour 2, dans l'ordre :

1. [Atelier1_6Piliers_Guide.md](../../02-prompt-engineering/formation-journee/Atelier1_6Piliers_Guide.md) (ou [Atelier1_6Piliers.html](../../02-prompt-engineering/formation-journee/Atelier1_6Piliers.html) pour les stagiaires)
2. [Atelier2_Exercices_Pratiques.md](../../02-prompt-engineering/formation-journee/Atelier2_Exercices_Pratiques.md) (ou [.html](../../02-prompt-engineering/formation-journee/Atelier2_Exercices_Pratiques.html))
3. [Atelier3_Techniques_Avancees.md](../../02-prompt-engineering/formation-journee/Atelier3_Techniques_Avancees.md) (ou [.html](../../02-prompt-engineering/formation-journee/Atelier3_Techniques_Avancees.html))
4. [Atelier4_Cas_Usage_Metier.md](../../02-prompt-engineering/formation-journee/Atelier4_Cas_Usage_Metier.md) (ou [.html](../../02-prompt-engineering/formation-journee/Atelier4_Cas_Usage_Metier.html)) **(nouveau)**
5. [Atelier5_Approche_Critique.md](../../02-prompt-engineering/formation-journee/Atelier5_Approche_Critique.md) (ou [.html](../../02-prompt-engineering/formation-journee/Atelier5_Approche_Critique.html)) **(nouveau)**

---

## Écart Restant (Non Traité dans Cette Mission)

- Le programme original du Jour 2 prévoyait un "Bilan & Boîte à Outils" de 1h en fin de journée, toujours marqué "⚠️ À développer" dans [formation-journee/README.md](../../02-prompt-engineering/formation-journee/README.md). Avec les horaires proposés ci-dessus, la journée se termine à 16h45 sans ce temps de clôture. Deux options : construire ce Bilan séparément (hors périmètre de cette mission), ou terminer la journée sur une clôture informelle animée à l'oral à partir du message de clôture de l'Atelier 5.

---

## Matériel Global Nécessaire (2 Jours)

- Un poste avec accès web par participant (ou par binôme), avec accès à un outil IA conversationnel (ChatGPT, Claude, Gemini, Copilot)
- Accès internet fiable (recherche web pour la vérification factuelle du Jour 2, chargement de Three.js pour la visualisation 3D du Deep Learning au Jour 1)
- Vidéoprojecteur pour les démonstrations et corrigés
- Chronomètre visible
- Pour le Jour 2, Atelier 4, Cas 5 : un outil IA avec mode Code Interpreter / Analyse de données avancée, à vérifier en amont

---

*Créé par S. JAUBERT - Pôle Formation UIMM CVDL*
