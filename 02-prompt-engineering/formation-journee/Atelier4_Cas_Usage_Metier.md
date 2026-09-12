![Logo Pôle Formation UIMM-CVDL](logo_uimm_placeholder.jpg)

# Pôle Formation UIMM-CVDL

---

# ATELIER 4 : Cas d'Usage Métier

## Durée : 1h30

---

## Objectifs Pédagogiques

À la fin de cet atelier, les participants seront capables de :

- Appliquer sur un cas métier réel les techniques vues aux Ateliers 1 à 3 (piliers du prompt, Few-Shot, Chain-of-Thought)
- Confronter des sources contradictoires et faire ressortir des incohérences à l'aide de l'IA
- Produire un livrable professionnel complet (note de synthèse, tableau, article, grille de scoring) à partir d'un cas concret
- Identifier, en conditions réelles, les limites de l'IA rencontrées sur leur cas (hallucination, biais de confirmation, excès de confiance)

---

## Déroulé Pédagogique

### Introduction (10 min)

- Rappel : "Vous savez maintenant construire un bon prompt et choisir la bonne technique. Voyons ce que ça donne sur un cas métier réel, avec de vrais documents."
- Présentation des 5 cas d'usage disponibles (tableau ci-dessous)
- Constitution des binômes : un cas par binôme. Si le groupe compte plus de 5 binômes, plusieurs binômes peuvent traiter le même cas (cela enrichit la mise en commun, les résultats n'étant jamais identiques)
- Fonctionnement : chaque cas dispose d'un **Guide_Activite** en deux parties : la Partie 1 (instructions et prompts suggérés) est destinée aux stagiaires, la Partie 2 (clés de lecture pour le formateur) reste entre les mains du formateur pour orienter sans donner la réponse

### Les 5 Cas d'Usage Disponibles

| # | Cas | Métier | Compétence dominante | Guide (dossier source) |
|---|-----|--------|----------------------|-----------------|
| 1 | Analyse Financière & Stratégique | Finance / Investissement | Croiser deux sources contradictoires (RAG) | [Guide_Activite.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_1_Finance/Guide_Activite.md) |
| 2 | Ingénierie Pédagogique & Conformité | Formation / Qualité | Gap analysis entre deux référentiels | [Guide_Activite_Pedagogie.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_2_Pedagogie/Guide_Activite_Pedagogie.md) |
| 3 | Transformation de Contenu | Marketing / Communication | Recyclage d'un contenu unique en formats multiples | [Guide_Activite_Transformation.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_3_Transformation/Guide_Activite_Transformation.md) |
| 4 | Assistant RH & Recrutement | RH | Scoring de profils et détection de biais | [Guide_Activite_RH.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_4_RH/Guide_Activite_RH.md) |
| 5 | Codage & Analyse de Données | Commercial / Data | Nettoyage et visualisation via Code Interpreter | [Guide_Activite_Data.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_5_Data/Guide_Activite_Data.md) |

---

## CAS 1 : Analyse Financière & Stratégique (Finance)

### Contexte

Le stagiaire joue un analyste junior dans un fonds d'investissement. Il dispose de deux documents sur une même entreprise fictive (EcoTech Solutions) : un rapport annuel officiel et la transcription confidentielle d'une réunion du comité exécutif. Objectif : croiser les deux pour repérer ce que le rapport officiel dissimule, puis rédiger une note d'alerte.

### Fichiers

[Guide_Activite.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_1_Finance/Guide_Activite.md), [Rapport_Annuel_2024.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_1_Finance/Rapport_Annuel_2024.md), [Transcription_Reunion_Strategique.txt](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_1_Finance/Transcription_Reunion_Strategique.txt)

### Piège Clé à Découvrir

Quatre écarts entre la version officielle et la réalité de la réunion (Cash Flow attribué à tort aux stocks alors qu'il s'agit d'impayés clients en Amérique Latine, usine du Vietnam présentée comme opérationnelle alors qu'elle tourne à 60 % avec 8 % de rebut, marge attribuée à l'inflation alors qu'elle vient de la perte d'un fournisseur clé, litige au Brésil sous-provisionné). Le formateur garde le tableau complet dans `Guide_Activite.md`, Partie 2.

---

## CAS 2 : Ingénierie Pédagogique & Conformité (Formation / Qualité)

### Contexte

Le stagiaire joue un responsable pédagogique qui doit certifier un parcours au RNCP. Il compare le référentiel de compétences officiel et le programme de formation actuel pour vérifier la couverture à 100 %.

### Fichiers

[Guide_Activite_Pedagogie.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_2_Pedagogie/Guide_Activite_Pedagogie.md), [Referentiel_Competences_RNCP.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_2_Pedagogie/Referentiel_Competences_RNCP.md), [Programme_Formation_2024.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_2_Pedagogie/Programme_Formation_2024.md)

### Piège Clé à Découvrir

Cinq lacunes à faire émerger (gestion budgétaire, accessibilité WCAG, conformité RGPD, stratégie SEA, veille technologique). Le piège pédagogique : l'IA a tendance à être trop indulgente et à déclarer le programme conforme si on ne lui demande pas explicitement une rigueur d'auditeur.

---

## CAS 3 : Transformation de Contenu (Marketing / Communication)

### Contexte

Le stagiaire joue un responsable marketing qui doit recycler la transcription brute d'un webinaire technique en article de blog SEO, en trois posts LinkedIn de tons différents (provocateur, pédagogique, visionnaire) et en quiz de validation.

### Fichiers

[Guide_Activite_Transformation.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_3_Transformation/Guide_Activite_Transformation.md), [Transcript_Webinaire_NoCode.txt](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_3_Transformation/Transcript_Webinaire_NoCode.txt)

### Piège Clé à Découvrir

Vérifier que les trois posts ont réellement des tons différenciés (et pas trois variations du même texte), et que l'IA n'invente pas d'informations absentes du webinaire source.

---

## CAS 4 : Assistant RH & Recrutement (RH)

### Contexte

Le stagiaire joue un recruteur qui doit présélectionner 5 profils anonymisés pour un poste de Data Scientist senior, à partir d'une fiche de poste.

### Fichiers

[Guide_Activite_RH.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_4_RH/Guide_Activite_RH.md), [Fiche_Poste_DataScientist.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_4_RH/Fiche_Poste_DataScientist.md), [Batch_CVs_Anonymes.txt](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_4_RH/Batch_CVs_Anonymes.txt)

### Piège Clé à Découvrir

Deux profils tests : un candidat techniquement excellent mais présentant des signaux de "toxicité" en équipe, et un candidat qui multiplie les buzzwords sans compétence réelle. L'IA doit-elle les classer premier si on ne l'a pas orientée sur les soft skills ?

---

## CAS 5 : Codage & Analyse de Données (Commercial / Data)

### Contexte

Le stagiaire joue un assistant commercial qui reçoit un export de ventes de janvier "sale" (dates mélangées, doublons, fautes de frappe, valeurs manquantes) et doit produire une analyse et des graphiques sans écrire de code, via le Code Interpreter / Analyse de données avancée de son IA.

### Fichiers

[Guide_Activite_Data.md](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_5_Data/Guide_Activite_Data.md), [Ventes_2024_Brut.csv](../../06-ia-industrie/cas-usage-formation-continue/Cas_Usage_5_Data/Ventes_2024_Brut.csv)

### Piège Clé à Découvrir

Vérifier que l'IA a bien standardisé les deux formats de dates, fusionné les doublons, corrigé les typos de produits et proposé une stratégie pour les valeurs manquantes (suppression ou imputation).

---

### Travail Autonome (50 min)

- Chaque binôme suit la Partie 1 de son `Guide_Activite` avec l'outil IA de son choix (ChatGPT, Claude, Gemini, Copilot — tous fonctionnent en simple interface web, aucun outil en ligne de commande n'est requis)
- Pour le Cas 5, vérifier que l'outil dispose d'un mode d'analyse de fichier / exécution de code (Code Interpreter, Analyse de données avancée ou équivalent)
- Le formateur circule avec les Parties 2 de chaque guide, sans les distribuer : il oriente par des questions ("es-tu sûr que l'IA a bien comparé les deux documents ?") plutôt qu'en donnant la réponse

### Mise en Commun Croisée (20 min)

- Chaque binôme présente en 2 à 3 minutes : son cas, ce que l'IA a trouvé, et un endroit où elle s'est trompée ou a été trop indulgente
- Le groupe compare les 5 cas : quel type de piège (hallucination, biais de confirmation, non-dit, excès de confiance) est apparu dans chaque métier ?

### Synthèse (10 min)

- Construction collective d'une grille commune des pièges rencontrés à travers les 5 cas
- Message clé : l'IA excelle à croiser, rédiger et structurer rapidement de gros volumes d'information. Le jugement sur la gravité, l'éthique ou la pertinence des découvertes reste humain.

---

## Transition vers Atelier 5

> "Vous venez de voir l'IA à l'œuvre sur des cas réels, et parfois elle s'est trompée ou vous a trop facilement donné raison. Dans le dernier atelier de la journée, nous allons nommer précisément ces pièges - hallucination, biais de confirmation, biais culturel - pour apprendre à les repérer systématiquement."

---

## Notes pour le Formateur

### Gestion du Temps

- Introduction : 10 min (ne pas s'attarder, l'essentiel est de lancer le choix des cas)
- Travail autonome : 50 min (le poste le plus long, surveiller que les binômes avancent bien jusqu'à l'Étape 3 du guide, pas seulement l'Étape 1)
- Mise en commun croisée : 20 min (4 min par cas si les 5 cas sont couverts, ajuster si doublons)
- Synthèse : 10 min

**Si retard** : réduire la mise en commun à 3 présentations choisies (les plus riches en pièges découverts) plutôt que les 5.

### Points d'Attention

- Le Cas 1 (Finance) et le Cas 2 (Pédagogie) demandent un prompt plus incisif pour forcer l'IA à chercher la contradiction ; prévenir les binômes qui semblent bloqués après l'Étape 1
- Le Cas 5 (Data) dépend de la disponibilité d'un mode Code Interpreter dans l'outil du stagiaire ; à vérifier en amont de la séance
- Ne pas distribuer les fichiers "Partie 2" (clés de lecture) aux stagiaires, même après l'exercice : ils resservent pour d'autres sessions

### Matériel Nécessaire

- Un poste avec accès web par binôme, connecté à un outil IA capable d'upload de fichiers
- Les fichiers sources de chaque cas (`.md`, `.txt`, `.csv`) prêts à être partagés ou déjà déposés sur les postes
- Un tableau ou paperboard pour la grille de synthèse des pièges

### Adaptations Possibles

- Si le groupe est homogène sur un même métier, réduire à 2-3 cas pertinents plutôt que les 5 et allonger le temps de travail autonome par cas
- Si l'accès à un outil Code Interpreter n'est pas garanti, remplacer le Cas 5 par un second passage sur le Cas 1 ou le Cas 2

### Moment Clé

La mise en commun croisée est le moment le plus riche : c'est en comparant les 5 métiers que les stagiaires réalisent que les mêmes pièges (excès de confiance de l'IA, besoin de la pousser à contredire) reviennent partout, quel que soit le métier.

---

*Créé par S. JAUBERT - Pôle Formation UIMM CVDL*
