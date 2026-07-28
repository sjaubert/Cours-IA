# Activité 5 : Documentation Technique Interactive

## 📋 Contexte

Vous devez former des nouveaux techniciens au dépannage d'un variateur de fréquence. Le manuel technique fait 80 pages. Votre mission : créer UN GUIDE RAPIDE (2 pages max) pour les pannes les plus fréquentes.

## ⏱️ Durée : 35 min

---

## Étape 1 : Lecture du Manuel (5 min)

Parcourez `manuel_variateur_complet.md` → C'est dense, technique, exhaustif.

**Votre défi** : Rendre ça accessible pour un débutant !

---

## Étape 2 : Extraction avec Gemini (20 min)

### Prompt 1 : Identification des Pannes Fréquentes

```
Je vais te fournir un extrait de manuel technique de variateur de fréquence.

[Copier-coller le manuel]

Identifie :
1. Les 5 codes d'erreur les plus critiques/fréquents
2. Pour chacun : cause probable + solution simple

Présente sous forme de tableau clair pour un technicien débutant.
```

### Prompt 2 : Création d'un Arbre Décisionnel

```
Crée un arbre décisionnel simple pour diagnostiquer une panne de variateur :

Commence par "Le variateur est en défaut" et pose des questions YES/NO simples
qui mènent au code erreur probable.

Exemple :
- Le variateur s'arrête en décélération ? OUI → Probable OVF
- Non → Le variateur chauffe ? OUI → Probable OHF
- Etc.

Format texte simple (style flowchart en texte).
```

### Prompt 3 : Simplification du Langage

```
Réécris ces explications techniques en langage simple pour un apprenti :

[Coller un extrait complexe du manuel]

Objectif : Compréhensible sans jargon, avec des exemples concrets.
```

---

## Étape 3 : Création du Guide Rapide (10 min)

Créez un document final structuré :

``markdown
# GUIDE RAPIDE DÉPANNAGE - Variateur ATV320

## 🚨 Top 5 des Pannes

### 1. Code OVF - Surten sion Bus

**Quand ?** Variateur s'arrête pendant le freinage  
**Pourquoi ?** Freinage trop rapide, énergie retourne dans le variateur  
**Solution** :  
1. Augmenter la rampe de décélération (menu DEC, passer de 3s à 20s)
2. Ou installer résistance de freinage

---

### 2. Code OHF - Surchauffe

**Quand ?** Variateur chaud, arrêt en cours de fonctionnement  
**Pourquoi ?** Ventilation bouchée ou température ambiante trop haute  
**Solution** :  
1. Nettoyer le filtre (sur côté variateur)
2. Vérifier T°C armoire < 40°C
3. Vérifier ventilateur tourne

---

[Etc. pour les 5 codes]

## 🔍 Arbre de Diagnostic Rapide

```
Le variateur est en DÉFAUT
│
├─ Il s'arrête pendant le FREINAGE ?
│  └─ OUI → Code OVF probable
│     └─ Action : Augmenter rampe DEC
│
├─ Il est CHAUD au toucher ?
│  └─ OUI → Code OHF probable
│     └─ Action : Nettoyer filtre
│
├─ Défaut quand il DEMARRE ?
│  └─ Mesurer tension réseau
│     ├─ Trop haute → OVF
│     └─ Trop basse → USF
│
└─ [Etc.]
```

##  ⚙️ Paramètres Importants à Connaître

| Paramètre | Où le trouver ? | Valeur typique |
|-----------|-----------------|----------------|
| Rampe accélération | Menu ACC | 10s pour pompe |
| Rampe décélération | Menu DEC | 20s pour ventilateur |
| Protection thermique moteur | Menu TH | = Intensité plaque moteur |

## 📞 Quand Appeler le Chef ?

- Défaut GF (terre) → Risque électrique
- Défaut SCF (court-circuit) → Risque matériel
- Défaut récurrent après reset → Problème profond
```

---

## 📊 Critères d'Évaluation

| Critère | Points |
|---------|--------|
| **Clarté** : Accessible pour débutant | 30% |
| **Concision** : Max 2 pages | 20% |
| **Pertinence** : Info utiles, pas superflu | 25% |
| **Utilité terrain** : Réellement utilisable | 25% |

---

## 💡 Conseils

1. **Pensez "terrain"** : Quelles infos sont VRAIMENT utiles en dépannage ?
2. **Simplifiez** : Pas de jargon inutile
3. **Visuels** : Tableaux, arbres décisionnels > longs paragraphes
4. **Testez** : Relisez en vous mettant à la place d'un débutant

---

## 🎯 Objectif Pédagogique

Apprendre à **synthétiser** et **vulgariser** de l'information technique complexe avec l'aide de l'IA.

---

**Bonne création de guide ! 📚**
