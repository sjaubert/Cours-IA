# Activité A6 : Challenge - Diagnostic d'une Panne Intermittente

## Contexte

Sur une ligne de conditionnement de bouteilles, le convoyeur principal s'arrête de manière aléatoire plusieurs fois par jour. L'écran de contrôle affiche une erreur "Overload Moteur M2", mais le moteur n'est ni chaud ni bloqué mécaniquement lorsque le technicien arrive. Le problème est non reproductible sur commande.

## Objectifs

Utiliser l'IA (Antigravity ou Gemini Chat) pour :

1. **Analyser les logs d'erreurs** pour identifier des motifs (fréquence, horaires, événements corrélés).
2. **Formuler des hypothèses** de causes racines en croisant les logs avec l'extrait de documentation technique.
3. **Proposer un protocole de test** précis pour valider la cause sans démonter inutilement l'installation.
4. **Rédiger une fiche de diagnostic** et une procédure de remise en service.

## Ressources disponibles (dans le dossier `data/`)

- `logs_convoyeur.csv` : Historique des arrêts, intensités mesurées et états des capteurs de présence.
- `doc_moteur_extrait.txt` : Spécifications techniques du moteur M2 et du variateur associé.

## Consignes pour le Prompting

- Appliquez la méthode **ROLE/CTCF** (voir note de synthèse).
- Soyez précis sur le **Format** attendu pour votre fiche de diagnostic.
- Challengez l'IA sur l'aspect "Intermittent" : Est-ce un problème électrique (parasites), mécanique (point dur furtif) ou de paramétrage variateur ?

## Livrables attendus

1. **Fiche de diagnostic** (tableau des causes/probabilités).
2. **Protocole de test** (étapes de vérification).
3. **Procédure de remise en service** sécurisée.
