# Module 3 — Les 15 Ressources GitHub de Référence
## Analyse détaillée de l'écosystème Claude Code

> **Durée :** 3h  
> **Objectif :** Connaître les 15 dépôts GitHub incontournables, comprendre leur valeur et savoir lesquels correspondent à votre profil

---

## 3.0 Comment lire ce module

Chaque ressource est présentée selon la même structure :
- **Ce que c'est** — description accessible
- **Ce qu'il contient** — les éléments concrets
- **Pour qui ?** — profils qui en tireront le plus de valeur
- **Valeur ajoutée** — ce que ça change concrètement
- **Lien GitHub** — accès direct

Les ressources sont regroupées en **5 catégories** qui correspondent aux 5 familles de l'écosystème décrites au module 1.

---

## Catégorie A — Les harnais complets (infrastructure clé en main)

Ces dépôts vous donnent une infrastructure complète : agents, hooks, règles, mémoire, sécurité — tout est préconfiguré et prêt à l'emploi.

---

### Ressource 1 — everything-claude-code

**Le harnais le plus complet disponible**

🔗 [github.com/affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)

#### Ce que c'est
Créé par Affaan Mustafa après dix mois d'usage quotidien en conditions réelles, ce dépôt a remporté le hackathon Anthropic × Forum Ventures. Il couvre une surface exceptionnellement large et fonctionne non seulement avec Claude Code, mais aussi avec Codex, OpenCode et Cursor — depuis un seul dépôt.

#### Ce qu'il contient
- Configuration complète d'agents et sous-agents
- Hooks et règles de comportement
- Configuration de serveurs MCP
- Système d'optimisation de la mémoire
- Module de scan de sécurité
- Boucles d'apprentissage continu
- Workflows de recherche
- Support de 12 écosystèmes de langages (v1.9.0)
- Routage de modèles via NanoClaw v2

#### Pour qui ?
✅ Équipes IT qui veulent déployer une infrastructure IA en production  
✅ Ingénieurs seniors qui veulent personnaliser profondément leur environnement  
⚠️ Nécessite un investissement de configuration initial — pas pour les débutants

#### Valeur ajoutée
Plutôt que de bricoler des configurations séparées pour chaque outil, vous disposez d'une base unifiée, éprouvée en production, avec des pratiques de sécurité intégrées dès le départ.

---

### Ressource 2 — superpowers

**Le workflow TDD agentique le plus influent de l'écosystème**

🔗 [github.com/obra/superpowers](https://github.com/obra/superpowers)  
⭐ **94 000 étoiles GitHub** — Accepté dans le marketplace officiel Anthropic (janvier 2026)

#### Ce que c'est
Créé par Jesse Vincent, ce dépôt a redéfini ce que signifie "bien utiliser Claude Code". Son idée centrale : appliquer la rigueur d'un développeur senior à chaque interaction avec l'agent.

#### Ce qu'il contient
Un workflow structuré en **7 phases** :
1. **Brainstorm** — Exploration du problème sans se précipiter sur les solutions
2. **Spec** — Rédaction d'une spécification précise de ce qu'on veut obtenir
3. **Plan** — Découpage en étapes concrètes et vérifiables
4. **TDD** — Définition des tests *avant* de produire quoi que ce soit
5. **Subagent Development** — Développement délégué aux agents spécialisés
6. **Review** — Revue critique du résultat
7. **Finalize** — Livraison propre

**Sa règle la plus radicale :** tout travail produit avant la définition des critères de validation est automatiquement supprimé.

#### Pour qui ?
✅ Équipes qui veulent homogénéiser leurs pratiques de travail avec l'IA  
✅ Managers qui souhaitent encadrer l'usage de l'IA dans leurs équipes  
✅ Tout profil souhaitant sortir du "demander puis corriger" pour aller vers "définir puis valider"

#### Valeur ajoutée
Simon Willison (référence mondiale sur les outils IA) qualifie ce projet de "fascinant" et son créateur de "l'un des utilisateurs les plus créatifs d'agents de codage". Le résultat concret : Claude peut travailler des heures en autonomie sans dériver du plan initial.

---

### Ressource 9 — claude-code-templates

**Les configurations prêtes à l'emploi**

🔗 [github.com/davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)

#### Ce que c'est
Une bibliothèque de configurations préconstruites pour les cas d'usage les plus courants. Vous choisissez un template, vous l'adaptez à votre contexte, et vous êtes opérationnel.

#### Ce qu'il contient
- Configurations d'agents pour différents types de projets
- Commandes personnalisées prêtes à l'emploi
- Hooks préconfigurés
- Paramètres recommandés
- Intégrations MCP courantes
- Templates de projets par type d'activité

#### Pour qui ?
✅ Toute personne qui veut commencer rapidement sans configuration manuelle  
✅ Équipes qui standardisent leurs pratiques Claude Code  
✅ Formateurs cherchant des exemples de configurations à montrer

#### Valeur ajoutée
Élimine la phase de configuration initiale — souvent la plus décourageante pour les nouveaux utilisateurs.

---

## Catégorie B — Les frameworks méthodologiques

Ces dépôts ne donnent pas des outils, mais des méthodes de travail. Ils structurent la manière dont vous interagissez avec Claude.

---

### Ressource 8 — gstack

**L'IA comme équipe de spécialistes**

🔗 [github.com/garrytan/gstack](https://github.com/garrytan/gstack)

#### Ce que c'est
La configuration personnelle de Garry Tan, rendue publique. Elle illustre concrètement le concept d'"équipe d'agents" : plutôt qu'un agent généraliste, vous définissez des rôles nommés avec des responsabilités précises.

#### Ce qu'il contient
Des rôles structurés via des skills et commandes slash :
- **CEO** — vision stratégique, arbitrages
- **Designer** — création visuelle et UX
- **Engineering Manager** — coordination technique
- **Release Manager** — gestion des livraisons
- **Doc Engineer** — documentation
- **QA** — assurance qualité

#### Pour qui ?
✅ Managers qui pilotent des projets complexes  
✅ Équipes projets qui veulent des handoffs clairs entre spécialités  
✅ Tout profil intéressé par l'orchestration d'agents

#### Valeur ajoutée
Montre que l'organisation en "équipe IA" n'est pas de la théorie — c'est une pratique quotidienne d'un professionnel de référence dans l'écosystème tech.

**Exemple concret pour l'industrie :**
```
Brief projet : "Préparer l'audit ISO 9001 du mois prochain"
→ Agent "Analyste Qualité" : collecte les indicateurs
→ Agent "Rédacteur" : prépare la documentation
→ Agent "Réviseur" : vérifie la conformité des livrables
→ Agent "Coordinateur" : crée le planning des revues
```

---

### Ressource 10 — get-shit-done

**La méthode anti-dérive pour les projets longs**

🔗 [github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done)

#### Ce que c'est
Une réponse directe au problème de "context drift" — ce phénomène où un agent perd le fil de sa mission au fil d'une longue session de travail.

#### Ce qu'il contient
Un workflow en 5 étapes explicites :
1. **Discussion** — Cadrage du besoin
2. **Planning** — Décomposition en tâches
3. **Execution** — Réalisation par étapes
4. **Verification** — Validation de chaque livrable
5. **Shipping** — Livraison finale

Chaque étape a des critères d'entrée et de sortie explicites.

#### Pour qui ?
✅ Tous profils travaillant sur des projets complexes ou multi-étapes  
✅ Particulièrement utile pour les rédactions longues, les analyses de données étendues

#### Valeur ajoutée
Résout le problème numéro un des utilisateurs avancés de Claude : les sessions longues qui "partent dans tous les sens". Avec cette méthode, l'agent reste sur les rails.

---

### Ressource 7 — claude-code-best-practice

**Le guide de référence des praticiens**

🔗 [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)

#### Ce que c'est
Une base de connaissances vivante, documentant ce qui fonctionne réellement en pratique quotidienne. Inclut des retours directs du créateur de Claude Code (Boris Cherny) et d'ingénieurs Anthropic.

#### Ce qu'il contient
- Patterns d'utilisation des commandes, skills, subagents et hooks
- Conseils de gestion de session
- Stratégies de prompting éprouvées
- Gestion du contexte
- Techniques de débogage
- Conseils de planification

#### Pour qui ?
✅ Toute personne qui utilise Claude Code régulièrement et veut progresser  
✅ Formateurs cherchant les meilleures pratiques officiellement reconnues

#### Valeur ajoutée
C'est le chemin le plus court de "ça marche parfois" à "ça marche systématiquement". Opinionné et direct.

---

## Catégorie C — Les bibliothèques de skills et sous-agents

Ces dépôts vous donnent des compétences spécialisées prêtes à être greffées sur Claude.

---

### Ressource 5 — awesome-claude-code-subagents

**La bibliothèque de 100+ sous-agents spécialisés**

🔗 [github.com/VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)

#### Ce que c'est
Une collection de définitions de sous-agents couvrant un éventail remarquable de domaines professionnels : développement, sécurité, documentation, recherche, **administration de la santé**, et bien d'autres.

#### Ce qu'il contient
- 100+ définitions de sous-agents spécialisés
- Routage automatique vers le modèle Claude optimal selon la tâche
- **airis-mcp-gateway** : un agrégateur Docker qui regroupe 60+ outils en 7 méta-outils (réduction de 97% de la consommation de tokens de contexte)
- Script d'installation interactif par catégories

#### Pour qui ?
✅ IT qui déploie des agents spécialisés pour différentes équipes  
✅ Managers de projet cherchant des agents prêts à l'emploi pour des rôles précis  
✅ Tout utilisateur souhaitant un point de départ pour des sous-agents spécialisés

#### Valeur ajoutée
La réduction de 97% des tokens de contexte via airis-mcp-gateway est une économie de coût massive pour les déploiements à grande échelle.

---

### Ressource 13 — awesome-agent-skills

**Les skills des grandes équipes d'ingénierie**

🔗 [github.com/VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)

#### Ce que c'est
Ce qui distingue ce dépôt des autres bibliothèques de skills : **la provenance**. Ces skills viennent d'équipes d'ingénierie réelles, qui les utilisent en production.

#### Ce qu'il contient
Skills provenant d'équipes officielles de :
- **Anthropic** — créateurs de Claude
- **Google Labs** — recherche IA
- **Vercel** — déploiement web
- **Stripe** — paiements
- **Cloudflare** — infrastructure réseau
- **Trail of Bits** — sécurité
- **Sentry** — monitoring
- **Expo** — développement mobile
- **Hugging Face** — modèles open source
- **Figma** — design

#### Pour qui ?
✅ Ingénieurs et équipes IT cherchant des pratiques de niveau "grands acteurs du secteur"  
✅ Compatible avec Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot et plus

#### Valeur ajoutée
Ces skills ont été testés en production réelle par des équipes exigeantes. Ils reflètent de vraies contraintes opérationnelles — pas des exemples académiques.

---

## Catégorie D — Les ressources d'apprentissage et de recherche

---

### Ressource 6 — learn-claude-code

**Comprendre en construisant**

🔗 [github.com/shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)

#### Ce que c'est
La seule ressource qui vous apprend à *construire* un système agentique plutôt qu'à simplement l'*utiliser*. C'est le "dessous des cartes" de Claude Code.

#### Ce qu'il contient
Un apprentissage progressif en couches :
1. La boucle agentique de base
2. Intégration d'outils
3. Systèmes de tâches
4. Architecture de sous-agents
5. Agents autonomes
6. Compression de contexte
7. Isolation via git worktree

#### Pour qui ?
✅ Profils IT et ingénieurs qui veulent comprendre les mécanismes internes  
✅ Formateurs qui veulent enseigner "pourquoi" et pas seulement "comment"  
✅ Tout curieux qui veut dépasser le niveau "utilisateur"

#### Valeur ajoutée
Comprendre l'architecture vous rend 10× plus efficace comme utilisateur. Vous savez pourquoi certains patterns fonctionnent, et vous pouvez diagnostiquer les problèmes plutôt que les subir.

---

### Ressource 4 — awesome-claude-code

**La carte de l'écosystème**

🔗 [github.com/hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)

#### Ce que c'est
Un répertoire curé de l'ensemble de l'écosystème Claude Code — skills, hooks, commandes, frameworks, applications, plugins. Construit autour de la qualité plutôt que de l'exhaustivité, avec des notes personnelles sur chaque entrée.

#### Ce qu'il contient
- Skills par domaine
- Hooks utiles
- Frameworks d'agents
- Applications construites avec Claude Code
- **Claude HUD** (Jarrod Watts) : affichage en temps réel du contexte, des outils actifs, des agents et des tâches
- **AgentSys** (avifenesh) : système d'automatisation de workflows (gestion PR, nettoyage de code, revue multi-agents)

#### Pour qui ?
✅ Toute personne qui découvre l'écosystème  
✅ Profils cherchant des outils pour des besoins spécifiques non couverts ailleurs

#### Valeur ajoutée
C'est la porte d'entrée vers l'ensemble de l'écosystème. Quand vous ne savez pas ce que vous cherchez, c'est ici que vous commencez.

---

### Ressource 11 — system-prompts-and-models-of-ai-tools

**Voir derrière le rideau des outils IA**

🔗 [github.com/x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

#### Ce que c'est
Une collection de prompts systèmes, définitions d'outils et métadonnées de modèles exposés par des outils IA commerciaux : Claude Code, Cursor, Devin, Replit, Windsurf, Lovable, Perplexity et d'autres.

#### Ce qu'il contient
- Prompts systèmes internes de nombreux outils IA
- Définitions des outils disponibles dans chaque système
- Métadonnées de modèles
- Comparaisons entre outils

#### Pour qui ?
✅ IT et ingénieurs qui évaluent des outils IA pour leur entreprise  
✅ Responsables achats qui veulent dépasser les argumentaires marketing  
✅ Formateurs qui enseignent les différences entre outils IA

#### Valeur ajoutée
Comprendre comment ces outils se "présentent" à leurs modèles vous donne une compréhension réelle de leurs capacités et limites — indépendamment du marketing.

---

### Ressource 12 — claude-code-system-prompts

**L'évolution de Claude Code version par version**

🔗 [github.com/Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)

#### Ce que c'est
Un suivi historique des prompts systèmes internes de Claude Code à travers toutes ses versions. Chaque mise à jour est documentée et comparée.

#### Ce qu'il contient
- Prompts systèmes par version
- Descriptions des outils intégrés
- Prompts des sous-agents
- Comptage de tokens
- Historique des changements

#### Pour qui ?
✅ Chercheurs en IA et ingénieurs avancés  
✅ Développeurs déboguant des comportements spécifiques à une version  
✅ Architectes d'agents comprenant les évolutions de comportement

#### Valeur ajoutée
Irremplaçable pour diagnostiquer pourquoi un workflow fonctionnait avec la version précédente mais plus avec la nouvelle.

---

### Ressource 15 — claude-code-handbook

**La référence encyclopédique du prompt engineering**

🔗 [github.com/ThamJiaHe/claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook)

#### Ce que c'est
Le manuel de référence le plus complet sur les techniques de prompting et de configuration pour Claude Code. Mis à jour **toutes les semaines** par un agent automatisé qui interroge Perplexity puis révise le contenu avec Claude Opus.

#### Ce qu'il contient
- Guide complet pour Claude Opus 4.6, Sonnet 4.6 et Haiku 4.5
- Skills, plugins, MCP, hooks, équipes d'agents, subagents
- Patterns de raisonnement avancé
- Dernière mise à jour : mars 2026 (v2.1.83)
- Application web compagnon **ClaudeForge** : génération de prompts optimisés directement depuis la documentation

#### Pour qui ?
✅ Toute personne qui veut systématiquement améliorer ses prompts  
✅ Formateurs cherchant une référence toujours à jour  
✅ Ingénieurs construisant des systèmes prompts complexes

#### Valeur ajoutée
C'est la seule documentation qui se maintient elle-même à jour. ClaudeForge transforme la documentation en outil actif de génération de prompts.

---

## Catégorie E — Les applications hors développement

---

### Ressource 3 — claude-code-action (officiel Anthropic)

**L'intégration CI/CD officielle**

🔗 [github.com/anthropics/claude-code-action](https://github.com/anthropics/claude-code-action)

#### Ce que c'est
L'unique dépôt de cette liste créé directement par **Anthropic**. Il intègre Claude Code dans GitHub Actions pour des revues automatiques, des corrections et des interactions en pull requests.

#### Ce qu'il contient
- Réponse aux mentions @claude dans les PRs et issues
- Revues de code automatisées
- Implémentation de corrections suggérées
- Environnement shell réel (pas seulement des commentaires)
- Multi-backends : API Anthropic, AWS Bedrock, Google Vertex AI, Microsoft Foundry

#### Pour qui ?
✅ Équipes IT et développement qui gèrent des pull requests régulières  
✅ Responsables qualité logicielle

#### Valeur ajoutée
Contrairement aux outils de revue IA classiques, Claude Code Action peut **réellement modifier le code** — lire des fichiers, exécuter git, éditer et pousser des commits. Coût : moins de 5€/mois pour 50 PRs.

---

### Ressource 14 — Claude-Code-Projects-Index

**Claude Code au-delà du développement**

🔗 [github.com/danielrosehill/Claude-Code-Projects-Index](https://github.com/danielrosehill/Claude-Code-Projects-Index)

#### Ce que c'est
La ressource la plus "perspective-shifting" de toute la liste. Daniel Rosehill a documenté six mois d'usage quotidien de Claude Code dans des domaines entièrement non-techniques.

#### Ce qu'il contient
75+ dépôts organisés par domaine :
- **Édition audio** — transcription, montage, organisation
- **Recherche juridique** — analyse de contrats, recherche de jurisprudence
- **Analyse SEO** — optimisation de contenu web
- **Documentation médicale** — organisation de dossiers de santé
- **Administration système** — automatisation de tâches IT
- Et des dizaines d'autres domaines...

Chaque workspace suit la même structure : CLAUDE.md pour les instructions, commandes slash, configurations MCP, sous-agents spécialisés.

#### Pour qui ?
✅ **TOUS les profils non-techniques** de cette formation — c'est la démonstration que Claude Code n'est pas un outil de développeurs
✅ RH, administratifs, formateurs, juristes, communicants…

#### Valeur ajoutée
C'est probablement le meilleur argument pour convaincre un sceptique non-technique : voir Claude Code appliqué à l'édition audio ou à la documentation médicale dissipe définitivement l'idée que c'est "un truc pour les développeurs".

---

## 3.1 Tableau de synthèse : quelle ressource pour quel profil ?

| Ressource | Administratifs | Ingénieurs | IT | RH | Formateurs |
|-----------|:---:|:---:|:---:|:---:|:---:|
| everything-claude-code | ○ | ✅ | ✅ | ○ | ○ |
| superpowers | ✅ | ✅ | ✅ | ✅ | ✅ |
| claude-code-action | ○ | ✅ | ✅ | ○ | ○ |
| awesome-claude-code | ✅ | ✅ | ✅ | ✅ | ✅ |
| awesome-claude-code-subagents | ○ | ✅ | ✅ | ✅ | ✅ |
| learn-claude-code | ○ | ✅ | ✅ | ○ | ✅ |
| claude-code-best-practice | ✅ | ✅ | ✅ | ✅ | ✅ |
| gstack | ✅ | ✅ | ✅ | ✅ | ✅ |
| claude-code-templates | ✅ | ✅ | ✅ | ✅ | ✅ |
| get-shit-done | ✅ | ✅ | ✅ | ✅ | ✅ |
| system-prompts-and-models | ○ | ✅ | ✅ | ○ | ✅ |
| claude-code-system-prompts | ○ | ○ | ✅ | ○ | ○ |
| awesome-agent-skills | ○ | ✅ | ✅ | ○ | ✅ |
| Claude-Code-Projects-Index | ✅ | ✅ | ✅ | ✅ | ✅ |
| claude-code-handbook | ✅ | ✅ | ✅ | ✅ | ✅ |

*✅ Fortement recommandé | ○ Optionnel ou avancé*

---

## 3.2 Par où commencer selon votre profil

**Si vous êtes administratif ou RH :**
Commencez par le dépôt 14 (Claude-Code-Projects-Index) pour voir ce qui est possible, puis le dépôt 7 (best-practice) pour apprendre à bien travailler.

**Si vous êtes ingénieur :**
Commencez par le dépôt 2 (superpowers) pour la méthodologie, puis le dépôt 13 (awesome-agent-skills) pour les compétences.

**Si vous êtes IT :**
Commencez par le dépôt 1 (everything-claude-code) pour l'infrastructure, puis le dépôt 5 (subagents) pour la spécialisation.

**Si vous êtes formateur :**
Commencez par le dépôt 4 (awesome-claude-code) pour la cartographie, puis le dépôt 15 (handbook) pour la référence toujours à jour.

---

## Points clés à retenir

- L'écosystème est riche et varié — il existe une ressource adaptée à chaque profil
- Les dépôts VoltAgent (5 et 13) offrent les bibliothèques de skills les plus larges
- Superpowers (2) est la référence méthodologique incontournable
- Claude-Code-Projects-Index (14) est la preuve que tout cela dépasse largement le développement logiciel
- La documentation officielle Anthropic (dépôt 3) offre la garantie de qualité et de support

---

*Module précédent : [← Concepts fondamentaux](02-concepts-fondamentaux.md) | Prochain module : [Cas d'usage métier →](04-cas-usage-metiers.md)*
