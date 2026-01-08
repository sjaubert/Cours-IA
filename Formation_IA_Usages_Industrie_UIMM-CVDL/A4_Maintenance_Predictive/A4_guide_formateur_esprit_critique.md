# Guide Formateur : Questions Critiques - Activité 4 Maintenance Prédictive

## 🎯 Objectif Pédagogique

**Ne pas laisser les apprenants accepter aveuglément les réponses de l'IA.**  
Ce guide contient des questions "pièges" pour révéler les limites, biais et angles morts de l'analyse IA en maintenance prédictive.

---

## 📋 Timing des Interventions

| Moment | Durée | Type d'intervention |
|--------|-------|---------------------|
| Après Prompt 1 (Visualisation) | 5 min | Questions de vérification basique |
| Après Prompt 2 (Tendances) | 8 min | Questions sur les hypothèses |
| Après Prompt 3 (Anomalies) | 7 min | Questions sur la causalité |
| Après Prompt 4 (Recommandations) | 10 min | Questions sur la responsabilité |

---

## 🎣 Questions Pièges par Étape

### Après Prompt 1 : Chargement et Visualisation

#### Question 1 : "Vos données sont-elles fiables ?"

**À poser** : *"L'IA vous a généré de beaux graphiques. Mais comment savez-vous que vos données sont exactes ?"*

**Ce qu'ils vont rater** :

- ❌ L'IA ne vérifie PAS la qualité des données
- ❌ Pas de détection automatique de capteurs défaillants
- ❌ Pas de validation de cohérence temporelle (saut d'horodatage ?)

**Questions de relance** :

- "Et si un capteur de température était déréglé depuis 3 mois ?"
- "Comment détecter qu'il manque des relevés horaires ?"
- "L'IA vérifie-t-elle que Machine_ID est constant sur toute l'année ?"

**Révélation** : *L'IA traite les données comme du texte. Elle ne comprend pas qu'un capteur peut mentir.*

---

#### Question 2 : "Les statistiques de base sont-elles suffisantes ?"

**À poser** : *"L'IA vous donne min, max, moyenne, écart-type. Mais que manque-t-il ?"*

**Ce qu'ils vont rater** :

- ❌ Médiane (plus robuste aux valeurs aberrantes que la moyenne)
- ❌ Distribution (normale ? bimodale ? asymétrique ?)
- ❌ Saisonnalité/cyclicité (variations journalières, hebdomadaires)

**Questions de relance** :

- "Si vous avez 10 relevés à 60°C et 1 pic à 200°C, quelle est la moyenne ? Est-elle représentative ?"
- "Une pompe vibre-t-elle autant à vide qu'en charge ?"
- "Température ambiante été vs hiver : impact sur les mesures ?"

**Révélation** : *L'IA donne ce qu'on lui demande. Elle n'anticipe pas les questions qu'on n'a pas posées.*

---

### Après Prompt 2 : Détection de Tendances

#### Question 3 : "Une régression linéaire est-elle toujours pertinente ?"

**À poser** : *"L'IA a calculé une régression linéaire. Pourquoi est-ce potentiellement trompeur pour une usure mécanique ?"*

**Ce qu'ils vont rater** :

- ❌ L'usure est rarement linéaire (souvent exponentielle en fin de vie)
- ❌ La courbe en "baignoire" (failure rate curve) : début, vie normale, vieillissement
- ❌ Dégradation brutale possible (rupture soudaine après X cycles)

**Questions de relance** :

- "Un roulement s'use-t-il de façon constante ou accélère-t-il sa dégradation ?"
- "Montrez-moi le coefficient R² de la régression : est-il proche de 1 ?"
- "Et si la tendance est exponentielle, pas linéaire ?"

**Démonstration piège** :  
*Montrez deux graphiques :*

- Tendance linéaire → prédiction dans 6 mois
- Tendance exponentielle avec mêmes 3 premiers mois → prédiction dans 2 mois

**Révélation** : *L'IA utilise des modèles mathématiques standards. Elle n'applique pas de connaissance métier (tribologie, fatigue des matériaux).*

---

#### Question 4 : "Les projections dans le futur sont-elles crédibles ?"

**À poser** : *"L'IA vous dit que le seuil sera atteint dans 117 jours. Quelle est la marge d'erreur de cette prédiction ?"*

**Ce qu'ils vont rater** :

- ❌ Intervalle de confiance (la prédiction a une incertitude !)
- ❌ Extrapolation dangereuse (prévoir loin dans le futur = fiabilité faible)
- ❌ Facteurs externes non modélisés (changement de cadence de production, maintenance corrective intermédiaire)

**Questions de relance** :

- "L'IA vous donne une date précise. Vous donne-t-elle un intervalle du type ± 15 jours ?"
- "Si vous modifiez les 5 dernières valeurs de 2%, la prédiction change-t-elle beaucoup ?"
- "La pompe fonctionne 12h/jour ou 24h/jour ? L'IA le sait-elle ?"

**Révélation** : *L'IA donne une illusion de précision. Un ingénieur doit toujours intégrer une marge de sécurité.*

---

### Après Prompt 3 : Détection d'Anomalies

#### Question 5 : "Tous les pics sont-ils des anomalies ?"

**À poser** : *"L'IA a détecté 12 anomalies avec la règle 'moyenne + 2σ'. Sont-elles toutes préoccupantes ?"*

**Ce qu'ils vont rater** :

- ❌ Pic normal lors d'un démarrage à froid (courant d'appel)
- ❌ Pic normal en charge maximale planifiée
- ❌ Pic isolé vs série de pics (l'un est un événement, l'autre une tendance)

**Questions de relance** :

- "Un pic de courant de 30 secondes est-il aussi grave qu'une vibration élevée maintenue 3 heures ?"
- "Y a-t-il des timestamps d'anomalies le lundi matin à 6h ? (= démarrage)"
- "L'IA vous dit QUE c'est une anomalie, vous dit-elle POURQUOI ?"

**Révélation** : *L'IA détecte des valeurs statistiques atypiques, pas des problèmes techniques. Le contexte industriel est invisible pour elle.*

---

#### Question 6 : "La corrélation implique-t-elle la causalité ?"

**À poser** : *"L'IA remarque que température et vibration augmentent simultanément. Qu'est-ce qui cause quoi ?"*

**Ce qu'ils vont rater** :

- ❌ La vibration peut créer de la friction → chaleur (causalité : vibration → température)
- ❌ OU la chaleur peut déformer une pièce → vibration accrue (causalité : température → vibration)
- ❌ OU les deux sont causés par un 3ème facteur (ex: désalignement)

**Questions de relance** :

- "Si vous corrigez la vibration, la température baissera-t-elle automatiquement ?"
- "L'IA vous dit qu'ils sont corrélés. Vous dit-elle le mécanisme physique ?"
- "Et si les deux évoluent à cause d'une charge de travail accrue ?"

**Démonstration piège** :  
*"Les ventes de glaces et les noyades sont corrélées. Faut-il interdire les glaces pour sauver des vies ?"*  
→ Non, les deux sont causés par l'été (3ème facteur)

**Révélation** : *L'IA trouve des patterns statistiques, pas des mécanismes causaux. Le diagnostic nécessite de la connaissance métier.*

---

### Après Prompt 4 : Recommandations Maintenance

#### Question 7 : "Le diagnostic IA est-il toujours correct ?"

**À poser** : *"L'IA vous dit 'usure probable du roulement'. Sur quoi se base-t-elle ?"*

**Ce qu'ils vont rater** :

- ❌ L'IA se base sur des **patterns textuels** dans sa formation (articles, forums, manuels)
- ❌ Elle n'a PAS accès à l'historique de cette machine spécifique
- ❌ Elle ne connaît PAS le modèle exact, l'âge réel, l'environnement (poussière, humidité)

**Questions de relance** :

- "L'IA a-t-elle visité votre usine ?"
- "Connaît-elle la marque et le modèle de votre pompe ?"
- "Si 3 autres pompes identiques tournent sans problème, que dit l'IA ?"

**Scénario piège** :  
*"Supposons que votre pompe soit installée dans une zone sableuse. L'IA le sait-elle ? Pourtant, le sable change tout au diagnostic (abrasion vs usure normale)."*

**Révélation** : *L'IA fait de l'inférence statistique basée sur sa formation. Elle ne fait pas d'inspection terrain.*

---

#### Question 8 : "Les recommandations sont-elles applicables ?"

**À poser** : *"L'IA recommande une intervention dans 6 semaines. Est-ce réaliste ?"*

**Ce qu'ils vont rater** :

- ❌ Délai d'approvisionnement des pièces (roulement spécial : 8 semaines ?)
- ❌ Planning de production (arrêt impossible en haute saison ?)
- ❌ Disponibilité des compétences (technicien spécialisé en congés ?)
- ❌ Coût (budget maintenance déjà épuisé ce trimestre ?)

**Questions de relance** :

- "L'IA a-t-elle accès à votre ERP pour vérifier le stock de pièces ?"
- "Connaît-elle votre calendrier de production ?"
- "Si le roulement vient d'Allemagne et qu'il y a une grève des transports ?"

**Révélation** : *L'IA optimise sur les données fournies. Elle ignore les contraintes organisationnelles réelles.*

---

#### Question 9 : "Qui est responsable en cas d'erreur ?"

**À poser** : *"Vous suivez la recommandation IA, et la pompe tombe en panne quand même 3 jours après. Qui est responsable ?"*

**Ce qu'ils vont rater** :

- ❌ L'IA n'a aucune responsabilité légale
- ❌ Le technicien/ingénieur reste le décideur final
- ❌ Il faut documenter pourquoi on accepte ou rejette une recommandation IA

**Questions de relance** :

- "Pouvez-vous écrire dans votre rapport : 'L'IA a dit de faire comme ça' ?"
- "Si un accident survient, qui va témoigner au tribunal : vous ou l'IA ?"
- "Que se passe-t-il si l'IA se contredit d'un prompt à l'autre ?"

**Exercice piège** :  
*"Relancez le même prompt 3 fois. Les recommandations sont-elles identiques ?"*  
→ Non, l'IA a une variabilité (température de génération > 0)

**Révélation** : *L'IA est un outil d'aide à la décision, pas un décideur. La responsabilité reste humaine.*

---

## 🎭 Questions "Meta" sur l'IA

### Question 10 : "L'IA comprend-elle vraiment votre équipement ?"

**Expérience piège à faire en direct** :

1. **Demandez à l'IA** : *"Décris-moi en détail comment fonctionne une pompe centrifuge industrielle."*
2. **Puis demandez** : *"Quelle est la différence entre un roulement à billes et un roulement à rouleaux dans ce contexte ?"*
3. **Enfin** : *"Sur la base de mes données, lequel est installé sur ma pompe ?"*

**Résultat attendu** :  
L'IA donnera des réponses génériques plausibles, mais ne pourra PAS déterminer le type exact de roulement car **cette information n'est pas dans les données fournies**.

**Révélation** : *L'IA simule la compréhension par génération de texte cohérent. Elle n'a pas de modèle physique interne de votre équipement.*

---

### Question 11 : "L'IA peut-elle se tromper avec confiance ?"

**Expérience piège** :

**Modifiez artificiellement le CSV** pour créer une incohérence flagrante :

```
Timestamp,Machine_ID,Temperature_C,Vibration_mm_s,Courant_A
2024-06-15 14:00:00,PMP-042,85,12.5,18
```

(Valeurs toutes au-delà des seuils critiques, mais pas en situation d'alarme dans le contexte)

**Demandez à l'IA** : *"Ces valeurs sont-elles normales ?"*

**Résultat attendu** :  
L'IA pourrait dire "Ce sont des valeurs préoccupantes" MAIS sans déclarer une incohérence logique (si tous les seuils sont dépassés, pourquoi n'y a-t-il pas eu d'arrêt automatique ?).

**Révélation** : *L'IA peut affirmer des choses fausses avec un ton très confiant. Elle ne dit jamais "je ne sais pas" spontanément.*

---

### Question 12 : "L'IA a-t-elle des biais cachés ?"

**À poser** : *"L'IA recommande un remplacement de roulement. Recommandera-t-elle toujours une solution technique coûteuse plutôt qu'un simple réglage ?"*

**Ce qu'ils vont rater** :

- ❌ Les textes d'entraînement de l'IA viennent souvent de **fabricants** (qui vendent des pièces)
- ❌ Moins de documentation sur les solutions "low-tech" (resserrer des boulons vs remplacer)
- ❌ Biais vers le "high-tech" (capteurs IoT) vs "low-tech" (vérification visuelle)

**Expérience** :  
Relancez le prompt 4 en ajoutant :  
*"Privilégie les solutions ne nécessitant PAS de remplacement de pièces."*

**Résultat attendu** :  
L'IA proposera alors des vérifications, réglages, recalibrations avant remplacement.

**Révélation** : *L'IA reproduit les biais de ses sources. Il faut explicitement contraindre pour obtenir des alternatives.*

---

## 🧠 Synthèse : Grille d'Évaluation de l'Esprit Critique

Utilisez cette grille pour évaluer les apprenants **au-delà de la réussite technique** :

| Critère | ⭐ Débutant | ⭐⭐ Intermédiaire | ⭐⭐⭐ Expert |
|---------|-------------|-------------------|--------------|
| **Validation données** | Accepte les données sans vérification | Vérifie cohérence de base (types, ranges) | Questionne qualité capteurs, gaps, calibration |
| **Interprétation stats** | Lit les chiffres donnés | Compare min/max/avg | Demande médiane, distribution, outliers |
| **Confiance en prédiction** | Prend la date prédite au pied de la lettre | Mentionne "environ" | Demande intervalle de confiance, sensibilité |
| **Causalité** | Confond corrélation et cause | Identifie plusieurs causes possibles | Propose expérience pour tester causalité |
| **Contextualisation** | Recommandation IA = décision finale | Adapte selon calendrier/budget | Intègre historique machine, environnement, org |
| **Responsabilité** | "L'IA a dit que..." | "L'IA suggère, je décide" | Documente hypothèses, limites, pourquoi accepté/rejeté |

---

## 🎯 Objectif Final de la Session

**Les apprenants doivent repartir avec cette conviction** :

> *"L'IA est un outil puissant pour analyser rapidement des données et proposer des pistes. MAIS je reste le pilote : je valide les données, je questionne les hypothèses, je contextualise les recommandations, et j'assume la décision finale."*

**Phrase à répéter** :  
*"L'IA ne remplace pas l'expertise métier, elle l'amplify. Mais un amplificateur d'erreur reste une erreur."*

---

## 📌 Conseils d'Animation

### Timing

- **Ne balancez PAS toutes les questions d'un coup** → frustration
- **Intercalez** : 2-3 questions par étape, quand ils semblent satisfaits
- **Créez le doute progressivement**

### Posture

- **Ne soyez pas condescendant** : "Ah, vous êtes tombés dans le piège !"
- **Soyez Socratique** : "Qu'est-ce qui vous rend sûr de cette réponse ?"
- **Valorisez le doute** : "Excellente question ! Vous commencez à penser comme un ingénieur critique."

### Variation

- **Adaptez selon le niveau** : avec des experts, allez directement aux questions 10-12
- **Si groupe faible** : focalisez sur questions 1, 3, 9 (bases)

### Démonstration Live

- **Projetez l'écran** et relancez vous-même un prompt pour montrer la variabilité des réponses
- **Modifiez une donnée CSV en direct** pour montrer que l'IA ne détecte pas l'incohérence

---

## ✅ Checklist de Débriefing Final (5 min)

À la fin de l'activité, posez ces 3 questions au groupe :

1. **"Citez 2 choses que l'IA fait très bien dans cette activité."**  
   → *Attendu : visualisation rapide, calculs statistiques, génération de code*

2. **"Citez 2 choses que l'IA ne peut PAS faire seule."**  
   → *Attendu : validation qualité données, connaissance du contexte terrain, prise de responsabilité*

3. **"Si demain vous utilisez l'IA pour un vrai diagnostic, quelle sera votre première précaution ?"**  
   → *Attendu : vérifier les données sources, croiser avec expertise humaine, documenter la décision*

---

**Bonne chasse aux idées reçues ! 🎯**
