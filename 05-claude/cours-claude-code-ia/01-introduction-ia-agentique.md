# Module 1 — Introduction à l'IA Agentique
## Comprendre la révolution Claude Code

> **Durée :** 1h30  
> **Objectif :** Situer Claude Code dans le paysage IA et comprendre pourquoi il représente un changement de paradigme

---

## 1.1 De l'assistant à l'agent : un saut qualitatif

### Ce que vous connaissez déjà

La plupart d'entre vous ont déjà utilisé un outil IA comme ChatGPT, Claude, ou Copilot. Ces outils répondent à des questions, rédigent des textes, résument des documents. Ils sont réactifs : vous posez une question, ils répondent. Point.

### La limite du chatbot classique

Imaginez que vous demandez à un assistant de **réorganiser tous vos fichiers de projet, mettre à jour votre tableau de bord, envoyer un email de synthèse à votre équipe et créer un rapport PDF** — en une seule instruction.

Un chatbot classique vous dira comment faire. Un **agent IA** le fera.

### La définition d'un agent IA

Un agent IA est un système capable de :

1. **Percevoir** son environnement (lire des fichiers, des emails, des bases de données)
2. **Planifier** une séquence d'actions pour atteindre un objectif
3. **Agir** de façon autonome (écrire, modifier, exécuter, envoyer)
4. **Vérifier** le résultat et s'adapter si nécessaire

> **Analogie :** Un chatbot, c'est un expert que vous consultez. Un agent IA, c'est un collaborateur qui prend en charge la tâche de bout en bout.

---

## 1.2 Qu'est-ce que Claude Code ?

### Présentation

Claude Code est un outil d'IA agentique développé par **Anthropic**, accessible via une interface en ligne de commande (CLI) et intégré à de nombreux environnements de travail.

Contrairement aux assistants IA classiques, Claude Code peut :

- **Lire et écrire des fichiers** sur votre ordinateur ou serveur
- **Exécuter des commandes** (scripts, tests, transformations de données)
- **Naviguer dans une base de code** ou une arborescence de documents
- **Piloter des workflows complexes** en plusieurs étapes
- **Déléguer des sous-tâches** à d'autres agents spécialisés
- **S'intégrer à des outils tiers** (GitHub, Slack, calendriers, bases de données…)

### Quelques chiffres pour mesurer l'ampleur

- **+81 000 étoiles GitHub** en moins d'un an
- **+20 millions de commits** touchés sur plus d'un million de dépôts
- Accepté dans le **marketplace officiel de plugins Anthropic** dès janvier 2026
- Utilisé dans des entreprises de toutes tailles, du startup à l'entreprise du CAC 40

### Les modèles Claude disponibles (2026)

| Modèle | Identifiant | Usage recommandé |
|--------|-------------|-----------------|
| Claude Opus 4.6 | `claude-opus-4-6` | Tâches complexes, raisonnement avancé |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | Équilibre qualité/coût, usage quotidien |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | Tâches rapides, coût minimal |

---

## 1.3 Pourquoi maintenant ?

### Trois convergences simultanées

**1. La maturité des modèles de langage**  
Les LLM (Large Language Models) ont franchi un seuil de compétence qui leur permet de suivre des instructions complexes, de raisonner sur plusieurs étapes et de gérer des contextes longs. Claude Opus 4.6 peut traiter des documents de plusieurs centaines de pages en une seule session.

**2. L'écosystème d'outils**  
En moins de deux ans, une communauté mondiale de développeurs a construit des centaines d'extensions, de workflows et d'intégrations. Les 15 dépôts GitHub que nous allons étudier en sont la meilleure illustration.

**3. L'accessibilité**  
Ce qui nécessitait autrefois une équipe de data scientists coûteuse est aujourd'hui accessible via une interface texte ou une application de bureau — pour quelques euros par mois.

### Le changement de paradigme pour les entreprises

| Avant | Avec les agents IA |
|-------|-------------------|
| Une tâche, une personne | Une instruction, des dizaines d'actions |
| Automatisation = développement | Automatisation = description en langage naturel |
| L'expert fait le travail | L'expert supervise et valide |
| Le savoir est dans la tête | Le savoir est capturé dans des instructions réutilisables |

---

## 1.4 L'écosystème en cinq grandes familles

La communauté Claude Code a produit des ressources regroupables en **cinq catégories** :

### 1. Skills et plugins (fichiers SKILL.md)
Des "compétences" que l'on greffe sur Claude pour lui donner des capacités spécifiques. Exemple : un skill "rédaction de compte-rendu de réunion" ou "analyse de données RH".

### 2. Frameworks d'agents
Des architectures complètes pour orchestrer plusieurs agents qui travaillent en parallèle sur une même tâche, avec des rôles définis (chef de projet, réviseur, testeur…).

### 3. Bibliothèques de prompts
Des collections de prompts systèmes éprouvés, prêts à l'emploi, qui définissent le comportement de l'agent pour des cas d'usage précis.

### 4. Ressources d'apprentissage
Des guides pas-à-pas, des méthodologies, des manuels de bonnes pratiques — dont ce cours s'inspire largement.

### 5. Intégrations CI/CD
Des outils qui connectent Claude Code directement aux pipelines automatisés : revue de code, tests, déploiement, génération de documentation.

> **Point clé :** Les meilleurs dépôts combinent plusieurs de ces catégories. C'est ce qui les rend si puissants.

---

## 1.5 Ce que cette formation vous apportera

### Pour tous les profils

- Comprendre le vocabulaire et les concepts pour ne plus être dépassé par les discussions sur l'IA dans votre entreprise
- Identifier les cas où un agent IA peut vous faire gagner du temps (et ceux où ce n'est pas pertinent)
- Évaluer les risques et les limites de ces technologies

### Selon votre métier

**Administratifs :** automatiser la gestion documentaire, la rédaction de courriers, la consolidation de données  
**Ingénieurs :** accélérer la documentation, les revues de conception, la génération de code de test  
**IT :** déployer des pipelines IA, configurer des agents, sécuriser les workflows automatisés  
**RH :** automatiser l'onboarding, analyser les retours d'entretien, structurer les fiches de poste  
**Formateurs :** créer des contenus pédagogiques, adapter des parcours, analyser les résultats d'évaluation

---

## Points clés à retenir

- Un agent IA agit, pas seulement répond. C'est la différence fondamentale.
- Claude Code peut lire, écrire, exécuter et orchestrer — de façon quasi-autonome.
- L'écosystème communautaire multiplie les capacités de base par 10, 100, voire plus.
- Cette technologie est accessible maintenant, sans formation technique préalable avancée.

---

## Questions de révision

1. Quelle est la différence fondamentale entre un chatbot et un agent IA ?
2. Citez trois actions qu'un agent Claude Code peut réaliser qu'un assistant classique ne peut pas faire.
3. Dans votre métier, quelle tâche répétitive pourrait bénéficier d'une automatisation par agent IA ?

---

*Prochain module : [Les concepts fondamentaux →](02-concepts-fondamentaux.md)*
