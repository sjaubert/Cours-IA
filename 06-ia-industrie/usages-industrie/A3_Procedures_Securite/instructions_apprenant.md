# Activité 3 : Génération de Procédures de Sécurité

## 📋 Contexte

Vous devez créer une procédure de consignation pour une intervention de maintenance. Vous allez utiliser l'IA pour générer un premier jet, puis le **critiquer et corriger** pour le rendre conforme aux normes de sécurité.

## ⏱️ Durée : 40 minutes

---

## Étape 1 : Choix du Contexte (5 min)

1. Lisez `contextes_interventions.md`
2. Choisissez un contexte
3. Consultez le `template_procedure.md` pour voir la structure attendue

---

## Étape 2 : Génération avec Gemini (15 min)

### Prompt Suggéré :

```
Je dois créer une procédure de consignation/déconsignation pour l'intervention suivante :

**Machine** : [Nom]
**Intervention** : [Description]

**Énergies présentes** :
- Électrique : [Détails]
- Mécanique : [Détails]
- [Autres énergies...]

**Environnement** :
- [Particularités]

En te basant sur les normes de sécurité françaises (NFC 18-510 pour l'électrique, 
Décret 88-1056 sur la consignation), génère une procédure détaillée de consignation/
déconsignation incluant :

1. Identification des risques
2. EPI nécessaires
3. Étapes de consignation (séparation, condamnation, vérification)
4. Étapes de déconsignation

Sois précis sur chaque action à effectuer.
```

**Copiez** la procédure générée dans un fichier texte.

---

## Étape 3 : Critique et Correction (15 min)

### Vérifications Obligatoires

Comparez avec le `template_procedure.md` et vérifiez :

#### ✅ Structure
- [ ] Identification complète (machine, type intervention)
- [ ] Risques identifiés (toutes les énergies)
- [ ] EPI listés
- [ ] Procédure de consignation étape par étape
- [ ] Procédure de déconsignation

#### ✅ Consignation Électrique (si applicable)
- [ ] Séparation : ouverture disjoncteur/sectionneur
- [ ] Condamnation : cadenas + étiquette
- [ ] Vérification : VAT (Vérificateur Absence Tension)
- [ ] Ordre correct : vérifier VAT → mesurer → revérifier VAT

#### ✅ Règle "1 Personne = 1 Cadenas"
- [ ] Mentionnée clairement
- [ ] Chaque intervenant pose SON propre cadenas

#### ✅ Énergies Résiduelles
- [ ] Si condensateurs : temps d'attente mentionné (3-5 min)
- [ ] Si pression : purge mentionnée
- [ ] Si température : refroidissement mentionné

#### ✅ Calage Mécanique
- [ ] Si système peut bouger sous gravité : calage obligatoire
- [ ] Type de cale précisé

### Liste de Corrections

Créez un document listant :

```markdown
## Corrections Apportées

### 1. [Titre de la correction]
**Problème identifié** : [Ce qui manquait ou était faux]
**Correction** : [Ce que vous avez ajouté/modifié]
**Justification** : [Pourquoi c'est nécessaire]

### 2. [Titre]
[...]
```

---

## Étape 4 : Procédure Finale (5 min)

Générez la version finale :
- Utilisez le format du `template_procedure.md`
- Intégrez toutes vos corrections
- Relisez pour cohérence

---

## 📊 Critères d'Évaluation

| Critère | Points |
|---------|--------|
| **Complétude** : Toutes les sections présentes | 20% |
| **Conformité électrique** : VAT, cadenas, MALT si HT | 25% |
| **Gestionénergies** : Toutes prises en compte | 20% |
| **Corrections pertinentes** : Esprit critique | 25% |
| **Rédaction** : Clarté, précision | 10% |

---

## ⚠️ Points Critiques (Fréquemment Oubliés par l'IA)

1. **Vérification VAT** en 3 temps (avant-pendant-après)
2. **Purge pneumatique/hydraulique** (actionner le vérin)
3. **Ordre de déconsignation** inverse de la consignation
4. **Calage mécanique** pour les systèmes pouvant bouger
5. **Temps d'attente** décharge condensateurs (variateurs)
6. **Balisage** de la zone de travail

---

## 💡 Conseils

- L'IA génère souvent des procédures "génériques" → **Adaptez** au contexte précis
- Vérifiez que chaque action est **concrète** (pas "couper l'alimentation" mais "ouvrir disjoncteur Q12")
- Pensez **sécurité** avant tout : en cas de doute, soyez plus restrictif

## 🚨 Sécurité Avant Tout

Cette activité porte sur la **sécurité des personnes**. Une procédure incomplète peut entraîner un accident mortel.  
→ Soyez **exigeant** avec la génération IA !

---

**Bon travail ! ⚡🔒**
