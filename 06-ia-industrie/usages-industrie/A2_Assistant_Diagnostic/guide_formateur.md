# Guide Formateur - Activité 2 : Assistant Diagnostic

## 📝 Fiche Activité

| Élément | Détail |
|---------|--------|
| **Titre** | Assistant Diagnostic de Pannes Multi-Sources |
| **Durée** | 45 minutes |
| **Niveau** | Débutant |
| **Prérequis** | Notions de base en maintenance |
| **Modalités** | Individuel |

---

## 🎯 Objectifs Pédagogiques

### Savoirs
- Connaître une méthode de diagnostic système
- Comprendre l'importance de la documentation technique

### Savoir-faire
- Structurer l'observation de symptômes
- Exploiter méthodiquement une documentation
- Utiliser l'IA comme assistant d'analyse
- Hiérarchiser les causes probables

### Savoir-être
- Rigueur dans l'observation
- Esprit critique face aux propositions IA
- Méthode et organisation

---

## 📅 Déroulé de Séance

### Introduction (5 min)
- Présentation du contexte diagnostic
- Importance de la méthodologie
- Rôle de l'IA comme assistant (pas oracle)

### Travail Individuel (35 min)
Guidé par `instructions_apprenant.md`

### Débrief (5 min)
- Présentation volontaires
- Discussion sur les difficultés
- Réflexion esprit critique

---

## 🔑 Solutions par Scénario

### Scénario 1 : Pompe Centrifuge

**Cause réelle** : **Roulements usés**

**Indices** :
- Sifflement aigu ✓
- Vibrations accrues ✓
- Échauffement palier ✓
- Proportionnel à la vitesse ✓
- Baisse légère débit (secondaire)

**Diagnostic différentiel** :
- Cavitation : NON (pas de baisse drastique débit)
- Désalignement : POSSIBLE (mais vibrations sans bruit fort)
- **Roulements : OUI** (tous symptômes concordent)

**Action** : Remplacement roulements

---

### Scénario 2 : Convoyeur (Variateur)

**Cause réelle** : **Surchauffe variateur** (défaut ventilation)

**Indices** :
- E12 = défaut thermique interne ATV320 ✓
- Température ambiante 32°C ✓
- Arrêts après 15-30 min (temps chauffe) ✓
- Ventilateur OK mais nettoyage récent (filtre retiré?)

**Actions** :
- Vérifier filtre variateur
- Améliorer ventilation armoire
- Éventuellement réduire fréquence découpage

---

### Scénario 3 : Vérin Pneumatique

**Cause réelle** : **Joints piston usés + manque lubrification**

**Indices** :
- Lenteur A+R ✓
- Fuite audible (joints) ✓
- Pression un peu basse (fuites réseau) ✓
- Pas de maintenance depuis 1 an ✓
- 7 ans de service

**Actions** :
- Remplacement kit joints
- Lubrification
- Vérifier/réparer fuites réseau

---

### Scénario 4 : Compresseur

**Cause réelle** : **Multi-facteurs : Filtration + Radiateur + Vidange**

**Indices** :
- Canicule (température ambiante) ✓
- Filtre encrassé ✓
- Radiateur obstrué ✓
- Vidange dépassée (4850h > 4000h) ✓

**Actions** (par ordre) :
1. Nettoyer radiateur huile (immédiat)
2. Remplacer filtre air
3. Vidange huile
4. Améliorer ventilation locale

---

### Scénario 5 : Variateur Overvoltage

**Cause réelle** : **Rampe décélération trop courte + forte inertie**

**Indices** :
- Overvoltage UNIQUEMENT en décélération ✓
- Ventilateur (forte inertie) ✓
- Rampe 3s (trop court) ✓
- Pas de résistance freinage ✓
- Vent fort → ventilateur freiné brutalement

**Actions** :
- Augmenter rampe à 30-60s
- Ou installer résistance freinage

---

## 💡 Points de Vigilance

### Erreurs Fréquentes

1. **Prompts trop vagues**
   - ❌ "Diagnostique cette panne"
   - ✅ "Voici les symptômes... quelles causes du manuel correspondent ?"

2. **Ne pas fournir le manuel à l'IA**
   - L'IA extrapole avec ses connaissances général
   - Risque de diagnostic hors contexte

3. **Confiance aveugle**
   - Ne pas vérifier dans le manuel
   - Accepter sans questionner

### Adaptations

**Si trop difficile** :
- Fournir un tableau symptômes/causes pré-rempli
- Limiter à 2 causes possibles
- Travail collaboratif binôme

**Si trop facile** :
- Diagnostiquer 2 scénarios
- Créer un scénario personnel
- Rédiger une procédure de dépannage complète

---

## 📊 Grille d'Évaluation

| Critère | Détail | Points |
|---------|--------|--------|
| **Interaction IA** | Prompts structurés, itération | 25 |
| **Diagnostic** | Causes pertinentes, hiérarchisées | 30 |
| **Plan vérification** | Logique, complet, réaliste | 25 |
| **Esprit critique** | Validation avec manuel, questions | 20 |
| **Total** | | 100 |

---

## 💬 Questions Débrief

1. Comment avez-vous structuré votre prompt initial ?
2. L'IA a-t-elle trouvé la bonne cause ?
3. Avez-vous validé avec le manuel ?
4. Qu'est-ce qui vous a aidé à discriminer entre plusieurs causes ?

---

**Fichiers nécessaires** :
- ✅ Scénarios
- ✅ Manuels techniques (3 fichiers)
- ✅ Instructions apprenant
- ✅ Ce guide formateur
