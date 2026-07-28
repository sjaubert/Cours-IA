# Guide d'Activité : Analyse Financière & Stratégique (RAG)

## Contexte du Scénario
Vous êtes analyste junior chez "InvestCorp", un fonds d'investissement. Votre directeur vous demande d'analyser la situation de l'entreprise **EcoTech Solutions** avant une potentielle prise de participation.
Vous disposez de deux documents :
1.  Le **Rapport Annuel 2024** (Public, officiel).
2.  Une **Transcription confidentielle** d'une réunion du Comité Exécutif (Fuite interne).

## Objectifs Pédagogiques
*   Utiliser l'IA pour synthétiser rapidement des documents volumineux.
*   Confronter des sources d'informations contradictoires (Cross-referencing).
*   Identifier les signaux faibles et les incohérences ("Hallucinations" vs "Mensonges par omission").
*   Produire une note de synthèse structurée.

---

## Partie 1 : Instructions pour l'Apprenant

### Étape 1 : Ingestion et Synthèse
1.  Ouvrez votre interface de chat avec l'IA.
2.  Uploadez le fichier `Rapport_Annuel_2024.md`.
3.  **Prompt suggéré** :
    > "Agis comme un analyste financier expert. Analyse ce rapport annuel et fais-moi une synthèse des points clés : Santé financière (CA, EBITDA, Cash Flow), Stratégie, et Risques majeurs. Sois factuel."

### Étape 2 : Confrontation (Le "Levier Cognitif")
1.  Uploadez maintenant le fichier `Transcription_Reunion_Strategique.txt`.
2.  **Prompt suggéré** :
    > "Je te fournis maintenant la transcription d'une réunion confidentielle du Comex de cette même entreprise. Compare les déclarations faites dans cette réunion avec les chiffres et affirmations du rapport annuel. Identifie toutes les incohérences, omissions ou contradictions. Présente-les sous forme de tableau : [Sujet] | [Version Officielle] | [Version Confidentielle] | [Niveau de Risque]."

### Étape 3 : Production du Livrable
1.  **Prompt suggéré** :
    > "Rédige une note de synthèse pour mon directeur d'investissement. Titre : 'Note d'alerte - EcoTech Solutions'. Résume les risques cachés que nous avons découverts (Problèmes Vietnam, Impayés LatAm, Litige Brésil, Fournisseur Lithium). Conclus par une recommandation : Faut-il investir ?"

---

## Partie 2 : Guide pour le Formateur (Solutions & Clés de lecture)

### Les "Pièges" à faire découvrir
L'IA doit permettre aux apprenants de découvrir les écarts suivants :

| Sujet | Version Officielle (Rapport Annuel) | Réalité (Transcription Comex) |
| :--- | :--- | :--- |
| **Cash Flow** | Baisse due aux stocks & investissements (Stratégique). | Baisse due aux **impayés clients** (15M€) en Amérique Latine. |
| **Usine Vietnam** | Opérationnelle depuis oct. 2024. | Tourne à **60%**, taux de rebut 8%, perte d'argent. |
| **Marge** | Impactée par l'inflation générale. | Impactée par la perte d'un **fournisseur clé** (achat au prix fort). |
| **Litige Brésil** | Risque faible, provision 0.5M€. | Risque élevé, **10-12M€** potentiels. |

### Points de vigilance (Debriefing)
*   **L'IA a-t-elle tout vu ?** Parfois, l'IA peut être "naïve" et croire le rapport officiel si le prompt n'est pas assez incisif sur la demande de *contradiction*.
*   **Hallucinations** : Vérifier que l'IA n'invente pas de chiffres qui ne sont dans aucun des deux documents.
*   **Biais de confirmation** : Si l'apprenant demande "Confirme que tout va bien", l'IA pourrait minimiser les risques de la transcription.
*   **Valeur ajoutée de l'humain** : L'IA trouve les écarts, mais c'est l'humain qui juge de la *gravité* éthique et financière (ex: la dissimulation volontaire du CEO).
