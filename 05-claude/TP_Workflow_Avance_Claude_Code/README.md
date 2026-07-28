# TP — Workflows avancés Claude Code : maîtriser le contexte

**Section 5 — Claude Code & Agents IA** | Niveau : Avancé | Durée : demi-journée (3 h 30)
Pôle Formation UIMM-CVDL — S. Jaubert

---

## Positionnement dans la formation

Ce TP complète la section 5 (Masterclass Claude Code, formations Skills, Hooks, Cowork).
Il suppose acquis : usage courant de Claude Code, notion de `CLAUDE.md`, premières
manipulations de Skills et de Hooks. Il ne réexplique pas ces briques : il apprend à les
**combiner** au service d'une idée directrice unique.

## Idée directrice

Le fil rouge de ce TP est une seule notion : **le contexte est une ressource**. Comme
toute ressource, il se remplit, se sature, se pollue, se compresse et se réinitialise.
Les neuf techniques travaillées ici sont toutes des manières de gérer cette ressource
de façon délibérée plutôt que subie.

Le TP s'appuie sur un tutoriel anglophone diffusé en ligne (« stop wasting time on slow
Claude Code workflows »). Ce tutoriel est pédagogiquement utile mais contient **deux
inexactitudes techniques**. Les corriger fait partie des objectifs : un formateur ne
transmet pas une commande sans l'avoir vérifiée.

## Objectifs pédagogiques

À l'issue du TP, l'apprenant est capable de :

1. placer une règle non négociable dans un **hook** plutôt que dans `CLAUDE.md` ;
2. dégraisser un `CLAUDE.md` et externaliser le contexte profond dans des fichiers compagnons ;
3. utiliser un **sous-agent** pour isoler le contexte d'une exploration ;
4. séparer une session de **spécification** d'une session d'**implémentation** ;
5. piloter `/compact` et `/clear` comme des outils de précision ;
6. encoder une convention métier dans un **Skill** ;
7. conduire une **migration en éventail** (fan-out) fiable ;
8. faire tourner deux sessions en parallèle via **git worktree** (rédacteur / relecteur) ;
9. **vérifier** une commande contre la documentation officielle avant de l'enseigner.

## Public et ancrage

Profils techniques : maintenance, méthodes, documentation technique, qualité. Tous les
exemples sont ancrés dans un cas industriel (données GMAO, relevés capteurs, procédures
d'intervention). Aucune compétence de développement applicatif n'est requise, mais l'aisance
avec un terminal et la notion de dépôt git sont nécessaires.

## Prérequis matériel

- Claude Code installé et fonctionnel (accès vérifié en amont).
- `git` installé ; `jq` installé (utilisé par les scripts de hook).
- Le projet fil rouge fourni : `ressources/projet-fil-rouge/`.

## Déroulé (3 h 30)

| Bloc | Technique(s) | Durée |
|---|---|---|
| Introduction — le contexte comme ressource | cadrage | 15 min |
| Exercice 1 — Hooks vs CLAUDE.md | hooks déterministes | 30 min |
| Exercice 2 — Dégraisser CLAUDE.md | mémoire à la demande | 25 min |
| Exercice 3 — Sous-agent explorateur | isolation de contexte | 30 min |
| Pause | | 10 min |
| Exercice 4 — Spécification puis implémentation | sessions séparées | 30 min |
| Exercice 5 — Piloter /compact et /clear | compression dirigée | 20 min |
| Exercice 6 — Skill de convention métier | préférences encodées | 25 min |
| Exercice 7 — Migration fan-out | tuning puis exécution | 30 min |
| Exercice 8 — git worktree rédacteur / relecteur | parallélisme sans conflit | 25 min |
| Synthèse — esprit critique sur le tutoriel source | vérification | 15 min |

Le bloc git worktree (exercice 8) peut être présenté en démonstration si le temps manque.

## Contenu du dossier

```
TP_Workflow_Avance_Claude_Code/
  README.md                      Ce document (vue d'ensemble formateur + apprenant)
  fiche_apprenant.md             Énoncés des 8 exercices, à distribuer
  guide_formateur.md             Minutage, corrigés, points de vigilance
  ressources/
    projet-fil-rouge/            Mini-dépôt à manipuler pendant le TP
      CLAUDE.md                  Volontairement trop long (exercice 2)
      .claude/
        settings.json            Hooks pré-configurés (exercice 1)
        agents/                  explorateur, migrateur, relecteur (exercices 3, 7, 8)
        skills/procedures-securite/SKILL.md   (exercice 6)
      memory/                    Fichiers compagnons cible (exercice 2)
      scripts/                   block-sensitive-writes.sh, valider_procedure.sh
      docs/                      Spec, template, anciennes procédures à migrer
      data/                      Échantillons GMAO et relevé capteurs
```

## Note d'honnêteté intellectuelle

Deux commandes du tutoriel source n'existent pas dans Claude Code et sont corrigées
dans ce TP (détail dans le guide formateur, exercices 4 et 9) :

- `claude --context spec.md` — ce drapeau n'existe pas ; on référence le fichier
  dans le prompt (par exemple `@docs/spec_analyse_anomalies.md`).
- `/caveman-compress` — cette commande n'est pas native ; le bon levier est `/compact`
  avec des instructions explicites.

*Dernière mise à jour : juin 2026.*
