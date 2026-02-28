# Plan d'Action : Document LaTeX sur la FSP et la Fonction Zêta de Riemann

Ce document détaille les étapes pour la création du cours niveau Master Mathématiques sur le rôle central de la Formule Sommatoire de Poisson (FSP) dans la théorie de la fonction Zêta de Riemann.

## Tâches

- [x] **Étape 1 : Veille et Extraction via NotebookLM**
  - Requêter le carnet "Poisson Summation and the Bridge of Divergent Series" pour s'imprégner de l'approche pédagogique et obtenir les éléments de contexte spécifiques mentionnés dans le document source.

- [x] **Étape 2 : Structuration du Document LaTeX**
  - Mettre en place le préambule LaTeX incluant l'identité visuelle obligatoire (Logo Pôle Formation UIMM - CVDL, Nom du formateur S. JAUBERT dans les en-têtes et pieds de page).
  - Définir les sections demandées :
    1. Introduction et rappels sur la fonction Zêta ($\zeta(s)$) et la transformée de Fourier.
    2. Le passage par la fonction Thêta de Jacobi (Symétrie modulaire et inversion).
    3. Le prolongement analytique de $\zeta(s)$ via la transformée de Mellin.
    4. La preuve de l'équation fonctionnelle ($\xi(s) = \xi(1-s)$).
    5. La preuve directe par annulation des infinis (régularisation avec $f(t) = |t|^{-s}$).
    6. L'équivalence mathématique stricte entre FSP et équation fonctionnelle.
    7. Conclusion : Vision moderne et Généralisation de Tate (Adèles).

- [x] **Étape 3 : Rédaction des Démonstrations (Niveau Master)**
  - Développer de manière rigoureuse les calculs : transformées, inversion série-intégrale, symétrie intégrale de 0 à 1 et de 1 à l'infini, prolongement et propriétés analytiques.

- [x] **Étape 4 : Création et Compilation**
  - Enregistrer le fichier dans un nouveau sous-répertoire distinctif : `NoteBLM/Poisson_Zeta_Riemann/poisson_zeta_riemann.tex`.

## Critères de Validation

- Le niveau mathématique cible est respecté.
- Les identifiants formateurs et logos sont présents sur toutes les pages.
- Le document couvre l'intégralité des 5 points et de la conclusion demandés.
