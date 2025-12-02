# Manuel Technique - Variateurs de Fréquence

## ⚡ Guide de Dépannage - Variateurs de Fréquence (VFD)

### Codes Défauts Fréquents

---

## 1. Défauts de Surtension / Sous-tension

### 1.1 Overvoltage DC Bus (Surtension Bus Continu)

**Code erreur** : OVF, OV, OUF selon marque

**Causes** :
1. **Freinage trop rapide** (cause #1)
   - Rampe de décélération trop courte
   - Charge à forte inertie (ventilateur, pompe)
   - Pas de résistance de freinage installée
   
2. **Surtension réseau** temporaire
   - Foudre proximité
   - Commutation condensateur compensation
   - Génératrice diesel mal régulée

3. **Résistance de freinage défectueuse**
   - Circuit ouvert
   - Transistor de freinage HS

**Diagnostic** :
- Défaut **pendant décélération** → Freinage régénératif 
- Défaut **au démarrage** → Surtension réseau
- Charge à forte inertie (ventilateur, compresseur) → Très probable

**Solutions** :
1. **Augmenter la rampe de décélération** (x2 ou x3)
2. **Installer une résistance de freinage** externe
3. **Activer le freinage DC** si disponible
4. Vérifier tension réseau avec analyseur

**Paramètres typiques** :
- Seuil surtension DC Bus : 800-850V (réseau 400V tri)
- Rampe décélération recommandée : 
  - Pompe : 10-30s
  - Ventilateur : 20-60s selon inertie

---

### 1.2 Undervoltage (Sous-tension)

**Code erreur** : LUF, UU, USF

**Causes** :
- Chute de tension réseau
- Phase manquante (câblage)
- Fusibles secteur grillés
- Contacteur amont défaillant

**Actions** :
- Mesurer tension entre phases en amont
- Vérifier fusibles et contacteurs
- Contrôler serrage borniers

---

## 2. Défauts Thermiques

### 2.1 Surchauffe Variateur

**Code** : OH, OHF, TH

**Causes** :
- **Ventilation insuffisante** (cause #1)
  - Filtre air colmaté
  - Ventilateur HS
  - Température ambiante > 40°C
  - Proximité source chaleur
  
- **Surcharge prolongée**
  - Courant > courant nominal > 1 minute
  - Sous-dimensionnement
  
- **Encrassement**
  - Poussière sur dissipateur
  - Ailettes obstruées

**Prévention** :
- Nettoyer filtre mensuel (environnement poussiéreux)
- Respecter espace ventilation : 100mm mini autour
- Température armoire < 40°C
- Utiliser si besoin un taux de déclassement (85% si 50°C)

---

### 2.2 Surchauffe Moteur

**Code** : OL, OH2, OLF

**Détection** :
- Via PTC moteur (si câblé)
- Via calcul I²t interne variateur

**Causes** :
- Surcharge mécanique
- Moteur sous-ventilé (basse vitesse prolongée)
- Court-circuit spires (moteur défaillant)

---

## 3. Défauts Électriques

### 3.1 Défaut de Terre / Fuite à la Terre

**Code** : GF, GRF, EF

**Causes** :
- **Câble moteur endommagé** (isolation)
- **Moteur défaillant** (bobinage terre)
- **Câble trop long** (capacité parasite)
  - > 50m sans filtre dv/dt
  - > 100m avec filtres
  
- **Humidité** dans bornier moteur

**Diagnostic** :
- Déconnecter moteur → Défaut persiste = Variateur
- Défaut disparaît = Problème câble ou moteur
- Mesurer isolement moteur (Mégohmmètre) : > 10 MΩ

---

### 3.2 Court-Circuit Sortie

**Code** : SCF, OCF, SC

**Causes** :
- Court-circuit entre phases câble moteur
- Phases inversées/touchées dans bornier
- Moteur en court-circuit

**Actions** :
- Déconnecter moteur et tester à vide
- Inspecter câble et connexions
- Tester moteur en direct réseau (rapide pour diagnostic)

---

## 4. Défauts de Communication

### 4.1 Perte Bus de Terrain

**Code** : CFF, CNF, COF

**Systèmes** : Modbus, Profibus, CANopen, Ethernet IP

**Causes** :
- Câble déconnecté/coupé
- Terminaison de bus manquante
- Adresse dupliquée
- Vitesse de communication incorrecte
- Bruit électromagnétique (CEM)

**Vérifications** :
- Check connexions physiques
- Vérifier résistances de terminaison (120Ω pour Modbus)
- Séparer câbles bus des câbles puissance (mini 30cm)

---

## 5. Messages Informatifs (Non Bloquants)

### 5.1 Error Code E12 (Exemple ATV320)

**Signification** : **Défaut thermique interne**

**Causes spécifiques ATV320/ATV340** :
- Température interne > 90°C
- Déclenchement thermistance interne
- Fréquence de commutation trop élevée

**Actions** :
1. Vérifier température ambiante armoire
2. Nettoyer ventilateur et dissipateur
3. Réduire fréquence de découpage (4kHz → 2,5kHz)
4. Améliorer ventilation armoire

---

## Codes Défauts par Marque

| Code | Schneider ATV | Siemens G120 | ABB ACS | Signification |
|------|---------------|--------------|---------|---------------|
| Surtension DC | OBF | F07201 | DCOV | Freinage régénératif |
| Sous-tension | USF | F07011 | DCUN | Chute tension réseau |
| Surcharge | OLF | A07320 | OL | Dépassement I nominal |
| Défaut terre | GF F | F07805 | GF | Court-circuit terre |
| Surchauffe | OH F | A05000 | OT | Température excessive |
| Court-circuit | SCF | F07320 | SC | CC entre phases |

---

## 📊 Tableau Diagnostic Rapide

| Symptôme | Causes Probables | Vérifications |
|----------|------------------|---------------|
| Arrêt sur OVF pendant freinage | Iner tie forte + rampe courte | Augmenter rampe ou ajouter résistance freinage |
| Arrêts aléatoires + surchauffe | Ventilation insuffisante | Nettoyer, vérifier T°C ambiante |
| Défaut terre intermittent | Câble moteur long ou humidité | Mesurer isolement, vérifier bornier |
| Perte communication | Bus déconnecté ou mal terminé | Check câbles, terminaisons 120Ω |
| Défaut E12 (ATV320) | Surchauffe interne | Ventilation, T°C ambiante, découpage |

---

## 🛠️ Paramétrage Important

### Rampes Accélération/Décélération

**Valeurs par défaut** : Souvent **3 secondes** (trop court !)

**Recommandations** :
- **Pompe centrifuge** : 
  - Acc : 5-10s
  - Dec : 10-20s
  
- **Ventilateur** :
  - Acc : 10-20s
  - Dec : 30-60s (forte inertie)
  
- **Convoyeur** :
  - Acc : 2-5s
  - Dec : 3-8s

### Protection Thermique Moteur

- **Toujours activer** la protection thermique
- Entrer le **courant nominal moteur** (plaque)
- Si moteur sous-ventilé à basse vitesse → Réduction automatique couple

### Fréquence de Découpage

- Standard : **4 kHz** (bon compromis)
- Environnement bruyant : 8-12 kHz (inaudible)
- Forte puissance : 2,5 kHz (réduction pertes)

**⚠️ Attention** : > 4kHz → Échauffement variateur accru

---

## 🔐 Sécurité

### Consignation Variateur

1. Couper alimentation amont
2. **ATTENDRE 5 MINUTES** (décharge condensateurs)
3. Vérifier absence tension avec VAT
4. Cadenasser
5. Ne JAMAIS fier aux voyants (peuvent être alimentés par bus)

### Distances Sécurité CEM

- Câble moteur ↔ câble signaux : > 30 cm
- Variateur ↔ équipements sensibles : > 50 cm
- Toujours utiliser câble blindé pour moteur si > 10m

---

**📘 Documentation Constructeur** : Toujours disponible en ligne (codes QR sur étiquette)
