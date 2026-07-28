# Plan de formation : Construire un agent IA avec Claude
## 4 étapes progressives — Cas d'usage professionnels et administratifs

---

## 🎯 Introduction — Ce que vous allez construire

Cette formation vous guide pas à pas dans la création d'un **agent IA professionnel** basé sur Claude, le modèle d'intelligence artificielle d'Anthropic.

Un agent IA, c'est un programme capable d'**effectuer des tâches à votre place** : rechercher des informations sur le web, rédiger des courriers, consulter votre agenda, retrouver un document, et enchaîner plusieurs de ces actions de façon autonome — tout en respectant les règles que vous lui fixez.

**À l'issue de cette formation, vous saurez :**
- Appeler Claude via une interface simple, sans installation complexe
- Rédiger des instructions précises (appelées *prompts*) qui guident l'agent efficacement
- Mesurer objectivement la qualité des réponses et les améliorer
- Connecter l'agent à vos outils métier (Drive, Calendar, messagerie)
- Diagnostiquer et corriger les erreurs les plus fréquentes

**Public visé :** Professionnels non-développeurs — responsables RH, administratifs, assistantes de direction, chefs de projet, formateurs.

**Aucune connaissance en programmation n'est requise** pour les Étapes 1 et 2. Les Étapes 3 et 4 introduisent progressivement des notions techniques, toujours expliquées en langage courant.

---

## Lexique — Termes techniques expliqués

Avant de commencer, voici les quelques termes techniques que vous rencontrerez dans ce document. Référez-vous à ce lexique en cas de doute.

| Terme | Explication simple |
|---|---|
| **API** | Interface de communication entre deux logiciels. C'est ce qui permet à votre outil de « parler » à Claude. |
| **Clé API** | Mot de passe personnel qui autorise votre outil à utiliser Claude. Ne jamais la partager. |
| **MCP** | *Model Context Protocol* — protocole qui permet à Claude de se connecter à vos outils (Drive, Calendar, Gmail…). C'est le « câble » entre l'agent et vos applications. |
| **Variable d'environnement** | Information secrète stockée dans votre système, hors du code. Permet de garder votre clé API invisible dans le code. |
| **Prompt** | Instruction ou question que vous donnez à l'agent. Un *prompt système* est l'instruction permanente qui définit le rôle de l'agent. |
| **Parsing** | Extraction et lecture structurée d'une réponse. Par exemple : isoler uniquement le texte d'une réponse qui contient aussi des métadonnées. |
| **Cron** | Système de planification automatique de tâches sur un ordinateur (ex : "lance cette action tous les matins à 8h"). |
| **Hallucination** | Terme technique pour désigner quand un modèle d'IA invente une information qui n'existe pas (chiffre, date, référence légale…). |
| **Artefact** | Dans Claude.ai, mini-application générée et exécutée directement dans la conversation. |

---

## Vue d'ensemble

| Étape | Thème | Durée | Niveau |
|---|---|---|---|
| 1 | Agent mono-outil : recherche + résumé | Semaines 1–2 | Débutant |
| 2 | Tests avec cas d'usage précis et mesurables | Semaines 2–3 | Intermédiaire |
| 3 | Ajout progressif d'outils et de mémoire | Semaines 3–5 | Avancé |
| 4 | Évaluation des erreurs et affinage des prompts | Semaines 5–6 | Expert |

---

## Avant de commencer — Comment exécuter le code ?

Tout au long de cette formation, vous rencontrerez des blocs de code JavaScript. Voici les **3 environnements** dans lesquels vous pouvez les exécuter, du plus simple au plus technique. Choisissez celui qui correspond à votre niveau et restez cohérent tout au long du parcours.

---

### Niveau A — Claude.ai (artefact interactif)
> **Pour qui :** Tous les profils, aucune installation requise.
> **Quand l'utiliser :** Idéal pour les Étapes 1 et 2 de cette formation.

#### Comment ça marche
Claude.ai peut générer et exécuter du code directement dans la conversation, dans ce qu'on appelle un **artefact** — une mini-application qui s'affiche à droite de la conversation. La clé API est gérée automatiquement par Claude.ai. Vous n'avez rien à configurer.

#### Comment démarrer
Au lieu de copier le code, vous formulez votre demande directement à Claude :

```
Prompt type à utiliser dans Claude.ai :

"Construis-moi un artefact interactif qui appelle l'API Claude
pour [ton cas d'usage]. L'utilisateur doit pouvoir saisir [son input]
et l'agent doit [ce qu'il doit faire]."
```

#### Exemple concret — Étape 1, veille RH
```
"Construis un artefact où je saisis un thème RH, et Claude
recherche sur le web et me résume les dernières évolutions
réglementaires en 3 points."
```

Claude va écrire le code, le faire tourner, et vous présenter l'interface directement dans la conversation.

#### Avantages / Limites

| ✅ Avantages | ⚠️ Limites |
|---|---|
| Zéro installation | Pas adapté aux projets en équipe |
| Clé API automatique | Données non persistantes entre sessions |
| Idéal pour apprendre | Pas de connexion à vos propres systèmes |
| Résultats immédiats | Moins de contrôle sur le code |

---

### Niveau B — Fichier HTML (navigateur)
> **Pour qui :** Profils non-développeurs à l'aise avec un éditeur de texte.
> **Quand l'utiliser :** Étapes 1 à 3. Bon pour tester avec de vraies données.

#### Comment ça marche
Vous créez un fichier texte avec l'extension `.html`, vous y collez le code, et vous l'ouvrez dans votre navigateur (Chrome, Firefox, Edge). Il vous faut une clé API Anthropic personnelle.

#### Obtenir votre clé API
1. Allez sur **console.anthropic.com**
2. Créez un compte (gratuit)
3. Dans "API Keys", cliquez sur "Create Key"
4. Copiez la clé — elle ne s'affiche qu'une fois

> ⚠️ **Règle de sécurité absolue :** Ne partagez jamais votre fichier HTML contenant votre clé API. Ne la postez pas sur GitHub. Ne l'envoyez pas par email.

#### Structure du fichier HTML de base

Créez un fichier `agent.html`, collez ce contenu, remplacez `TA_CLE_API_ICI` :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Mon agent Claude</title>
</head>
<body>

  <h2>Mon agent IA</h2>
  <textarea id="question" rows="4" cols="60"
    placeholder="Pose ta question ici..."></textarea>
  <br><br>
  <button onclick="callClaude()">Envoyer</button>
  <hr>
  <div id="reponse" style="white-space: pre-wrap; max-width: 700px;"></div>

  <script>
  async function callClaude() {
    const question = document.getElementById("question").value;
    document.getElementById("reponse").innerText = "En cours...";

    try {
      const response = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": "TA_CLE_API_ICI",         // ← remplacez ici
          "anthropic-version": "2023-06-01",
          "anthropic-dangerous-direct-browser-access": "true"
        },
        body: JSON.stringify({
          model: "claude-sonnet-4-6",             // ← modèle actuel (2026)
          max_tokens: 1000,
          system: "Tu es un assistant professionnel. Réponds en français.",
          messages: [{ role: "user", content: question }]
        })
      });

      const data = await response.json();
      document.getElementById("reponse").innerText =
        data.content[0].text;

    } catch (err) {
      document.getElementById("reponse").innerText =
        "Erreur : " + err.message;
    }
  }
  </script>
</body>
</html>
```

#### Comment ajouter la recherche web (Étape 1)

Ajoutez simplement le paramètre `tools` dans le `body` :

```javascript
body: JSON.stringify({
  model: "claude-sonnet-4-6",
  max_tokens: 1000,
  system: "Ton prompt système ici",
  tools: [{
    type: "web_search_20250305",
    name: "web_search"
  }],
  messages: [{ role: "user", content: question }]
})
```

Et adaptez la lecture de la réponse (Claude peut renvoyer plusieurs blocs) :

```javascript
// Parsing de la réponse :
// Claude peut renvoyer plusieurs blocs (texte + résultats de recherche).
// On garde uniquement les blocs de type "text" pour l'affichage.
const data = await response.json();
const texte = data.content
  .filter(b => b.type === "text")   // garde seulement les blocs texte
  .map(b => b.text)                  // extrait le contenu de chaque bloc
  .join("\n");                       // les assemble en un seul texte
document.getElementById("reponse").innerText = texte;
```

#### Avantages / Limites

| ✅ Avantages | ⚠️ Limites |
|---|---|
| Pas d'installation (juste un éditeur texte) | Clé API visible dans le fichier |
| Vous contrôlez le code | Pas adapté à la production |
| Facile à partager localement | Pas de persistance des données |
| Bon pour tester avec de vraies données | Mise à jour manuelle du fichier |

---

### Niveau C — Node.js (ligne de commande)
> **Pour qui :** Profils techniques, développeurs, chefs de projet avancés.
> **Quand l'utiliser :** Étapes 3 et 4. Indispensable pour les agents en production.

#### Comment ça marche
Node.js est un environnement qui permet d'exécuter JavaScript sur votre ordinateur, en dehors du navigateur. C'est la base de tout projet d'agent IA sérieux : vous pouvez connecter des bases de données, automatiser des tâches planifiées (avec un *cron* — un programme qui déclenche des actions à heure fixe comme "tous les matins à 7h"), et déployer sur un serveur.

#### Installation (une seule fois)

```bash
# 1. Téléchargez et installez Node.js sur nodejs.org (version LTS)

# 2. Vérifiez l'installation
node --version   # doit afficher v20.x ou supérieur
npm --version    # doit afficher 10.x ou supérieur

# 3. Créez un dossier pour votre projet
mkdir mon-agent-ia
cd mon-agent-ia

# 4. Initialisez le projet
npm init -y

# 5. Installez le SDK officiel d'Anthropic
npm install @anthropic-ai/sdk
```

#### Configurer votre clé API de façon sécurisée

```bash
# Sur Mac / Linux — ajoutez cette ligne dans votre fichier ~/.zshrc ou ~/.bashrc
export ANTHROPIC_API_KEY="sk-ant-..."

# Sur Windows (PowerShell)
$env:ANTHROPIC_API_KEY = "sk-ant-..."

# Rechargez votre terminal
source ~/.zshrc
```

> ✅ Avec cette méthode (appelée *variable d'environnement*), votre clé n'apparaît **jamais** dans votre code. Si quelqu'un accède à votre fichier, il ne peut pas utiliser votre compte Anthropic.

#### Fichier de départ — agent.mjs

```javascript
// agent.mjs
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
// La clé est lue automatiquement depuis la variable d'environnement ANTHROPIC_API_KEY

async function callAgent(question) {
  const response = await client.messages.create({
    model: "claude-sonnet-4-6",     // modèle actuel (2026)
    max_tokens: 1000,
    system: "Tu es un assistant professionnel. Réponds en français.",
    messages: [{ role: "user", content: question }]
  });

  return response.content[0].text;
}

// Point d'entrée
const reponse = await callAgent("Quelles sont les tendances RH du moment ?");
console.log(reponse);
```

```bash
# Lancer l'agent
node agent.mjs
```

#### Ajouter la recherche web (Étape 1, niveau C)

```javascript
const response = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1000,
  system: "Ton prompt système ici",
  tools: [{ type: "web_search_20250305", name: "web_search" }],
  messages: [{ role: "user", content: question }]
});

// Parsing de la réponse : on extrait uniquement les blocs texte
const texte = response.content
  .filter(b => b.type === "text")
  .map(b => b.text)
  .join("\n");

console.log(texte);
```

#### Avantages / Limites

| ✅ Avantages | ⚠️ Limites |
|---|---|
| Clé API sécurisée (variable d'environnement) | Installation requise |
| Adapté à la production | Courbe d'apprentissage |
| Connexion à des bases de données possible | Nécessite des notions de terminal |
| Automatisation et planification (cron) | Déploiement plus complexe |
| Travail en équipe (Git) | |

---

### Récapitulatif — Quel niveau choisir selon l'étape ?

| Étape de formation | Niveau A (Claude.ai) | Niveau B (HTML) | Niveau C (Node.js) |
|---|---|---|---|
| Étape 1 — Mono-outil | ✅ Recommandé | ✅ Possible | ✅ Possible |
| Étape 2 — Tests mesurables | ✅ Recommandé | ✅ Recommandé | ✅ Possible |
| Étape 3 — Multi-outils + mémoire | ⚠️ Limité | ✅ Recommandé | ✅ Recommandé |
| Étape 4 — Évaluation + production | ❌ Insuffisant | ⚠️ Limité | ✅ Indispensable |

---

## Étape 1 — Agent mono-outil : recherche web + résumé

> ⏱ **Durée estimée :** 2 semaines — exercice pratique : **45 minutes**

### Objectifs pédagogiques
- Appeler l'API Claude avec un outil (web_search)
- Écrire un prompt système efficace
- Lire et extraire la réponse (parsing)
- Gérer les erreurs basiques

### Cas d'usage professionnel : Veille réglementaire RH

**Contexte :** Une PME RH veut automatiser la veille sur l'évolution du droit du travail.

**Prompt système prêt à l'emploi :**
```
Tu es un assistant juridique RH spécialisé dans le droit du travail français.
Ton rôle est de surveiller les évolutions réglementaires et d'en extraire
les informations utiles pour une PME de 50 salariés.

Quand tu recherches une information, tu dois :
1. Identifier les sources officielles (Légifrance, service-public.fr, URSSAF)
2. Résumer le changement en 3 points maximum, en langage accessible
3. Indiquer la date d'entrée en vigueur et les actions à prendre
4. Préciser si tu n'es pas certain d'une information

Ne jamais inventer de références légales. Si tu n'es pas sûr, dis-le.
```

**Code JavaScript prêt à l'emploi :**
```javascript
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "claude-sonnet-4-6",     // modèle actuel (2026)
    max_tokens: 1000,
    system: `Tu es un assistant juridique RH. Recherche des infos
fiables, résume en 3 points max, indique les actions à prendre.
Si tu n'es pas certain, dis-le clairement.`,
    tools: [{
      type: "web_search_20250305",
      name: "web_search"
    }],
    messages: [{
      role: "user",
      content: "Dernières évolutions télétravail France 2025 ?"
    }]
  })
});

// Parsing de la réponse :
// Claude peut renvoyer plusieurs blocs (texte + résultats de recherche web).
// On garde uniquement les blocs de type "text" pour l'affichage final.
const data = await response.json();
const answer = data.content
  .filter(b => b.type === "text")
  .map(b => b.text)
  .join("\n");

console.log(answer);
```

### Autres cas d'usage niveau 1
- **Administratif :** Synthèse quotidienne du Journal Officiel
- **Comptabilité :** Veille sur les taux TVA et seuils fiscaux
- **Achats :** Résumé des actualités sur les fournisseurs clés

### Exercice pratique — 45 min
Testez l'agent avec ces 3 questions et comparez les réponses :
1. "Quelles sont les règles du temps de travail pour les cadres en 2025 ?"
2. "Montant du SMIC en vigueur ?"
3. "Conditions pour bénéficier du dispositif FNE-Formation ?"

---

## Étape 2 — Tests avec cas d'usage précis et mesurables

> ⏱ **Durée estimée :** 1 semaine — exercice pratique : **1 heure**

### Métriques cibles à définir

| Métrique | Cible recommandée |
|---|---|
| Taux de pertinence (évaluation humaine) | > 85% |
| Temps de réponse moyen | < 3 secondes |
| Taux de réponses hors périmètre | < 5% |
| Hallucinations détectées | 0% toléré |

### Cas d'usage professionnel : Rédaction de courriers administratifs

**Prompt système :**
```
Tu es un assistant administratif pour une collectivité locale.
Tu rédiges des courriers officiels conformes aux normes de la fonction publique.

Règles strictes :
— Formule de politesse adaptée au destinataire
  (citoyen, élu, préfecture, tribunal...)
— Structure : Objet → Contexte (2 phrases max) →
  Demande → Suite attendue → Formule de politesse
— Jamais d'informations inventées → indiquer [À COMPLÉTER]
— Longueur : 150 à 250 mots
— Ton : formel, neutre, bienveillant
```

**Scénarios de test structurés :**

> 💡 **En clair — ce que fait ce code :**
> Ce bloc définit une liste de scénarios de test (`testCases`) avec, pour chaque scénario : la question posée à l'agent et les critères que la réponse doit respecter (formule de politesse présente ? structure correcte ? longueur entre 150 et 250 mots ?). La fonction `scoreResponse` calcule combien de critères sont remplis et retourne un pourcentage de réussite. Ce n'est pas du code à copier tel quel — c'est un modèle que vous adaptez en remplaçant les critères par ceux de votre propre cas d'usage.

```javascript
const testCases = [
  {
    id: "T01",
    input: `Rédige un courrier de relance pour un administré
            dont la demande de permis de construire est
            sans réponse depuis 3 mois.`,
    criteres: {
      formule_politesse: true,
      structure_respectee: true,
      placeholder_si_manque: true,
      longueur_mots: "150-250",
      ton_officiel: true
    }
  },
  {
    id: "T03", // CAS LIMITE : demande volontairement floue
    input: "Écris un mail à Jean pour le permis.",
    attendu: "Demande de clarification ou présence de [À COMPLÉTER]",
    criteres: { refus_hallucination: true }
  }
];

// scoreResponse vérifie combien de critères sont remplis
// et retourne un pourcentage de réussite pour guider l'amélioration du prompt
function scoreResponse(response, criteres) {
  const total = Object.keys(criteres).length;
  // → Ajoutez votre logique de validation ici
  return { total, pct: "?%" };
}
```

**Signaux d'alerte :**
- Score < 70% → retravailler le prompt
- Zéro [À COMPLÉTER] sur des tests lacunaires → risque d'hallucination
- Réponses quasi-identiques à des questions différentes → manque de contexte

---

## Étape 3 — Ajout progressif d'outils et de mémoire

> ⏱ **Durée estimée :** 2 semaines — exercices : **2 × 1 heure**

### Stratégie d'ajout semaine par semaine

- **Semaine 3 :** Google Drive uniquement. 5 tests de recherche de documents.
- **Semaine 3 fin :** Ajouter Google Calendar. Vérifier le bon choix d'outil.
- **Semaine 4 :** Gmail en lecture seule. Pas d'envoi automatique.
- **Semaine 4 fin :** Envoi d'emails après confirmation explicite.
- **Semaine 5 :** Mémoire conversationnelle (historique complet).

### Cas d'usage : Assistant RH multi-outils

**Prompt système avec arbre de décision :**
```
Tu es l'assistant RH de l'entreprise.

Ordre de priorité des outils :
1. Drive → si la demande porte sur un document, un contrat, une politique RH
2. Calendar → si la demande porte sur des dates ou des disponibilités
3. Gmail → uniquement si demandé explicitement, après confirmation

Règles de sécurité :
— Aucune action irréversible sans confirmation explicite de l'utilisateur
— Indiquer quelle source tu consultes et pourquoi à chaque étape
— Si l'information est introuvable dans les outils, le dire clairement
```

**Code avec 3 outils MCP et mémoire conversationnelle :**

> 💡 **En clair — ce que fait ce code :**
> La variable `conversationHistory` (historique) stocke tous les échanges en mémoire. À chaque appel, on envoie tout l'historique à Claude — c'est ce qui lui permet de se souvenir du contexte de la conversation précédente. La section `mcp_servers` liste les outils à connecter via le protocole MCP.
>
> ⚠️ **Important :** Les URLs indiquées dans le code sont des **exemples fictifs** servant à illustrer la structure. En pratique, les adresses réelles dépendent de votre configuration MCP — consultez votre administrateur système ou la documentation de votre fournisseur d'outils pour obtenir les bonnes URLs.

```javascript
const conversationHistory = [];

async function askAgent(userMessage) {
  // On ajoute le nouveau message à l'historique de la conversation
  conversationHistory.push({ role: "user", content: userMessage });

  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "claude-sonnet-4-6",     // modèle actuel (2026)
      max_tokens: 1000,
      system: `Tu es l'assistant RH. Ordre : Drive → Calendar → Gmail.
Confirme avant toute action irréversible.`,
      mcp_servers: [
        // ⚠️ URLs illustratives — à remplacer par les adresses réelles
        // de votre déploiement MCP (fourni par votre administrateur système)
        { type: "url", url: "URL_SERVEUR_DRIVE_DE_VOTRE_ENTREPRISE",    name: "google-drive" },
        { type: "url", url: "URL_SERVEUR_CALENDAR_DE_VOTRE_ENTREPRISE", name: "google-calendar" },
        { type: "url", url: "URL_SERVEUR_GMAIL_DE_VOTRE_ENTREPRISE",    name: "gmail" }
      ],
      messages: conversationHistory  // ← tout l'historique = la mémoire de l'agent
    })
  });

  const data = await response.json();
  const answer = data.content.filter(b => b.type === "text").map(b => b.text).join("\n");

  // On ajoute la réponse de l'agent à l'historique pour nourrir les prochains échanges
  conversationHistory.push({ role: "assistant", content: data.content });
  return answer;
}

// Séquence avec mémoire — l'agent se souvient des échanges précédents
await askAgent("Trouve le contrat de Marie Durand.");
await askAgent("Planifie son entretien annuel la semaine prochaine.");
await askAgent("Envoie-lui une convocation par email."); // → demande confirmation
```

**Tests multi-outils à exécuter :**
```
Q1 (→ Drive)    : "Quelle est notre politique de télétravail ?"
Q2 (→ Calendar) : "Quand a lieu le prochain CODIR ?"
Q3 (ambigu)     : "Prépare la réunion RH de vendredi."
→ Attendu : demande de clarification (créer l'événement ?
  envoyer les convocations ? rédiger l'ordre du jour ?)
```

---

## Étape 4 — Évaluation des erreurs et affinage des prompts

> ⏱ **Durée estimée :** 1 semaine — exercice pratique : **1h30**

### Catalogue des 4 erreurs les plus fréquentes

#### Erreur 1 : Hallucination de données
**Symptôme :** L'agent invente des chiffres ou des références légales.

**Fix prompt :**
```
Si tu n'as pas l'information exacte, écris [DONNÉE MANQUANTE]
plutôt que d'estimer. Ne jamais inventer de numéros d'articles
de loi, de montants ou de dates.
```

#### Erreur 2 : Mauvais outil sélectionné
**Fix prompt :**
```
Avant de choisir un outil :
- Document ou politique ? → Drive
- Dates ou disponibilités ? → Calendar
- Envoyer ou lire des messages ? → Gmail
En cas de doute, demande une clarification.
```

#### Erreur 3 : Boucle infinie
**Symptôme :** L'agent tourne en rond et ne s'arrête jamais.

**Fix code :**
```javascript
// On fixe un nombre maximum de tentatives pour éviter que l'agent boucle indéfiniment.
// Si au bout de 5 essais l'agent n'a pas trouvé de réponse,
// il s'arrête et demande à l'utilisateur de reformuler.
const MAX_ITERATIONS = 5;
let iterations = 0;
while (!taskComplete && iterations < MAX_ITERATIONS) {
  await callAgent();
  iterations++;
}
if (iterations >= MAX_ITERATIONS) {
  return "Je n'ai pas pu trouver l'info. Pouvez-vous reformuler ?";
}
```

#### Erreur 4 : Réponse hors périmètre
**Fix prompt :**
```
Tu réponds uniquement aux questions liées à [domaine précis].
Pour toute autre demande : "Je suis spécialisé en [domaine]
et ne peux pas répondre à cela. Pour ce type de question,
contactez [ressource appropriée]."
```

### Cas d'usage : Agent comptable suivi de factures

**Prompt v1 (trop vague) :**
```
Tu es un assistant comptable. Aide à gérer les factures.
```

**Prompt v3 (après corrections) :**
```
Tu es un assistant comptable pour une TPE.

Règles issues des tests :
— Montants : toujours 2 décimales (ex: 1 234,56 €), jamais d'arrondi
— Si facture ambiguë : demander clarification AVANT d'analyser
— Distinguer explicitement HT / TTC / TVA dans chaque réponse
— Montant absent ou illisible → écrire MONTANT MANQUANT en majuscules
— Ne pas proposer d'écriture comptable sans identifier le type de dépense
— Toujours rappeler le numéro de facture et la date
```

### Cycle d'amélioration continue (méthode OODA)

> 💡 **En clair — le principe du cycle OODA :**
> OODA est une méthode de décision en 4 étapes pour améliorer progressivement votre agent. Elle est utilisée en pilotage militaire, puis reprise en gestion de projet. Appliquée ici :
>
> 1. **Observer** — collectez les réponses insatisfaisantes (score < 80%)
> 2. **Orienter** — classez-les par type d'erreur : hallucination / format incorrect / hors sujet / mauvais outil
> 3. **Décider** — identifiez le type d'erreur le plus fréquent
> 4. **Agir** — corrigez le prompt pour ce type d'erreur, relancez les tests
>
> Répétez le cycle jusqu'à atteindre votre seuil de qualité cible (85% recommandé). Le code ci-dessous traduit ce cycle en langage informatique pour les profils techniques.

```javascript
// Version code du cycle OODA — pour les profils Niveau C uniquement
const affinageCycle = {
  // 1. Observer — collecter les réponses dont le score est insuffisant
  observer: (log) => log.filter(r => r.scorePct < 80),

  // 2. Orienter — classer les erreurs par catégorie
  orienter: (erreurs) => ({
    hallucination: erreurs.filter(e => e.type === "donnee_inventee"),
    format:        erreurs.filter(e => e.type === "format_incorrect"),
    perimetre:     erreurs.filter(e => e.type === "hors_domaine"),
    outil:         erreurs.filter(e => e.type === "mauvais_outil")
  }),

  // 3. Décider — prioriser la catégorie la plus fréquente
  decider: (categories) =>
    Object.entries(categories).sort((a, b) => b[1].length - a[1].length)[0],

  // 4. Agir — ajouter une règle corrective au prompt et relancer les tests
  agir: (prompt, correctif, version) =>
    prompt + `\n\n// Règle v${version} :\n${correctif}`
};
```

### Checklist de validation avant mise en production

- [ ] Score moyen > 85% sur la batterie de tests complète
- [ ] Zéro hallucination détectée sur 20 tests variés
- [ ] L'agent demande une clarification face aux questions ambiguës
- [ ] L'agent refuse d'agir de façon irréversible sans confirmation
- [ ] La boucle d'itération est limitée (max_iterations configuré)
- [ ] Le périmètre est respecté (tests avec questions hors domaine)
- [ ] La mémoire fonctionne sur au moins 5 tours de conversation
- [ ] Les erreurs sont loggées et catégorisées automatiquement

---

## Ressources pour aller plus loin

- **Documentation API Claude :** https://docs.claude.ai
- **Guide de prompting :** https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
- **MCP (Model Context Protocol) :** https://docs.anthropic.com

---

*Plan de formation — Pôle Formation UIMM-CVDL — S. Jaubert — Mai 2026*
*Rédigé avec Claude*
