# Semaine 6 — Évaluation finale, OODA et mise en production

> **Étape 4 · Semaine 6 sur 6 — Séance finale**
> ⏱ 2 × 1 h · 🎓 Bilan · 👥 Tous profils

---

## 🎯 Objectifs de cette dernière séance

- ✅ Mesurer vos progrès depuis la semaine 3
- ✅ Appliquer le cycle OODA pour améliorer son agent
- ✅ Valider son agent avec la checklist de production
- ✅ Identifier ses prochaines étapes

---

## 🔄 Le cycle OODA — amélioration continue de votre agent

OODA = **Observer → Orienter → Décider → Agir**. Appliqué à un agent IA, c'est une boucle d'amélioration continue.

| Étape | Question à se poser | Exemple concret |
|---|---|---|
| 👁️ **Observer** | Que s'est-il passé exactement ? | « Claude a donné un taux de TVA de 5,5 % sur un produit taxé à 20 %. » |
| 🧭 **Orienter** | Quelle est la cause racine ? | « Le prompt système ne demande pas de vérifier les taux avec web_search. » |
| 🎯 **Décider** | Quelle correction précise vais-je faire ? | « Ajouter : "Pour tout taux réglementaire, utilise web_search pour vérifier." » |
| ⚡ **Agir** | Appliquer, retester, comparer les scores. | Score exactitude : 1/3 → 3/3 après correction. |

---

## ⚠️ Les 6 erreurs les plus fréquentes — et leurs corrections

| Erreur | Symptôme | Correction à ajouter dans le prompt |
|---|---|---|
| **Hallucination de chiffre** | Claude donne un taux ou un montant sans le vérifier | *« Pour tout chiffre réglementaire, utilise web_search. Sinon, écris [À VÉRIFIER]. »* |
| **Réponse hors rôle** | Claude répond à des questions hors de son domaine | *« Si la question dépasse ton domaine, dis-le explicitement. »* |
| **Format inadapté** | Prose au lieu d'un tableau, ou inversement | *« Sauf demande contraire, structure : résumé 2 lignes + détails en bullet points. »* |
| **Réponse trop longue** | Claude développe plus que nécessaire | *« Résumé en 5 lignes maximum, sauf demande contraire. »* |
| **Perte de contexte** | Claude "oublie" des infos données plus tôt | Vérifier que l'historique de conversation est bien transmis. Résumer le contexte en début de session longue. |
| **Excès de prudence** | Claude refuse ou sur-nuance des questions simples | Clarifier dans le prompt les cas où il peut répondre sans réserve. |

---

## 🛠️ Activité 1 — Mesurer ses progrès (bilan des scores)

⏱ 25 min · 📊 Grille de qualité · 👤 Individuel

Reposez vos 5 scénarios de test (rédigés en semaine 3) à votre agent actuel et comparez les scores.

| Scénario | Score S3 | Score S6 | Évolution | Critère amélioré |
|---|---|---|---|---|
| Scénario 1 | __ / 15 | __ / 15 | +__ | |
| Scénario 2 | __ / 15 | __ / 15 | +__ | |
| Scénario 3 | __ / 15 | __ / 15 | +__ | |
| Scénario 4 | __ / 15 | __ / 15 | +__ | |
| Scénario 5 | __ / 15 | __ / 15 | +__ | |
| **Moyenne** | **__ / 15** | **__ / 15** | **+__** | |

### 📋 Étapes à suivre

1. Copiez chacun de vos 5 scénarios dans votre agent.
2. Évaluez avec la grille à 5 critères et notez le score.
3. Comparez avec vos scores de la semaine 3.
4. Identifiez le scénario où la progression est la plus faible — appliquez un cycle OODA complet dessus.

---

## 🛠️ Activité 2 — Checklist de mise en production

⏱ 20 min · ✅ Validation · 👥 En binôme (validez la checklist de votre voisin)

### 🎯 Fonctionnement de base
- [ ] Mon agent répond correctement à mes 5 scénarios de test (score moyen ≥ 10/15)
- [ ] Le prompt système est rédigé en français, clair et sans ambiguïté
- [ ] J'ai testé avec des questions hors-sujet — l'agent les refuse correctement
- [ ] web_search est activé si l'agent a besoin d'informations récentes

### 🔐 Sécurité et données
- [ ] Ma clé API n'est pas visible dans le code source partagé
- [ ] L'agent ne traite pas de données personnelles sensibles (RGPD)
- [ ] Si l'agent a accès à Gmail/Drive, les droits accordés sont limités au strict nécessaire
- [ ] J'ai informé mon responsable qu'un agent IA accède à certains outils de l'entreprise

### 📋 Gouvernance et qualité
- [ ] J'ai documenté ce que fait l'agent (fiche d'1 page pour mes collègues)
- [ ] J'ai planifié une revue mensuelle des scores de qualité
- [ ] Je sais comment mettre l'agent en pause si une erreur grave est détectée
- [ ] Les réponses générées par Claude sont relues avant d'être envoyées à des tiers

### 🚀 Mise en service
- [ ] J'ai testé l'agent avec 2 collègues qui ne connaissent pas Claude
- [ ] J'ai un fichier de backup de mon prompt système
- [ ] Je sais où mettre à jour le modèle si une nouvelle version de Claude est disponible

**Score de maturité :** 13–15 ✅ prêt · 10–12 ⚠️ quelques ajustements · < 10 🔴 reprendre avant déploiement

---

## 🎓 Compétences acquises — Formation complète

À l'issue de ces 6 semaines, vous maîtrisez :

| Domaine | Compétence |
|---|---|
| Prompting | Formule Rôle + Contexte + Tâche + Format |
| Niveau A | Agent Claude.ai sans code |
| Niveau B | Agent HTML + clé API Anthropic |
| Recherche | web_search — accès à l'actualité en temps réel |
| Qualité | Grille 5 critères + 5 scénarios de test |
| MCP | Drive + Agenda + Gmail |
| Mémoire | Mémoire conversationnelle |
| Automation | Workflows multi-outils |
| Amélioration | Cycle OODA |
| Production | Checklist de validation |

---

## 🚀 Pour aller plus loin

- **Niveau C — Node.js** : agents avec mémoire persistante en base de données, tâches planifiées (cron), intégrations Slack/Teams
- **Claude Code** : interface CLI pour déléguer des tâches de développement et d'automatisation à Claude depuis un terminal
- **Masterclass Workflow** : orchestration d'agents IA dans des workflows métier complexes (multi-agents, boucles de décision, reporting automatique)

---

*← [Semaine 5](semaine5.md) · [Plan général](plan_formation_agent_claude.html)*
