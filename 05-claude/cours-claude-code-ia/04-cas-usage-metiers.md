# Module 4 — Cas d'Usage par Métier
## Applications concrètes dans l'industrie

> **Durée :** 3h  
> **Objectif :** Identifier et mettre en œuvre des workflows IA adaptés à son propre métier

---

## Introduction

Ce module est le cœur pratique de la formation. Chaque section présente des scénarios concrets pour un profil métier, avec des exemples de prompts réels et des workflows détaillés.

**Comment utiliser ce module :**
- Lisez la section de votre propre métier en détail
- Parcourez les autres sections pour comprendre comment vos collègues pourraient utiliser ces outils
- Les workflows intersecteurs (section 4.6) sont valables pour tous

---

## 4.1 Profil Administratif

### Contexte
Le travail administratif est caractérisé par la gestion de volumes importants de documents, la rédaction répétitive, la coordination d'informations entre services et la production de rapports récurrents.

### Cas d'usage 1 — Traitement du courrier entrant

**Situation :** Chaque matin, 20 à 50 emails et courriers arrivent et doivent être triés, priorisés et routés vers les bons interlocuteurs.

**Workflow avec Claude :**
```
CLAUDE.md du projet "Gestion courrier" :
──────────────────────────────────────
Tu es l'assistant administratif de la direction.
Pour chaque courrier reçu, tu dois :
1. Identifier l'expéditeur et la nature de la demande
2. Lui attribuer une priorité (URGENT / NORMAL / INFO)
3. Identifier le destinataire interne approprié
4. Rédiger un accusé de réception si nécessaire
5. Créer une entrée dans le tableau de suivi Excel

Règles :
- Les demandes impliquant des délais légaux sont toujours URGENT
- Les factures vont à la comptabilité
- Les réclamations clients vont au service qualité
```

**Prompt d'usage quotidien :**
> "Voici les 12 emails reçus ce matin [contenu joint]. Traite-les selon notre processus standard et génère le tableau de suivi du jour."

**Gain estimé :** 45 à 90 minutes par jour

---

### Cas d'usage 2 — Rédaction de comptes-rendus de réunion

**Situation :** Après chaque réunion de direction, il faut produire un compte-rendu structuré, identifier les décisions prises et les actions assignées.

**Prompt exemple :**
> "Voici les notes de la réunion de direction du [date] [notes en vrac jointes]. Rédige un compte-rendu au format de l'entreprise avec : résumé exécutif en 5 lignes, décisions prises, actions avec responsable et date limite. Utilise notre template habituel."

**Ressource utile :** Le dépôt [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) fournit des patterns de prompting pour des rédactions répétitives de qualité constante.

---

### Cas d'usage 3 — Génération de rapports récurrents

**Situation :** Chaque mois, consolidation de données de plusieurs services pour produire le rapport de gestion.

**Workflow multi-agents :**
```
Agent "Collecteur" → extrait les données des fichiers Excel des services
Agent "Vérificateur" → détecte les incohérences et valeurs manquantes
Agent "Consolidateur" → fusionne les données selon les règles comptables
Agent "Rédacteur" → génère le rapport Word avec commentaires
Agent "Alerteur" → identifie les points nécessitant une attention humaine
```

**CLAUDE.md pour ce projet :**
```markdown
# Rapport de Gestion Mensuel

## Sources de données
- /data/commercial/chiffre_affaires_[mois].xlsx
- /data/rh/effectifs_[mois].xlsx
- /data/production/indicateurs_[mois].xlsx

## Template de sortie
- /templates/rapport_gestion_template.docx

## Règles de consolidation
- Le CA est exprimé HT en euros
- Les effectifs incluent les intérimaires
- Les alertes : écart > 10% par rapport au mois précédent

## Destinataires
- Direction générale : direction@entreprise.fr
- DAF : daf@entreprise.fr
```

**Gain estimé :** 1 à 2 jours de travail par mois

---

### Cas d'usage 4 — Gestion documentaire et archivage

**Prompt exemple :**
> "Analyse les 847 documents du dossier /Archives/2024/ et propose un plan de classement selon notre nomenclature. Identifie les doublons, les documents périmés et ceux qui nécessitent une validation avant archivage définitif."

---

## 4.2 Profil Ingénieur

### Contexte
Les ingénieurs jonglent entre documentation technique, analyses, rapports de conception, revues de plans et coordination avec les équipes terrain. La précision et la traçabilité sont critiques.

### Cas d'usage 1 — Documentation technique automatisée

**Situation :** Chaque fois qu'un système ou process évolue, la documentation technique doit être mise à jour — une tâche chronophage souvent négligée.

**Workflow :**
```
CLAUDE.md du projet "Documentation technique" :
──────────────────────────────────────────────
Tu es un ingénieur documentaliste spécialisé dans notre domaine industriel.
Standards de documentation : ISO 17025 / IEC 62443
Langue : français technique
Format : Word selon template /templates/doc_technique_v3.docx
Niveau de détail : opérateurs (pas les concepteurs)
Inclure systématiquement : schémas de principe, gammes de paramètres, points de contrôle
```

**Prompt exemple :**
> "Voici le rapport de modification du système de refroidissement [PDF joint] et les anciennes procédures [fichiers joints]. Génère la documentation technique mise à jour pour les opérateurs. Identifie et liste les paramètres qui ont changé."

**Ressource utile :** Le skill `docx` permet de générer des documents Word formatés directement, sans copier-coller.

---

### Cas d'usage 2 — Analyse de défaillances (AMDEC / FMEA)

**Situation :** L'analyse AMDEC est essentielle mais chronophage. Elle requiert l'analyse systématique de chaque composant.

**Prompt exemple :**
> "À partir de la nomenclature du système [fichier joint] et des historiques de pannes [fichier joint], génère la première version de l'AMDEC selon la méthode IEC 60812. Pour chaque mode de défaillance, évalue la criticité (Gravité × Occurrence × Détection). Priorise les 10 défaillances les plus critiques."

**Valeur :** Ce qui prend 3 à 5 jours à un ingénieur peut être produit en quelques heures, puis révisé et validé par l'expert.

---

### Cas d'usage 3 — Revue de conception assistée

**Workflow inspiré du dépôt [superpowers](https://github.com/obra/superpowers) :**
```
Phase 1 - Spec : "Voici les exigences du cahier des charges [document]. Synthétise les 
             critères de validation de la conception."

Phase 2 - Plan : "Sur la base de ces critères, propose un plan de revue de conception 
             en 8 points. Identifie les points de risque."

Phase 3 - Review : "Voici les documents de conception [fichiers]. Évalue chaque 
               critère. Attribue un statut (OK / A clarifier / Non conforme) 
               avec justification."

Phase 4 - Synthèse : "Génère le rapport de revue avec les actions correctives 
               classées par priorité."
```

---

### Cas d'usage 4 — Veille technique automatisée

**Prompt pour mise en place :**
> "Mets en place une veille hebdomadaire sur les sujets suivants : [liste]. Chaque lundi, génère un bulletin de 1 page avec : les 5 actualités les plus pertinentes pour notre activité, les nouvelles normes ou réglementations, les évolutions technologiques à surveiller."

**Ressource :** Le dépôt [claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) est lui-même mis à jour par un tel système de veille automatisée.

---

## 4.3 Profil IT / Informatique

### Contexte
Les équipes IT gèrent à la fois la dimension technique (déploiement, sécurité, maintenance) et la dimension service (support, onboarding, documentation). L'IA peut accélérer les deux.

### Cas d'usage 1 — Revue de code et sécurité automatisée

**Basé sur [claude-code-action](https://github.com/anthropics/claude-code-action) :**

Chaque pull request GitHub reçoit automatiquement :
- Une revue des bonnes pratiques de code
- Une analyse des vulnérabilités de sécurité
- Des suggestions de correction avec code prêt à intégrer
- Une vérification de la conformité aux standards internes

**Configuration dans GitHub Actions :**
```yaml
# .github/workflows/claude-review.yml
name: Claude Code Review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

**Économie :** Moins de 5€/mois pour 50 pull requests — et une qualité de revue constante.

---

### Cas d'usage 2 — Documentation système automatisée

**Situation :** La documentation d'infrastructure est toujours en retard sur la réalité.

**Workflow :**
```
Agent "Auditeur" → analyse les configurations existantes
Agent "Documentariste" → génère les procédures d'exploitation
Agent "Vérificateur" → teste la procédure sur un environnement de staging
Agent "Diffuseur" → met à jour le wiki interne
```

**Prompt d'audit :**
> "Analyse cette configuration serveur [logs et configs joints] et génère : le schéma d'architecture, les procédures d'exploitation courantes, les points de surveillance critiques, les procédures de reprise après incident."

---

### Cas d'usage 3 — Déploiement d'agents pour d'autres équipes

**Rôle stratégique de l'IT :** Les équipes IT sont souvent en position de **déployeur d'IA** pour toute l'entreprise. Le dépôt [everything-claude-code](https://github.com/affaan-m/everything-claude-code) est la référence pour ce type de déploiement centralisé.

**Checklist de déploiement :**
```markdown
# Déploiement agent IA — Checklist IT

## Sécurité
[ ] Définir les permissions minimales (principe du moindre privilège)
[ ] Configurer les hooks de sécurité (validation avant action irréversible)
[ ] Mettre en place l'audit log de toutes les actions
[ ] Définir les données exclues de tout traitement par l'IA

## Configuration
[ ] CLAUDE.md adapté au contexte métier
[ ] Skills installés selon les besoins documentés
[ ] MCP configurés uniquement pour les outils nécessaires
[ ] Modèle approprié sélectionné (Haiku pour les tâches simples, Sonnet pour le quotidien, Opus pour l'analyse complexe)

## Formation
[ ] L'équipe utilisatrice a été formée
[ ] Procédure d'escalade définie si l'agent commet une erreur
[ ] Mécanisme de feedback utilisateur en place
```

---

### Cas d'usage 4 — Support niveau 1 automatisé

**Prompt de configuration d'agent support :**
```
Tu es l'assistant support IT de niveau 1.
Tu réponds aux questions courantes des utilisateurs.
Si tu ne peux pas résoudre le problème en moins de 3 étapes, 
tu escalades automatiquement vers le support niveau 2 en créant 
un ticket Jira avec : description complète, logs pertinents, 
étapes déjà tentées.
Tu ne tentes jamais d'accéder à des données utilisateurs sans 
confirmation explicite du manager IT.
```

---

## 4.4 Profil Ressources Humaines

### Contexte
Les RH gèrent des volumes importants de candidatures, produisent de nombreux documents normatifs et assurent le suivi de processus qui impliquent beaucoup de personnes.

### Cas d'usage 1 — Analyse de candidatures

**Situation :** Pour un poste, 150 candidatures arrivent. Lire et évaluer chacune prend des jours.

**CLAUDE.md pour ce projet :**
```markdown
# Analyse Candidatures — Technicien Qualité Industrie

## Critères obligatoires
- Diplôme : BTS/DUT Qualité ou équivalent minimum
- Expérience : 2 ans minimum en industrie de process
- Maîtrise : logiciels SPC, normes ISO 9001

## Critères différenciants (points positifs)
- Connaissance secteur automobile (+ 2 points)
- Expérience audit interne (+ 1 point)
- Anglais professionnel (+ 1 point)

## Format de sortie
- Score sur 10
- Points forts (max 3)
- Points d'attention
- Recommandation : ENTRETIEN / DOSSIER À REVOIR / REFUS

## Important
Ne jamais mentionner ni prendre en compte : âge, origine,
situation familiale ou tout autre critère non-professionnel.
```

**Prompt :**
> "Voici 25 CV [fichiers joints]. Analyse chacun selon nos critères. Produis un tableau de synthèse trié par score avec recommandation. Mets en évidence les profils exceptionnels."

**Gain estimé :** 2 à 4 heures sur 150 candidatures vs 2 jours

---

### Cas d'usage 2 — Création et mise à jour de fiches de poste

**Prompt exemple :**
> "Nous ouvrons un nouveau poste d'Ingénieur Process Senior. Notre entreprise est dans la fabrication de composants aéronautiques. Génère une fiche de poste conforme à nos standards RH [template joint], en intégrant : les missions principales définies en réunion [notes jointes], les compétences techniques requises, les compétences comportementales recherchées, la position dans l'organigramme. Adapte la formulation à notre secteur."

---

### Cas d'usage 3 — Onboarding automatisé

**Workflow d'onboarding :**
```
J-5 avant arrivée :
Agent "Admin" → génère le badge, accès informatiques, tickets IT
Agent "Logistique" → vérifie disponibilité bureau, équipements
Agent "Communication" → envoie email de bienvenue personnalisé

Jour J :
Agent "Guide" → prépare le programme d'intégration personnalisé
Agent "Formation" → génère le planning de formation des 30 premiers jours
Agent "Tuteur" → crée la liste des contacts clés avec présentation

J+30 :
Agent "Suivi" → prépare le questionnaire de bilan d'intégration
Agent "Synthèse" → analyse les retours et identifie les points d'amélioration
```

**Ressource utile :** Le dépôt [Claude-Code-Projects-Index](https://github.com/danielrosehill/Claude-Code-Projects-Index) contient des exemples d'automatisation RH dans de nombreux secteurs.

---

### Cas d'usage 4 — Analyse des entretiens annuels

**Prompt exemple :**
> "Voici les synthèses anonymisées de 48 entretiens annuels de l'équipe production [fichier]. Identifie : les tendances générales en termes de satisfaction, les besoins de formation récurrents, les risques de départ (signaux faibles), les points de satisfaction à valoriser. Génère un rapport anonymisé pour la direction avec recommandations."

---

## 4.5 Profil Formateur

### Contexte
Les formateurs créent des contenus, adaptent des parcours, évaluent les apprenants et gèrent la logistique pédagogique. L'IA peut accélérer et enrichir chacune de ces dimensions.

### Cas d'usage 1 — Création de contenu pédagogique

**Prompt de création de module :**
> "Je dois créer un module de formation de 3h sur 'La sécurité des données industrielles' pour des techniciens de maintenance (niveau bac, pas informaticiens). Génère : les objectifs pédagogiques en termes de compétences acquises, le plan détaillé avec timing, les 5 mises en situation pratiques adaptées à notre contexte usine, 20 questions QCM de validation, les points d'évaluation formative."

---

### Cas d'usage 2 — Adaptation des niveaux et profils

**Situation :** Le même contenu doit être adapté pour différents niveaux.

**Prompt :**
> "Voici mon module de formation sur [sujet] [contenu joint]. Adapte-le en trois versions : Version 1 : Opérateurs (pas de formation préalable, vocabulaire simplifié, focus sur le geste métier). Version 2 : Techniciens (niveau intermédiaire, inclure les 'pourquoi'). Version 3 : Ingénieurs (niveau expert, inclure les mécanismes et les choix de conception)."

---

### Cas d'usage 3 — Évaluation et feedback personnalisé

**Workflow :**
```
Agent "Correcteur" → évalue les productions des apprenants selon la grille
Agent "Analyseur" → identifie les erreurs récurrentes dans le groupe
Agent "Conseiller" → génère un feedback personnalisé pour chaque apprenant
Agent "Rapporteur" → produit le rapport de session pour le formateur
```

**CLAUDE.md pour ce projet :**
```markdown
# Évaluation Formation Sécurité Industrielle

## Grille d'évaluation
- Identification des risques (40%)
- Application des procédures (30%)
- Communication et signalement (30%)

## Règles de feedback
- Toujours commencer par un point positif
- Maximum 3 axes d'amélioration
- Proposer une ressource de remédiation pour chaque axe
- Ton encourageant mais précis

## Confidentialité
Les résultats individuels ne sont partagés qu'avec l'apprenant concerné.
Le rapport de groupe est anonymisé.
```

---

### Cas d'usage 4 — Mise à jour des formations réglementaires

**Situation :** Les réglementations évoluent et les formations doivent être mises à jour régulièrement.

**Prompt :**
> "Voici notre module de formation 'Habilitation électrique BR-B2' version 2022 [fichier] et le nouveau texte réglementaire NF C 18-510 mis à jour en 2024 [fichier]. Identifie tous les points qui nécessitent une mise à jour. Génère la liste des modifications avec le texte actuel et le texte proposé pour chaque point."

**Ressource :** Le dépôt [claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) est lui-même un exemple de documentation maintenue à jour automatiquement — un modèle pour les formateurs.

---

## 4.6 Cas d'usage intersectoriels

Ces workflows sont utiles à tous les profils.

### Recherche et synthèse documentaire

**Applicable à :** Tous métiers

**Prompt :**
> "Fais une synthèse de ces 8 rapports techniques [fichiers] sur le sujet de [X]. Pour chaque rapport, identifie les points clés, les données chiffrées et les recommandations. Synthétise ensuite les points de convergence et les divergences entre les sources. Produis un résumé exécutif de 2 pages."

---

### Préparation de réunions

**Applicable à :** Tous métiers

**Workflow :**
```
La veille :
Agent → analyse l'ordre du jour + documents préparatoires
Agent → identifie les décisions à prendre et les informations nécessaires
Agent → génère un briefing d'une page avec questions clés

Pendant la réunion :
Agent → prend des notes structurées (si interface disponible)

Après :
Agent → génère le compte-rendu
Agent → crée les tâches dans l'outil de gestion de projet
Agent → envoie les actions assignées aux responsables
```

---

### Gestion de projet transversale

**Basé sur le workflow du dépôt [get-shit-done](https://github.com/gsd-build/get-shit-done) :**

```
Étape 1 - Discussion : Cadrer le projet avec l'agent
Étape 2 - Planning : L'agent décompose en tâches avec responsables
Étape 3 - Exécution : L'agent produit les livrables par étape
Étape 4 - Vérification : L'agent contrôle chaque livrable
Étape 5 - Livraison : L'agent consolide et distribue
```

**Point clé :** Chaque étape a des critères clairs pour passer à la suivante. Cela évite la dérive de scope et le travail refait.

---

## 4.7 Les limites à connaître

### Ce que Claude fait bien
- Rédaction, synthèse, structuration de l'information
- Analyse de documents et extraction de données
- Génération de premières versions (jamais parfaites mais toujours utilisables)
- Tâches répétitives avec des patterns clairs
- Traduction et adaptation de niveau

### Ce que Claude fait moins bien
- Juger de l'opportunité stratégique (le "oui ou non" final reste humain)
- Accéder aux systèmes internes sans connexion MCP explicite
- Garantir l'exactitude des données chiffrées sans source (toujours vérifier)
- Remplacer l'expertise métier rare et pointue

### La règle d'or
> **L'IA produit, l'humain valide.** Pour toute décision à enjeu (réglementaire, financier, humain), la validation humaine est non négociable.

---

## Points clés à retenir

- Chaque métier a des tâches hautement automatisables avec un ROI immédiat
- La clé du succès est un CLAUDE.md bien rédigé qui capture les règles métier
- Les workflows multi-agents permettent de traiter des volumes impossibles manuellement
- La validation humaine reste essentielle sur les décisions à enjeu
- Commencer par une tâche simple et reproductible pour prendre confiance

---

## Atelier pratique (45 minutes)

**Exercice individuel :**
1. Identifiez la tâche la plus chronophage et répétitive de votre semaine
2. Rédigez un CLAUDE.md de 10 lignes pour cette tâche (contexte, règles, format de sortie)
3. Formulez le prompt de base pour déclencher le workflow
4. Partagez avec le groupe pour retours et enrichissements

---

*Module précédent : [← Les 15 ressources GitHub](03-ressources-github.md) | Prochain module : [Méthodologies →](05-methodologies-pratiques.md)*
