# Fiche apprenant — Workflows avancés Claude Code

**Maîtriser le contexte comme une ressource**
Pôle Formation UIMM-CVDL | Niveau Avancé | Demi-journée

---

## Avant de commencer

Ouvrez un terminal dans le dossier `ressources/projet-fil-rouge/`. C'est votre bac à
sable pour toute la séance. Vérifiez que `git`, `jq` et Claude Code répondent :

```bash
git --version && jq --version && claude --version
```

Initialisez un dépôt git dans le projet fil rouge (nécessaire pour l'exercice 8) :

```bash
cd ressources/projet-fil-rouge
git init && git add -A && git commit -m "Etat initial du TP"
```

Fil conducteur de tous les exercices : un dépôt de maintenance industrielle (données
GMAO, relevés capteurs de la presse PH-200, procédures d'intervention).

---

## Exercice 1 — Une règle qui ne se discute pas : le hook (30 min)

**Idée.** `CLAUDE.md` est un conseil que Claude interprète. Un hook est déterministe :
il se déclenche à chaque appel d'outil correspondant, sans exception. Tout ce qui ne doit
**jamais** arriver appartient à un hook.

**Cas industriel.** Les exports GMAO bruts et les fichiers de configuration automate ne
doivent jamais être modifiés par l'agent. On le garantit par un hook `PreToolUse` qui
bloque l'écriture (code de sortie `2`).

**À faire.**

1. Ouvrez `.claude/settings.json` et `scripts/block-sensitive-writes.sh`. Repérez la ligne
   `exit 2` : c'est elle qui bloque l'action.
2. Lancez Claude Code dans le projet. Demandez :
   > Crée un fichier `data/gmao_brut/test.csv` avec une ligne d'en-tête.
3. Observez : l'écriture est refusée par le hook. Notez le message affiché.
4. Demandez maintenant la création de `docs/note.md` : l'écriture passe.

**Question.** Pourquoi cette garantie ne pourrait-elle pas être obtenue de façon fiable
avec une simple consigne dans `CLAUDE.md` ?

**Livrable.** Une capture ou une note décrivant les deux comportements observés.

---

## Exercice 2 — Dégraisser le CLAUDE.md (25 min)

**Idée.** Chaque token de `CLAUDE.md` est chargé à chaque session et entre en concurrence
avec votre tâche réelle. Règle simple : si une directive n'a pas modifié le comportement
de Claude cette semaine, elle ne mérite pas le `CLAUDE.md`. Le contexte profond va dans des
fichiers compagnons (`memory/`) que l'on référence à la demande.

**À faire.**

1. Lisez `CLAUDE.md` (volontairement trop long) et `memory/conventions-doc-technique.md` /
   `memory/regles-securite.md` (déjà extraits pour vous).
2. Réécrivez `CLAUDE.md` pour qu'il tienne sur **une page écran**. Conservez uniquement ce
   qui guide Claude au quotidien ; remplacez le reste par des renvois du type
   `voir memory/regles-securite.md`.
3. Repérez le bloc qui fait **doublon** avec le Skill `procedures-securite` : supprimez-le
   du `CLAUDE.md`.

**Question.** Quels blocs avez-vous supprimés, et pourquoi ne servaient-ils pas Claude
à chaque session ?

**Livrable.** Le `CLAUDE.md` raccourci.

---

## Exercice 3 — Isoler une exploration dans un sous-agent (30 min)

**Idée.** Quand vous explorez un module inconnu dans votre session principale, chaque
impasse s'accumule dans le contexte et finit par dégrader la suite. Un sous-agent explore
dans **son propre** contexte et ne vous renvoie que la synthèse : la pollution ne remonte pas.

**Cas industriel.** Vous devez intervenir sur les scripts d'analyse GMAO que vous ne
connaissez pas.

**À faire.**

1. Ouvrez `.claude/agents/explorateur.md` : notez `tools: Read, Glob, Grep` (lecture seule)
   et `model: sonnet` (suffisant et économique pour de l'exploration).
2. Dans Claude Code :
   > Utilise le sous-agent explorateur pour analyser le dossier `data/` et le dossier
   > `docs/`, et résume-moi leur structure et les formats de données.
3. Récupérez la synthèse. Constatez que votre session principale n'a pas été encombrée
   par la lecture détaillée des fichiers.

**Question.** En quoi `tools: Read, Glob, Grep` est-il un choix de sécurité autant qu'un
choix de performance ?

**Livrable.** La synthèse produite par l'explorateur.

---

## Exercice 4 — Spécifier, puis implémenter : deux sessions (30 min)

**Idée.** Mener la spécification et l'implémentation dans la même session produit du code
à reprendre : au moment d'écrire, le contexte est saturé d'idées à demi formées. La parade :
deux sessions distinctes.

**Cas industriel.** Écrire un script de détection d'anomalies sur le relevé capteurs de
la presse PH-200.

**À faire.**

1. **Session 1 (spécification).** Demandez à Claude de produire UN document de spécification
   (objectif, entrée, sortie, règle de détection, cas limites, hors-périmètre) à partir de
   `data/releve_capteurs.csv`. Comparez votre résultat au modèle fourni :
   `docs/spec_analyse_anomalies.md`.
2. Fermez la session (ou `/clear`).
3. **Session 2 (implémentation).** Démarrez **propre**. Donnez la spec comme seule entrée :
   > Implémente le script décrit dans `@docs/spec_analyse_anomalies.md`. Ne fais que ce
   > que la spec demande.

**Piège volontaire à corriger.** Le tutoriel source propose de lancer la session 2 avec
`claude --context spec.md`. **Ce drapeau n'existe pas.** Vérifiez-le avec `claude --help`,
puis utilisez la bonne méthode : référencer le fichier dans le prompt avec `@chemin`.

**Livrable.** La spec + le script, et une phrase expliquant ce que `claude --help` confirme.

---

## Exercice 5 — /compact et /clear comme outils de précision (20 min)

**Idée.** `/compact` accepte des **instructions** : vous dictez ce qu'il faut préserver et
ce qu'il faut jeter. `/clear` réinitialise tout. Deux échecs d'affilée sur le même problème
sont le signal d'un `/clear`, pas d'une troisième reformulation.

**À faire.**

1. Dans une session un peu chargée, lancez un compactage dirigé :
   > /compact conserve toutes les décisions sur la règle de détection et leurs raisons,
   > garde chaque message d'erreur et sa solution, liste les fichiers modifiés, résume les
   > pistes abandonnées en une ligne chacune.
2. Ajoutez une politique de compactage permanente dans `CLAUDE.md` (section
   « Instructions de compactage » déjà amorcée) pour que les compactages automatiques
   suivent les mêmes règles.

**Piège volontaire à corriger.** Le tutoriel mentionne une commande `/caveman-compress`
qui réduirait les tokens de 46 %. **Elle n'est pas native.** Le bon levier est `/compact`
avec instructions.

**Livrable.** La section « Instructions de compactage » rédigée dans `CLAUDE.md`.

---

## Exercice 6 — Encoder une convention métier dans un Skill (25 min)

**Idée.** Un Skill ne charge ses instructions complètes que lorsque Claude détecte un
contexte correspondant (au démarrage, il ne lit que le nom et la description). C'est l'endroit
idéal pour vos conventions : des choses que Claude sait faire, mais doit faire **à votre manière**.

**Cas industriel.** Toute procédure d'intervention doit suivre la structure maison en cinq
rubriques (pré-requis, consignation, mode opératoire, vérification, remise en service).

**À faire.**

1. Lisez `.claude/skills/procedures-securite/SKILL.md`. Repérez le champ `description` : c'est
   la **règle de routage** qui décide quand le Skill se déclenche.
2. Demandez à Claude :
   > Rédige la procédure de remplacement du flexible hydraulique de la presse PH-200.
3. Vérifiez que la sortie respecte les cinq rubriques et la règle « une étape = une action ».
4. Modifiez la `description` du Skill pour qu'elle décrive plus précisément le contexte de
   déclenchement, et observez l'effet.

**Livrable.** La procédure générée + la `description` améliorée.

---

## Exercice 7 — Migration en éventail (fan-out) (30 min)

**Idée.** Migrer beaucoup de fichiers dans une seule longue session est lent et peu fiable :
le contexte se sature, la qualité dérive. La parade : régler le patron sur 2-3 fichiers
représentatifs, puis **fan-out** vers le reste via des sous-agents en parallèle.

**Cas industriel.** Migrer les anciennes procédures de `docs/anciennes/` vers le patron
`docs/procedure_template.md`, sans toucher au fond technique (valeurs, références).

**À faire.**

1. **Phase de réglage.** Sur un seul fichier (`docs/anciennes/proc_remplacement_flexible_PH200.md`),
   demandez la transformation vers le template et validez le diff.
2. **Phase d'exécution.** Une fois le patron jugé bon, lancez le sous-agent `migrateur`
   sur le dossier :
   > Utilise le sous-agent migrateur pour appliquer le patron de
   > `docs/procedure_template.md` à tous les fichiers de `docs/anciennes/`.
3. Vérifiez que les valeurs techniques (45 N.m, 7 bar...) sont **inchangées**.

**Question.** Pourquoi régler le patron AVANT de fan-out change-t-il la fiabilité du résultat ?

**Livrable.** Les procédures migrées + une vérification que le fond n'a pas bougé.

---

## Exercice 8 — Rédacteur / relecteur via git worktree (25 min)

**Idée.** Deux sessions Claude sur le même dossier se marchent dessus. `git worktree` donne
à chaque session son propre chemin physique pointant vers le même dépôt : plus de conflit.
Le binôme rédacteur / relecteur est l'usage le plus utile — le relecteur juge sans connaître
les décisions prises, donc plus objectivement.

**À faire.**

1. Créez un worktree de revue :
   ```bash
   git worktree add ../projet-revue HEAD
   ```
2. **Session rédacteur** (dossier d'origine) : finalisez une procédure d'intervention.
3. **Session relecteur** (dossier `../projet-revue`) : lancez le sous-agent `relecteur`
   pour produire une liste d'observations classées par criticité.
4. Nettoyez :
   ```bash
   git worktree remove ../projet-revue
   ```

**Livrable.** La liste d'observations du relecteur.

---

## Synthèse — l'esprit critique du formateur (15 min)

Vous avez corrigé deux commandes inexactes du tutoriel source (`claude --context` et
`/caveman-compress`). Formalisez la règle que vous en tirez : **toute commande est vérifiée
contre la documentation officielle avant d'être enseignée.**

Documentation de référence : `https://code.claude.com/docs` (hooks, sous-agents, `/compact`).

**Discussion finale.** Les neuf techniques répondent à une seule question : comment garder
le contexte propre et dense ? Reformulez chacune en une phrase sous cet angle.
