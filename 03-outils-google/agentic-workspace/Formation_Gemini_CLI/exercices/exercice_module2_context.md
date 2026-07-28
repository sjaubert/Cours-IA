# Module 2 Exercice : Le Context Engineering (GEMINI.md et Reproductibilité)

**But :** Définir un fichier `GEMINI.md` (System-wide Context) qui force l'agent à respecter des règles d'entreprise strictes, rendant ainsi les sessions reproductibles.

## Consigne

Créez le contenu d'un fichier `GEMINI.md` pour une entreprise de e-commerce. L'agent IA doit toujours suivre ces règles :

1. Les rapports générés doivent avoir un titre commençant par 🛒.
2. Si une analyse de ventes montre une baisse de plus de 10%, l'agent doit insérer l'alerte suivante en gras : **ALERTE COMMERCIALE CRITIQUE**.
3. Lors de la création de code pour les calculs de prix, l'agent doit toujours utiliser la bibliothèque `decimal` (pas de `float` classiques) en Python.
4. L'agent doit toujours enregistrer ses plans dans `tasks/todo.md`.

Rédigez le fichier `GEMINI.md` qui instruit l'agent de suivre ces 4 règles.

---

```markdown
# Contexte d'Entreprise : Projet E-Commerce
[A COMPLÉTER : Rédigez ici vos instructions (System-wide Context) pour l'agent]
```

## Bonus (La Règle d'Apprentissage)
Ajoutez une règle dans ce `GEMINI.md` exigeant que l'agent lise toujours le fichier `tasks/lessons.md` au démarrage pour ne pas reproduire les erreurs passées.
