---
title: "Formation : L'Art du Prompt Engineering en Entreprise"
author: "S. JAUBERT - Pôle Formation UIMM - CVDL"
date: "2026"
---

![Logo UIMM](./Formation_Prompt/logo_uimm_placeholder.jpg){width=150px}
**Pôle Formation UIMM - CVDL** | Formateur : **S. JAUBERT**

***

# Formation : Techniques de Prompt pour l'Entreprise

## Introduction : L'importance d'un "Prompt" Parfait

Les grands modèles de langage (LLMs) peuvent produire n'importe quelle séquence de caractères, dans n'importe quel langage ou format. Cependant, la qualité de cette production est extrêmement variable. 

Le modèle peut fournir une réponse banale, remplie d'explications superflues, ou à l'inverse, rédiger un texte percutant, proposer un code informatique parfait ou analyser précisément un document complexe. La différence entre ces deux résultats réside dans une seule condition : **la qualité de votre instruction, ou "Prompt"**.

Cette formation vous donne les outils nécessaires pour construire des prompts maîtrisés et tirer le plein potentiel de l'intelligence artificielle pour vos tâches professionnelles.

## 1. Le Framework AUTOMAT

Le framework AUTOMAT définit les ingrédients clés d'une instruction parfaite pour structurer ce dont vous avez besoin :

- **A - Act as (Agir comme) :** Définir le rôle que doit jouer l'IA (ex: "Agis comme un analyste financier senior").
- **U - User Persona & Audience (Audience ciblée) :** Préciser à qui s'adresse le résultat.
- **T - Targeted Action (Action ciblée) :** Définir clairement l'objectif de la tâche.
- **O - Output Definition (Format de sortie) :** Indiquer sous quelle forme l'information doit être rendue (tableau, texte, etc.).
- **M - Mode / Tonality / Style (Ton et Style) :** Préciser la manière de communiquer (professionnel, concis, bienveillant).
- **A - Atypical Cases (Cas atypiques) :** Indiquer comment l'IA doit réagir face à des exceptions ou des données manquantes.
- **T - Topic Whitelisting (Sujets autorisés) :** Restreindre le périmètre des sujets abordables pour éviter les hors-sujets.

## 2. Le Framework CO-STAR

Une approche alternative et tout aussi efficace, centrée sur le contexte global :

- **C - Context (Contexte) :** Planter le décor et fournir les détails contextuels nécessaires à la compréhension.
- **O - Objective (Objectif) :** Définir la tâche à accomplir pour focaliser le résultat.
- **S - Style & Tone (Style et Ton) :** Habiller le texte avec le style d'écriture et l'émotion souhaités.
- **A - Audience (Audience) :** Connaître le lecteur final pour adapter le niveau de langage.
- **R - Response (Réponse) :** Choisir le format de sortie attendu.

## 3. Définir le Format de Sortie (Output Format)

La définition du format de sortie indique au modèle exactement comment présenter sa réponse. Mieux que de longues explications, n'hésitez pas à fournir un exemple réel du résultat attendu.

- Spécifiez les formats souhaités (ex: JSON, liste à puces, tableau Markdown).
- Définissez les valeurs et les limites autorisées.
- Donnez des instructions précises si les données sont indisponibles.

## 4. L'Apprentissage par l'Exemple (Few-Shot Learning)

Le "Few-Shot Learning" consiste à montrer au modèle quelques exemples de problèmes et de solutions avant qu'il ne commence sa tâche réelle :
- **Cas standards :** Montrer comment transformer les données d'entrée vers la sortie attendue.
- **Cas spéciaux :** Montrer comment traiter les valeurs aberrantes ou comment répondre si un utilisateur pose une question non pertinente.

## 5. La Chaîne de Pensée (Chain of Thought)

Forcer le modèle à "penser à voix haute" et à effectuer un raisonnement étape par étape avant de donner la réponse finale améliore considérablement la qualité des résultats, en particulier pour les problèmes complexes. Vous pouvez demander au modèle de séparer son raisonnement de sa réponse finale.

## 6. Les Modèles de Prompts (Templates)

Dans un cadre professionnel ou applicatif, on utilise rarement un prompt figé. Privilégiez des modèles (templates) contenant des variables à remplir selon la situation :
*Exemple : "Rédige un email de relance pour [NOM_DU_CLIENT] concernant la facture [NUMERO_FACTURE]."*

## 7. RAG (Retrieval Augmented Generation)

Le RAG est l'une des techniques les plus puissantes. Elle permet aux LLMs d'accéder à vos propres données ou documents d'entreprise pour répondre à une question. Cela permet de contourner les limites de connaissances du modèle et d'obtenir des réponses exhaustives, factuelles et à jour.

## 8. Formatage et Délimiteurs

Les modèles ne lisent votre prompt qu'une seule fois. Ils doivent comprendre instantanément la structure de vos informations (ce qui relève de l'instruction, de l'exemple ou du contexte).
Structurez vos requêtes en utilisant des caractères de délimitation clairs :
- Les hashtags (`###`) pour les titres.
- Les triples guillemets (`"""` ou `'''`) pour encadrer du texte source.
- Les sauts de ligne pour aérer.

## 9. Assemblage d'un Prompt Complexe

Pour un prompt complexe performant, l'ordre d'apparition des éléments est crucial. Une structure recommandée est la suivante :
1. L'instruction principale
2. Les exemples (Few-shot)
3. Les données de contexte
4. Le format de sortie exigé
5. L'historique de l'interaction (le cas échéant)

## 10. L'Approche Multi-Prompts

Pour une tâche très complexe (ex: traiter entièrement un dossier de sinistre), un seul prompt long est souvent insuffisant. Il est plus simple et plus précis de diviser la tâche en sous-tâches (catégorisation, vérification des données, calcul, réponse) gérées par une chaîne de requêtes séquentielles.

***

**Pôle Formation UIMM - CVDL** | Formateur : **S. JAUBERT**