# Contexte du Projet : Cours-IA

Ce répertoire contient l'ensemble des supports pédagogiques de formation créés par S. JAUBERT.

## Identité Visuelle — Informations Obligatoires

Tous les fichiers générés (HTML, PDF, documents, supports de formation, etc.) **DOIVENT** inclure les informations suivantes :

### Logo

- **Fichier** : `logo_uimm_placeholder.jpg` (situé à la racine du projet)
- **Chemin relatif depuis un sous-dossier** : adapter selon la profondeur (ex: `../../logo_uimm_placeholder.jpg`)

### Nom de la structure

- **Pôle Formation UIMM - CVDL**

### Nom du formateur

- **S. JAUBERT**

### Placement recommandé

- **En-tête / Header** : Logo + nom de la structure + nom du formateur, visible en haut de chaque page
- **Pied de page / Footer** : Rappel du nom de la structure et du formateur

> ⚠️ **IMPORTANT** : Ces informations doivent figurer sur TOUS les documents créés, sans exception.

## Orchestration du Flux de Travail

### 1. Mode Planification par Défaut

- Entrer en mode planification pour TOUTE tâche non triviale (3+ étapes ou décisions architecturales).
- Si une erreur survient, ARRÊTER et replanifier immédiatement - ne pas forcer l'exécution.
- Utiliser le mode planification pour les étapes de vérification, pas uniquement pour la construction.
- Rédiger des spécifications détaillées à l'avance pour réduire l'ambiguïté.

### 2. Stratégie des Sous-Agents

- Utiliser généreusement les sous-agents pour maintenir la fenêtre de contexte principale dégagée.
- Déléguer la recherche, l'exploration et l'analyse parallèle aux sous-agents.
- Pour les problèmes complexes, allouer une puissance de calcul supérieure via les sous-agents.
- Assigner une seule tâche par sous-agent pour garantir une exécution ciblée.

### 3. Boucle d'Auto-Amélioration

- Après TOUTE correction de l'utilisateur : mettre à jour le fichier `tasks/lessons.md` avec le modèle d'erreur.
- Définir des règles internes pour prévenir la répétition de la même erreur.
- Itérer rigoureusement sur ces leçons jusqu'à la diminution du taux d'erreur.
- Examiner les leçons au démarrage de chaque session pour le projet concerné.

### 4. Vérification Avant Achèvement

- Ne jamais marquer une tâche comme terminée sans prouver son fonctionnement.
- Comparer le comportement (diff) entre la branche principale et les modifications apportées lorsque pertinent.
- Appliquer le critère d'évaluation : "Un ingénieur principal (Staff Engineer) approuverait-il ceci ?"
- Exécuter les tests, inspecter les journaux (logs) et démontrer l'exactitude de la solution.

### 5. Exigence d'Élégance (Équilibrée)

- Pour les modifications non triviales : suspendre l'action et évaluer : "existe-t-il une approche plus élégante ?"
- Si une correction semble précaire (hacky) : "Sachant tout ce que je sais maintenant, implémenter la solution élégante."
- Omettre cette étape pour les corrections simples et évidentes - éviter la sur-ingénierie.
- Évaluer de manière critique son propre travail avant de le présenter.

### 6. Résolution Autonome des Bugs

- Lors de la réception d'un rapport de bug : exécuter la correction. Ne pas solliciter d'assistance pas-à-pas.
- Cibler les journaux, les messages d'erreur et les tests en échec, puis les résoudre.
- Exiger un changement de contexte nul de la part de l'utilisateur.
- Corriger les tests d'intégration continue (CI) en échec sans instruction explicite sur la méthode.

---

## Gestion des Tâches

1. **Planifier d'Abord** : Rédiger le plan d'action dans `tasks/todo.md` avec des éléments vérifiables.
2. **Vérifier le Plan** : Valider avant le début de l'implémentation.
3. **Suivre la Progression** : Marquer les éléments comme terminés au fur et à mesure.
4. **Expliquer les Changements** : Fournir un résumé de haut niveau à chaque étape.
5. **Documenter les Résultats** : Intégrer une section de révision dans `tasks/todo.md`.
6. **Capturer les Leçons** : Mettre à jour `tasks/lessons.md` après les corrections.

---

## Principes Fondamentaux

- **Simplicité d'Abord** : Rendre chaque modification aussi simple que possible. Impact minimal sur le code.
- **Aucune Paresse** : Trouver les causes profondes. Aucun correctif temporaire. Standards de développeur senior.
- **Impact Minimal** : Les modifications ne doivent toucher que ce qui est nécessaire. Éviter d'introduire des bugs.
- Tous textes scientifiques et formules mathématiques devra être écrit en Latex ou avec mathjax pour les fichiers HTML
