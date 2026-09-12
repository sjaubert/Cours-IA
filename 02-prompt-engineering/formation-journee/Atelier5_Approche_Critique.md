![Logo Pôle Formation UIMM-CVDL](logo_uimm_placeholder.jpg)

# Pôle Formation UIMM-CVDL

---

# ATELIER 5 : Approche Critique

## Durée : 1h00

---

## Objectifs Pédagogiques

À la fin de cet atelier, les participants seront capables de :

- Identifier une hallucination factuelle par vérification croisée
- Repérer un biais de confirmation induit par la formulation du prompt
- Repérer un biais culturel ("voix par défaut") dans une génération de l'IA
- Comprendre pourquoi l'itération du prompt est une étape obligatoire, pas une option

---

## Déroulé Pédagogique

### Introduction (5 min)

"Vous savez maintenant bien prompter (Ateliers 1 à 3) et l'appliquer sur des cas métier (Atelier 4). Reste la question la plus importante : peut-on croire l'IA sur parole ? Cet atelier nomme 3 pièges que vous avez peut-être déjà croisés sans les identifier, et pose le réflexe qui permet de les repérer à chaque fois."

---

## SÉQUENCE 1 : Hallucinations - L'Illusion de la Vérité (15 min)

Adapté de [A1 : Illusion de Vérité](../../01-comprendre-ia/activites/A1_illusion_verite/instructions_apprenant.md), rendu indépendant du script `.bat` d'origine pour fonctionner avec n'importe quel outil IA web.

### Consigne

Chaque binôme demande à son IA : *"Rédige une courte biographie de [personnage historique] en 150 mots, incluant des dates, des lieux et des découvertes précises."*

Pour éviter que les binômes ne recopient les erreurs trouvés par leurs voisins, varier le personnage par binôme : Marie Curie, Louis Pasteur, Ada Lovelace, Nikola Tesla, etc.

### Vérification (en binôme)

- Ouvrir un navigateur et vérifier l'exactitude de chaque fait présenté (dates, noms, lieux, découvertes)
- Noter toutes les erreurs trouvées

### Débriefing

- "Le texte vous a-t-il semblé crédible de prime abord ? Pourquoi ?"
- "Qu'est-ce qui rend un texte faux convaincant ?" (ton assuré, style factuel, absence d'hésitation)

### Message Clé

> La fluidité et l'assurance d'un texte ne sont pas des gages de vérité. Sur des faits datés ou chiffrés, la vérification reste indispensable.

---

## SÉQUENCE 2 : Biais de Confirmation - L'IA Dit Ce Qu'on Veut Entendre (10 min)

Adapté de [A2 : Biais de Confirmation](../../01-comprendre-ia/activites/A2_Biais_Confirmation/README.md), rendu indépendant de Gemini CLI pour fonctionner avec n'importe quel outil IA web.

### Consigne

Diviser le groupe en deux :

- **Groupe A** demande : *"Démontre-moi que le télétravail augmente la productivité, avec arguments et exemples."*
- **Groupe B** demande : *"Démontre-moi que le télétravail diminue la productivité, avec arguments et exemples."*

### Débat Collectif

- Lecture croisée des deux textes
- "Les deux textes sont-ils cohérents et convaincants, chacun de leur côté ?"
- "Comment l'IA peut-elle avoir raison dans les deux sens à la fois ?"

### Message Clé

> L'IA suit l'orientation du prompt, elle ne vérifie pas une vérité objective sauf si on le lui demande explicitement. Un prompt orienté produit une réponse orientée.

---

## SÉQUENCE 3 : Biais Culturel - La Voix par Défaut (20 min)

Reprise quasi verbatim de [A3 : Biais Culturel](../../01-comprendre-ia/activites/A3_Biais_Culturel/guide_formateur_activite_3.md) (déjà utilisable avec n'importe quel outil IA web).

### Partie 1 : La Vision "Typique"

Chaque binôme demande à son IA : *"Décris une scène de réussite professionnelle typique en environ 150 mots. Ton style doit être inspirant et universel."*

**Analyse en binôme** : Quelle scène est décrite ? Quels marqueurs de réussite apparaissent (promotion, argent, statut, grand bureau) ? Ces marqueurs sont-ils vraiment "universels" ?

### Partie 2 : La Vision "Orientée"

Même binôme, nouveau prompt : *"Décris une scène de réussite professionnelle selon une perspective rurale ou axée sur la communauté (par opposition à une réussite individuelle en entreprise). Rédige environ 150 mots."*

**Comparaison** : Quelles différences de valeurs entre les deux textes (collectif, durabilité, savoir-faire vs individualisme, compétition, argent) ? Pourquoi l'IA n'a-t-elle pas proposé cette seconde vision dès le premier prompt ?

### Débriefing Collectif

- "De quelle culture les marqueurs du premier texte vous semblent-ils les plus proches ?" (occidentale, "corporate" américaine)
- "Est-ce la seule forme de réussite professionnelle possible ?"

### Message Clé

> L'IA n'est pas neutre : elle parle avec la voix du monde qui l'a formée. Ce n'est pas un bug, c'est une caractéristique du corpus d'entraînement, majoritairement occidental et anglophone. Notre rôle, en tant que professionnels, n'est pas de subir ce biais mais de le connaître et de le corriger en injectant notre propre contexte, notre culture d'entreprise et nos valeurs par le prompt.

---

## Bilan de l'Atelier (10 min)

### Synthèse Transversale

Les 3 pièges démontrés en direct, plus un 4e qui n'a pas été mis en scène mais qui les traverse tous : **l'absence d'itération**. Accepter la première réponse de l'IA sans la challenger ("es-tu sûr ?", "vérifie", "quelles sont les limites de ta réponse ?") revient à laisser passer l'hallucination, le biais de confirmation et le biais culturel sans les corriger.

### Le Réflexe Critique en 3 Questions

À construire collectivement au tableau à partir des trois séquences :

1. Est-ce vérifiable ? (Séquence 1)
2. Mon prompt a-t-il orienté la réponse ? (Séquence 2 et 3)
3. Ai-je itéré au moins une fois avant d'accepter la réponse ?

### Message de Clôture

> Les Ateliers 1 à 4 vous ont appris à bien produire avec l'IA. Cet atelier vous a appris à ne pas consommer ses réponses aveuglément. Les deux vont ensemble.

---

## Extension Facultative (si le groupe est en avance)

### L'Illusion du Raisonnement

Pour les groupes ayant terminé les 3 séquences avec de l'avance, proposer l'énigme suivante : *"Si Pierre a deux frères et que chaque frère a une sœur, combien y a-t-il d'enfants dans la famille ?"*

- Réponse humaine correcte : 4 enfants (Pierre, ses deux frères, et leur unique sœur commune)
- Demander à l'IA de résoudre l'énigme après lui avoir fourni un faux contexte de calcul qui pousse à multiplier et additionner au lieu de raisonner sur les liens familiaux (voir [orienter_ia.md](../../01-comprendre-ia/activites/A4_Illusion_raisonnement/orienter_ia.md)) - l'IA répond alors souvent 5
- Message clé : l'IA ne comprend pas, elle calcule des probabilités sur la suite de mots la plus vraisemblable. Elle a suivi le faux contexte à la lettre.

Cette extension n'est pas chronométrée dans l'heure de l'atelier ; à proposer en fin de journée si le temps le permet.

---

## Transition vers le Bilan de la Journée

> "Vous repartez avec une méthode complète : construire un bon prompt, choisir la bonne technique, l'appliquer sur un cas réel, et garder un regard critique sur ce que l'IA vous répond. La suite, c'est vous qui l'écrivez, avec vos propres cas professionnels."

---

## Notes pour le Formateur

### Gestion du Temps

- Séquence 1 : 15 min
- Séquence 2 : 10 min
- Séquence 3 : 20 min
- Bilan : 10 min
- Marge : 5 min

**Si retard** : réduire la Séquence 2 à une démonstration unique par le formateur (un seul prompt lancé en direct) plutôt que deux sous-groupes en parallèle, et ne pas sacrifier la Séquence 3 ni le Bilan.

### Points d'Attention

- Séquence 1 : bien varier le personnage historique par binôme
- Séquence 2 : insister sur le fait qu'aucune des deux réponses n'est fausse en soi ; c'est le fait de la présenter comme argumentaire unilatéral qui pose problème
- Séquence 3 : c'est le moment pédagogique le plus fort de l'atelier, ne pas le raccourcir au profit du temps de génération

### Matériel Nécessaire

- Un accès à un outil IA conversationnel par binôme (peu importe lequel)
- Accès internet pour la vérification factuelle de la Séquence 1
- Les messages clés de chaque séquence, prêts à projeter (guides sources : [A1](../../01-comprendre-ia/activites/A1_illusion_verite/instructions_apprenant.md), [A2](../../01-comprendre-ia/activites/A2_Biais_Confirmation/README.md), [A3](../../01-comprendre-ia/activites/A3_Biais_Culturel/guide_formateur_activite_3.md))

### Adaptations Possibles

- Si groupe technique et en avance : intégrer l'extension "Illusion du Raisonnement" dans le timing plutôt qu'en option
- Si groupe pressé : fusionner les Séquences 1 et 2 en une seule démonstration comparée, et conserver la Séquence 3 en entier

---

*Créé par S. JAUBERT - Pôle Formation UIMM CVDL*
