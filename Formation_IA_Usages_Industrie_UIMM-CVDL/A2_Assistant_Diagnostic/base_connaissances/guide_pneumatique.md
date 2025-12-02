# Manuel Technique - Systèmes Pneumatiques

## 💨 Guide de Dépannage - Vérins et Circuits Pneumatiques

---

## 1. Vérins Lents ou Manque de Force

### 1.1 Lenteur Générale (Avance ET Retour)

**Causes probables** :
1. **Pression réseau insuffisante** (cause #1)
   - Pression < 5,5 bars (nominal 6 bars)
   - Compresseur sous-dimensionné
   - Fuites importantes sur réseau
   - Filtre régulateur bouché

2. **Débit d'air insuffisant**
   - Flexible trop long ou trop fin (Ø4 au lieu de Ø6)
   - Électrovanne sous-dimensionnée
   - Silencieux colmaté

3. **Frottements internes** du vérin
   - Joints secs (manque de lubrification)
   - Tige voilée ou griffée
   - Guidage grippé

**Diagnostic** :
- Mesurer **pression en bout de flexible** (proche du vérin)
- Si pression OK → Problème vérin (joints, frottement)
- Si pression basse → Problème alimentation

---

### 1.2 Lenteur Uniquement en Avance (ou Retour)

**Causes** :
- Fuite interne vérin (joint piston usé)
- Électrovanne défaillante (un orifice bouché)
- Régleur de débit déréglé ou bloqué

**Test** :
- Débrancher flexible de la chambre lente
- Souffler manuellement → Si difficile = restriction
- Inverser les raccords → Si problème suit = Problème vérin

---

## 2. Fuites d'Air

### 2.1 Fuite Audible en Position Statique

**Localisation** :

**Si fuite au niveau du vérin** :
- **Joints de tige** usés (fuite externe visible)
- **Joints piston** usés (fuite interne, sifflement)
- **Racleurs** détériorés

**Si fuite au niveau de l'électrovanne** :
- Clapet usé ou encrassé
- Joint torique siège détérioré
- Corps étranger empêche fermeture

**Durée de vie joints vérin** :
- Utilisation intensive : 2-5 ans
- Utilisation normale : 5-10 ans
- Facteurs aggravants : environnement poussiéreux, absence lubrification

---

### 2.2 Pression Réseau Qui Chute

**Causes réseau** :
- Fuites sur réseau distribution
- Raccords instantanés desserrés (vieillissement)
- Tuyauterie percée ou fissurée

**Détection fuites** :
1. Méthode eau savonneuse (bulles)
2. Détecteur ultrason (fuites invisibles)
3. Arrêt production + observation pression

**Impact économique** :
- Fuite Ø1mm = 100 €/an (24/7)
- Fuite Ø5mm = 2500 €/an

---

## 3. Vérin Bloqué ou Irrégulier

### 3.1 Blocage Complet

**Causes** :
- Vérin grippé (absence lubrification)
- Tige voilée (choc)
- Corps étranger dans le cylindre
- Électrovanne non pilotée

**Vérifications** :
1. Vérifier signal électrique électrovanne (LED)
2. Permuter commande manuelle électrovanne
3. Démonter vérin et inspecter

---

### 3.2 Mouvement Saccadé (Stick-Slip)

**Causes** :
- **Frottement sec** (absence lubrification) - cause principale
- Pression trop faible
- Charge trop importante
- Joints gonflés (mauvaise compatibilité fluide)

**Solutions** :
- Lubrifier l'air (brouillard d'huile)
- Lubrificateur automatique 1 goutte/m³ air
- Huile ISO VG 32 spéciale pneumatique

---

## 4. Électrovannes

### 4.1 Électrovanne Ne Commute Pas

**Vérifications** :
1. **Électrique** :
   - Tension présente? (Mesurer aux bornes)
   - Bobine OK? (Mesurer résistance : 5-15Ω selon modèle)
   - Bobine brûlée si R = ∞

2. **Mécanique** :
   - Permutateur manuel fonctionne?
   - Si oui → Problème bobine
   - Si non → Problème mécan ique interne

3. **Pneumatique** :
   - Pression pilotage suffisante (mini 3 bars)

---

### 4.2 Electrovanne Lente ou Hésitante

**Causes** :
- Ressort de rappel fatigué
- Encrassement interne
- Pression trop juste
- Frottement noyau mobile

**Nettoyage** :
- Démonter et nettoyer au white spirit
- Souffler avec air comprimé
- Remonter avec graisse silicone (légère)

---

## 5. Problèmes de FRL (Filtre Régulateur Lubrificateur)

### 5.1 Filtre Colmaté

**Symptômes** :
- Perte de charge

 importante (ΔP > 0,5 bar)
- Débit réduit
- Vérins lents

**Détection** :
- Indicateur visuel (rouge si colmaté)
- Bol du filtre noirci

**Maintenance** :
- Nettoyer ou remplacer cartouche tous les 6-12 mois
- Plus fréquent en environnement poussiéreux

---

### 5.2 Régulateur de Pression Déréglé

**Symptômes** :
- Pression instable
- Vérins trop rapides ou trop lents

**Réglage** :
1. Tourner molette pour ajuster pression souhaitée
2. Bloquer contre-écrou
3. Pression usine standard : **6 bars**

---

### 5.3 Lubrificateur Vide

**Symptômes** :
- Vérins de plus en plus lents
- Bruits de frottement
- Usure prématurée joints

**Vérification** :
- Niveau d'huile visible sur bol
- Réglage goutte-compte : 1 goutte/ 1-2 m³ (#compter via hublot)

**Huile** :
- Huile ISO VG 32 pneumatique
- Jamais huile moteur ou hydraulique !

---

## 6. Dimensionnement et Choix

### 6.1 Diamètre de Vérin

**Force théorique** (approximation) :
- F (daN) = P (bars) × S (cm²) 
- S = π × (Ø/2)²

**Exemple** :
- Vérin Ø40mm, P=6bars
- S = 12,56 cm²
- F ≈ 75 daN (avance) ou 50 daN (retour, avec tige)

**Coefficient de sécurité** : 2× minimum

---

### 6.2 Diamètre de Flexible

| Débit (NL/min) | Longueur flexible | Ø Mini |
|----------------|-------------------|--------|
| < 50 | < 2m | Ø4mm |
| < 50 | > 2m | Ø6mm |
| 50-150 | < 3m | Ø6mm |
| > 150 | Toute longueur | Ø8mm |

**Règle** : Plus le flexible est long, plus le diamètre doit être grand

---

## 7. Maintenance Préventive

### Quotidien
- Purge eau condensée (bol filtre)
- Vérification visuelle fuites

### Mensuel
- Vérifier niveau lubrificateur
- Contrôle pression réglée
- Inspection visuelle flexibles

### Annuel
- Remplacement cartouche filtre
- Nettoyage régulateur
- Contrôle état joints vérins (si accessibles)

### 3-5 ans
- Remplacement préventif joints vérin
- Révision électrovannes

---

## 📊 Tableau Diagnostic Rapide

| Symptôme | Diagnostic Rapide |  Action Immédiate |
|----------|-------------------|-------------------|
| Vérin lent (A+R) + sifflement | Fuite interne (joints) | Remplacer kit joints |
| Vérin lent + pression basse | Restriction arrivée air | Vérifier filtre, flexibles, électrovanne |
| Mouvement saccadé | Manque lubrification | Vérifier lubrificateur, remplir |
| Blocage total | Vérin grippé ou électrovanne HS | Test manuel électrovanne |
| Pression réseau chute | Fuite sur réseau | Méthode savonneuse, colmater |

---

## ⚙️ Normes et Standards

**Normes ISO** :
- ISO 6432 : Vérins compacts Ø8 à Ø25
- ISO 15552 : Vérins Ø32 à Ø320
- ISO 5599-1 : Électrovannes (raccords interface)

**Pression standard** :
- Réseau : 6-7 bars
- Utilisation : 5-6 bars (avec régulateur)

**Qualité air ISO 8573-1** :
- Classe 3.4.2 recommandée (industrie)
- Filtration 5μm minimum

---

**🔧 Conseil** : 60% des problèmes pneumatiques = fuites ou manque de lubrification !
