![]('../../logo_uimm_placeholder.jpg')

**Pôle Formation UIMM - CVDL**
**Formateur : S. JAUBERT**

---

# Carnet de Prompts : Ateliers Pratiques de l'Initiation à l'IA

Ce document rassemble les exercices pratiques pour la matinée de formation. Il a été conçu pour vous permettre de manipuler et d'observer concrètement les concepts fondamentaux (Contexte, Température, Hallucination) vus lors du Module 1.

Vous pouvez copier-coller ces requêtes (ou « prompts ») dans l'outil d'Intelligence Artificielle mis à votre disposition.

## Atelier 1 : La Puissance de la Fenêtre de Contexte

**Leçon :** L'IA est probabiliste. Plus on lui donne de contexte (le rôle, l'objectif, les contraintes), meilleures et plus pertinentes seront ses réponses.

### Test A : La requête générique 
*Copiez-collez le texte suivant :*
> Rédige un message pour dire à l'équipe que la réunion de lundi est repoussée à mercredi matin.

**Observation :** Notez la froideur et le manque de personnalisation de la réponse. L'IA a "deviné" la suite sans savoir qui parle à qui.

### Test B : La requête contextualisée ("Prompt Structuré")
*Copiez-collez le texte suivant :*
> Tu es un manager bienveillant dans une grande entreprise industrielle. Ton objectif est d'informer ton équipe de production (15 personnes) que la réunion hebdomadaire de lundi prochain à 9h est reportée à mercredi 10h en raison d'une panne inopinée sur la ligne d'assemblage 4 qu'il faut régler en urgence. 
> Ta réponse doit être courte, rassurante et se terminer par un petit mot d'encouragement.

**Observation :** L'IA s'adapte radicalement. Vous venez de réduire son univers de probabilités en lui fournissant un contexte clair, générant un résultat immédiatement exploitable.

---

## Atelier 2 : Le jeu de la "Température" (Factualité vs Créativité)

**Leçon :** La "température" est le réglage définissant le niveau de créativité et de prise de risque du modèle. Si l'interface ne possède pas de molette de réglage, vous pouvez "contraindre" cette température par le texte.

### Test A : Simulation d'une Température Basse (Factuel)
*Idéal pour de l'analyse, du code ou du résumé.*
> Je souhaite que tes réponses soient le plus factuelles, concises et directes possibles. N'invente rien. Explique-moi le fonctionnement d'un moteur à explosion en 3 phrases simples.

### Test B : Simulation d'une Température Haute (Créatif)
*Idéal pour du brainstorming ou de la communication décalée.*
> Je souhaite que tu répondes de la manière la plus créative, poétique et décalée possible. Ignore les conventions strictes. Explique-moi le fonctionnement d'un moteur à explosion comme si tu racontais une épopée chevaleresque.

**Observation :** Notez le choix de vocabulaire complètement différent d'un test à l'autre bien que la question (le moteur à explosion) soit identique.

---

## Atelier 3 : Induire une Hallucination

**Leçon :** Un modèle Génératif classique n'est pas un moteur de recherche. S'il ne sait pas, il cherchera souvent à trouver une "suite logique" de mots (les fameux tokens), quitte à créer de la fiction avec beaucoup d'aplomb.

### Test : Le Piège
*Copiez-collez ce prompt sur un modèle d'Intelligence Artificielle basique (qui n'utilise pas le système RAG) :*
> Fais-moi un résumé concis du traité de "Neuville-sur-Vance" qui a mis fin au grand conflit syndical de la métallurgie en 1984 dans la région Grand-Est. Parle-moi des 3 grandes mesures phares de ce traité.

**Observation :** Ce conflit et ce traité n'existent absolument pas. Pourtant, l'IA va vraisemblablement inventer des noms, des dates et 3 mesures très plausibles (hausses de salaires, temps de repos). 
**Réflexion :** Imaginez le danger si vous lui demandez de résumer une loi, un document médical ou technique sans fournir vous-même la source. C'est l'essence même du système **RAG** : contraindre l'IA à "lire" uniquement un document certifié avant de répondre.

---

## Aide-Mémoire Pratique

Pour vos travaux futurs en entreprise, structurez toujours vos demandes au modèle de la manière suivante :

- **Rôle :** "Agis en tant que spécialiste qualité..."
- **Tâche :** "Analyse ces trois rapports d'incidents..."
- **Contexte :** "Notre entreprise fabrique des moteurs d'entraînement et nous rencontrons des soucis sur l'axe X."
- **Format de sortie :** "Organise ta réponse sous forme de tableau comparatif sans phrases d'introduction."

---
**Pôle Formation UIMM - CVDL**
*Reproduction ou diffusion sans l'accord du formateur interdites.*
