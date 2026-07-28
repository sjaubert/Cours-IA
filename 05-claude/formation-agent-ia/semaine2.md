# Semaine 2 — Premier agent HTML avec recherche web

> **Étape 1 · Semaine 2 sur 6**
> ⏱ 2 h 30 · 🔵 Niveau B — Fichier HTML local · 👥 Profils mixtes

---

## 🎯 Ce que vous allez savoir faire à la fin de cette séance

- ✅ Ouvrir et utiliser un fichier agent HTML
- ✅ Configurer une clé API Anthropic dans le fichier
- ✅ Écrire un prompt système adapté à votre métier
- ✅ Interroger Claude avec accès à la recherche web
- ✅ Comprendre la différence entre les niveaux A et B

---

## 🧩 Les concepts clés de cette semaine

| Terme | Définition |
|---|---|
| 🔑 **Clé API** | Mot de passe unique qui identifie votre application auprès d'Anthropic. Format : `sk-ant-api03-…` |
| 📝 **Prompt système** | Instruction permanente que Claude reçoit avant votre question — définit son rôle, sa personnalité, ses limites. |
| 🌐 **web_search** | Outil qui permet à Claude de chercher des informations récentes sur internet avant de répondre. |
| 📦 **localStorage** | Espace dans votre navigateur où la clé API est stockée localement — elle ne quitte jamais votre ordinateur. |
| 🔵 **Niveau B** | Agent dans un fichier HTML local. Plus puissant que le niveau A, sans installation de logiciel. |
| 💬 **Messages** | Historique de la conversation envoyé à Claude à chaque message — c'est ce qui lui permet de « se souvenir ». |

> ⚠️ **Sécurité** : votre clé API ne doit jamais être partagée, envoyée par mail ou publiée sur internet. Si vous la divulguez par erreur, révoquez-la immédiatement sur [console.anthropic.com](https://console.anthropic.com).

---

## 🛠️ Activité 1 — Personnaliser son agent avec un prompt système

⏱ 45 min · 🔵 Niveau B — Fichier HTML · 👤 Individuel

Ouvrez le fichier `agent_base.html` fourni par le formateur, saisissez votre clé API, puis remplacez le prompt système par celui correspondant à votre profil.

### 🟢 Prompt système — Profil RH

```
Tu es un assistant RH expert spécialisé dans le droit du travail français
et la gestion des ressources humaines pour les PME industrielles.

Tu réponds toujours en français, de façon précise et professionnelle.
Si une information peut avoir évolué récemment (loi, jurisprudence),
tu le signales.

Tu ne donnes jamais de conseil juridique engageant — tu orientes vers
un avocat ou l'inspection du travail pour les cas complexes.
```

### 🔵 Prompt système — Profil Comptabilité

```
Tu es un assistant comptable et fiscal pour PME françaises.
Tu maîtrises le plan comptable général, la TVA, les déclarations
fiscales courantes et la gestion de trésorerie.

Tu réponds en français, avec des exemples concrets. Tu signales toujours
si une règle fiscale a pu évoluer et recommandes de vérifier avec
l'expert-comptable pour les situations complexes.
```

### 🟣 Prompt système — Profil Manager / Production

```
Tu es un assistant pour responsable d'atelier dans l'industrie
manufacturière. Tu maîtrises le lean management, la sécurité au travail,
la gestion de production et l'amélioration continue.

Tu proposes des solutions pratiques, directement applicables en atelier.
Tu utilises un langage simple et opérationnel, sans jargon excessif.
```

### 📋 Étapes à suivre

1. Ouvrez le fichier `agent_base.html` dans votre navigateur (double-clic).
2. Dans la zone **« Clé API »**, saisissez votre clé (`sk-ant-…`) et cliquez « Sauvegarder ».
3. Cliquez sur **« ⚙️ Modifier le prompt système »** et collez le texte de votre profil.
4. Posez 3 questions professionnelles concrètes et évaluez la qualité des réponses.
5. Modifiez une phrase du prompt système et observez comment les réponses changent.

---

## 🛠️ Activité 2 — Activer la recherche web (web_search)

⏱ 35 min · 🔵 Niveau B · 👥 En binôme puis individuel

L'outil **web_search** permet à Claude d'aller chercher des informations récentes sur internet avant de répondre. Sans cet outil, Claude ne connaît que ce qu'il a appris jusqu'à début 2025 environ.

### Questions test à poser avec web_search activé

**🟢 RH :**
```
Quel est le montant du SMIC horaire brut en vigueur aujourd'hui en France ?
```

**🔵 Comptabilité :**
```
Quels sont les taux de TVA applicables en France en 2026 ?
```

**🟣 Manager :**
```
Quelles sont les dernières évolutions réglementaires en matière de sécurité
au travail dans l'industrie française ?
```

**Tous profils — Test comparatif :**
Posez la même question avec et sans web_search, et comparez les deux réponses. Notez les différences.

### 📋 Étapes à suivre

1. Activez l'option **web_search** dans l'interface de votre agent.
2. Posez la question correspondant à votre profil.
3. Observez : Claude indique-t-il ses sources ? La réponse semble-t-elle plus récente ?
4. Désactivez web_search et reposez la même question. Comparez les deux réponses.

---

## 📌 Ce que vous emportez de cette séance

- Un agent HTML fonctionnel, personnalisé pour votre métier — utilisable dès demain
- **web_search = Claude avec accès à l'actualité.** Sans web_search = connaissances figées à début 2025
- La semaine prochaine : comment mesurer et améliorer objectivement la qualité des réponses

---

*← [Semaine 1](semaine1.md) · [Plan général](plan_formation_agent_claude.html) · [Semaine 3 →](semaine3.md)*
