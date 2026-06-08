# Guide formateur — Workflows avancés Claude Code

**Maîtriser le contexte comme une ressource**
Pôle Formation UIMM-CVDL | Niveau Avancé | Demi-journée (3 h 30)

---

## Intention pédagogique

Le TP ne vise pas à empiler neuf astuces, mais à faire émerger **un principe unique** :
le contexte est une ressource finie qui se pollue, se compresse et se réinitialise. Chaque
exercice est un cas particulier de gestion de cette ressource. En clôture, l'apprenant doit
pouvoir reformuler les neuf techniques sous ce seul angle.

Second objectif, transversal et propre à un public de formateurs : **l'esprit critique sur
les sources**. Le tutoriel d'origine contient deux commandes inexistantes. Les faire repérer
et corriger par les apprenants ancre une règle professionnelle : on ne transmet pas une
commande sans l'avoir vérifiée. Ce fil rejoint la démarche « esprit critique » déjà présente
dans la formation (sections 1 et 6).

## Préparation matérielle (à vérifier la veille)

- Claude Code installé et connecté sur chaque poste.
- `git` et `jq` installés (`jq` est indispensable aux scripts de hook).
- Le dossier `ressources/projet-fil-rouge/` copié en local sur chaque poste, **hors** dépôt
  git de la formation (les apprenants vont y faire `git init`).
- Sur Windows, les scripts `.sh` supposent un shell type Git Bash ou WSL. Le prévoir, ou
  faire l'exercice 1 en démonstration sur un poste de référence.

## Minutage détaillé

| Séquence | Durée | Animation |
|---|---|---|
| Introduction : le contexte comme ressource | 15 min | Exposé + schéma au tableau |
| Ex. 1 — Hooks vs CLAUDE.md | 30 min | Manipulation individuelle |
| Ex. 2 — Dégraisser CLAUDE.md | 25 min | Manipulation + mise en commun |
| Ex. 3 — Sous-agent explorateur | 30 min | Manipulation individuelle |
| Pause | 10 min | |
| Ex. 4 — Spec puis implémentation | 30 min | Manipulation + correction du piège |
| Ex. 5 — /compact et /clear | 20 min | Manipulation + démonstration |
| Ex. 6 — Skill de convention | 25 min | Manipulation individuelle |
| Ex. 7 — Migration fan-out | 30 min | Manipulation guidée |
| Ex. 8 — git worktree | 25 min | Démonstration ou binômes |
| Synthèse + esprit critique | 15 min | Discussion collective |

Total : 3 h 35 pause comprise. Variable d'ajustement : l'exercice 8 (git worktree) passe
en démonstration si le groupe a pris du retard.

## Corrigés et points de vigilance par exercice

### Exercice 1 — Hooks vs CLAUDE.md

Réponse attendue à la question : une consigne `CLAUDE.md` est **interprétée** ; Claude peut
décider qu'une situation justifie de s'en écarter. Un hook `PreToolUse` qui sort en code `2`
**bloque** l'appel d'outil de façon déterministe, indépendamment du raisonnement du modèle —
y compris en mode permissions assouplies. C'est ce qu'on veut pour une donnée sensible.

Points de vigilance :
- Le code de sortie qui bloque est **2** (pas 1 : un code 1 est une erreur non bloquante).
- `block-sensitive-writes.sh` lit l'entrée JSON sur stdin et extrait `tool_input.file_path`
  via `jq`. Si `jq` manque, le hook échoue : le vérifier avant la séance.
- Frontière à faire verbaliser : règle absolue -> hook ; jugement situationnel (conventions
  de nommage, style d'API) -> `CLAUDE.md`.

### Exercice 2 — Dégraisser CLAUDE.md

Blocs à supprimer ou externaliser dans le `CLAUDE.md` fourni :
- « Historique détaillé des versions » -> `memory/conventions-doc-technique.md`.
- « Liste exhaustive des équipements » -> `memory/regles-securite.md`.
- « Conventions de rédaction des procédures » -> **doublon** du Skill `procedures-securite`,
  à supprimer purement.
- « Procédure de déploiement des rapports » -> peu utile au quotidien, externaliser.

Conserver : présentation courte du projet, renvois `voir memory/...`, conventions Python
réellement actives, amorce de la section « Instructions de compactage ».

Critère de réussite : le `CLAUDE.md` final tient sur une page écran et ne contient plus de
contenu dupliqué avec les Skills ou les fichiers compagnons.

### Exercice 3 — Sous-agent explorateur

Réponse attendue : `tools: Read, Glob, Grep` interdit toute écriture, donc l'explorateur ne
peut rien casser ni modifier (sécurité), et son contexte d'exploration reste dans sa propre
fenêtre, sans polluer la session principale (performance). Double bénéfice.

Point de vigilance : insister sur le fait que le gain principal n'est pas la parallélisation
mais **l'isolation**. C'est le contresens le plus fréquent sur les sous-agents.

### Exercice 4 — Spécification puis implémentation

Correction du piège : le tutoriel propose `claude --context spec.md`. **Ce drapeau n'existe
pas.** Faire exécuter `claude --help` aux apprenants pour le constater. La bonne méthode :
démarrer une session propre et référencer le fichier dans le prompt (`@docs/spec_analyse_anomalies.md`),
ou en coller le contenu.

Critère de réussite : le script produit en session 2 traite bien les trois cas limites de la
spec (trous de mesure signalés, pressions négatives écartées et comptées, première fenêtre
de 24 h sur seuils durs seulement).

### Exercice 5 — /compact et /clear

`/compact` accepte bien des instructions en argument : c'est documenté et réel. La politique
de compactage dans `CLAUDE.md` est reprise à chaque compactage automatique.

Correction du second piège : `/caveman-compress` et le chiffre « -46 % » ne correspondent à
aucune commande native. Le levier réel est `/compact` avec instructions. Faire le lien avec
la règle de vérification.

Message clé sur `/clear` : deux échecs d'affilée = contexte ancré sur une hypothèse fausse ;
reformuler une troisième fois coûte plus cher que repartir propre.

### Exercice 6 — Skill de convention

Faits à valider auprès du groupe : au démarrage, Claude ne lit que `name` et `description`
de chaque Skill ; les instructions complètes ne se chargent que sur correspondance. Le champ
`description` est donc une **règle de routage** : plus il décrit précisément le contexte de
déclenchement, plus le routage est fiable.

Distinction à faire passer : Skill de « montée en capacité » (capacité que Claude n'a pas
seul) vs Skill de « préférence encodée » (façon de faire maison). Celui du TP relève de la
seconde catégorie.

### Exercice 7 — Migration fan-out

Réponse attendue : régler le patron sur un échantillon garantit que chaque agent parallèle
reçoit une transformation **déjà vérifiée**. Sans cela, on parallélise une erreur. Le contrôle
décisif est que le fond technique (45 N.m +/- 2, 7 bar) reste intact : la migration est
structurelle, pas éditoriale.

Point de vigilance : rappeler que le sous-agent `migrateur` a accès en écriture
(`Write, Edit, Bash`) — d'où l'importance d'avoir validé le patron avant de le lâcher.

### Exercice 8 — git worktree

Pré-requis : le `git init` initial de la fiche apprenant doit être fait, sinon `git worktree`
échoue. Le vérifier en début de séquence.

Message clé : le relecteur (depuis le worktree) n'a pas le contexte des décisions de
rédaction, ce qui rend sa critique plus objective qu'une auto-relecture dans la même session.
C'est l'application concrète de l'isolation de contexte vue à l'exercice 3.

## Synthèse attendue en clôture

Faire produire au groupe une reformulation des neuf techniques sous l'angle « gestion du
contexte » :

1. Hook — sortir une règle absolue du champ interprétable du contexte.
2. CLAUDE.md court — ne charger que le contexte réellement actif.
3. Sous-agent — confiner un contexte d'exploration ailleurs.
4. Spec / implémentation — repartir d'un contexte propre pour écrire.
5. /compact, /clear — compresser à dessein, ou réinitialiser.
6. Skill — charger une convention seulement quand le contexte l'appelle.
7. Fan-out — éviter de saturer un seul contexte sur un gros volume.
8. git worktree — donner à chaque contexte son espace physique.
9. Vérification — ne pas polluer son enseignement avec une source non vérifiée.

## Erreurs fréquentes à anticiper

- `jq` absent : les hooks échouent silencieusement. Tester avant la séance.
- Scripts `.sh` non exécutables : `chmod +x scripts/*.sh`.
- Oubli du `git init` avant l'exercice 8.
- Confusion sous-agent / parallélisme : recentrer sur l'isolation.
- Apprenants qui recopient `claude --context` ou `/caveman-compress` sans vérifier : c'est
  précisément le réflexe que le TP cherche à corriger.

## Prolongements possibles

- Ajouter un hook `Stop` ou `SessionStart` pour automatiser un rappel de convention.
- Construire un Skill de « montée en capacité » (génération de PDF de procédure) pour
  illustrer la seconde catégorie de Skills.
- Articuler ce TP avec la Masterclass Claude Code et la formation Hooks de la section 5.

*Dernière mise à jour : juin 2026.*
