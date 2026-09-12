# Conducteur Pédagogique et Plan Détaillé — Formation Introduction à l'IA (2026)

**Structure :** Pôle Formation UIMM - CVDL  
**Formateur :** S. JAUBERT  
**Date d'actualisation :** Septembre 2026  
**Public cible :** Stagiaires, alternants techniciens supérieurs et ingénieurs (BTS, Bachelor, Ingénieur), formateurs  
**Support interactif associé :** [Présentation Web Interactive 2026](index.html)

---

## 1. Objectifs Pédagogiques Globaux

A l'issue de cette formation, l'apprenant est capable de :
1. **Démystifier le fonctionnement réel de l'IA** en distinguant l'intelligence biologique du calcul statistique probabiliste.
2. **Identifier les étapes clés de l'histoire de l'IA**, du paradigme symbolique déductif au paradigme connexionniste inductif.
3. **Expliquer le fonctionnement interne d'un modèle d'apprentissage profond**, du neurone artificiel aux mécanismes d'attention des Transformers (*embeddings*, tokenisation, prédiction auto-régressive).
4. **Comprendre et mobiliser les ruptures 2022-2026** : modèles multimodaux, modèles de raisonnement (*Reasoning / Test-Time Compute*), architectures RAG et systèmes agentiques (protocole MCP).
5. **Analyser les impacts industriels, réglementaires (AI Act européen) et éthiques** pour adopter une posture professionnelle critique, responsable et souveraine.

---

## 2. Déroulé Modulaire et Références Documentaires Sourcées

### Module 1 : Démystifier l'IA — Origines, Définitions et Paradigmes (Durée : 1h30)

#### 1.1 Représentations initiales et tour de table
- Recueil des usages quotidiens des apprenants (traduction, assistants vocaux, synthèse d'images, chatbots, code).
- Déconstruction des idées reçues : l'IA n'est ni omnisciente ni consciente, elle traite des structures d'information formelles.

#### 1.2 Qu'appelle-t-on "intelligence" ?
- **L'approche opérationnelle d'Alan Turing (1950) :** substitution de la question ontologique *"Les machines peuvent-elles penser ?"* par le test d'imitation comportementale.
  - *Source :* [Turing, A. M. (1950). Computing Machinery and Intelligence. *Mind*, 59(236), 433–460](https://doi.org/10.1093/mind/LIX.236.433).
- **La théorie des intelligences multiples d'Howard Gardner :** réfutation du QI unique, identification de 8 formes d'intelligence (linguistique, logico-mathématique, spatiale, kinesthésique, musicale, interpersonnelle, intrapersonnelle, naturaliste). L'IA actuelle se concentre presque exclusivement sur les composantes linguistique et logico-statistique.
  - *Source :* [Gardner, H. (1993). *Frames of Mind: The Theory of Multiple Intelligences*. Basic Books](https://www.howardgardner.com/multiple-intelligences).
  - *Source critique pédagogique :* [Fondation La main à la pâte — L'idée d'intelligences multiples et son application en classe](https://synapses-lamap.org/2020/04/02/que-peut-on-dire-de-lidee-dintelligences-multiples-et-de-son-application-en-classe/).
- **L'éthologie et l'intelligence collective :** l'apprentissage social chez l'abeille domestique (danse frétillante) et la drosophile démontre que des comportements adaptatifs sophistiqués émergent de règles simples distribuées sans conscience individuelle centralisée.

#### 1.3 Les deux grands paradigmes : Symbolisme vs Connexionnisme
- **L'école symbolique (déductive) :** manipule des symboles explicites et applique des règles logiques définies par l'humain ($A \implies B$). Triomphe des systèmes experts dans les années 1970-1980, mais incapacité à traiter l'ambiguïté du monde physique (paradoxe de Moravec).
- **L'école connexionniste (inductive) :** infère des pondérations statistiques à partir de corpus d'exemples massifs. La connaissance est distribuée dans des matrices de poids numériques.

#### 1.4 Les jalons historiques et les hivers de l'IA
- **1943-1946 :** Conférences de Macy et fondation de la cybernétique (Norbert Wiener, Warren McCulloch, Walter Pitts).
- **1956 :** L'atelier d'été du Dartmouth College (John McCarthy, Marvin Minsky, Claude Shannon, Nathaniel Rochester) où l'expression *"Artificial Intelligence"* est officialisée.
  - *Source :* [Dartmouth Artificial Intelligence Conference (1956) — Proposal](http://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html).
- **1958 :** Le Perceptron de Frank Rosenblatt sur l'ordinateur Mark I de l'US Navy.
  - *Source :* [Rosenblatt, F. (1958). The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain. *Psychological Review*, 65(6), 386–408](https://doi.org/10.1037/h0042519).
- **1969 :** Premier hiver de l'IA. Démonstration par Marvin Minsky et Seymour Papert de l'incapacité du perceptron mono-couche à résoudre des problèmes non-linéaires élémentaires (fonction OU Exclusif / XOR).
  - *Source :* [Minsky, M., & Papert, S. (1969). *Perceptrons: An Introduction to Computational Geometry*. MIT Press](https://mitpress.mit.edu/9780262631111/perceptrons/).

---

### Module 2 : Sous le Capot — Des Neurones Artificiels aux Transformers (Durée : 2h00)

#### 2.1 Le neurone artificiel formel
- Structure mathématique : entrées $x_i$, poids synaptiques $w_i$, terme de biais $b$, somme pondérée $z = \sum_{i=1}^n w_i x_i + b$, et fonction d'activation non-linéaire $f(z)$ (Sigmoïde, Tanh, ReLU).
- Rétropropagation du gradient d'erreur (*Backpropagation*) : algorithme de Rumelhart, Hinton et Williams (1986) permettant d'ajuster les millions de paramètres par descente de gradient stochastique.
  - *Source :* [Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323(6088), 533–536](https://doi.org/10.1038/323533a0).
- Atelier illustratif : classification du jeu de données *Iris* de Fisher (1936) via régression logistique.

#### 2.2 La rupture du Deep Learning (2012)
- Le point d'inflexion d'AlexNet au concours ImageNet (septembre 2012) : réduction de moitié du taux d'erreur par rapport aux approches conventionnelles.
  - *Source :* [Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet Classification with Deep Convolutional Neural Networks. *NeurIPS Proceedings*](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf).
- Les trois moteurs de la renaissance :
  1. *Données massives :* numérisation globale du web et création de bancs d'essais annotés.
  2. *Puissance matérielle (Hardware) :* détournement des cartes graphiques (GPU NVIDIA) conçues pour le rendu 3D matriciel pour le calcul en virgule flottante parallèle (TFLOPS).
  3. *Optimisations algorithmiques :* fonctions ReLU, normalisation par lot (*Batch Normalization*), architectures résiduelles (ResNet, He et al., 2015).

#### 2.3 L'architecture Transformer et les Grands Modèles de Langage (2017-2022)
- L'article fondateur de Google Brain : *"Attention Is All You Need"* (juin 2017).
  - *Source :* [Vaswani et al. (2017). Attention Is All You Need. *arXiv:1706.03762*](https://arxiv.org/abs/1706.03762).
- Le mécanisme d'attention par produit scalaire pondéré (*Self-Attention*) :
  $$ \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V $$
  Capacité à modéliser les dépendances textuelles et contextuelles sur l'ensemble de la phrase simultanément sans goulot d'étranglement séquentiel.
- **De la lettre à l'espace sémantique (Embeddings) :**
  - Découpage en sous-mots (*Tokens*).
  - Projection dans un espace vectoriel dense à haute dimension (ex: 1536 ou 4096 dimensions). La proximité géométrique (distance cosinus) reflète la proximité sémantique.
- **La génération auto-régressive :**
  - Modélisation de la distribution conditionnelle :
    $$ P(w_t \mid w_1, w_2, \dots, w_{t-1}) $$
  - Paramètres de décodage : température, Top-P, pénalité de répétition.
  - *Démonstrateur interactif recommandé :* [Transformer Explainer (Polo Club of Data Science, Georgia Tech)](https://poloclub.github.io/transformer-explainer/).

---

### Module 3 : La Rupture 2022-2026 — Multimodalité, Raisonnement et Systèmes Agentiques (Durée : 2h30)

#### 3.1 La multimodalité native et l'expansion industrielle
- Les modèles ne sont plus cantonnés au texte brut : ils traitent conjointement l'image d'atelier, le schéma électrique, les plans techniques (formats vectoriels ou matriciels), les spectrogrammes vibratoires de machines-outils et le code automate/Python.
- Comparaison des écosystèmes :
  - **Modèles propriétaires Cloud :** Google Gemini (Gemini 2.x/3.x avec contextes jusqu'à 2 millions de tokens), Anthropic Claude (Claude 3.5 Sonnet / Claude 3.7 Sonnet), OpenAI (GPT-4o).
    - *Source :* [Google DeepMind — Gemini Technical Report](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_report.pdf).
    - *Source :* [Anthropic — Claude Model Specifications & Research](https://www.anthropic.com/research).
  - **Modèles ouverts souverains (*Open-Weights*) :**
    - Mistral AI (France/Europe) : modèles Mistral Large, Mistral NeMo, Codestral pour l'ingénierie logicielle.
      - *Source :* [Mistral AI Documentation & Modèles](https://docs.mistral.ai/).
    - Meta Llama 3 / 3.3 (Meta AI) : architecture ouverte de 8B à 70B paramètres.
      - *Source :* [Meta AI — Llama Models](https://ai.meta.com/llama/).
    - Google Gemma 2 & Gemma 3 : modèles ouverts dérivés des avancées de Gemini.
      - *Source :* [Google AI for Developers — Gemma Open Models](https://ai.google.dev/gemma).
    - Alibaba Qwen 2.5 / Qwen 3 : spécialisation poussée en raisonnement mathématique et code.
      - *Source :* [Qwen Technical Reports](https://qwenlm.github.io/).

#### 3.2 Le saut qualitatif du Raisonnement (*Reasoning & Test-Time Compute*)
- La distinction psychologique de Daniel Kahneman appliquée aux architectures d'IA :
  - **Système 1 :** génération textuelle immédiate et fluide mais sensible aux pièges logiques et aux hallucinations statistiques.
  - **Système 2 :** délibération lente, vérification formelle, génération d'arbres d'hypothèses et correction autonome avant l'émission de la réponse finale.
- La chaîne de pensée (*Chain of Thought*) :
  - *Source fondatrice :* [Wei et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *arXiv:2201.11903*](https://arxiv.org/abs/2201.11903).
- Les modèles de raisonnement par renforcement :
  - DeepSeek-R1 : modèle ouvert démontrant l'émergence de comportements de réflexion autonome sans supervision humaine massive.
    - *Source :* [DeepSeek-AI (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *arXiv:2501.12948*](https://arxiv.org/abs/2501.12948).
  - OpenAI o1 & o3 : apprentissage par renforcement appliqué à la résolution de problèmes scientifiques et mathématiques complexes.
    - *Source :* [OpenAI (2024). Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/).

#### 3.3 Des Chatbots aux Systèmes Agentiques
- Le modèle ne se contente plus de prédire, il orchestre un plan d'action : **Percevoir $\implies$ Planifier $\implies$ Agir $\implies$ Évaluer**.
- **Architecture RAG (Retrieval-Augmented Generation) :**
  - Ancrer les réponses dans la base documentaire fermée de l'entreprise (manuels d'atelier, gammes de fabrication, procédures de sécurité) sans ré-entraîner le modèle de fondation.
  - *Source fondatrice :* [Lewis et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *arXiv:2005.11401*](https://arxiv.org/abs/2005.11401).
- **L'appel d'outils (*Tool Calling / Function Calling*) :**
  - Capacité du modèle à générer des appels structurés en JSON pour interroger des bases SQL, piloter des API industrielles ou exécuter du code dans un bac à sable isolé.
- **Le standard ouvert MCP (Model Context Protocol) :**
  - Protocole universel initié par Anthropic pour standardiser la connexion entre agents d'IA et systèmes d'information d'entreprise (bases de données, serveurs de fichiers, dépôts Git, capteurs IoT).
  - *Source officielle :* [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io/) et [Dépôt GitHub MCP](https://github.com/modelcontextprotocol).
- **Les environnements de travail agentiques :**
  - Assistants d'ingénierie et de développement : Claude Code, Continue.dev, Goose, Cline.
    - *Source :* [Documentation officielle Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).
    - *Source :* [Continue.dev — The Open-Source AI Code Assistant](https://www.continue.dev).
    - *Source :* [Goose — An Open Source AI Agent for Engineers (Block)](https://block.github.io/goose/).

---

### Module 4 : Enjeux Industriels, Cadre Juridique et Esprit Critique (Durée : 1h30)

#### 4.1 Le cadre réglementaire européen : L'AI Act (Législation sur l'IA)
- **Texte juridique de référence :** Règlement (UE) 2024/1689 du Parlement européen et du Conseil du 13 juin 2024 établissant des règles harmonisées concernant l'intelligence artificielle (entré en vigueur le 1er août 2024 avec calendrier d'application échelonné 2025-2026).
  - *Source officielle EUR-Lex :* [Règlement (UE) 2024/1689 du Journal Officiel de l'Union Européenne](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).
  - *Source institutionnelle Commission Européenne :* [European Artificial Intelligence Act & AI Office](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai).
  - *Source d'analyse nationale :* [Direction Générale des Entreprises (DGE) — Règlement européen sur l'IA](https://www.entreprises.gouv.fr/fr/numerique/enjeux-du-numerique/reglement-europeen-sur-l-intelligence-artificielle-ia-act).
  - *Source de conformité :* [CNIL — Intelligence artificielle et AI Act](https://www.cnil.fr/fr/intelligence-artificielle/ia-act).
- **La classification quadripartite par les risques :**
  1. *Risque inacceptable (Systèmes interdits) :* manipulation comportementale cognitive, notation sociale (*social scoring*), identification biométrique à distance en temps réel dans l'espace public (sauf exceptions pénales strictes).
  2. *Haut risque (Systèmes fortement encadrés) :* infrastructures critiques (énergie, transport), recrutement et gestion RH, éducation et formation professionnelle, dispositifs médicaux et sécurité des machines industrielles. Obligations : gouvernance des données d'entraînement, documentation technique rigoureuse, traçabilité (*logging*), supervision humaine effective, robustesse et cybersécurité.
  3. *Risque limité (Obligations de transparence) :* systèmes en interaction avec l'humain (chatbots), détection d'émotions, contenus générés artificiellement (*deepfakes*) devant être obligatoirement étiquetés comme tels.
  4. *Risque minimal ou nul :* filtres anti-spam, jeux vidéo, outils de diagnostic d'optimisation d'usinage interne (usage libre sans contrainte spécifique).
- **Les obligations spécifiques pour les modèles d'IA à usage général (GPAI) :** transparence sur les données protégées par le droit d'auteur, respect des règles d'opt-out pour le fouillage de textes et de données (*TDM*), gestion des risques systémiques pour les modèles dépassant $10^{25}$ FLOPs.

#### 4.2 Souveraineté des données, secret d'affaires et cybersécurité
- **Les risques industriels avérés :**
  - Fuite de plans confidentiels, de recettes chimiques ou de codes sources propriétaires injectés dans des services cloud grand public non contractuellement protégés (ré-utilisation pour l'entraînement).
  - Attaques par injection de prompt (*Prompt Injection* indirecte) et empoisonnement de données de contexte.
  - *Référence de sécurité :* [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/).
- **L'alternative souveraine : l'IA locale et on-premise :**
  - Déploiement de modèles ouverts (Mistral, Llama, Qwen) sur des serveurs d'entreprise ou des stations de travail étanches sans connexion Internet.
  - Solutions d'inférence locales : Ollama, llama.cpp, vLLM, Jan.
    - *Source :* [Ollama — Get up and running with large language models](https://ollama.com).
    - *Source :* [llama.cpp (GGML)](https://github.com/ggml-org/llama.cpp).

#### 4.3 Frugalité et transition environnementale
- L'empreinte écologique des centres de données : consommation en mégawatts d'électricité et prélèvements d'eau pour le refroidissement des baies de serveurs IA.
- L'impératif de sobriété numérique : préférer des petits modèles spécialisés quantifiés (4-bit, SLM de 3B à 8B) adaptés au cas d'usage précis plutôt que d'interroger un modèle généraliste massif de plusieurs centaines de milliards de paramètres.

#### 4.4 Métacognition et posture de l'ingénieur/technicien
- **L'illusion de compétence et l'effet Dunning-Kruger démultiplié :** la fluidité syntaxique d'une réponse générée donne l'illusion de l'exactitude scientifique.
- **Les biais cognitifs induits par le prompting :**
  - *Biais de confirmation :* orienter sans le savoir la réponse du modèle par une question biaisée.
  - *Biais d'ancrage :* accorder un crédit excessif à la première proposition émise par l'IA.
- **Le protocole de questionnement critique :**
  1. Vérifier les sources primaires indépendantes.
  2. Forcer le modèle à chercher des contre-arguments et des failles dans son propre raisonnement.
  3. Auditer les résultats chiffrés manuellement ou par des programmes déterministes.

#### 4.5 Conclusion épistémologique : "Penser avec l'IA"
- **Texte de clôture (repris du diaporama historique de S. JAUBERT) :**
  > *« L'intelligence artificielle n'est pas un substitut à la pensée mais une épreuve qui oblige à la rehausser.*  
  > *On ne peut pas véritablement "penser avec" l'IA si l'on ne dispose pas soi-même d'un socle solide : un corpus de références, une bibliothèque mentale de concepts, d'auteurs et de faits. Sans cet appui, impossible de distinguer l'erreur de l'exactitude, le plausible du vrai, l'intuition féconde de l'anachronisme grossier.*  
  > *Celui qui délègue son entendement à la machine en sera prisonnier et cela pourrait lui être fatal : son destin sera celui de l'outil qu'il a choisi d'imiter, efficace peut-être, mais sans profondeur, sans vie.*  
  > *L'IA appelle donc moins à la paresse qu'à l'exigence : elle exige d'aiguiser son esprit critique, d'élargir ses savoirs, de fortifier sa culture dans des domaines où il y a peu de gains de productivité : la lecture lente, la fréquentation des classiques, la confrontation patiente aux grandes œuvres, la méditation silencieuse, l'expérience vécue.*  
  > *Dans un monde où, pour reprendre Jean-François Lyotard, "avoir du succès, c'est gagner du temps", quel cruel destin que de devoir encore lire un livre jusqu'au bout...*  
  > *L'IA est donc paradoxalement une alliée : non pas pour remplacer la pensée mais pour la rendre plus indispensable que jamais. »*

---

## 3. Bibliographie et Sitographie Complète de Référence

1. **Textes juridiques et institutionnels :**
   - Règlement (UE) 2024/1689 du Parlement européen et du Conseil (AI Act) : [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
   - European Commission AI Office : [Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/ai-office)
   - CNIL — Dossier Intelligence Artificielle : [cnil.fr](https://www.cnil.fr/fr/intelligence-artificielle)
   - Direction Générale des Entreprises : [entreprises.gouv.fr](https://www.entreprises.gouv.fr/fr/numerique/enjeux-du-numerique/reglement-europeen-sur-l-intelligence-artificielle-ia-act)
2. **Papiers fondateurs et articles scientifiques :**
   - Turing, A. M. (1950). *Computing Machinery and Intelligence*. [DOI:10.1093/mind/LIX.236.433](https://doi.org/10.1093/mind/LIX.236.433)
   - Rosenblatt, F. (1958). *The Perceptron*. [DOI:10.1037/h0042519](https://doi.org/10.1037/h0042519)
   - Rumelhart et al. (1986). *Learning representations by back-propagating errors*. [Nature](https://doi.org/10.1038/323533a0)
   - Krizhevsky et al. (2012). *ImageNet Classification with Deep CNNs*. [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
   - Vaswani et al. (2017). *Attention Is All You Need*. [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
   - Lewis et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
   - Wei et al. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
   - DeepSeek-AI (2025). *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)
3. **Standards techniques, outils et démonstrateurs :**
   - Model Context Protocol (MCP) : [modelcontextprotocol.io](https://modelcontextprotocol.io/)
   - Transformer Explainer (Georgia Tech) : [poloclub.github.io/transformer-explainer](https://poloclub.github.io/transformer-explainer/)
   - OWASP GenAI Security Project : [genai.owasp.org](https://genai.owasp.org/)
   - Ollama (Runner local) : [ollama.com](https://ollama.com)
   - Mistral AI : [mistral.ai](https://mistral.ai/)
