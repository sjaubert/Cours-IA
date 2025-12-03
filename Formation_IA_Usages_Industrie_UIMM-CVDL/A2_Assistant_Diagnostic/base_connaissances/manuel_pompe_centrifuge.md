# Manuel Technique - Pompe Centrifuge

## 🔧 Guide de Dépannage - Pompes Centrifuges

### Types de Pannes Courantes

---

## 1. Bruit Anormal et Vibrations

### 1.1 Sifflement Aigu

**Causes possibles** :
- **Cavitation** (cause la plus fréquente)
  - Pression d'aspiration insuffisante
  - NPSH disponible < NPSH requis
  - Température fluide trop élevée
  - Air dans le circuit d'aspiration
  
- **Détérioration des roulements**
  - Usure normale (durée de vie : 20 000 - 50 000h)
  - Lubrification insuffisante
  - Contamination du lubrifiant
  
- **Roue endommagée**
  - Érosion, corrosion
  - Choc corps étranger

**Diagnostic** :
- Sifflement + baisse de débit → **Cavitation probable**
- Sifflement + vibrations croissantes → **Roulements usés**
- Sifflement intermittent → **Air dans l'aspiration**

**Actions correctives** :
- Vérifier le niveau du réservoir d'aspiration
- Contrôler l'étanchéité côté aspiration
- Inspecter et remplacer les roulements si nécessaire
- Vérifier l'alignement pompe-moteur

---

### 1.2 Vibrations Excessives

**Seuils d'alerte** (ISO 10816) :
- < 2,8 mm/s RMS : Bon
- 2,8 - 7,1 mm/s : Acceptable
- 7,1 - 18 mm/s : Inadmissible
- \> 18 mm/s : Dangereux

**Causes fréquentes** :
1. **Défaut d'équilibrage** de la roue
2. **Désalignement** pompe-moteur (> 0,1mm)
3. **Roulements défectueux**
4. **Balourd** (dépôts, usure asymétrique)
5. **Fixation desserrée**

**Méthode d'analyse** :
- Mesurer vibrations en 3 axes (horizontal, vertical, axial)
- Identifier la fréquence dominante :
  - 1× vitesse de rotation → Balourd
  - 2× vitesse → Désalignement
  - Fréquences multiples → Roulements

---

## 2. Échauffement Anormal

### 2.1 Paliers Chauds

**Températures normales** :
- Paliers à roulements : 40-60°C (ambiance +20°C)
- Limite maximum : 80°C

**Causes si > 80°C** :
- Roulements usés ou grippés
- Lubrification insuffisante ou excessive
- Désalignement sévère
- Contamination du lubrifiant

**Actions** :
- Vérifier quantité de graisse (ni trop, ni trop peu)
- Contrôler la qualité du lubrifiant
- Remplacer les roulements si jeu excessif

---

### 2.2 Moteur en Surchauffe

**Causes** :
- Surcharge (hauteur manométrique trop élevée)
- Phases déséquilibrées
- Ventilation moteur obstruée
- Température ambiante excessive

---

## 3. Diminution de Débit

**Causes probables** :
- **Cavitation** (voir 1.1)
- **Roue usée** (jeu roue-corps > 0,5mm)
- **Fuite interne** (joint d'usure détérioré)
- **Colmatage** du filtre d'aspiration
- **Vanne refoulement** partiellement fermée
- **Vitesse de rotation** incorrecte

**Vérifications** :
1. Contrôler le sens de rotation
2. Mesurer la vitesse réelle
3. Inspecter l'intérieur de la pompe
4. Vérifier les jeux internes

---

## 4. Fuite au Niveau du Joint Mécanique

### Types de Fuites

**Fuite normale** :
- 1-2 gouttes/minute → Acceptable (film de lubrification)

**Fuite anormale** :
- Écoulement continu → Joint défectueux

**Causes de défaillance prématurée** :
- Fonctionnement à sec (même bref)
- Température excessive du fluide
- Contamination (particules)
- Montage incorrect
- Vibrations excessives

**Durée de vie typique** :
- 2-5 ans selon conditions d'utilisation

---

## 5. Arbre Grippé / Pompe Bloquée

**Causes** :
- Roulements grippés
- Dépôts calcaire (eau dure)
- Corps étranger coincé
- Corrosion (arrêt prolongé)

**Prévention** :
- Rotation manuelle hebdomadaire si arrêt long
- Rinçage avant arrêt prolongé
- Protection anticorrosion

---

## 📊 Tableau Récapitulatif : Symptômes → Causes

| Symptôme | Causes Probables (par ordre de fréquence) |
|----------|-------------------------------------------|
| Sifflement + baisse débit | 1. Cavitation 2. Air aspiration 3. Roue endommagée |
| Vibrations + échauffement palier | 1. Roulements usés 2. Désalignement 3. Balourd |
| Baisse de débit seule | 1. Vanne partiellement fermée 2. Colmatage 3. Usure interne |
| Fuite joint mécanique | 1. Usure normale 2. Fonctionnement à sec 3. Vibrations |
| Échauffement moteur | 1. Surcharge 2. Ventilation obstruée 3. Problème électrique |

---

## 🛠️ Plan de Maintenance Préventive

### Quotidien
- Vérification visuelle (fuites, bruits anormaux)
- Contrôle température paliers (main)

### Mensuel
- Mesure vibrations
- Contrôle niveau/état lubrifiant
- Serrage boulonnerie

### Annuel
- Remplacement lubrifiant
- Contrôle alignement
- Inspection interne
- Contrôle jeux internes

### 3-5 ans
- Remplacement roulements
- Remplacement joint mécanique

---

## ⚙️ Caractéristiques Techniques Standard

**Pompe centrifuge industrielle type** :
- Puissance : 0,5 - 200 kW
- Débit : 5 - 500 m³/h
- HMT : 10 - 100 m CE
- Vitesse : 1450 ou 2900 tr/min (50 Hz)
- Roulements : Type 6205, 6305 (roulement à billes)
- NPSH requis : 2 - 8 m (selon modèle)

---

**🔴 Sécurité** : Toujours consigner électriquement et mécaniquement avant intervention !
