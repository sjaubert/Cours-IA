# Semaine 5 — Gmail, mémoire et workflows automatisés

> **Étape 3 · Semaine 5 sur 6**
> ⏱ 1 h 30 · 🔵 Niveau B/C — MCP Gmail · 👥 Profils mixtes

---

## 🎯 Ce que vous allez savoir faire à la fin de cette séance

- ✅ Comprendre ce que Claude peut faire avec vos emails
- ✅ Utiliser la mémoire conversationnelle dans un agent
- ✅ Concevoir un workflow email → action automatique
- ✅ Définir les limites éthiques de l'automatisation des emails

---

## 🧩 Les concepts clés de cette semaine

| Terme | Définition |
|---|---|
| 📧 **MCP Gmail** | Protocole qui connecte Claude à votre boîte Gmail — lire, trier, rédiger, et envoyer (avec votre accord). |
| 🧠 **Mémoire conversationnelle** | Historique des échanges transmis à Claude à chaque message, pour qu'il garde le contexte de la conversation. |
| 🔄 **Workflow** | Enchaînement automatique d'actions : lire un email → extraire une info → créer un événement → envoyer un accusé. |
| ✅ **Validation humaine** | Étape obligatoire avant qu'un agent envoie une communication en votre nom. L'humain reste responsable. |

---

## Ce que Claude peut faire avec Gmail (via MCP)

**✅ Actions recommandées (sans validation préalable)**
- Lire et résumer les emails non lus
- Trier par priorité (urgent / important / info)
- Proposer des brouillons de réponse
- Identifier les emails nécessitant une action
- Extraire des dates, chiffres, demandes
- Archiver ou étiqueter automatiquement

**⛔ Actions à valider impérativement avant exécution**
- Envoyer un email en votre nom
- Répondre à un client ou fournisseur
- Supprimer des emails
- Partager des informations confidentielles

---

## 🧠 Comment fonctionne la mémoire conversationnelle ?

```
Vous posez Q1          Claude répond        Vous posez Q2
« Qui est             → stocké dans    →   « Rédige-lui
  Marie Dupont ? »      la mémoire           un mail »
                                             ↓
                                        Claude utilise la réponse
                                        à Q1 sans que vous répétiez
```

> ⚠️ **Limite importante** : la mémoire ne dure que le temps de la conversation. Si vous fermez l'onglet et rouvrez le fichier HTML, l'historique est perdu.

---

## 🛠️ Activité 1 — Trier et résumer ses emails non lus

⏱ 20 min · 🔌 MCP Gmail · 👤 Individuel

### Requête de tri et priorisation

```
Lis mes 20 derniers emails non lus.

Classe-les en 3 catégories :
🔴 URGENT : nécessite une action aujourd'hui
🟡 IMPORTANT : nécessite une action cette semaine
🟢 INFO : aucune action requise, peut être archivé

Pour chaque email urgent et important, indique :
- Expéditeur et objet
- Ce qu'il faut faire exactement
- Date limite si mentionnée
```

### Requête de rédaction de réponse

```
Pour l'email de [nom de l'expéditeur] concernant [objet],
rédige une réponse professionnelle qui :
- Accuse réception de sa demande
- Indique que je traiterai cela avant vendredi
- Demande les pièces justificatives manquantes

Ton : professionnel et cordial. Longueur : 5-8 lignes maximum.

⚠️ NE PAS ENVOYER — me soumettre le brouillon d'abord.
```

> 💡 **Bonne pratique** : incluez toujours la mention « NE PAS ENVOYER » dans vos requêtes de rédaction, même si votre agent n'est pas configuré pour envoyer automatiquement.

---

## 🛠️ Activité 2 — Concevoir son premier workflow automatisé

⏱ 30 min · 🔵 Niveaux B/C · 👥 En binôme

Remplissez cette fiche pour définir votre workflow email personnalisé :

```
ÉTAPE 1 — Définir le déclencheur
Quel événement déclenche le workflow ?
□ Réception d'un email avec un mot-clé spécifique
□ Email d'un expéditeur précis (client, fournisseur…)
□ Email avec une pièce jointe d'un certain type
□ Autre : _________________________________

ÉTAPE 2 — Définir les actions
Que doit faire Claude automatiquement ?
□ Lire et résumer l'email
□ Extraire des données (montant, date, nom…)
□ Créer un fichier dans Drive
□ Ajouter un événement à l'Agenda
□ Rédiger un brouillon de réponse
□ Autre : _________________________________

ÉTAPE 3 — Définir les points de validation humaine
Qu'est-ce que Claude doit vous soumettre avant d'exécuter ?
□ Toutes les actions
□ Seulement les envois d'email
□ Seulement les créations de documents
□ Aucune (tout automatisé)
```

### Exemples de workflows métier

**🟢 RH :**
Email de candidature reçu → extraire CV + coordonnées → créer fiche candidat dans Drive → proposer créneau entretien dans Agenda

**🔵 Comptabilité :**
Email facture reçue → extraire montant + date + fournisseur → mettre à jour suivi des factures → créer rappel paiement Agenda

**🟣 Manager :**
Email incident de production reçu → classer par niveau de gravité → notifier les bonnes personnes → créer ticket de suivi Drive

---

## 📌 Ce que vous emportez de cette semaine

- Gmail + Drive + Agenda = un agent qui couvre l'essentiel du travail administratif quotidien
- La mémoire conversationnelle : Claude garde le fil d'une conversation, pas d'une session à l'autre
- **Règle d'or** : toujours valider avant qu'un email parte en votre nom
- La semaine prochaine (dernière !) : mesurer les progrès, corriger les erreurs, préparer la mise en production

---

*← [Semaine 4](semaine4.md) · [Plan général](plan_formation_agent_claude.html) · [Semaine 6 →](semaine6.md)*
