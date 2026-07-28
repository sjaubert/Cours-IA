# Module 5 — Méthodologies et Bonnes Pratiques
## Travailler efficacement avec les agents IA

> **Durée :** 2h  
> **Objectif :** Maîtriser les méthodes qui transforment Claude d'un outil occasionnel en collaborateur fiable

---

## 5.1 Le principe fondamental : définir avant d'agir

### Le problème des utilisateurs débutants

La grande majorité des utilisateurs déçus par les outils IA font la même erreur : ils demandent de l'aide avant d'avoir clairement défini ce qu'ils attendent.

**Exemple de mauvais usage :**
> "Prépare-moi un rapport sur nos ventes"

**Ce que l'agent ne sait pas :**
- Quelles ventes ? Quelle période ? Quel marché ?
- Quel format ? Quelle longueur ?
- Pour qui ? Quel niveau de détail ?
- Quelles données utiliser ?
- Quels indicateurs sont importants pour l'entreprise ?

Le résultat est inévitablement une production générique que vous devrez refaire.

**La règle des 3 C :**
Avant toute demande, définissez :
- **Contexte** : Qui vous êtes, où vous en êtes, quel est l'environnement
- **Critères** : Comment vous saurez que le résultat est bon
- **Contraintes** : Ce qui ne peut pas être fait, les limites à respecter

---

## 5.2 La méthode Superpowers — le workflow en 7 phases

Inspiré du dépôt [superpowers](https://github.com/obra/superpowers) (94 000 ⭐), cette méthodologie est la plus rigoureuse disponible dans l'écosystème.

### Principe
> Travailler avec Claude comme avec un collaborateur senior : d'abord penser, puis planifier, puis produire, puis vérifier.

### Les 7 phases

#### Phase 1 — Brainstorm
**Objectif :** Explorer le problème avant de se précipiter sur les solutions.

**Prompt type :**
> "Je dois [décrire l'objectif]. Avant que nous commencions à produire quoi que ce soit, aide-moi à explorer toutes les dimensions de ce problème. Quelles sont les questions que je devrais me poser ? Quels sont les risques ? Les alternatives ?"

**Durée recommandée :** 10 à 20% du temps total du projet

---

#### Phase 2 — Spec (Spécification)
**Objectif :** Définir précisément et par écrit ce qu'on veut obtenir.

**Document produit :**
```markdown
# Spécification : [Nom du livrable]

## Objectif
[Ce qu'on veut obtenir et pourquoi]

## Public cible
[Qui va utiliser/lire ce livrable]

## Format et contraintes
[Format exact, longueur, outils à utiliser, standards à respecter]

## Critères de succès
[Comment on sait que c'est bon - critères vérifiables]

## Hors périmètre
[Ce qu'on ne veut PAS dans ce livrable]
```

---

#### Phase 3 — Plan
**Objectif :** Décomposer le travail en étapes séquentielles et vérifiables.

**Prompt type :**
> "Sur la base de cette spécification [joindre le doc], propose un plan de travail en [5 à 8] étapes. Pour chaque étape : ce qui sera produit, comment on vérifie que c'est fait, ce qui bloque la suite si ce n'est pas validé."

**Résultat attendu :**
```
Étape 1 → Livrable : [...] → Vérification : [...]
Étape 2 → Livrable : [...] → Vérification : [...] → Bloquant si : [...]
...
```

---

#### Phase 4 — TDD (Validation avant production)
**Objectif :** Définir les critères de validation *avant* de produire.

**Ce que ça signifie hors développement logiciel :**
- Pour un rapport : définir les questions auxquelles il doit répondre avant de l'écrire
- Pour une procédure : définir les cas de test qu'elle doit couvrir avant de la rédiger
- Pour une formation : définir les compétences attendues avant de créer le contenu

**Prompt type :**
> "Avant de commencer la production, définis les 5 tests que le livrable final devra passer pour être accepté. Formule-les comme des questions auxquelles une personne lambda devrait pouvoir répondre après avoir lu/utilisé le livrable."

---

#### Phase 5 — Développement (par sous-agents)
**Objectif :** Produire selon le plan, avec des agents spécialisés si nécessaire.

**Règle clé :** L'agent produit par étapes, en validant chaque étape avant de passer à la suivante.

**Anti-pattern à éviter :**
> "Fais tout le rapport d'un coup"

**Pattern recommandé :**
> "Produis l'étape 1 du plan. Attends ma validation avant de continuer."

---

#### Phase 6 — Review (Revue)
**Objectif :** Évaluer le résultat produit par rapport aux critères définis en phase 4.

**Prompt de review :**
> "Voici le livrable produit [joindre]. Évalue-le par rapport aux critères de validation définis [joindre]. Pour chaque critère : est-il satisfait ? Quel est le niveau de qualité ? Que faudrait-il améliorer ?"

**Important :** Cette revue peut (et doit) impliquer l'humain. L'agent peut faire une auto-évaluation, mais la validation finale reste humaine.

---

#### Phase 7 — Finalize (Livraison)
**Objectif :** Produire la version finale propre, sans les "résidus" du travail de production.

**Prompt type :**
> "Sur la base de la revue, produis la version finale du livrable. Élimine les notes de travail, les commentaires de production, les versions intermédiaires. Le livrable doit être directement utilisable par son destinataire."

---

### Application rapide de la méthode

Pour les tâches courtes, vous n'avez pas besoin des 7 phases complètes. Un mini-workflow en 3 étapes suffit :

```
1. SPEC (2 minutes) : Écrire ce qu'on veut, pour qui, en quel format
2. PRODUCE : Laisser l'agent travailler
3. REVIEW : Vérifier par rapport à la spec
```

---

## 5.3 La gestion du contexte — éviter la dérive

### Le problème de la dérive de contexte

Dans une longue session de travail, l'agent peut progressivement "oublier" les instructions initiales. C'est le "context drift". Inspiré du dépôt [get-shit-done](https://github.com/gsd-build/get-shit-done).

### Symptômes à surveiller

- L'agent commence à ignorer des contraintes définies au début
- Les livrables divergent du format demandé
- L'agent réintroduit des approches que vous aviez écartées
- Les réponses deviennent plus génériques

### Stratégies de prévention

**1. Sessions courtes et ciblées**
Plutôt qu'une session de 4 heures, faites 4 sessions d'une heure avec un résumé de handoff entre chaque.

**2. Le fichier CLAUDE.md comme ancre**
Les instructions dans CLAUDE.md sont relues à chaque session. Ce qu'on veut garder permanent doit y être.

**3. Le "résumé de session"**
En fin de session :
> "Fais un résumé de 10 lignes de ce que nous avons accompli et des décisions prises. Je le garderai pour la prochaine session."

Ce résumé devient le contexte de départ de la session suivante.

**4. Les points de contrôle explicites**
> "Avant de continuer, récapitule : quel est notre objectif ? Où en sommes-nous ? Quelles contraintes devons-nous respecter ?"

---

## 5.4 L'art du prompt — écrire pour être compris

### Les principes du bon prompt

**Principe 1 — La précision sur la généralité**
❌ "Améliore ce document"  
✅ "Dans ce document, améliore la clarté des deux premiers paragraphes pour un public non-expert. Garde le même fond, reformule uniquement les phrases de plus de 30 mots."

**Principe 2 — Le contexte avant l'instruction**
❌ "Rédige un email pour refuser cette demande"  
✅ "Je suis responsable achats dans une entreprise aéronautique. Un fournisseur demande une extension de 30 jours de délai de paiement. Nous ne pouvons pas accorder cette extension pour raison de trésorerie, mais nous voulons maintenir la relation commerciale. Rédige un email de refus poli et constructif."

**Principe 3 — Les exemples valent mieux que les descriptions**
❌ "Écris dans un style professionnel"  
✅ "Voici un exemple de notre style de communication : [extrait]. Écris dans ce même style."

**Principe 4 — Définir le format de sortie explicitement**
❌ "Résume ce document"  
✅ "Résume ce document sous forme d'un tableau à 3 colonnes : Sujet | Point clé | Action recommandée. Maximum 10 lignes."

**Principe 5 — Les contraintes négatives**
Dire ce qu'on ne veut pas est aussi important que dire ce qu'on veut.
> "Ne pas inclure d'introduction générale. Ne pas dépasser 2 pages. Ne pas utiliser de jargon technique."

### Structure d'un prompt complet

```
[RÔLE] Tu es [qui]
[CONTEXTE] Dans le cadre de [situation]
[TÂCHE] Tu dois [action précise]
[FORMAT] Le résultat doit être [format, longueur, structure]
[CONTRAINTES] Tu ne dois pas [ce qui est exclu]
[EXEMPLES] Voici un exemple de ce que j'attends : [exemple]
[VALIDATION] Je saurai que c'est bon si [critère vérifiable]
```

### Le prompt engineering avancé

La ressource ultime pour aller plus loin : [claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) et sa documentation hebdomadaire.

La documentation officielle Anthropic : [docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)

---

## 5.5 L'orchestration d'équipes — diviser pour mieux régner

### Pourquoi plusieurs agents valent mieux qu'un seul

Un agent unique qui traite une tâche très longue accumule du contexte, fatigue, dérive. Plusieurs agents spécialisés sont plus fiables car :
- Chacun a un contexte court et ciblé
- Leurs erreurs ne se propagent pas
- Ils peuvent travailler en parallèle
- Les handoffs sont des points de contrôle naturels

### Le modèle d'équipe projet (inspiré de [gstack](https://github.com/garrytan/gstack))

```
Chef de projet (Agent principal)
│
├── Spécialiste domaine → produit le contenu expert
│
├── Réviseur → vérifie la qualité et la cohérence
│
├── Communicant → adapte le contenu au public cible
│
└── Contrôleur → vérifie la conformité aux contraintes
```

### Comment définir les rôles

Chaque agent a besoin de :
1. **Un nom de rôle clair** : "Analyste Qualité" plutôt que "Assistant 1"
2. **Une mission précise** : "Tu analyses uniquement les données de non-conformité"
3. **Des outils spécifiques** : Accès aux données, aux templates, aux outils de son domaine
4. **Des critères de livraison** : Comment on sait que son travail est terminé
5. **Une règle d'escalade** : Quand doit-il demander une validation humaine ?

---

## 5.6 Sécurité et gouvernance des agents

### Les principes de base

La mise en place d'agents IA dans une entreprise doit respecter des principes de gouvernance. Le dépôt [everything-claude-code](https://github.com/affaan-m/everything-claude-code) intègre un module de sécurité complet.

**Principe 1 — Moindre privilège**
Un agent ne doit avoir accès qu'aux données et systèmes nécessaires à sa tâche, et rien de plus.

**Principe 2 — Traçabilité**
Toute action d'un agent doit être loggée et auditable. Qui a demandé quoi, quand, résultat obtenu.

**Principe 3 — Validation humaine obligatoire sur les actions irréversibles**
Supprimer des fichiers, envoyer des emails à des tiers, modifier des données de référence — toujours avec confirmation humaine.

**Principe 4 — Données sensibles**
Définir explicitement dans CLAUDE.md les données qui ne doivent jamais être traitées par un agent IA (données personnelles, données confidentielles, secrets commerciaux).

### Un framework de gouvernance simple

```markdown
# Politique d'usage des agents IA — [Entreprise]

## Données autorisées pour traitement IA
- Documents internes non confidentiels
- Données agrégées et anonymisées
- Correspondances de travail standard

## Données interdites pour traitement IA
- Données personnelles des salariés (sauf RH avec protocole spécifique)
- Données clients avec identifiants
- Informations contractuelles confidentielles
- Données financières nominatives

## Actions nécessitant validation humaine
- Envoi d'emails externes
- Modification de données de référence
- Suppression de fichiers
- Actions sur systèmes de production

## Revue obligatoire
Tout workflow agent utilisé plus de 10 fois par semaine doit être reviewé
mensuellement par le responsable IT.
```

---

## 5.7 Mesurer et améliorer

### Calculer le ROI d'un agent

Pour justifier l'investissement en temps de configuration :

```
ROI = (Temps gagné par usage × Fréquence) - Temps de configuration

Exemple :
- Configuration d'un agent de rapport mensuel : 4h
- Gain par rapport : 6h (de 8h à 2h)
- Fréquence : 12 fois/an
- ROI = (6h × 12) - 4h = 68h gagnées dès la première année
```

### Les indicateurs à suivre

- Temps de cycle de la tâche (avant/après)
- Nombre de révisions nécessaires sur les livrables
- Taux d'utilisation (les agents non utilisés n'ont pas d'intérêt)
- Satisfaction des utilisateurs / qualité perçue

### L'amélioration continue

Chaque agent doit être amélioré régulièrement :
1. Collecter les feedbacks d'utilisation
2. Identifier les cas où le résultat était décevant
3. Analyser la cause racine (mauvais prompt ? contexte insuffisant ? contrainte manquante ?)
4. Mettre à jour le CLAUDE.md
5. Retester sur les cas problématiques

---

## Points clés à retenir

- Définir avant d'agir : spec, critères, contraintes — puis produire
- La méthode Superpowers en 7 phases garantit des résultats cohérents sur les projets longs
- La gestion du contexte est critique : sessions courtes, résumés de handoff, CLAUDE.md comme ancre
- Un bon prompt = rôle + contexte + tâche + format + contraintes + critères de validation
- La gouvernance des agents est une responsabilité partagée IT/métier

---

## Questions de révision

1. Quelles sont les 3 phases les plus importantes de la méthode Superpowers et pourquoi ?
2. Vous constatez que les livrables de votre agent deviennent de plus en plus génériques au fil de la journée. Quel est le problème probable et comment le résoudre ?
3. Définissez les données de votre métier qui ne devraient JAMAIS être traitées par un agent IA.

---

*Module précédent : [← Cas d'usage métier](04-cas-usage-metiers.md) | Prochain module : [Guide de démarrage →](06-guide-demarrage.md)*
