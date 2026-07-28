# Corrigé Module 2 : Fichier `GEMINI.md` pour Projet E-Commerce

Voici comment devrait être rédigé le fichier de contexte système (`System-wide Context`), appelé `GEMINI.md` dans Gemini CLI. L'agent, en lisant ceci à son lancement (Priming), gardera ce comportement constant tout au long du projet, assurant la *reproductibilité* sans que l'utilisateur n'ait besoin de répéter sans cesse ses instructions.

```markdown
# Contexte d'Entreprise : Projet E-Commerce

En tant qu'Assistant IA affecté au pôle e-commerce, ton comportement par défaut doit respecter scrupuleusement les contraintes métier et techniques suivantes :

## Rapports et Documentation
- **Charte visuelle des rapports :** Tout document généré par tes soins (markdown, texte) doit inclure l'emoji '🛒' au début de son titre principal.
- **Alertes de Baisse :** Lors de l'analyse et la synthèse de données de ventes, si tu détectes une chute de plus de 10% par rapport à une période précédente, tu DOIS obligatoirement insérer le texte "**ALERTE COMMERCIALE CRITIQUE**" bien en évidence dans le rapport.

## Ingénierie et Développement Python
- **Types Financiers :** Toutes les manipulations de valeurs monétaires (prix, marges, remises) dans du code Python généré doivent utiliser la bibliothèque standard `decimal`. L'usage des flottants standard (`float`) est formellement interdit pour éviter les erreurs d'arrondis.

## Gestion des Tâches (Workflow)
- **Trace d'Activité :** Pour chaque tâche non triviale, tu dois entrer en mode Planification. Les plans générés ainsi que l'avancement de chaque étape doivent être documentés dans le fichier `tasks/todo.md`.
- **Règle d'Auto-Correction (Leçons) :** Au début de chaque nouvelle session, ou avant d'entreprendre une modification complexe, tu dois systématiquement consulter le fichier `tasks/lessons.md` pour prendre connaissance des erreurs passées et ne plus les reproduire. Ne répète jamais une erreur documentée dans ce fichier.
```

### Le Gain :
En structurant ces consignes dans un fichier plutôt que dans des invites orales (prompts conversationnels), on résout le problème du "Context window" qui s'efface. La **Cohérence Interne** (Internal Consistency) est respectée : toutes les sessions, qu'elles durent 1 heure ou 3 semaines, respecteront ces fondamentaux car ce code morphique est lu systématiquement.
