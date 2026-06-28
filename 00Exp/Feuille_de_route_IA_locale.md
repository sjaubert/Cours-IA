# Feuille de route : monter une IA locale pour comprendre et enseigner

Pôle Formation UIMM-CVDL — S. Jaubert
Document de travail, juin 2026. Objectif : apprendre par l'expérimentation, puis transmettre.

---

## 0. Comment lire ce document

Trois paliers, du plus simple au plus exigeant :

1. **Démo pédagogique** : faire tourner un modèle, voir les tokens défiler, mesurer, diagnostiquer. Tourne sur presque n'importe quel portable.
2. **Assistant de code** dans VS Code avec Continue. C'est exactement le setup du prof qui t'inspire. Tourne sur matériel modeste.
3. **Agent autonome** avec Goose, qui agit sur tes fichiers. Tourne sur ta machine, à démontrer aux étudiants. Pas réaliste sur chaque portable étudiant.

Chaque palier reprend les cinq intentions pédagogiques du post : écologie, sécurité, disponibilité, démontrer, diagnostiquer.

---

## 1. Mise au point critique avant de commencer

Tu m'as demandé des avis tranchés. En voici deux qui corrigent des idées reçues avant de te lancer.

### 1.1 "Ollama est-il indispensable, y a-t-il plus léger ?" repose sur une fausse prémisse

Ollama, LM Studio, Jan, llama.cpp tournent **tous sur le même moteur** (llama.cpp). Les écarts de vitesse sont de l'ordre de 5 %. Le runner n'est pas ce qui consomme tes ressources.

Ce qui consomme, c'est **le modèle chargé en mémoire**. Un Gemma 3 27B mangera ta VRAM quel que soit le runner. Un Gemma 3 1B sera léger partout.

Conclusion : tu as déjà Ollama, garde-le. C'est le bon choix pour ton usage (CLI simple, API locale standard, intégration directe avec Continue et Goose). Ta vraie variable d'ajustement, c'est **la taille et la quantification du modèle**, pas le logiciel qui le lance.

Quand envisager autre chose :

| Outil | Quand le préférer à Ollama |
|---|---|
| [**LM Studio**](https://lmstudio.ai) | Tu veux une interface graphique pour que des étudiants débutants choisissent et téléchargent un modèle sans terminal. Bon pour une démo grand public. |
| [**Jan**](https://www.jan.ai) | Priorité absolue à la confidentialité et au zéro télémétrie, open source. Argument fort pour ton cours souveraineté. |
| [**llama.cpp brut**](https://github.com/ggml-org/llama.cpp) | Tu veux montrer la mécanique la plus bas niveau, ou bricoler du matériel exotique. Pédagogique mais aride. |

### 1.2 La tension que tu dois assumer

Tu as choisi "postes étudiants hétérogènes" ET "agent autonome". Sur des portables sans carte graphique dédiée, un agent qui manipule des fichiers a besoin d'un modèle capable d'appeler des outils en produisant du JSON valide. Les petits modèles sur CPU produisent justement le JSON malformé décrit comme un bug dans tes guides. Ce n'est pas un réglage à trouver, c'est une limite structurelle des petits modèles.

Donc : paliers 1 et 2 pour tous. Palier 3 sur ta machine, en démonstration.

---

## 2. Le matériel : ce qui compte vraiment

Trois chiffres, dans l'ordre d'importance.

1. **VRAM (mémoire de la carte graphique)**. Si le modèle tient dans la VRAM, l'inférence est rapide. S'il déborde, une partie bascule en RAM système et la vitesse s'effondre.
2. **RAM système**. Permet de faire tourner un modèle sur CPU quand il n'y a pas de GPU, ou quand le GPU est saturé. Plus lent mais fonctionnel.
3. **CPU**. Compte surtout en mode CPU pur (pas de GPU dédié), cas fréquent sur portables étudiants.

### Règle de dimensionnement (quantification 4-bit, la norme)

Ordre de grandeur : un modèle en 4-bit occupe environ **0,7 Go par milliard de paramètres**, plus une marge pour le contexte.

| Modèle | Paramètres | Empreinte 4-bit approx. | Tient sur |
|---|---|---|---|
| Petit | 1 à 1,5 B | ~1 Go | N'importe quel portable, même sans GPU |
| Moyen | 3 à 4 B | ~3 Go | Portable 8 Go RAM, ou petit GPU |
| Confort | 7 à 8 B | ~5 Go | GPU 6 Go (juste), ou 16 Go RAM en CPU |
| Lourd | 12 à 14 B | ~9 Go | GPU 12 Go et plus |
| Très lourd | 27 à 32 B | ~18-20 Go | Station de travail, GPU 24 Go |

### Ce que je recommande selon la machine

- **Portable étudiant sans GPU, 8 Go RAM** : modèles 1B à 4B. Lent mais ça marche. Parfait pour le palier 1.
- **Portable 16 Go RAM, GPU intégré** : 4B fluide, 7B jouable.
- **Ta machine type RTX 2060 6 Go / 32 Go RAM** : 7B en 4-bit sur GPU (tient à l'étroit), ou 4B très confortable. Suffisant pour les trois paliers en démo.

**Point d'honnêteté** : je ne connais pas le parc réel de tes étudiants. Avant de promettre un setup uniforme, fais-leur lancer la commande de diagnostic du palier 1 et relève VRAM et RAM. On calibrera sur le plus petit dénominateur réel, pas supposé.

---

## 3. Choix des modèles open source (juin 2026)

Tu citais Qwen-coder et DeepSeek. Bons réflexes. Voici le panorama utile.

| Famille | Variantes utiles | Pour quoi | Remarque |
|---|---|---|---|
| **Gemma 3** | `gemma3:1b`, `gemma3:4b`, `gemma3:12b`, `gemma3:27b` | Généraliste, multilingue, vision (4B et +) | Excellent rapport qualité/taille. Le 4B est le couteau suisse pédagogique. |
| **Qwen2.5-Coder** | `qwen2.5-coder:1.5b`, `:7b` | Code | Le 1.5B sait faire du "fill-in-the-middle" (autocomplétion). Choix établi et fiable. |
| **Qwen3** | `qwen3:4b`, `qwen3:8b` | Généraliste récent, raisonnement, appel d'outils | Bon candidat pour l'agent si GPU correct. |
| **Llama 3.2** | `llama3.2:1b`, `:3b` | Généraliste léger | Très rapide sur CPU, idéal démo "voir les tokens". |
| **DeepSeek** | `deepseek-r1` (distillations), `deepseek-coder-v2` | Raisonnement, code | Plus gourmand. À réserver à ta machine, pas aux portables. |

**Incertitude que je signale** : les tags exacts des dernières versions Qwen3-Coder évoluent vite. Vérifie le nom précis sur `ollama.com/library` avant de lancer un `pull`, ne recopie pas un tag de mémoire.

**Choix par défaut que je te conseille pour démarrer :**

- Démo et chat : `gemma3:4b` (ou `llama3.2:1b` pour la démo "tokens en direct" ultra-rapide).
- Autocomplétion de code : `qwen2.5-coder:1.5b`.
- Chat de code : `qwen2.5-coder:7b` (sur ta machine).

---

## 4. Palier 1 — Démo pédagogique : faire tourner et comprendre

Objectif : l'étudiant voit une IA fonctionner sur sa propre machine, sans réseau, et comprend ce qui se passe.

### 4.1 Vérifier l'installation et le matériel

```bash
ollama --version
```

Diagnostic matériel rapide à faire faire aux étudiants :

- Windows : Gestionnaire des tâches > Performance > GPU (relever la mémoire dédiée) et Mémoire (RAM totale).
- En ligne de commande, pour voir si un GPU NVIDIA est détecté : `nvidia-smi` (ne fonctionne que si pilotes NVIDIA installés).

### 4.2 Premier modèle et premier dialogue

```bash
ollama run llama3.2:1b
```

Au premier lancement, le modèle se télécharge. Ensuite, pose une question. **Fais observer le défilement des tokens** : c'est le coeur de la démo. Le modèle ne "réfléchit" pas, il prédit le mot suivant, un par un. C'est visible en direct.

**Cas d'usage à faire tester par les étudiants** (copier-coller dans l'invite `>>>`) :

| Prompt | Ce que ça montre |
|---|---|
| `Explique ce qu'est un octet à un élève de 3e.` | Vulgarisation : le modèle s'adapte au niveau demandé. |
| `Combien font 17 x 23 ? Donne seulement le résultat.` | Piège : un petit modèle se trompe souvent en calcul. Vérifie à la calculatrice. Démonstration directe de l'hallucination. |
| `Traduis en anglais technique : "régler le couple de serrage à 12 newtons-mètres".` | Traduction métier, utile en contexte industriel. |
| `Résume ce texte en 3 points : [colle un paragraphe].` | Synthèse, la tâche où les LLM excellent. |

Insiste sur le deuxième : un modèle de langage prédit du texte plausible, il ne calcule pas. C'est exactement le lien avec ton activité "Illusion de Vérité".

> **Défi étudiant.** Trouve une question simple où `llama3.2:1b` se trompe mais où `gemma3:4b` répond juste. Note les deux réponses. Conclusion : la taille du modèle change la fiabilité, pas seulement la vitesse.

### 4.3 Mesurer (écologie et performance)

`/set verbose` n'est pas une commande du terminal Windows. C'est une commande **interne à Ollama**, qu'on tape une fois entré dans le dialogue avec le modèle. Déroulé exact.

**1.** Lance le modèle depuis le terminal :

```bash
ollama run gemma3:4b
```

**2.** Ollama affiche une invite à trois chevrons. C'est là qu'on écrit :

```
>>>
```

**3.** Tape la commande, puis Entrée. Le message de confirmation apparaît :

```
>>> /set verbose
Set 'verbose' mode.
```

**4.** Pose une vraie question :

```
>>> Explique en deux phrases ce qu'est un token.
```

**5.** Le modèle répond, puis **sous sa réponse** s'affiche un bloc de statistiques. C'est le résultat attendu :

```
total duration:       4.812s
load duration:        38.7ms
prompt eval count:    18 token(s)
prompt eval duration: 412ms
prompt eval rate:     43.7 tokens/s
eval count:           96 token(s)
eval duration:        4.3s
eval rate:            22.3 tokens/s
```

**Lecture des chiffres.** La ligne qui compte est la dernière, `eval rate` : la vitesse de génération en tokens par seconde. Plus c'est haut, plus le modèle écrit vite. C'est l'indicateur à comparer entre modèles.

- `total duration` : temps total de la requête.
- `load duration` : temps de chargement du modèle en mémoire (quasi nul s'il était déjà chargé).
- `prompt eval count` / `prompt eval rate` : nombre de tokens de ta question, et vitesse de lecture.
- `eval count` : nombre de tokens générés dans la réponse.
- `eval rate` : vitesse de génération de la réponse.

**La démo écologie.** Pose la même question sur deux modèles et compare `eval rate` :

```
ollama run llama3.2:1b      -> eval rate ~60 a 100 tokens/s (leger)
ollama run gemma3:4b        -> eval rate ~15 a 30 tokens/s (plus capable, plus lourd)
```

Les chiffres exacts dépendent de la machine. Ne les annonce pas d'avance, fais-les mesurer en direct. Message en une phrase : un modèle plus gros écrit plus lentement et consomme plus de calcul pour la même réponse. Le bon réflexe n'est pas "le plus puissant" mais "le plus petit qui fait le travail".

Deux commandes pour finir la session :

```
/set quiet     désactive l'affichage des stats
/bye           quitte le dialogue, retour au terminal
```

### 4.4 Diagnostiquer quand ça plante

Trois pannes classiques à savoir reconnaître :

- **Le serveur ne répond pas** : `ollama list` échoue. Le service Ollama n'est pas lancé. Relancer l'application Ollama.
- **Modèle absent** : message "model not found". Faire `ollama pull <nom>` d'abord.
- **Lenteur extrême** : le modèle déborde de la VRAM vers la RAM. Solution : prendre un modèle plus petit (`gemma3:4b` au lieu d'un 12B).

Commandes utiles :

```bash
ollama list      # modèles installés
ollama ps        # modèles actuellement chargés en mémoire
ollama rm <nom>  # libérer de l'espace disque
```

### 4.5 Souveraineté : la preuve par la coupure réseau

Démo marquante : coupe le Wi-Fi, relance `ollama run gemma3:4b`, pose une question. Ça marche. Aucune donnée ne sort. C'est l'argument souveraineté rendu tangible.

### 4.6 Optimisation du stockage (optionnel)

Par défaut Ollama stocke sur le disque système. Pour rediriger (utile sur SSD système plein), variable d'environnement `OLLAMA_MODELS` pointant vers un autre disque, puis redémarrage. Tes guides décrivent correctement la procédure Windows.

---

## 5. Palier 2 — Assistant de code dans VS Code avec Continue

C'est précisément le setup du prof : deux modèles, un léger pour l'autocomplétion, un plus costaud pour le chat de code, gestion des tokens et de l'énergie, et pas de clé API qui traîne.

### 5.1 Pourquoi deux modèles

Continue distingue deux rôles :

- **autocomplete** : suggère du code pendant que tu tapes. Doit être très rapide. Petit modèle.
- **chat / edit** : répond à des questions, explique, refactore. Peut être plus lent et plus gros.

### 5.2 Télécharger les modèles

```bash
ollama pull qwen2.5-coder:1.5b   # autocomplétion (sait faire du fill-in-the-middle)
ollama pull qwen2.5-coder:7b     # chat de code (sur ta machine)
```

Sur un portable étudiant faible, remplace le chat 7B par `qwen2.5-coder:1.5b` aussi, ou `gemma3:4b`.

### 5.3 Installer Continue

Dans VS Code : extension [Continue](https://www.continue.dev) depuis la marketplace. Documentation : [docs.continue.dev](https://docs.continue.dev).

### 5.4 Configurer (config.yaml de Continue)

Continue se configure par un fichier `config.yaml`. Exemple minimal, 100 % local :

```yaml
name: Setup local UIMM
version: 0.0.1
schema: v1
models:
  - name: Chat Code 7B
    provider: ollama
    model: qwen2.5-coder:7b
    roles:
      - chat
      - edit
  - name: Autocomplete 1.5B
    provider: ollama
    model: qwen2.5-coder:1.5b
    roles:
      - autocomplete
```

Vérifie aussi dans les réglages VS Code que `editor.inlineSuggest.enabled` est à `true`, sinon l'autocomplétion ne s'affiche pas.

### 5.5 Les cinq intentions pédagogiques, concrètement

- **Écologie** : le modèle léger (1.5B) tourne en permanence pour l'autocomplétion, le gros (7B) seulement à la demande. On ne sort le calcul lourd que quand c'est nécessaire.
- **Sécurité** : montre que dans cette config, il n'y a **aucune clé API**. Tout est local. Compare avec une config cloud où une clé OpenAI traînerait en clair dans un fichier versionné par erreur. C'est l'erreur classique à ne pas commettre.
- **Disponibilité** : tu peux ajouter un modèle de secours dans la liste. Si l'un ne charge pas, on bascule sur l'autre.
- **Démontrer** : garde un terminal `ollama ps` ouvert pendant que tu codes. Les étudiants voient le modèle se charger et répondre en temps réel.
- **Diagnostiquer** : si l'autocomplétion ne vient pas, vérifier dans l'ordre : modèle téléchargé (`ollama list`), serveur lancé (`ollama ps`), `inlineSuggest` activé, bon nom de modèle dans `config.yaml`.

### 5.6 Cas d'usage à montrer en cours

L'autocomplétion (pendant la frappe) et le chat (sélectionner du code, poser une question) se complètent. Exemples concrets, orientés BTS et industrie.

**Autocomplétion.** Crée un fichier `analyse.py`, commence à taper, laisse le modèle proposer la suite :

```python
import csv

def moyenne_temperatures(fichier_csv):
    # place le curseur ici et laisse l'autocomplétion proposer le corps
```

**Chat de code** (sélectionne du code, ou pose la question dans le panneau Continue) :

| Demande au chat | Compétence travaillée |
|---|---|
| "Explique cette expression régulière ligne par ligne." | Lecture de code existant. |
| "Écris la docstring de cette fonction." | Documentation. |
| "Génère des tests unitaires pytest pour cette fonction." | Test, validation. |
| "Refactore cette boucle for en compréhension de liste." | Bonnes pratiques Python. |
| "Ce script lit un CSV de relevés machine. Ajoute le calcul de la moyenne et de l'écart-type." | Cas industriel concret. |

**Le réflexe esprit critique à enseigner** : le code généré n'est pas garanti correct. On le lit, on le teste, on ne l'exécute jamais en aveugle. C'est le pendant "code" de l'activité sur l'hallucination.

> **Défi étudiant.** Fais générer par le chat une fonction qui lit un CSV de températures et signale les valeurs au-dessus d'un seuil. Puis demande-lui d'écrire les tests. Lance les tests. Combien passent du premier coup ? Corrige ce qui ne marche pas. C'est ça, travailler avec une IA, pas la croire sur parole.

---

## 6. Palier 3 — Agent autonome avec Goose (sur ta machine)

Objectif : une IA qui ne se contente pas de répondre, mais **agit** : elle crée des dossiers, lit et écrit des fichiers, lance des scripts. C'est le saut conceptuel le plus important du cours.

### 6.1 Comment fonctionne un agent (la notion clé à transmettre)

Un agent, c'est trois choses : **un LLM + des outils + une boucle**.

Le cycle, à dessiner au tableau :

1. Tu donnes un objectif en langage naturel.
2. Le LLM **raisonne** et décide quel outil utiliser (lire un fichier, en écrire un, lancer une commande).
3. L'outil **s'exécute** et renvoie un résultat.
4. Le LLM **observe** ce résultat et décide de l'étape suivante.
5. Il recommence jusqu'à atteindre l'objectif, puis s'arrête.

La différence avec un chatbot tient en une phrase : **le chatbot produit du texte, l'agent produit des actions.** Le LLM décide, les outils agissent.

**MCP en une phrase** : le Model Context Protocol est le standard qui branche des outils sur l'agent (système de fichiers, GitHub, récupération web). Dans Goose, ces outils s'appellent des "extensions".

### 6.2 Avertissement de réalisme, à dire aux étudiants

Un agent fiable a besoin d'un modèle qui **appelle des outils proprement**. Sur petit modèle CPU, les appels d'outils échouent souvent (JSON malformé). Ce n'est pas un bug à corriger, c'est la limite du modèle. Donc :

- Démo de l'agent sur **ta** machine (GPU 6 Go minimum), pas sur les portables étudiants.
- Modèle conseillé : `qwen3:8b` ou `qwen2.5-coder:7b`, qui gèrent mieux l'appel d'outils que les 1B-4B.
- Pose des objectifs simples et vérifiables, pas des missions complexes en un seul prompt.

Goose, lancé par Block, est passé sous la Linux Foundation fin 2025 (Agentic AI Foundation) ; son dépôt a déménagé de `block/goose` vers `aaif-goose/goose`. Il existe en application desktop et en CLI, et supporte Ollama en local. Documentation : [goose-docs.ai](https://goose-docs.ai).

### 6.3 Installer Goose (Windows, version desktop)

1. Va sur la page officielle des versions : [github.com/aaif-goose/goose/releases](https://github.com/aaif-goose/goose/releases).
2. Télécharge l'installeur Windows (fichier `Goose-Setup-x.x.x.exe`).
3. Lance le `.exe`, installe, puis ouvre l'application Goose Desktop.

Prérequis : Ollama doit déjà tourner (palier 1). Vérifie avec `ollama ps` dans un terminal.

### 6.4 Configurer Goose pas à pas

1. Ouvre les paramètres de Goose (icône engrenage).
2. Section **Provider** (fournisseur de modèle) : choisis **Ollama**.
3. **URL** : laisse `http://localhost:11434` (c'est l'adresse locale d'Ollama, le trafic ne sort pas de la machine).
4. **Modèle** : sélectionne `qwen3:8b` (télécharge-le avant avec `ollama pull qwen3:8b` si besoin).
5. **Étanchéité** : vérifie qu'aucun provider cloud (OpenAI, Anthropic) n'est actif. C'est la mesure anti-fuite de données.
6. Section **Extensions** : active **File System** (Développeur / Developer selon les versions). Sans elle, l'agent ne peut ni lire ni écrire de fichiers.

### 6.5 Sécurité : toujours travailler dans un bac à sable

Un agent peut écraser ou supprimer des fichiers. Ne le lâche jamais sur tout ton disque.

- Crée un dossier dédié, par exemple `00Exp/bac_a_sable`, et donne tes objectifs en restant dans ce dossier.
- Fais une sauvegarde ou un commit Git avant une tâche qui modifie des fichiers existants.
- Lis ce que l'agent propose **avant** de valider une action destructrice. Goose montre ses étapes, ne clique pas "oui" en aveugle.

### 6.6 Cinq cas d'usage progressifs (avec comportement attendu)

Tous à lancer dans `bac_a_sable`. Pour les cas 3 et 5, crée d'abord les fichiers d'exemple.

**Cas 1 — Échauffement (écriture simple).**
Prompt : *"Crée un fichier bonjour.txt contenant la date du jour et la phrase : IA locale opérationnelle."*
Comportement attendu : l'agent utilise l'outil d'écriture de fichier. Vérifie : le fichier existe, il contient le texte.

**Cas 2 — Générer et exécuter du code.**
Prompt : *"Crée fibonacci.py qui affiche la suite de Fibonacci jusqu'à 20, puis exécute-le et montre-moi la sortie."*
Comportement attendu : l'agent écrit le fichier, le lance, et te renvoie la sortie réelle. Deux outils enchaînés (écrire, exécuter). C'est ici qu'on voit la boucle.

**Cas 3 — Analyse de données machine (cas industriel).**
Prépare d'abord un fichier `releves.csv` dans `bac_a_sable` :

```
machine,temperature
P1,72
P2,88
P3,65
P4,91
P5,79
```

Prompt : *"Lis releves.csv. Calcule la température moyenne. Liste les machines dont la température dépasse 80. Écris le tout dans rapport.md."*
Comportement attendu : l'agent lit le CSV, calcule, filtre, écrit un rapport Markdown. Vérifie le calcul à la main : moyenne = (72+88+65+91+79)/5 = 79. Machines au-dessus de 80 : P2 et P4.

**Cas 4 — Rangement de fichiers.**
Prompt : *"Range les fichiers de ce dossier dans des sous-dossiers selon leur extension : un dossier txt, un dossier py, un dossier csv."*
Comportement attendu : l'agent liste les fichiers et les déplace. À montrer pour illustrer une vraie automatisation. Rappelle la règle du bac à sable : déplacer, ça peut casser des chemins ailleurs.

**Cas 5 — Synthèse multi-documents.**
Crée deux ou trois petits fichiers `.md` dans `bac_a_sable`.
Prompt : *"Lis tous les fichiers .md de ce dossier et écris une synthèse en 5 points dans synthese.md."*
Comportement attendu : l'agent lit chaque fichier, agrège, rédige. C'est le cas le plus proche de ton métier de formateur (synthétiser des supports).

### 6.7 Les cinq intentions pédagogiques, version agent

- **Écologie** : un agent enchaîne plusieurs inférences pour une seule tâche. C'est plus coûteux qu'un chat. Message : on n'envoie pas un agent faire ce qu'un simple chat suffit à faire.
- **Sécurité** : tout est local, aucune donnée ne sort, et le bac à sable limite les dégâts. Montre les deux niveaux de protection.
- **Disponibilité** : si le modèle d'agent rame, on bascule sur un modèle plus petit pour les démos simples.
- **Démontrer** : Goose affiche chaque étape (raisonnement, appel d'outil, résultat). C'est la boucle agentique rendue visible, en direct.
- **Diagnostiquer** : voir ci-dessous.

### 6.8 Diagnostiquer l'agent

- **L'agent boucle ou échoue sur un appel d'outil** : modèle trop petit. Passer à un 7B-8B.
- **Rien ne s'écrit sur le disque** : extension File System non activée, ou l'agent travaille dans le mauvais dossier. Précise le chemin dans le prompt.
- **Réponses très lentes** : normal, chaque étape est une inférence complète. Réduire la taille du modèle ou découper la tâche.
- **L'agent invente un résultat au lieu de lire le fichier** : reformule en exigeant l'usage de l'outil ("lis réellement le fichier, ne devine pas").

> **Défi étudiant.** Donne à l'agent le cas 3 (analyse du CSV). Vérifie son calcul de moyenne à la main. S'est-il trompé ? A-t-il bien lu le fichier ou inventé des chiffres ? Conclusion : même un agent doit être contrôlé. L'autonomie n'est pas la fiabilité.

### 6.9 Alternative honnête

Le prof du post n'utilise pas Goose, il utilise Continue. Pour un premier contact avec l'agentique, le mode agent/edit de [Continue](https://www.continue.dev), ou [Cline](https://cline.bot) / [Aider](https://aider.chat) dans VS Code, suffisent souvent et se débuggent plus facilement qu'un agent desktop. Ne complique pas si le palier 2 couvre déjà ton besoin.

---

## 7. Pièges réels (pas ceux inventés par les guides)

- **Confondre runner et modèle** : changer de logiciel ne réglera pas un problème de mémoire. Réduis la taille du modèle.
- **Vouloir le plus gros modèle** : contre-productif sur matériel modeste. Le bon modèle est le plus petit qui fait le travail.
- **Recopier des noms de modèles de mémoire ou depuis un PDF** : vérifie toujours le tag exact sur `ollama.com/library` avant un `pull`. Un document peut citer un nom de modèle qui n'existe pas.
- **Clé API dans un fichier versionné** : en local pur tu n'en as pas, c'est un avantage sécurité. Si un jour tu ajoutes un modèle cloud de secours, mets la clé dans une variable d'environnement, jamais dans le dépôt.
- **Promettre un setup uniforme sans connaître le parc** : mesure d'abord (palier 1, étape 4.1).

---

## 8. Ce que je ne sais pas et que tu dois vérifier toi-même

- Le parc matériel réel de tes étudiants. À mesurer.
- Les tags exacts des toutes dernières versions Qwen3-Coder sur Ollama. À vérifier sur la source primaire avant `pull`.
- Le comportement précis de Goose sur ta machine spécifique : à tester, l'agentique locale reste plus fragile que le chat.

Je n'ai rien inventé dans ce document. Quand je n'étais pas sûr, je l'ai écrit.

---

## 9. Prochaine étape proposée

Commence par le palier 1 sur ta machine cette semaine. Mesure les tokens par seconde de `llama3.2:1b` et `gemma3:4b`. Quand tu as ces deux chiffres, on calibre le choix de modèle pour les étudiants, et je te prépare la version HTML pédagogique de cette feuille de route.

---

## Outils mentionnés : liens officiels

| Outil | Rôle | Lien officiel |
|---|---|---|
| Ollama | Moteur d'inférence local | https://ollama.com |
| LM Studio | Runner local, interface graphique | https://lmstudio.ai |
| Jan | Runner local, open source, offline | https://www.jan.ai |
| llama.cpp | Moteur bas niveau (socle des autres) | https://github.com/ggml-org/llama.cpp |
| Continue | Assistant de code dans VS Code | https://www.continue.dev |
| Goose | Agent autonome | https://goose-docs.ai |
| Cline | Agent de code dans VS Code | https://cline.bot |
| Aider | Agent de code en terminal, orienté Git | https://aider.chat |
| Bibliothèque de modèles Ollama | Vérifier les noms et tailles | https://ollama.com/library |

## Sources

- [Gemma 3 sur Ollama](https://ollama.com/library/gemma3)
- [Gemma 3 — guide d'exécution Unsloth](https://unsloth.ai/docs/models/tutorials/gemma-3-how-to-run-and-fine-tune)
- [Comparatif Ollama / LM Studio / llama.cpp / Jan / vLLM (Glukhov)](https://www.glukhov.org/llm-hosting/comparisons/hosting-llms-ollama-localai-jan-lmstudio-vllm-comparison/)
- [Meilleurs modèles de code locaux 2026 (Pinggy)](https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/)
- [Configuration autocomplétion Continue (docs officielles)](https://docs.continue.dev/customize/deep-dives/autocomplete)
- [Setup Continue + Ollama + Qwen-Coder (SitePoint)](https://www.sitepoint.com/local-ai-coding-assistant-vscode-ollama-continue/)
- [Goose — agent open source](https://goose-docs.ai/)
- [Agents IA locaux : Goose, AnythingLLM (AIMultiple)](https://aimultiple.com/local-ai-agent)
