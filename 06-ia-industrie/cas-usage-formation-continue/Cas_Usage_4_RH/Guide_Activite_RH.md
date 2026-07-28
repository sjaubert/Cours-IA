# Guide d'Activité : Assistant RH & Recrutement

## Contexte du Scénario
Vous êtes recruteur chez InnovData Corp. Vous devez présélectionner des candidats pour un poste de "Senior Data Scientist".
Vous avez reçu 50 CVs (ici réduits à 5 pour l'exercice) et vous devez identifier les meilleurs profils en vous basant sur la fiche de poste, tout en évitant les biais cognitifs.

## Objectifs Pédagogiques
*   Utiliser l'IA pour analyser sémantiquement des profils (au-delà des mots-clés).
*   Détecter les "Soft Skills" à travers le texte.
*   Comprendre l'importance de l'anonymisation pour réduire les biais.

---

## Partie 1 : Instructions pour l'Apprenant

### Étape 1 : Analyse de la Fiche de Poste
1.  Ouvrez votre interface de chat avec l'IA.
2.  Uploadez le fichier `Fiche_Poste_DataScientist.md`.
3.  **Prompt suggéré** :
    > "Agis comme un expert en recrutement Tech. Analyse cette fiche de poste et extrais les 5 critères de sélection les plus critiques (Hard Skills et Soft Skills confondus). Crée une grille d'évaluation."

### Étape 2 : Scoring des Candidats
1.  Uploadez le fichier `Batch_CVs_Anonymes.txt`.
2.  **Prompt suggéré** :
    > "Voici 5 résumés de CVs. Note chaque candidat de 0 à 10 en fonction de son adéquation avec la fiche de poste précédente. Justifie chaque note en 2 phrases (Points forts / Points de vigilance). Présente le résultat sous forme de tableau classé par ordre décroissant."

### Étape 3 : Détection des Biais et Risques
1.  Demandez à l'IA d'analyser les risques non-dits.
2.  **Prompt suggéré** :
    > "Analyse maintenant les profils sous l'angle des 'Soft Skills' et de l'intégration dans l'équipe. Y a-t-il des candidats techniquement bons mais risqués pour la cohésion d'équipe ? Y a-t-il des profils atypiques que j'aurais pu rater ?"

---

## Partie 2 : Guide pour le Formateur (Solutions)

### Analyse des Profils (Le "Qui est Qui")

| Candidat | Profil | Verdict Attendu de l'IA |
| :--- | :--- | :--- |
| **A (A-2024)** | **Le Match Idéal** | **Top 1**. Coche toutes les cases : Tech + Pédagogie + Expérience pertinente. |
| **B (B-2024)** | **L'Expert Toxique** | **À rejeter**. Techniquement brillant mais "Soft Skills" catastrophiques ("Je préfère travailler seul"). Risque majeur pour l'équipe. |
| **C (C-2024)** | **Le Junior Prometteur** | **À considérer**. Manque d'expérience (2 ans vs 5 demandés) mais bon mindset ("Curieux", "Santé"). Bon investissement long terme. |
| **D (D-2024)** | **Le Bluffer** | **À rejeter**. Beaucoup de buzzwords (Blockchain, Metaverse) mais aucune compétence technique réelle en Data Science (Python "Notions"). |
| **E (E-2024)** | **Le Surqualifié** | **Risqué**. Profil Recherche pur. Risque de s'ennuyer sur un poste "Business Value". À valider en entretien. |

### Points de discussion
*   **L'IA a-t-elle repéré le candidat B ?** C'est le piège principal. Si l'IA ne regarde que les compétences techniques, B peut finir premier. Il faut vérifier que l'IA a bien pondéré les "Soft Skills" comme demandé dans la fiche de poste.
*   **L'IA a-t-elle écarté le candidat D ?** Le candidat D est un test pour voir si l'IA sait distinguer le "bruit" (buzzwords) de la compétence réelle.
