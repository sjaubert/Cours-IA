# Guide d'Activité : Ingénierie Pédagogique & Conformité

## Contexte du Scénario
Vous êtes responsable pédagogique dans un centre de formation. Votre organisme souhaite faire certifier son parcours "Chef de Projet Digital" au RNCP (Répertoire National des Certifications Professionnelles).
Vous disposez de deux documents :
1.  Le **Référentiel de Compétences Officiel** (RNCP).
2.  Le **Programme de Formation Actuel** (Syllabus 2024).

Votre mission est de vérifier si votre programme couvre bien 100% des compétences exigées par le référentiel.

## Objectifs Pédagogiques
*   Utiliser l'IA pour comparer deux documents structurés (Mapping).
*   Identifier les écarts (Gap Analysis) avec précision.
*   Générer des propositions d'amélioration pour combler les lacunes.

---

## Partie 1 : Instructions pour l'Apprenant

### Étape 1 : Analyse Comparative (Le "Mapping")
1.  Ouvrez votre interface de chat avec l'IA.
2.  Uploadez les deux fichiers : `Referentiel_Competences_RNCP.md` et `Programme_Formation_2024.md`.
3.  **Prompt suggéré** :
    > "Agis comme un auditeur qualité Qualiopi. Compare mon programme de formation actuel avec le référentiel de compétences officiel RNCP. Crée une matrice de correspondance sous forme de tableau. Pour chaque compétence du référentiel, indique si elle est 'Couverte', 'Partiellement couverte' ou 'Non couverte' par le programme, en citant le module correspondant."

### Étape 2 : Identification des Lacunes ("Trous dans la raquette")
1.  Demandez à l'IA de lister explicitement ce qui manque.
2.  **Prompt suggéré** :
    > "Liste maintenant uniquement les compétences qui sont 'Non couvertes' ou 'Partiellement couvertes'. Sois très précis."

### Étape 3 : Ingénierie de Formation (Remédiation)
1.  Demandez à l'IA de proposer des ajouts au programme.
2.  **Prompt suggéré** :
    > "Propose-moi des modules complémentaires ou des modifications du programme existant pour couvrir ces lacunes et atteindre 100% de conformité. Précise les objectifs pédagogiques et la durée estimée pour chaque ajout."

---

## Partie 2 : Guide pour le Formateur (Solutions & Clés de lecture)

### Les "Trous dans la raquette" (Solutions)
L'IA doit permettre aux apprenants d'identifier les manques suivants dans le programme actuel :

| Compétence RNCP | Statut dans le Programme | Détail du Manque |
| :--- | :--- | :--- |
| **C1.2 - Gestion budgétaire** | **Non Couvert** | Le module 1 parle de planning (Gantt) mais pas de **budget** ni de suivi financier. |
| **C1.3 - Accessibilité (WCAG)** | **Non Couvert** | Le module 3 parle de HTML/CSS mais ne mentionne pas l'**accessibilité numérique** (Pourtant obligatoire). |
| **C1.3 - Conformité RGPD** | **Non Couvert** | Aucune mention de la protection des données dans les modules techniques ou gestion. |
| **C2.1 - Stratégie SEA** | **Partiellement** | Le module 2 couvre le SEO mais le **SEA** (Publicité payante) est absent. |
| **C3.2 - Veille Techno** | **Non Couvert** | Pas de module dédié à la méthodologie de veille. |

### Points de vigilance
*   **Faux Positifs** : L'IA peut parfois considérer que "Gestion de projet Agile" couvre tout, y compris le budget. Il faut pousser l'IA à vérifier la présence explicite des termes financiers.
*   **Hallucinations de conformité** : L'IA peut être "trop gentille" et dire que le programme est conforme globalement. L'apprenant doit exiger une rigueur d'auditeur.
*   **Pertinence des solutions** : Vérifier que les propositions de l'IA sont réalistes (ex: ne pas rajouter 200 heures de cours pour un point de détail).
