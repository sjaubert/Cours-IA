---
exported: 2026-06-13T04:40:32.692Z
source: NotebookLM
type: note
title: "Lexique des Fondamentaux de l'Intelligence Artificielle et de l'Explicabilité"
---
# Lexique des Fondamentaux de l'Intelligence Artificielle et de l'Explicabilité

导出时间: 13/06/2026 06:40:32

---

Voici les termes techniques extraits du document, classés par ordre alphabétique, avec leur définition reformulée en une phrase et la page source :

| Terme technique                                 | Définition reformulée en une phrase                                                                                                                                                                                                              | Page source    |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Algorithme                                      | Suite d'instructions formelles et explicites données à une machine, notion qui doit être distinguée de la structure abstraite du modèle d'apprentissage-machine lui-même[1].                                                                 | Page 29        |
| Apprentissage-machine (Machine Learning, ML)    | Méthode de l'intelligence artificielle qui s'adapte statistiquement en associant des données de manière performante, sans que toutes ses règles d'association soient formulées explicitement par des concepteurs[2].                          | Page 29        |
| Arbres de décision (CART)                      | Méthode prédictive qui divise de manière séquentielle les individus en groupes de plus en plus purs, en appliquant des conditions successives sur leurs caractéristiques[3],[4].                                                              | Pages 53-54    |
| Boîte noire                                    | Caractéristique d'un modèle d'IA dont la complexité architecturale, les approximations informatiques et les ajustements automatiques rendent le cheminement interne cognitivement insaisissable pour l'humain[5],[6],[7].                       | Pages 58, 63   |
| Calibration                                     | Propriété statistique cherchant à assurer que les scores ou probabilités de risque produits par un modèle correspondent véritablement à la fréquence réelle de l'évènement au sein de la population ciblée[8].                         | Page 221       |
| Classification                                  | Tâche d'un modèle consistant à séparer les données ou les individus en inférant pour chacun d'eux une catégorie préalablement définie, comme le remboursement ou le défaut d'un crédit[9].                                              | Page 30        |
| Courbe ROC                                      | Représentation graphique permettant de mesurer la performance globale d'un classifieur en évaluant l'arbitrage entre son taux de vrais positifs et son taux de faux positifs pour chaque seuil de décision imaginable[10],[11].                 | Pages 205-206  |
| Descente de gradient                            | Procédure mathématique et informatique d'optimisation par laquelle un réseau de neurones ajuste automatiquement ses paramètres (ou poids) de couche en couche, afin de minimiser son taux d'erreur[12],[13].                                   | Pages 46, 58   |
| Égalité des Chances (Equalized Odds, EO)      | Métrique d'équité algorithmique consistant à égaliser à la fois les taux de vrais positifs (TPR) et les taux de faux positifs (FPR) du modèle entre les différents groupes démographiques observés[14],[15].                             | Pages 186, 207 |
| Explicabilité post-hoc                         | Ensemble de techniques (comme LIME ou SHAP) intervenant après l'entraînement d'un modèle d'IA et visant à reconstituer, estimer ou quantifier l'influence de variables sur le cheminement cognitif du modèle[16],[17],[18].                   | Pages 68, 105  |
| Gradient boosting (Stimulation de gradient)     | Méthode prédictive extrêmement performante sur des données tabulaires consistant à assembler une séquence d'arbres de décision simples, chaque nouvel arbre apprenant à minimiser l'erreur résiduelle des précédents[19],[20].          | Page 56        |
| Indice de Gini                                  | Mesure statistique calculant le niveau d'impureté d'un groupe, ce qui permet aux arbres de décision d'identifier systématiquement la variable la plus pertinente pour diviser des individus[4],[21].                                            | Pages 54-55    |
| Intelligibilité                                | Dimension cruciale de l'explication consistant à adapter le discours sur l'IA et ses supports explicatifs aux catégories de compréhension, pratiques professionnelles et attentes de justice de l'utilisateur final[22],[23].                   | Pages 31, 136  |
| Intelligence Artificielle (IA)                  | Vaste domaine de recherche technique visant à automatiser ou simuler par une machine les tâches propres à l'intelligence humaine, dont les succès récents reposent grandement sur l'apprentissage-machine[24].                                | Page 29        |
| Interchange Intervention Training (IIT)         | Méthode de transparence contraignant l'IA durant son entraînement à réagir aux perturbations (interventions) sur ses données d'entrée exactement de la même manière qu'un modèle causal simplifié de haut niveau[25],[26].               | Pages 86-87    |
| Justification                                   | Dimension de l'explication d'un modèle d'IA s'attachant à rendre compte de la représentation du monde et des valeurs d'égalité de traitement que véhiculent ou reflètent les prédictions algorithmiques[27],[28].                          | Pages 31, 153  |
| Modèle (d'apprentissage-machine)               | Structure mathématique et abstraite entraînée pour inférer une sortie probable à partir de la représentation mathématique de caractéristiques données en entrées[29].                                                                    | Page 29        |
| Modèle causal structurel (SCM)                 | Formalisation rigoureuse de la causalité d'un système qui nécessite l'identification exhaustive des variables (observées et inobservées) ainsi que des mécanismes déterministes menant d'une cause à une prédiction[30],[31].             | Page 88        |
| Paradoxe de Simpson                             | Phénomène statistique et conceptuel dans lequel une tendance perçue au niveau d'un échantillon global s'inverse ou disparaît totalement lorsqu'on examine ce même échantillon selon des lectures conditionnelles aux vrais labels[32],[33]. | Pages 198-202  |
| Parité Démographique (Demographic Parity, DP) | Standard d'équité algorithmique réclamant que le taux global de sélection ou de prédiction positive soit strictement identique d'un groupe protégé à un autre [par exemple, entre hommes et femmes](34),[35].                              | Page 174       |
| Précision (Valeur Prédictive Positive)        | Ratio statistique mesurant, parmi tous les individus que le modèle a classés comme positifs (par exemple fortunés), la proportion exacte de ceux qui détiennent réellement cette caractéristique[36].                                        | Page 211       |
| Prédiction (Efficacité prédictive)           | Capacité statistique globale d'un modèle d'apprentissage-machine à identifier avec exactitude des profils cibles sur des données d'entraînement, et à généraliser cette même exactitude sur des données inédites[37],[38].              | Page 30        |
| Reliance (Dépendance acceptée)                | Forme de confiance en acte par laquelle un agent accepte concrètement de s'en remettre à la prédiction d'une IA [par exemple, en refusant de vérifier ou d'outrepasser manuellement son alerte](39),[40].                                      | Page 267       |
| Réseaux de neurones par graphes (GNN)          | Outils d'apprentissage-machine performants qui distillent l'information en s'appuyant sur la similarité et la proximité (voisinage) d'individus représentés spatialement comme des nœuds connectés[41],[42].                                 | Pages 97-98    |
| Taux de Faux Positifs (FPR)                     | Pourcentage mesurant la proportion d'individus ne possédant pas la caractéristique ciblée, mais que le classifieur a sélectionnées et classées à tort dans cette catégorie[14].                                                            | Page 186       |
| Taux de Vrais Positifs (TPR / Rappel)           | Pourcentage évaluant quelle part des individus possédant véritablement la caractéristique ciblée dans la réalité a été correctement détectée et classée par le modèle d'IA[14],[36].                                                  | Pages 186, 211 |
| Transparence fonctionnelle                      | Dimension descriptive de l'explication consistant à expliciter, reconstituer ou contraindre les mécanismes internes reliant les entrées aux sorties pour éclaircir le cheminement de l'IA[27],[16].                                            | Pages 31, 68   |
| Valeurs de Shapley                              | Concept mathématique issu de la théorie des jeux largement réemployé en IA pour évaluer et quantifier la contribution ou l'influence marginale spécifique de chaque variable dans la prédiction finale du modèle[43],[44].                 | Page 70        |
| XIA (IA explicable)                             | Domaine de recherche foisonnant produisant des solutions techniques pour rendre descriptibles les modèles opaques d'apprentissage-machine et donner un sens contextuel à leurs classifications individuelles[45],[46].                           | Pages 67, 255  |

---

## Sources citées

[1] Souverain_2024_These.pdf
[2] Souverain_2024_These.pdf
[3] Souverain_2024_These.pdf
[4] Souverain_2024_These.pdf
[5] Souverain_2024_These.pdf
[6] Souverain_2024_These.pdf
[7] Souverain_2024_These.pdf
[8] Souverain_2024_These.pdf
[9] Souverain_2024_These.pdf
[10] Souverain_2024_These.pdf
[11] Souverain_2024_These.pdf
[12] Souverain_2024_These.pdf
[13] Souverain_2024_These.pdf
[14] Souverain_2024_These.pdf
[15] Souverain_2024_These.pdf
[16] Souverain_2024_These.pdf
[17] Souverain_2024_These.pdf
[18] Souverain_2024_These.pdf
[19] Souverain_2024_These.pdf
[20] Souverain_2024_These.pdf
[21] Souverain_2024_These.pdf
[22] Souverain_2024_These.pdf
[23] Souverain_2024_These.pdf
[24] Souverain_2024_These.pdf
[25] Souverain_2024_These.pdf
[26] Souverain_2024_These.pdf
[27] Souverain_2024_These.pdf
[28] Souverain_2024_These.pdf
[29] Souverain_2024_These.pdf
[30] Souverain_2024_These.pdf
[31] Souverain_2024_These.pdf
[32] Souverain_2024_These.pdf
[33] Souverain_2024_These.pdf
[34] Souverain_2024_These.pdf
[35] Souverain_2024_These.pdf
[36] Souverain_2024_These.pdf
[37] Souverain_2024_These.pdf
[38] Souverain_2024_These.pdf
[39] Souverain_2024_These.pdf
[40] Souverain_2024_These.pdf
[41] Souverain_2024_These.pdf
[42] Souverain_2024_These.pdf
[43] Souverain_2024_These.pdf
[44] Souverain_2024_These.pdf
[45] Souverain_2024_These.pdf
[46] Souverain_2024_These.pdf
