![Logo UIMM](../../../logo_uimm_placeholder.jpg)
**Pôle Formation UIMM - CVDL | Formateur : S. JAUBERT**

# Guide de l'Apprenant : Maîtriser l'IA avec les "Skills" Personnalisés

Bienvenue dans votre manuel pratique pour transformer l'intelligence artificielle en un veritable collegue augmente, adapte a l'ensemble des metiers et des methodes de votre entreprise. 

---

## 1. Comprendre l'Outil (Pourquoi utiliser des Skills ?)

Aujourd'hui, si vous demandez a Claude de generer un "Tableau de synthese de fin de mois", il ignorera quelles sont vos colonnes prioritaires, votre style ou la longueur habituelle du document. Le resultat : **Beaucoup de temps perdu a le corriger**. 

### Qu'est ce qu'un Skill ?
Un "Skill" (competence) est une **boite a outils memoire**. C'est un simple dossier contenant :
- Les instructions (Le fameux `SKILL.md`).
- Des modeles d'exemples et des documents de references (ex. vos chartes graphiques).
- Eventuellement, des scripts pour nettoyer la donnee avant (pour garantir que la tache est parfaitement accomplit sans "creation d'information" par l'IA).

**L'avantage majeur :** Le systeme ne charge votre guide de style ou votre logique de bilan que lorsqu'il en a besoin ! Cela evite l'engorgement mental de l'IA.

---

## 2. Comment invoquer un Skill ? (Syntaxe et Bonnes Pratiques)

Il n'y a rien a coder ! L'installation place les fichiers sur votre poste, vous n'avez plus qu'a **"appeler"** le skill dans votre conversation via le signe `@` depuis le terminal, Cursor ou l'interface compatible que vous utilisez. 

### Exemple de syntaxe a eviter / a utiliser :
- **A eviter** : *Aide moi a evaluer ces bilans d'entretiens.* (L'IA improvisera).
- **A utiliser** : *Utilise `@hr-pro` pour m'aider a evaluer ces bilans selon notre regle d'evaluation annuelle.* (L'IA chargera la methode precise).

### La Magie : La Composabilite
Contrairement aux prompts classiques, vous pouvez appeler **plusieurs Skills a la fois**.
Exemple : 
> *Analyse les resultats du sondage client. Utilise `@data-analyst` pour extraire les metrics, puis `@seo-content-writer` et `@brand-guidelines` pour rediger le bilan marketing a la direction.*

---

## 3. Livres de Recettes : Cas Pratiques par Metiers

Ce catalogue vous presente des exemples de situations courantes, avec l'approche traditionnelle contre de l'utilisation d'un *Skill*.

### A. Administration et Ressources Humaines
**Douleur frequente :** Rediger les offres ou trier des donnees massives RH basees sur un referentiel metier ou fiche de poste de l'entreprise.
- **La solution "Skill"** : En utilisant `@hr-pro` associe a un template propre a l'entreprise. 
- **Prompt Actionnable :** 
  > *Examine ce CV et utilise `@hr-pro` pour me dire si les competences du candidat repondent aux 4 criteres stricts de notre fiche referentiel Ingenieur Qualite. Liste les ecarts (Gaps) potentiels.*
- **Le Resultat :** Un tableau d'analyse qui filtre les informations inutiles, se basant uniquement sur la "jurisprudence" enseignee au skill.

### B. Management et Planification
**Douleur frequente :** Organiser un projet ou repartir des taches sur un cahier des charges long, ou chaque participant a des contraintes.
- **La solution "Skill"** : Utiliser `@brainstorming` (pour definir exactement vos limites avant de generer le plan) puis `@concise-planning`.
- **Prompt Actionnable :** 
  > *Voici un mail decrivant notre projet "Innovation Q4". Ne redige pas de plan pour le moment. Utilise `@brainstorming` pour me poser une question a la fois afin que nous couvrions toutes mes contraintes de timing. Ensuite, on utilisera `@concise-planning`.*
- **Le Resultat :** Un gestionnaire de projet AI qui ne court-circuite pas votre prise de decision manageriale en proposant "trop vite" une reponse inadaptee.

### C. Ingenierie et Developpement
**Douleur frequente :** Demander a l'IA de faire une passe ou une revision de procedure sur de la documentation ou un code sans maitriser les standards en interne.
- **La solution "Skill"** : Demander la generation d'un checklist prealable via un skill metier comme `@systematic-debugging`.
- **Prompt Actionnable :** 
  > *Voici le rapport d'incident reseau (Log 2A49). Utilise le skill `@systematic-debugging` pour isoler le goulot d'etranglement. N'aborde que les defaillances materielles.*
- **Le Resultat :** L'AI ne proposera pas de revoir la gestion du reseau globale, elle va s'appliquer a isoler le blocage selon un protocole strict.

### D. Departement Formation (Pedagogie)
**Douleur frequente :** Assurer la creation de guides ou de supports de cours qui conservent les dernieres consignes legales / RNCP ("Institutional Memory"). 
- **La solution "Skill"** : Regrouper dans un skill toutes les methodes d'evaluation et le vocabulaire lie au module vise (Exemple : "De-silotage journalier" ou "Ingenierie Pedagogique ATI"). L'utilisation de ce skill (`@formation-ati`) forcera les regles a tout support d'examen genere. 

---

## 4. "Skill-Creator" : Creer votre propre Skill !

La veritable force de l'outil, c'est **vous** qui allez la concevoir. 
Que vous utilisiez `antigravity-awesome-skills` ou l'API de base, le composant integré (souvent appele `@skill-creator` ou equivalent) ecoute votre methode pour la "sauvegarder".

**Mode d'emploi en 4 etapes :**
1. **Ouvrez un chat** et dites : *Je souhaite creer un Skill dedie a la validation des notes de frais selon le bareme Urssaf et nos conditions internes.*
2. **Fournissez vos references** (PDF, fichiers de tableaux precedents en exemples).
3. **Repondez aux questions** que l'assistant pose sur "Quels sont les criteres de bon sens pour un humain qui fera la meme chose ?".
4. **Acceptez le fichier .zip genere** contenant votre fichier `SKILL.md` ou demandez a ce qu'il s'enregistre de lui meme.

**Alerte** : Verifiez de maniere tres agressive que les "Scripts" integres dans ces skills sur internet sont de confiance. L'acces au disque ou au code d'entreprise doit etre restreint (Sandbox) pour empecher des fuites ou erreurs fatales lors de modifications (Suppression de donnees involontaires).

---

> *L'Intelligence artificielle, seule, est une memoire vive puissante mais sans trace. En developpant les Skills au sein de votre equipe, vous la transformez en memoire procedurale perenne : un veritable atout pour l'entreprise !*

---
**Pôle Formation UIMM - CVDL | Formateur : S. JAUBERT**
