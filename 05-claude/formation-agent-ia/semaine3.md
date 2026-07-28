# Semaine 3 — Mesurer et améliorer la qualité des réponses

> **Étape 2 · Semaine 3 sur 6**
> ⏱ 2 × 1 h · 🔵 Niveau B — Fichier HTML · 👥 Profils mixtes

---

## 🎯 Ce que vous allez savoir faire à la fin de cette semaine

- ✅ Évaluer objectivement une réponse de Claude
- ✅ Utiliser une grille de qualité à 5 critères
- ✅ Constituer une bibliothèque de 5 scénarios de test
- ✅ Améliorer son prompt système de façon mesurable
- ✅ Distinguer une réponse correcte d'une hallucination

---

## 🧩 Les concepts clés de cette semaine

| Terme | Définition |
|---|---|
| 📊 **Grille d'évaluation** | Outil structuré pour noter objectivement une réponse selon plusieurs critères. Évite le jugement subjectif. |
| 🧪 **Scénario de test** | Question type représentative d'un usage réel, que l'on repose régulièrement pour surveiller la qualité. |
| 🌀 **Hallucination** | Quand Claude invente une information fausse avec l'air d'être sûr de lui. |
| ⚙️ **Prompt engineering** | L'art d'améliorer son prompt de façon itérative : tester → mesurer → modifier → retester. |

---

## 📊 La grille de qualité — 5 critères, score sur 15

Pour chaque réponse de votre agent, attribuez un score de **0 à 3** sur chacun des 5 critères :

| Critère | 0 — Insuffisant | 1 — Partiel | 2 — Correct | 3 — Excellent |
|---|---|---|---|---|
| **Pertinence** — répond-il à la question ? | Hors sujet | Partiellement | Oui, globalement | Précisément et complètement |
| **Exactitude** — informations vérifiables ? | Erreur grave ou invention | Approximatif | Correct mais incomplet | Précis et vérifiable |
| **Clarté** — compréhensible par le destinataire ? | Incompréhensible | Difficile à lire | Clair avec effort | Immédiatement clair |
| **Format** — mis en forme adapté à l'usage ? | Inadapté | Utilisable avec retouches | Adapté | Parfaitement adapté |
| **Prudence** — signale-t-il ses incertitudes ? | Aucune nuance | Vague | Signale les limites | Transparent sur ce qu'il ignore |

**Interprétation :**
- 0–5 : agent à retravailler en priorité
- 6–9 : utilisable avec relecture obligatoire
- 10–12 : bon niveau, à peaufiner
- 13–15 : agent de qualité production

---

## 🛠️ Activité 1 — Évaluer 3 réponses de son agent

⏱ 20 min · 🔵 Niveau B · 👤 Individuel

Posez les questions ci-dessous à votre agent (semaine 2). Pour chaque réponse, remplissez la grille et calculez votre score total.

### Questions de test par profil

**🟢 RH**
1. Quelles sont les conditions légales pour mettre un salarié en chômage partiel ?
2. Rédige un courrier de convocation à entretien préalable au licenciement.
3. Quelle est la durée légale du préavis pour un cadre avec 5 ans d'ancienneté ?

**🔵 Comptabilité**
1. Comment comptabiliser une facture d'achat avec TVA déductible à 20 % ?
2. Quels sont les délais de paiement légaux entre professionnels en France ?
3. Explique la différence entre charge et immobilisation pour l'achat d'un ordinateur.

**🟣 Manager**
1. Comment gérer un conflit entre deux opérateurs sur le planning de week-end ?
2. Quels indicateurs de sécurité dois-je afficher obligatoirement dans mon atelier ?
3. Propose un plan d'action pour réduire le taux d'absentéisme de 15 % en 6 mois.

### 📋 Étapes à suivre

1. Copiez chaque question dans votre agent HTML et envoyez-la.
2. Lisez attentivement la réponse, sans chercher à la corriger immédiatement.
3. Notez un score de 0 à 3 pour chacun des 5 critères.
4. Identifiez le critère le plus faible — c'est votre priorité d'amélioration.
5. Comparez vos scores avec votre voisin sur la même question.

---

## 🛠️ Activité 2 — Construire ses 5 scénarios de test

⏱ 25 min · 🔵 Niveau B · 👤 Individuel

Ces 5 questions deviendront votre **étalon** : vous les reposerez à chaque modification de votre agent pour vérifier que la qualité s'améliore.

Recopiez et complétez ce modèle pour chacun de vos 5 scénarios :

```
SCÉNARIO DE TEST N°__

Question posée :
(Écrivez ici la question exacte que vous envoyez à l'agent)

Contexte d'usage :
(Dans quelle situation réelle poseriez-vous cette question ?)

Réponse attendue — critères de succès :
- Pertinence : ___________________________
- Exactitude : ___________________________
- Clarté : ______________________________
- Format : ______________________________
- Prudence : ____________________________

Score obtenu aujourd'hui : ___ / 15
Score cible (semaine 6) :   ___ / 15
```

> 💡 **Comment choisir ses 5 scénarios ?** Variez : une question simple (vérification factuelle), deux questions de rédaction, une question d'analyse, une question sur un cas délicat ou ambigu.

---

## 🛠️ Activité 3 — Améliorer son prompt selon le critère le plus faible

⏱ 15 min · 🔵 Niveau B · 👥 En binôme

Identifiez votre critère le plus faible, puis ajoutez la correction correspondante à la fin de votre prompt système :

| Critère faible | Ajout à faire dans le prompt système |
|---|---|
| **Pertinence** | *« Si ma question ne concerne pas ton domaine d'expertise, dis-le et redirige-moi vers la bonne ressource plutôt que d'inventer une réponse. »* |
| **Exactitude** | *« Si tu n'es pas certain d'une information réglementaire ou chiffrée, indique-le avec la mention [À VÉRIFIER]. »* |
| **Clarté** | *« Mon interlocuteur n'est pas spécialiste. Utilise des phrases courtes, évite le jargon, illustre avec un exemple concret. »* |
| **Format** | *« Sauf demande contraire, structure tes réponses : un résumé en 2 lignes, puis les détails en bullet points. »* |
| **Prudence** | *« Rappelle systématiquement que tes réponses sont informatives et ne remplacent pas l'avis d'un professionnel. »* |

### 📋 Étapes à suivre

1. Identifiez votre critère le plus faible (score moyen le plus bas sur vos 3 tests).
2. Copiez la correction correspondante du tableau ci-dessus.
3. Ajoutez-la à la fin de votre prompt système dans le fichier HTML.
4. Reposez la question qui avait eu le score le plus faible. Réévaluez avec la grille.
5. Le score a-t-il augmenté ? De combien de points ?

---

## 📌 Ce que vous emportez de cette semaine

- Une grille de qualité à 5 critères, applicable à n'importe quel agent IA
- 5 scénarios de test documentés, votre référence pour toute la suite
- La méthode : **tester → mesurer → modifier le prompt → retester**
- La semaine prochaine : connecter Claude à vos outils (Drive, Agenda) via les MCP

---

*← [Semaine 2](semaine2.md) · [Plan général](plan_formation_agent_claude.html) · [Semaine 4 →](semaine4.md)*
