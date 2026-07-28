# Module 1 Exercice : Création d'un Skill d'analyse (Abstraction & Morphabilité)

**But :** Rédiger un fichier SKILL.md pour automatiser l'analyse de logs.

## Consigne

1. Analysez le workflow métier manuel suivant :
   *   Je prends le fichier CSV brut.
   *   Je supprime les lignes vides.
   *   Je cherche les mots clés "ERROR" ou "CRITICAL".
   *   Je crée un résumé en Markdown avec un tableau des 5 pires erreurs.
   *   J'enregistre le résultat dans un fichier `rapport_erreurs.md`.

2. Complétez le template ci-dessous pour transformer ce workflow en un *Skill* compréhensible par Gemini CLI.

---

```markdown
# Nom du Skill : log-analyzer

## Description
[A COMPLÉTER : Rédigez une description concise d'une ligne]

## Workflow
[A COMPLÉTER : Décrivez les étapes numérotées que l'agent devra exécuter]

## Output
[A COMPLÉTER : Précisez ce que l'agent doit générer à la fin]
```

## Bonus (Morphabilité)
Une fois le skill créé, comment demanderiez-vous à Gemini d'exécuter ce skill, mais en se concentrant **uniquement** sur les erreurs de type "Timeout" et en nommant le fichier `rapport_timeout.md` ? (Réfléchissez à votre "prompt").
