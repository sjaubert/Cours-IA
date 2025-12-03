# Scénarios de Pannes - Activité 2

Voici 5 scénarios réalistes de pannes rencontrées en maintenance industrielle. Lisez-les et choisissez-en un à diagnostiquer avec l'aide de Gemini.

---

## 🔴 Scénario 1 : Pompe Centrifuge Bruyante

### Contexte
**Équipement** : Pompe centrifuge PMP-042 (circuit de refroidissement)  
**Occurrence** : Depuis 2 jours  
**Impact** : Production ralentie

### Symptômes Observés
- ✅ **Bruit anormal** : Sifflement aigu en fonctionnement
- ✅ **Vibrations** : Augmentation notable des vibrations au niveau du palier
- ✅ **Température** : Palier moteur plus chaud que d'habitude (+15°C)
- ✅ **Débit** : Légèrement diminué (-10%)
- ❌ **Fuite** : Aucune fuite visible
- ❌ **Disjonctions** : Aucune

### Observations Complémentaires
- La pompe a 8 ans (durée de vie prévue : 10 ans)
- Dernière intervention : Changement du joint mécanique il y a 3 mois
- Le bruit apparaît après 5 minutes de fonctionnement
- Intensité du bruit proportionnelle à la vitesse de rotation

### Informations Contextuelles
- Fluide pompé : Eau + glycol (non corrosif)
- Régime : 1450 tr/min
- Puissance moteur : 5,5 kW

---

## 🟠 Scénario 2 : Convoyeur à Arrêts Intempestifs

### Contexte
**Équipement** : Convoyeur à bande CVY-015 (ligne d'emballage)  
**Occurrence** : 4 arrêts aujourd'hui (aléatoires)  
**Impact** : Arrêt production à chaque fois

### Symptômes Observés
- ✅ **Arrêts aléatoires** : Le convoyeur s'arrête sans raison apparente
- ✅ **Voyant défaut** : LED rouge "Défaut moteur" allumée à chaque arrêt
- ✅ **Réarmement** : Redémarre normalement après réarmement manuel
- ❌ **Bruit anormal** : Aucun
- ❌ **Surchauffe** : Température moteur normale
- ✅ **Code erreur** : Affichage "E12" sur le variateur

### Observations Complémentaires
- Les arrêts surviennent après 15-30 minutes de fonctionnement
- Température ambiante élevée aujourd'hui (32°C dans l'atelier)
- Le variateur de fréquence a été nettoyé la semaine dernière
- Ventilateur du variateur fonctionne

### Informations Contextuelles
- Variateur : ATV320 (Schneider)
- Charge transportée : Cartons légers (sous-utilisation)
- Installation : 5 ans

---

## 🟡 Scénario 3 : Vérin Pneumatique Lent

### Contexte
**Équipement** : Vérin pneumatique double effet VER-208 (poste de serrage)  
**Occurrence** : Progressif depuis 1 semaine  
**Impact** : Augmentation du temps de cycle (+30%)

### Symptômes Observés
- ✅ **Lenteur** : Vitesse de sortie ET de rentrée de tige diminuée
- ✅ **Manque de force** : Pièce parfois mal serrée
- ✅ **Fuite audible** : Léger sifflement en position sortie
- ❌ **Blocage** : Aucun, le vérin complète toujours sa course
- ✅ **Pression réseau** : Mesurée à 5,8 bars (normale : 6 bars)

### Observations Complémentaires
- Le vérin effectue environ 200 cycles/jour
- En service depuis 7 ans
- Aucun entretien récent (pas de lubrification depuis 1 an)
- Flexible d'alimentation : Ø6mm, longueur 3m

### Informations Contextuelles
- Type : ISO 6432, Ø40mm, course 100mm
- Électrovanne : 5/2 monostable
- Environnement : Atelier poussiéreux

---

## 🟢 Scénario 4 : Compresseur en Surchauffe

### Contexte
**Équipement** : Compresseur à vis CMP-003 (air comprimé atelier)  
**Occurrence** : Depuis ce matin  
**Impact** : Arrêt sécurité toutes les 2 heures

### Symptômes Observés
- ✅ **Surchauffe** : Arrêt sur défaut "Température huile > 95°C"
- ✅ **Température ambiante** : Locale compresseur : 38°C (canicule)
- ✅ **Niveau d'huile** : Correct, au repère max
- ✅ **Filtre à air** : Encrassé (gris foncé)
- ❌ **Fuites** : Aucune fuite d'huile visible
- ✅ **Ventilateur** : Tourne, mais pales poussiéreuses

### Observations Complémentaires
- Le compresseur tourne en charge à 95% (forte demande)
- Radiateur d'huile : Ailettes obstruées par poussière
- Dernière vidange : Il y a 6 mois (préconisé : 4000h ou 1 an)
- Compteur horaire : 4850h depuis dernière vidange

### Informations Contextuelles
- Puissance : 37 kW
- Débit : 5,5 m³/min
- Huile : ISO VG 46 (synthétique)
- Ventilation locale : Naturelle (pas de VMC)

---

## 🔵 Scénario 5 : Variateur en Défaut Intermittent

### Contexte
**Équipement** : Variateur de fréquence VAR-019 (ventilateur d'extraction)  
**Occurrence** : 2-3 fois par semaine  
**Impact** : Arrêt ventilation → alerte atmosphère confinée

### Symptômes Observés
- ✅ **Code défaut** : "Overvoltage DC Bus" (surtension bus continu)
- ✅ **Moment du défaut** : Toujours pendant la décélération
- ✅ **Conditions météo** : Défaut plus fréquent lors de vents forts
- ✅ **Réarmement** : Fonctionne après reset, parfois pendant plusieurs jours
- ❌ **Câblage** : Visuellement correct, serré
- ❌ **Température** : Variateur froid

### Observations Complémentaires
- Le variateur pilote un gros ventilateur (forte inertie)
- Rampe de décélération actuelle : 3 secondes
- Pas de résistance de freinage installée
- Tension réseau mesurée : 395V (normal : 400V ±10%)

### Informations Contextuelles
- Puissance moteur : 22 kW
- Variateur : Altivar ATV71 (Schneider)
- Type de charge : Ventilateur axial, inertie élevée
- Installation : 3 ans

---

## 📋 Instructions

1. **Choisissez un scénario** qui vous intéresse
2. **Lisez attentivement** tous les symptômes
3. **Consultez la documentation** dans `base_connaissances/`
4. **Suivez** les instructions dans `instructions_apprenant.md`
5. **Utilisez Gemini** pour analyser et diagnostiquer

## 💡 Conseil

Un bon diagnostic commence par une **observation méthodique** et une **exploitation systématique** de la documentation technique !

---

**Note formateur** : Les causes réelles sont documentées dans le `guide_formateur.md`
