# Module 6 — Guide de Démarrage Pratique
## Votre feuille de route personnalisée

> **Durée :** 2h  
> **Objectif :** Repartir avec un plan d'action concret et les ressources pour avancer seul

---

## 6.1 Les premières 24 heures

### Ce que vous pouvez faire dès aujourd'hui

Sans aucune configuration technique, vous pouvez commencer à utiliser Claude via [claude.ai](https://claude.ai) pour des tâches immédiates.

**Exercice de démarrage — 30 minutes ce soir :**
1. Ouvrez [claude.ai](https://claude.ai)
2. Choisissez une tâche que vous faites régulièrement (rédaction, analyse, synthèse)
3. Utilisez la structure de prompt apprise au module 5 : Rôle + Contexte + Tâche + Format
4. Observez le résultat, notez ce qui manque
5. Affinez le prompt et recommencez

Ce premier cycle vous donnera plus de confiance que toute lecture supplémentaire.

---

## 6.2 Feuilles de route par profil

### Administratifs — Les 30 premiers jours

**Semaine 1 — Prise en main**
- Créer un compte Claude sur [claude.ai](https://claude.ai)
- Tester 3 tâches de rédaction courante (email, compte-rendu, résumé)
- Explorer le dépôt [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) — section "prompting patterns"

**Semaine 2 — Premier workflow**
- Identifier votre tâche la plus chronophage et répétitive
- Rédiger un CLAUDE.md pour cette tâche (template fourni ci-dessous)
- Tester sur 3 vrais cas de votre quotidien

**Semaine 3 — Intégration**
- Explorer le dépôt [Claude-Code-Projects-Index](https://github.com/danielrosehill/Claude-Code-Projects-Index) pour trouver des cas similaires au vôtre
- Adapter un template existant à votre contexte
- Partager vos retours avec l'équipe

**Semaine 4 — Optimisation**
- Identifier les points faibles de votre workflow
- Lire [claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) pour les sections pertinentes
- Formaliser votre meilleur workflow dans un document partageable

**Ressource prioritaire :** [Claude-Code-Projects-Index](https://github.com/danielrosehill/Claude-Code-Projects-Index) — 75+ projets non-techniques documentés

---

### Ingénieurs — Les 30 premiers jours

**Semaine 1 — Exploration**
- Tester Claude sur un vrai problème d'analyse (données, AMDEC, rapport...)
- Explorer [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) pour cartographier les outils disponibles

**Semaine 2 — Méthodologie**
- Étudier le dépôt [superpowers](https://github.com/obra/superpowers) — lire le README complet
- Appliquer les phases Spec + Plan + TDD à un prochain projet réel
- Tester la structure d'équipe multi-agents sur un rapport de conception

**Semaine 3 — Skills**
- Explorer [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) pour les skills d'ingénierie
- Tester les skills de documentation technique et de revue de conception

**Semaine 4 — Production**
- Mettre en place un workflow de documentation automatisée
- Calculer le ROI réel sur un premier cas d'usage
- Documenter les leçons apprises pour l'équipe

**Ressource prioritaire :** [superpowers](https://github.com/obra/superpowers) — la méthodologie de référence

---

### IT — Les 30 premiers jours

**Semaine 1 — Infrastructure**
- Cloner et explorer [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- Lire la documentation sur la gestion de la sécurité et des hooks
- Évaluer les MCP disponibles pour votre environnement

**Semaine 2 — Déploiement pilote**
- Déployer un agent sur un cas d'usage interne non critique
- Tester [claude-code-action](https://github.com/anthropics/claude-code-action) sur un dépôt de test
- Configurer les logs et l'audit

**Semaine 3 — Spécialisation**
- Explorer [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) pour des agents IT spécialisés
- Tester l'airis-mcp-gateway pour réduire la consommation de tokens

**Semaine 4 — Scale**
- Définir la politique de gouvernance (template fourni au module 5)
- Former un premier groupe d'utilisateurs métier pilotes
- Mettre en place les métriques de suivi

**Ressource prioritaire :** [everything-claude-code](https://github.com/affaan-m/everything-claude-code) — l'infrastructure de référence

---

### RH — Les 30 premiers jours

**Semaine 1 — Familiarisation**
- Tester Claude sur l'analyse d'un lot de CV anonymisés
- Tester la génération d'une fiche de poste à partir d'un brief
- Explorer [Claude-Code-Projects-Index](https://github.com/danielrosehill/Claude-Code-Projects-Index) section "HR & administration"

**Semaine 2 — Processus de recrutement**
- Créer un CLAUDE.md pour l'analyse de candidatures (modèle au module 4)
- Tester sur 10 vrais CV avec grille d'évaluation comparée (humain vs agent)
- Évaluer la qualité et les biais potentiels

**Semaine 3 — Processus documentaires**
- Automatiser la génération de contrats types (avec validation juridique obligatoire)
- Tester le workflow d'onboarding automatisé
- Explorer les subagents RH dans [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)

**Semaine 4 — Analyse et reporting**
- Tester l'analyse des entretiens annuels (données anonymisées)
- Créer un tableau de bord RH automatisé
- Évaluer les enjeux éthiques et de conformité RGPD

**Ressource prioritaire :** [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) — agents spécialisés RH

---

### Formateurs — Les 30 premiers jours

**Semaine 1 — Création de contenu**
- Tester la génération d'un module de formation sur un sujet maîtrisé
- Évaluer la qualité pédagogique (objectifs, progression, évaluation)
- Explorer [claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) — un modèle de documentation auto-mise-à-jour

**Semaine 2 — Adaptation**
- Tester la déclinaison d'un contenu existant en 3 niveaux
- Tester la génération de QCM et de mises en situation
- Explorer [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) pour les skills de rédaction

**Semaine 3 — Évaluation**
- Mettre en place un workflow de correction automatisée
- Tester la génération de feedback personnalisé
- Explorer les limitations et les ajustements nécessaires

**Semaine 4 — Intégration dans le parcours**
- Créer un template de workflow "formation complète" (contenu + évaluation + feedback)
- Calculer le gain de temps sur un cycle complet
- Former un collègue formateur à l'outil

**Ressource prioritaire :** [claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) — référence toujours à jour

---

## 6.3 Template CLAUDE.md de démarrage

Voici un template universel à adapter pour votre premier workflow :

```markdown
# [Nom de votre workflow]

## Mon rôle et contexte
Je suis [votre poste] dans [votre entreprise/secteur].
Ce workflow m'aide à [description de la tâche].

## Ce que tu dois faire
[Description précise de la tâche en 3 à 5 lignes]

## Règles importantes
- [Règle 1 : ce qui est obligatoire]
- [Règle 2 : ce qu'on ne fait jamais]
- [Règle 3 : contrainte de format ou de style]

## Format de sortie attendu
- Format : [Word / Excel / texte / tableau / ...]
- Longueur : [X pages / X lignes / ...]
- Structure : [Plan attendu]

## Exemples de référence
- Bon exemple : [décrire ou joindre]
- À éviter : [décrire ce qu'on ne veut pas]

## Validation humaine obligatoire
Avant de [action critique], attends ma confirmation explicite.

## Données sensibles
Ne jamais traiter : [lister les données confidentielles]
```

---

## 6.4 Exercices pratiques

### Exercice 1 — Le premier prompt (15 minutes)

**Contexte :** Vous devez rédiger un email à un partenaire externe pour reporter une réunion de 15 jours.

**À faire :**
1. Rédigez le prompt en respectant la structure Rôle + Contexte + Tâche + Format + Contraintes
2. Soumettez à Claude
3. Évaluez le résultat sur 3 critères : ton, précision, utilisabilité
4. Affinez et relancez

---

### Exercice 2 — Le CLAUDE.md de votre tâche clé (30 minutes)

**À faire :**
1. Identifiez la tâche répétitive qui vous prend le plus de temps
2. Remplissez le template CLAUDE.md ci-dessus pour cette tâche
3. Testez avec Claude en commençant par : "Voici mon contexte de travail [coller le CLAUDE.md]. Ma tâche d'aujourd'hui est..."
4. Notez ce qui fonctionne et ce qui nécessite des ajustements

---

### Exercice 3 — Le workflow en 7 phases (45 minutes, en binôme)

**À faire :**
Choisissez un livrable réel à produire (rapport, analyse, formation...) et appliquez les 3 premières phases de la méthode Superpowers :
1. Phase Brainstorm (10 min) : Explorer le problème avec Claude
2. Phase Spec (10 min) : Rédiger la spécification
3. Phase Plan (10 min) : Décomposer en étapes
4. Comparez avec ce que vous auriez fait sans méthode

---

### Exercice 4 — L'analyse de ressource GitHub (20 minutes)

**À faire :**
Choisissez l'une des 15 ressources GitHub qui vous a le plus interpellé. Ouvrez-la sur GitHub et répondez :
1. Quel problème précis résout-elle ?
2. Quelles sont les 3 premières étapes pour l'utiliser dans votre contexte ?
3. Quel serait le premier cas d'usage dans votre équipe ?

---

## 6.5 Ressources de référence consolidées

### Les 15 dépôts GitHub de l'écosystème

| # | Dépôt | Priorité par profil | Lien |
|---|-------|--------------------|----|
| 1 | everything-claude-code | IT ★★★ / Ing ★★ | [github.com/affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) |
| 2 | superpowers | Tous ★★★ | [github.com/obra/superpowers](https://github.com/obra/superpowers) |
| 3 | claude-code-action | IT ★★★ / Ing ★★ | [github.com/anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) |
| 4 | awesome-claude-code | Découverte ★★★ | [github.com/hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) |
| 5 | awesome-claude-code-subagents | IT ★★★ / RH ★★ | [github.com/VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) |
| 6 | learn-claude-code | IT ★★★ / Form ★★ | [github.com/shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) |
| 7 | claude-code-best-practice | Tous ★★★ | [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) |
| 8 | gstack | Managers ★★★ | [github.com/garrytan/gstack](https://github.com/garrytan/gstack) |
| 9 | claude-code-templates | Démarrage ★★★ | [github.com/davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) |
| 10 | get-shit-done | Tous ★★★ | [github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) |
| 11 | system-prompts-and-models | IT ★★ / Ing ★★ | [github.com/x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) |
| 12 | claude-code-system-prompts | IT avancé ★★ | [github.com/Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) |
| 13 | awesome-agent-skills | Ing ★★★ / IT ★★ | [github.com/VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) |
| 14 | Claude-Code-Projects-Index | Non-tech ★★★ | [github.com/danielrosehill/Claude-Code-Projects-Index](https://github.com/danielrosehill/Claude-Code-Projects-Index) |
| 15 | claude-code-handbook | Tous ★★★ | [github.com/ThamJiaHe/claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) |

### Documentation officielle Anthropic

- [Documentation principale](https://docs.claude.com)
- [Support utilisateurs](https://support.claude.com)
- [Guide Prompt Engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Interface Claude](https://claude.ai)

---

## 6.6 Les pièges à éviter

### Piège 1 — La perfection du premier coup
L'agent ne produira jamais quelque chose de parfait au premier essai. C'est normal. Planifiez 2 à 3 itérations pour tout livrable important.

### Piège 2 — L'absence de validation humaine
Plus vous gagnez en confiance, plus vous serez tenté de ne pas relire. Résistez. Surtout sur les communications externes et les données sensibles.

### Piège 3 — Le prompt trop court
"Aide-moi avec mon rapport" ne donnera jamais un bon résultat. Investissez 5 minutes de plus dans votre prompt pour économiser 1 heure de correction.

### Piège 4 — Oublier les limites légales et RGPD
Les données personnelles, les informations couvertes par le secret professionnel et les données sensibles ne doivent pas être copiées dans un système IA sans protocole de sécurité établi par votre entreprise.

### Piège 5 — Partir sur des cas complexes
Commencez par des tâches simples, maîtrisez-les, puis montez en complexité. Les "tâches complexes dès le départ" génèrent de la frustration et de la méfiance vis-à-vis de l'outil.

---

## 6.7 Tableau de bord de progression personnelle

Utilisez ce tableau pour suivre votre progression après la formation :

```
SEMAINE 1
[ ] J'ai utilisé Claude pour une vraie tâche professionnelle
[ ] J'ai rédigé mon premier prompt structuré (Rôle + Contexte + Tâche + Format)
[ ] J'ai exploré au moins 2 dépôts GitHub de la liste

SEMAINE 2-4
[ ] J'ai créé mon premier CLAUDE.md
[ ] J'ai appliqué la méthode Spec + Plan + Produce sur un projet
[ ] J'ai calculé le temps gagné sur au moins une tâche

MOIS 2-3
[ ] J'ai formé au moins un collègue à un workflow que j'utilise
[ ] J'ai contribué à définir les règles de gouvernance de mon équipe
[ ] J'ai documenté et partagé mon meilleur cas d'usage

MOIS 6
[ ] J'ai au moins 3 workflows stables et régulièrement utilisés
[ ] L'IA est intégrée dans mon organisation du travail habituelle
[ ] Je peux évaluer de nouveaux outils IA de façon autonome
```

---

## 6.8 Pour aller plus loin

### Communautés actives

- **Reddit** : r/ClaudeAI — actualités, retours d'expérience, questions
- **Discord Anthropic** : communauté officielle des développeurs et utilisateurs
- **LinkedIn** : suivre les créateurs des dépôts étudiés (Jesse Vincent / obra, Garry Tan, Daniel Rosehill...)

### Veille sur l'écosystème

- [claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) — mis à jour automatiquement chaque semaine
- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — nouvelles ressources ajoutées régulièrement
- Les notes de version Claude sur [docs.claude.com](https://docs.claude.com)

### Formation complémentaire suggérée

Pour les profils IT/Ingénieurs qui veulent approfondir :
- Lire [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) en entier (environ 10h)
- Construire un agent de bout en bout sur un vrai problème interne
- Contribuer à l'un des dépôts open source de l'écosystème

---

## Conclusion de la formation

### Ce que vous avez acquis

Au terme de ces deux jours, vous disposez de :

**La compréhension** — Vous savez ce qu'est un agent IA, comment il fonctionne et pourquoi l'écosystème Claude Code est devenu la référence.

**Les connaissances** — Vous connaissez les 15 ressources GitHub incontournables et savez lesquelles correspondent à votre profil et vos besoins.

**Les méthodes** — Vous avez les outils pour travailler efficacement avec Claude : prompts structurés, workflows en phases, gestion du contexte, orchestration d'agents.

**Les cas d'usage** — Vous avez identifié au moins 3 applications concrètes dans votre métier, avec les prompts et workflows correspondants.

**La feuille de route** — Vous repartez avec un plan des 30 prochains jours adapté à votre profil.

### Le message final

L'IA n'est pas un outil magique qui remplace la réflexion humaine. C'est un amplificateur : elle décuple ce que vous savez faire et vous libère du temps pour ce qui compte vraiment — le jugement, la créativité, la relation.

Les professionnels qui tireront le meilleur de cette révolution ne seront pas forcément les plus techniques. Ce seront ceux qui sauront **définir clairement ce qu'ils veulent**, **structurer leur façon de travailler** et **maintenir leur expertise métier** au centre des processus.

C'est ce que vous avez appris ici. Maintenant, à vous de jouer.

---

*Module précédent : [← Méthodologies](05-methodologies-pratiques.md) | [Retour au sommaire →](README.md)*

---

*Formation réalisée en mai 2026 — Basée sur l'analyse de l'écosystème Claude Code*  
*Sources principales : les 15 dépôts GitHub référencés tout au long du cours*
