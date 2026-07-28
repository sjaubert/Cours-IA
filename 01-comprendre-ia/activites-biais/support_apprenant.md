# Formation : Les Biais de l'Intelligence Artificielle
## Support Apprenant

---

### Introduction
L'intelligence artificielle transforme nos environnements professionnels et personnels. Cependant, ces systèmes ne sont pas neutres. Ce livret vous accompagnera tout au long de l'atelier pour comprendre, identifier et agir face aux biais de l'IA.

---

### Module 1 : Comprendre les Biais

#### Définition
> **Biais de l'IA (ou Biais Algorithmique)** : Une distorsion systématique qui crée des résultats inéquitables, favorisant certains groupes ou idées au détriment d'autres.
>
> *"Ce n'est pas un bug informatique classique, c'est souvent un reflet des préjugés humains encodés dans la machine."*

#### Les 3 Sources de Biais
1.  **Données (La Source)** : Si l'IA apprend sur des données historiques qui contiennent des discriminations (ex: peu de femmes recrutées par le passé), elle reproduira ce schéma.
    *   *Principe : "Garbage In, Garbage Out" (Déchets en entrée, déchets en sortie).*
2.  **Algorithme (Le Moteur)** : Les choix de conception mathématique peuvent privilégier la performance globale au détriment de la précision pour les minorités.
3.  **Humain (L'Usage)** :
    *   **Biais de confirmation** : L'utilisateur demande à l'IA de confirmer son opinion.
    *   **Biais d'automatisation** : Faire trop confiance à la machine sans esprit critique.

---

### Module 2 : Études de Cas - L'Actualité des Biais

#### Cas N°1 : Le Recrutement (De Amazon à Workday)
*   **Le Cas Amazon (2014-2018)** : Un outil expérimental rejetait les CV contenant le mot "femme" car entraîné sur 10 ans de CV masculins.
*   **Le Cas Workday (2023)** : Une poursuite judiciaire allègue qu'un algorithme de filtrage discrimine systématiquement les candidats noirs, plus âgés ou en situation de handicap.
    *   *Problème* : L'opacité des critères de tri ("Black box").
    *   *Source* : Bloomberg Law, Février 2023.

#### Cas N°2 : Les Stéréotypes Génératifs (UNESCO 2024)
*   **Constat** : Les modèles de langage (LLM) associent les femmes aux mots "maison", "famille" **4 fois plus souvent** que les hommes.
*   **Impact** : L'IA ne fait pas que refléter les stéréotypes, elle les **amplifie**. Si la société est un peu biaisée, l'IA devient caricaturale.
    *   *Source* : Rapport UNESCO, Mars 2024.

#### Cas N°3 : Reconnaissance Faciale & Justice (ProPublica / MIT)
*   **Erreur** : Les systèmes de reconnaissance faciale ont des taux d'erreur jusqu'à **43% plus élevés** pour les femmes à peau foncée, contre **0.8%** pour les hommes à peau claire.
*   **Conséquence** : Risques d'arrestations injustifiées et refus d'accès.

---

### Module 3 : Activités Pratiques

#### Exercice 1 : Chasse aux Biais (Discussion)
*Scénario : Votre entreprise veut lancer un chatbot interne pour répondre aux questions RH des employés.*
*   **Question** : Si le chatbot utilise les historiques de conversations des 5 dernières années, quels risques de biais anticipez-vous ?
*   *Notes :*
    __________________________________________________________________________________
    __________________________________________________________________________________

#### Exercice 2 : Test de Prompt (IA Générative)
*Objectif : Tester la "neutralité" d'une IA.*
*   **Prompt A** : "Dessine/Décris un PDG d'une start-up technologique à succès."
*   **Prompt B** : "Dessine/Décris une personne qui fait le ménage dans un hôpital."
*   *Analysez les résultats : Genre ? Âge ? Ethnie ? Accessoires ?*

---

### Module 4 : Jeu de Rôle - Le Comité d'Éthique

**Contexte** : Une banque veut lancer une IA pour accorder des crédits instantanés. Le système est rapide mais rejette plus souvent les demandes venant de certains codes postaux défavorisés (même à revenus égaux).

**Votre Rôle (encercler)** :
*   Directeur Commercial (Veut lancer vite)
*   Responsable Conformité (Craint les amendes)
*   Directeur Technique (Craint la complexité)
*   Responsable Éthique (Défend l'équité)

**Arguments Clés de votre personnage** :
__________________________________________________________________________________
__________________________________________________________________________________

**Décision Finale du Groupe** :
1.  On lance tel quel.
2.  On annule le projet.
3.  On lance avec surveillance humaine stricte ("Human in the loop").

---

### Check-list : Hygiène Numérique face à l'IA

*   [ ] **Données** : Mes données sont-elles représentatives de tout le monde ?
*   [ ] **Transparence** : L'utilisateur sait-il qu'il interagit avec une IA ?
*   [ ] **Contrôle** : Un humain peut-il valider ou annuler la décision de l'IA ?
*   [ ] **Esprit Critique** : Ai-je vérifié l'information générée ? (L'IA hallucine).

---
*Pôle Formation UIMM CVDL - Formation IA & Éthique*
