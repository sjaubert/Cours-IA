# Activité 2 : Assistant Diagnostic de Pannes Multi-Sources

## 📋 Contexte Professionnel

Vous êtes technicien de maintenance et devez diagnostiquer une panne sur un équipement. Vous disposez de manuels techniques et de guides de dépannage. L'IA va vous aider à **exploiter systématiquement** cette documentation pour établir un diagnostic méthodique.

## 🎯 Objectifs Pédagogiques

1. Structurer l'observation des symptômes
2. Exploiter efficacement une base documentaire technique
3. Établir un diagnostic par élimination
4. Proposer un plan de vérification

## ⏱️ Durée

**45 minutes**

## 📦 Livrables Attendus

1. Fiche de diagnostic complétée
2. Liste hiérarchisée des causes probables
3. Plan d'action de vérification

---

## 🛠️ Étapes de Travail

### Étape 1 : Choix du Scénario (5 min)

1. **Lisez** le fichier `scenarios_pannes.md`
2. **Choisissez** un des 5 scénarios proposés
3. **Notez** tous les symptômes observés

### Étape 2 : Analyse avec Gemini (20 min)

#### Prompt Étape 1 : Chargement de la Documentation

```
Je vais te fournir un manuel technique de dépannage. Lis-le attentivement.

[Copier-coller le contenu du manuel correspondant à votre équipement]

Confirme que tu as bien lu et compris ce manuel avant que je te présente le problème.
```

#### Prompt Étape 2 : Présentation du Problème

```
Voici le problème que je rencontre :

**Equipement** : [Nom de l'équipement]

**Symptômes observés** :
- [Symptôme 1]
- [Symptôme 2]
- [Etc.]

**Observations complémentaires** :
- [Information contextuelle 1]
- [Information contextuelle 2]

En te basant UNIQUEMENT sur le manuel technique que je t'ai fourni,
quelles sont les 3 causes les plus probables de cette panne ?

Classe-les par ordre de probabilité et explique pourquoi.
```

#### Prompt Étape 3 : Plan de Vérification

```
Pour vérifier ces hypothèses, quel serait ton plan d'action ?

Indique pour chaque cause probable :
1. Les vérifications à effectuer
2. L'ordre dans lequel les faire (du plus simple au plus complexe)
3. Les outils/instruments nécessaires
```

**À faire** :
- Suivre les recommandations de l'IA
- **Vérifier** la pertinence par rapport au manuel
- **Questionner** si une recommandation semble incohérente

### Étape 3 : Compléter la Fiche de Diagnostic (15 min)

Utilisez le template suivant :

```markdown
# FICHE DE DIAGNOSTIC

## Identification
- **Date** : [Date]
- **Équipement** : [ID + Type]
- **Technicien** : [Votre nom]

## Symptômes Observés
-  Symptôme 1][Description précise]
- [Symptôme 2]
- [...]

## Causes Probables (par ordre de probabilité)

### 1. [Cause #1] - Probabilité : ÉLEVÉE
**Indices concordants** :
- [Pourquoi cette hypothèse]

**Vérifications à effectuer** :
1. [Action 1]
2. [Action 2]

**Matériel nécessaire** :
- [Outil/instrument]

---

### 2. [Cause #2] - Probabilité : MOYENNE
[Même structure]

---

### 3. [Cause #3] - Probabilité : FAIBLE
[Même structure]

## Plan d'Action

**Ordre d'intervention** :
1. [Vérification la plus simple/rapide]
2. [Vérification suivante]
3. [...]

**Durée estimée** : [Temps]

**Pièces à prévoir** :
- [Si remplacement probable]

## Validation Formateur
Cause réelle identifiée : ☐ OUI ☐ NON
Démarche méthodique : ☐ OUI ☐ NON
```

### Étape 4 : Débrief (5 min)

**Questions de réflexion** :
1. L'IA a-t-elle identifié la cause correcte ?
2. A-t-elle proposé des vérifications pertinentes ?
3. Y a-t-il des incohérences dans ses recommandations ?
4. Comment as-tu utilisé ta connaissance métier pour valider/corriger ?

---

## 📊 Critères d'Évaluation

| Critère | Points |
|---------|--------|
| **Qualité de l'interaction avec l'IA** : Prompts structurés, questions pertinentes | 25% |
| **Diagnostic** : Causes probables pertinentes et bien hiérarchisées | 30% |
| **Plan de vérification** : Logique, complet, réaliste | 25% |
| **Esprit critique** : Validation des recommandations IA, utilisation du manuel | 20% |

---

## 💡 Conseils

1. **Structurez vos prompts** : Plus vous êtes précis, meilleure sera la réponse
2. **Fournissez le contexte** : L'IA doit connaître la documentation
3. **Vérifiez systématiquement** : Comparez les réponses avec le manuel
4. **Itérez** : N'hésitez pas à poser des questions de suivi
5. **Restez critique** : L'IA peut extrapoler ou se tromper

## ⚠️ Pièges à Éviter

- ❌ **Ne pas lire le manuel** : L'IA doit s'appuyer sur la doc fournie
- ❌ **Accepter aveuglément** : Toujours valider avec la documentation
- ❌ **Prompts trop vagues** : "Diagnostique cette panne" → Trop général
- ❌ **Oublier le contexte** : Préciser équipement, historique, environnement

## 🚀 Aller Plus Loin (Optionnel)

Si vous terminez en avance :

1. **Comparez** votre diagnostic avec celui d'un camarade sur le même scénario
2. **Diagnostiquez** un deuxième scénario
3. **Créez** votre propre scénario à partir d'une vraie situation rencontrée en stage

---

**Documentation disponible** :
- `base_connaissances/manuel_pompe_centrifuge.md` → Scénario 1
- `base_connaissances/guide_variateur_frequence.md` → Scénarios 2 et 5
- `base_connaissances/guide_pneumatique.md` → Scénario 3
- Pour le scénario 4 (compresseur), utilisez les connaissances générales IA

---

**Bonne chance pour votre diagnostic ! 🔍**
