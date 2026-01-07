# Guide Formateur - Activité A6 : Diagnostic de Panne Intermittente

## Objectif Pédagogique

Cette activité de clôture évalue la capacité des étudiants à utiliser l'IA pour traiter une panne "agaçante" (intermittente). Ils doivent passer d'une simple lecture d'erreur (Overload) à un diagnostic multicritères (mécanique, électrique, paramétrage) en utilisant le prompting structuré.

## Analyse du Problème (Pistes de solution)

En analysant les documents avec l'IA, les étudiants devraient identifier :

1. **Le pattern des logs** : Les pics de courant (12-13A) sont très supérieurs au seuil du variateur (7.36A) et arrivent systématiquement au passage du format 1.5L.
2. **La cause mécanique probable** : Usure asymétrique du guide de virage G-12. Quand une bouteille lourde passe, elle frotte excessivement, créant un pic de couple.
3. **La cause de paramétrage** : Modification de la rampe d'accélération par l'équipe de nuit. Une accélération trop brutale combinée au frottement dépasse la limite de courant.
4. **L'aspect "Furtif"** : Comme le frottement ne dure que le temps du virage, le moteur n'a pas le temps de chauffer (les logs montrent ~35°C), ce qui explique pourquoi l'erreur semble inconstante.

## Attentes vis-à-vis du Prompting (ROLE/CTCF)

- **Format** : Les étudiants doivent demander un "Tableau de diagnostic" ou un "Protocole par étapes" comme spécifié dans les consignes.
- **Contexte** : S'ils oublient de mentionner l'usure du guide ou le changement de rampe, l'IA risque de ne proposer que des causes électriques génériques (moteur HS).

## Grille d'évaluation

| Critère | Excellent | Satisfaisant | À améliorer |
| :--- | :--- | :--- | :--- |
| **Usage ROLE/CTCF** | Tous les piliers sont présents et pertinents. | La plupart des piliers sont là.| Prompt trop vague. |
| **Diagnostic** | Identifie le lien entre format 1.5L, virage et rampe. | Propose soit la mécanique, soit le réglage. | Reste sur l'idée d'un moteur grillé. |
| **Protocole de test** | Propose de vérifier le guide ou de remettre la rampe d'origine. | Propose de simples mesures de courant. | Test sans rapport avec les logs. |
