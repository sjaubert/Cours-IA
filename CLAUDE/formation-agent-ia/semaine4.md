# Semaine 4 — Connecter Claude à Drive et Agenda

> **Étape 3 · Semaine 4 sur 6**
> ⏱ 1 h 30 · 🔵 Niveau B/C — MCP Google · 👥 Profils mixtes

---

## 🎯 Ce que vous allez comprendre et savoir faire

- ✅ Comprendre ce qu'est un MCP et à quoi il sert
- ✅ Savoir ce que Claude peut faire avec Drive et Agenda
- ✅ Formuler des requêtes vers un agent multi-outils
- ✅ Identifier 2 cas d'usage MCP dans votre métier

---

## 🧩 Les concepts clés de cette semaine

| Terme | Définition |
|---|---|
| 🔌 **MCP** | Model Context Protocol — protocole standard qui connecte Claude à des outils extérieurs (Drive, Agenda, Gmail…). |
| 🛠️ **Outil (tool)** | Fonction spécifique mise à disposition de Claude par un MCP. Ex : `list_files`, `read_document`, `create_event`. |
| 🔐 **OAuth** | Système d'autorisation : vous autorisez Claude à accéder à votre Drive sans lui donner votre mot de passe. |
| 📋 **Agent multi-outils** | Agent capable d'utiliser plusieurs MCP dans une seule requête : lire Drive + créer un événement Agenda. |

### Comment ça fonctionne ?

```
🧠 Claude  ⟺  🔌 MCP  ⟺  📁 Drive
                        +  📅 Agenda
```

Sans MCP, Claude ne peut pas lire vos fichiers Drive ni créer des événements dans votre Agenda — même si vous le lui demandez. Le MCP est le câble qui crée la connexion.

---

## Ce que Claude peut faire avec Drive (via MCP)

- Lister les fichiers d'un dossier
- Lire le contenu d'un document
- Rechercher un fichier par nom ou contenu
- Créer un nouveau document
- Résumer un rapport
- Extraire des données d'une feuille de calcul

## Ce que Claude peut faire avec Agenda Google (via MCP)

- Lister vos événements du jour ou de la semaine
- Créer un rendez-vous
- Déplacer un événement
- Vérifier les disponibilités
- Envoyer une invitation

---

## 🛠️ Activité 1 — Interroger l'agent sur un dossier Drive partagé

⏱ 20 min · 🔌 MCP Drive · 👤 Individuel

Le formateur a préparé un dossier Drive partagé avec des documents exemples. Testez ces requêtes sur l'agent configuré avec le MCP Drive.

### Requêtes à tester

```
# Requête 1 — Lister les fichiers disponibles
Liste tous les fichiers dans le dossier partagé "Formation-MCP".
Pour chaque fichier, indique son type et sa date de modification.
```

```
# Requête 2 — Lire et résumer un document
Lis le fichier "rapport_mensuel_avril.docx" et fais-moi
un résumé en 5 points clés, avec les chiffres importants.
```

```
# Requête 3 — Recherche thématique (RH)
Dans tous les documents du dossier, trouve les mentions
de "congés payés" ou "arrêt maladie" et liste les
décisions ou procédures associées.
```

```
# Requête 4 — Extraction de données (Compta)
Dans la feuille de calcul "suivi_factures_2026.xlsx",
liste toutes les factures dont le statut est "impayé"
et dont le montant dépasse 1000 €.
```

### 📋 Étapes à suivre

1. Ouvrez l'agent configuré avec le MCP Drive (lien fourni en séance).
2. Testez chacune des 4 requêtes ci-dessus. Notez le temps de réponse.
3. Inventez votre propre requête liée à votre métier et testez-la.
4. Évaluez la réponse avec votre grille de qualité (semaine 3).

---

## 🛠️ Activité 2 — Créer des événements Agenda à partir de documents

⏱ 25 min · 🔌 MCP Drive + Agenda · 👥 En binôme

En une seule requête, l'agent lit un document Drive et crée automatiquement des événements dans Google Agenda.

### Requête multi-outils

```
Lis le fichier "CR_reunion_planification_mai.docx"
dans le dossier Formation-MCP.

Extrais toutes les actions décidées avec leur responsable
et leur date limite.

Pour chaque action, crée un événement dans mon agenda Google avec :
- Titre : "[ACTION] " + description courte
- Date : la date limite mentionnée dans le CR
- Description : le contexte complet de l'action
- Durée : 30 minutes (rappel de suivi)

Si une date est manquante ou ambiguë, demande-moi de confirmer
avant de créer l'événement.
```

### Variantes par profil

**🟢 RH :**
```
Lis le planning des entretiens annuels et crée un événement Agenda
pour chaque entretien avec le nom du salarié en titre.
```

**🔵 Comptabilité :**
```
Lis le tableau des échéances fiscales et crée un rappel Agenda
5 jours avant chaque deadline.
```

**🟣 Manager :**
```
Lis le planning de maintenance préventive et crée un événement
hebdomadaire récurrent pour chaque machine.
```

---

## 📌 Ce que vous emportez de cette semaine

- Un MCP = une connexion entre Claude et un outil. Chaque outil a son MCP.
- Claude peut enchaîner plusieurs outils dans une seule requête (lire Drive → créer Agenda)
- La configuration des MCP se fait **une fois par l'équipe technique** — ensuite, l'utilisateur formule sa requête en langage naturel
- La semaine prochaine : Gmail + mémoire conversationnelle

---

*← [Semaine 3](semaine3.md) · [Plan général](plan_formation_agent_claude.html) · [Semaine 5 →](semaine5.md)*
