# Manuel Technique Variateur - Version Complète

*Ce manuel simule un document technique dense et complexe*

---

## ALTIVAR ATV320 - MANUEL TECHNIQUE

### 1. Spécifications Électriques

Le variateur de vitesse ATV320 (gamme 0,18 kW à 15 kW en monophasé 200-240V et 0,37 kW à 15 kW en triphasé 200-240V et 380-480V) intègre les fonctions de contrôle et de protection moteur conformément aux normes IEC 61800-5-1, IEC 61800-3 catégorie C3 pour environnements industriels de second niveau. La section puissance utilise des modules IGBT de dernière génération permettant une fréquence de découpage ajustable de 2 à 12 kHz (défaut 4 kHz) avec déclassement automatique au-delà de 40°C de température ambiante selon la courbe fournie en annexe 3.2.

Les protections intégrées comprennent : surtension/sous-tension bus DC (paramètres OVF à 800V±5% et USF à 385V±5% pour réseau 400V tri), surcharge moteur par calcul thermique I²t ou sonde PTC, court-circuit de sortie détection en 5μs, défaut terre par mesure homopolaire avec seuil ajustable 0,3 à 3A...

[Le manuel continue sur 80 pages avec spécifications détaillées, schémas électriques, tableaux paramétriques...]

---

### 5. CODES DÉFAUTS ET DÉPANNAGE

#### 5.1 Défaut OVF - Overvoltage Fault (Surtension Bus DC)

**Description technique** : Ce défaut survient lorsque la tension mesurée sur le bus continu intermédiaire dépasse le seuil paramétré (USt, défaut 800V pour réseau 400V tri±10%, temps de détection 10ms). Les origines sont multiples et peuvent être classées selon leur occurrence statistique établie sur notre base de données SAV (n= 12.458 cas) : freinage régénératif sans dissipateur externe (68,2%), surtension transitoire réseau (18,7%), dysfonctionnement carte électronique (8,3%), mauvais dimensionnement (2,1%), causes diverses (2,7%).

**Analyse phénoménologique** : Lors d'une décélération, le moteur asynchrone se comporte en génératrice asynchrone et réinjecte de l'énergie dans le variateur via les diodes antiparallèles des IGBT. Cette énergie charge les condensateurs du bus DC. Sans dissipation externe (résistance de freinage commandée par transistor de roue libre), la tension du bus croît selon l'équation dU/dt = P/(C×U) où P est la puissance régénérée, C la capacité équivalente du bus. Pour une charge inertielle J tournant à vitesse ω avec une rampe de freinage t_dec, la puissance de pointe est approximativement P_peak ≈ J×ω²/(2×t_dec). Un calcul conservatif impose t_dec > √(J×ω²×C×U_max)/(ΔU×η) où η rendement variateur+moteur.

**Actions correctives hiérarchisées** :
1. Augmentation paramètre DEC (rampe de décélération) : Accès via interface HMI → Menu 1.3 > CONF > DEC, ajuster en fonction du calcul ou empiriquement (multiplication par facteur 2-3). Vérifier compatibilité processus industriel (temps de cycle).
2. Installation résistance de freinage externe : Sélection selon abaque constructeur (Annexe 8.4), dimensionnement thermique RMS et crête...

[Le manuel continue avec explications ultra-techniques, formules, références normes...]

---

#### 5.2 Défaut OHF - OverHeating Fault

Déclenchement à T°C > 90°C mesurée par thermistance CTN (coefficient négatif β=3950K) montée sur radiateur IGBT. Origine multicritère : température ambiante excessive (>40°C nominal, >50°C absolu), fréquence découpage élevée (pertes commutation proportionnelles à f_sw), surcharge prolongée >105% I_nom, colmatage filtration air (ΔP critique 50Pa), défaillance ventilateur (détection tachymétrique en option)...

[...]

#### 5.3 Défaut GF - Ground Fault

Détection fuite terre par sommateur de courant phases (transformateur tore homopolaire). Seuil paraméterable GFt de 0,3 à 3A selon installation...

#### 5.4 Défaut SCF - Short-Circuit Fault

Détection hardware par comparateur analogique sur shunt de mesure courant, seuil 6×I_nom, temps réponse <5μs, coupure IGBT par circuit Desaturation avec blocage hardware 10μs...

#### 5.5 Défaut USF - Under-voltage Fault

[...]

#### 5.6 Défaut LUF3 - Phase Loss

[...]

---

### 6. PARAMETRAGE AVANCÉ

#### 6.1 Loi U/f

Le mode de contrôle scalaire par loi tension/fréquence implémente...

[...]

---

*Manuel fictif dense pour simulation d'extraction/simplification IA*
