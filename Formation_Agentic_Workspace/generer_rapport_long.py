#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de Rapport Annuel Substantiel
Crée un rapport fictif d'environ 50+ pages pour démonstration IA
"""

import random
from datetime import datetime

def generer_rapport():
    """Génère un rapport annuel détaillé et réaliste"""
    
    rapport = []
    
    # En-tête
    rapport.append("=" * 80)
    rapport.append("RAPPORT ANNUEL 2023")
    rapport.append("DIGITECH SOLUTIONS S.A.")
    rapport.append("Document d'Enregistrement Universel")
    rapport.append("=" * 80)
    rapport.append("\n" * 3)
    
    # Table des matières
    rapport.append("TABLE DES MATIÈRES")
    rapport.append("-" * 80)
    rapport.append("\n1. MESSAGE DU PRÉSIDENT")
    rapport.append("2. PRÉSENTATION DU GROUPE")
    rapport.append("3. GOUVERNANCE ET ORGANISATION")
    rapport.append("4. ANALYSE FINANCIÈRE DÉTAILLÉE")
    rapport.append("5. ACTIVITÉS ET PERFORMANCES PAR DIVISION")
    rapport.append("6. RESSOURCES HUMAINES")
    rapport.append("7. INNOVATION ET R&D")
    rapport.append("8. RESPONSABILITÉ SOCIÉTALE (RSE)")
    rapport.append("9. GESTION DES RISQUES")
    rapport.append("10. PERSPECTIVES ET STRATÉGIE 2024")
    rapport.append("11. ANNEXES ET DONNÉES COMPLÉMENTAIRES")
    rapport.append("\n" * 3)
    
    # 1. MESSAGE DU PRÉSIDENT
    rapport.append("\n" + "=" * 80)
    rapport.append("1. MESSAGE DU PRÉSIDENT")
    rapport.append("=" * 80 + "\n")
    rapport.append("""
Chers actionnaires, partenaires et collaborateurs,

L'année 2023 restera dans l'histoire de DigiTech Solutions comme une année
charnière, marquée par une transformation profonde de notre modèle économique
et une accélération sans précédent de notre croissance internationale.

Dans un contexte économique mondial caractérisé par une forte volatilité et
des tensions géopolitiques persistantes, notre groupe a su faire preuve de
résilience et d'agilité. Nous avons enregistré une croissance organique de
18,5%, portant notre chiffre d'affaires consolidé à 2,4 milliards d'euros,
contre 2,03 milliards en 2022.

Cette performance remarquable s'explique par plusieurs facteurs clés :

1. L'ACCÉLÉRATION DE NOTRE TRANSFORMATION DIGITALE
Notre investissement massif dans l'intelligence artificielle et le cloud
computing a porté ses fruits. Notre nouvelle plateforme DigitalCore AI,
lancée en mars 2023, a déjà conquis plus de 1 200 clients entreprises dans
15 pays, générant un chiffre d'affaires récurrent de 340 millions d'euros.

2. L'EXPANSION GÉOGRAPHIQUE STRATÉGIQUE
Notre implantation réussie en Asie-Pacifique, avec l'ouverture de bureaux
à Singapour, Tokyo et Sydney, nous positionne désormais comme un acteur
véritablement global. La région Asie représente maintenant 22% de notre
chiffre d'affaires total, contre seulement 8% en 2022.

3. LES ACQUISITIONS CIBLÉES
L'acquisition de CloudSecure Technologies en juin 2023 pour 450 millions
d'euros nous a permis de renforcer significativement notre offre en
cybersécurité, un marché en croissance exponentielle. Cette opération
stratégique contribue déjà positivement à nos résultats.

4. L'ENGAGEMENT DE NOS ÉQUIPES
Nos 12 500 collaborateurs répartis dans 28 pays ont fait preuve d'un
engagement exceptionnel. Leur expertise, leur créativité et leur détermination
sont les véritables moteurs de notre succès.

RÉSULTATS FINANCIERS SOLIDES

Les performances opérationnelles se traduisent par des résultats financiers
robustes :
- Chiffre d'affaires : 2,4 milliards d'euros (+18,5%)
- EBITDA : 456 millions d'euros (+22,3%)
- Résultat opérationnel : 312 millions d'euros (+19,8%)
- Résultat net part du groupe : 218 millions d'euros (+16,4%)
- Free cash-flow : 285 millions d'euros (+24,1%)

Notre marge d'EBITDA atteint 19%, en progression de 60 points de base,
témoignant de l'amélioration continue de notre efficacité opérationnelle.

DIVIDENDE ET CRÉATION DE VALEUR

Fort de ces excellents résultats, le Conseil d'Administration proposera à
l'Assemblée Générale du 15 mai 2024 un dividende de 2,80 euros par action,
en hausse de 16,7% par rapport à 2022, représentant un taux de distribution
de 35% du résultat net.

RESPONSABILITÉ SOCIÉTALE ET ENVIRONNEMENTALE

Notre engagement RSE s'est renforcé en 2023 avec des résultats concrets :
- Réduction de 32% de nos émissions de CO2 (scope 1 et 2) par rapport à 2022
- 45% de femmes dans les postes de direction (+8 points)
- 98% de nos datacenters alimentés par des énergies renouvelables
- 15 000 heures de formation continue par collaborateur en moyenne
- Notation ESG : A- (MSCI), confirmant notre leadership sectoriel

STRATÉGIE ET PERSPECTIVES 2024

Pour 2024, nous poursuivons notre ambition de croissance rentable avec
trois priorités stratégiques :

1. Consolidation de notre leadership en IA générative
2. Expansion accélérée sur le marché nord-américain
3. Renforcement de notre excellence opérationnelle

Nous visons une croissance organique du chiffre d'affaires comprise entre
15% et 17% et une marge d'EBITDA supérieure à 19,5%.

REMERCIEMENTS

Je tiens à remercier chaleureusement nos actionnaires pour leur confiance
constante, nos clients pour leur fidélité, nos partenaires pour leur
collaboration, et tout particulièrement nos collaborateurs dont le talent
et l'engagement font la force de DigiTech Solutions.

Ensemble, nous construisons le leader technologique européen de demain.

Jean-Philippe MOREAU
Président-Directeur Général
""")
    
    # 2. PRÉSENTATION DU GROUPE
    rapport.append("\n" + "=" * 80)
    rapport.append("2. PRÉSENTATION DU GROUPE")
    rapport.append("=" * 80 + "\n")
    rapport.append("""
2.1 HISTORIQUE ET ÉVOLUTION

DigiTech Solutions S.A. a été fondée en 1998 par trois ingénieurs diplômés
de l'École Polytechnique : Jean-Philippe Moreau, Marie Dubois et Laurent
Chen. Initialement spécialisée dans le développement de logiciels de gestion
pour PME, la société a rapidement évolué vers des solutions d'entreprise
plus complexes.

DATES CLÉS :
- 1998 : Création de DigiTech Solutions à Paris (5 collaborateurs)
- 2002 : Lancement de notre première suite ERP "DigiManage 1.0"
- 2005 : Introduction en Bourse sur Euronext Paris (valorisation : 45M€)
- 2008 : Franchissement du cap des 100 millions d'euros de CA
- 2011 : Acquisition de SoftCloud GmbH (Allemagne) - expansion européenne
- 2014 : Lancement de notre plateforme Cloud "DigiCloud Enterprise"
- 2017 : Ouverture du premier centre R&D en intelligence artificielle
- 2019 : Dépassement du milliard d'euros de chiffre d'affaires
- 2021 : Acquisition de DataAnalytics Pro (leader en Big Data)
- 2023 : Acquisition de CloudSecure Technologies - CA : 2,4 Mds€

En 25 ans, DigiTech Solutions est devenue une entreprise technologique
de référence en Europe, employant plus de 12 500 personnes dans 28 pays
et servant plus de 8 500 clients entreprises à travers le monde.

2.2 MODÈLE ÉCONOMIQUE

Notre modèle économique repose sur trois piliers complémentaires :

A) LICENCES ET ABONNEMENTS SOFTWARE (52% du CA)
Commercialisation en mode SaaS de nos solutions logicielles avec des
contrats récurrents allant de 12 à 60 mois. Taux de rétention client : 94%.

B) SERVICES PROFESSIONNELS (31% du CA)
Intégration, conseil, formation et support pour accompagner nos clients
dans leur transformation digitale. Marge opérationnelle : 16,5%.

C) INFRASTRUCTURE CLOUD (17% du CA)
Hébergement et gestion d'infrastructures cloud privées et hybrides.
Forte croissance (+34% en 2023) avec une marge récurrente élevée (28%).

2.3 CHIFFRES CLÉS 2023

DONNÉES FINANCIÈRES
- Chiffre d'affaires : 2 412 M€
- EBITDA : 456 M€ (marge : 19,0%)
- Résultat opérationnel : 312 M€
- Résultat net : 218 M€
- Free cash-flow : 285 M€
- Investissements R&D : 193 M€ (8% du CA)
- Dette nette : 423 M€ (ratio dette/EBITDA : 0,93x)

DONNÉES OPÉRATIONNELLES
- Collaborateurs : 12 547 (vs 10 890 en 2022)
- Pays de présence : 28
- Clients actifs : 8 672
- Nouveaux clients 2023 : 1 845
- Taux de rétention : 94%
- NPS (Net Promoter Score) : 68

DONNÉES RSE
- Émissions CO2 (scope 1&2) : 18 500 tonnes (-32% vs 2022)
- Femmes cadres dirigeants : 45%
- Heures de formation : 187 500 heures
- Taux d'accidents : 0,12 (en baisse)
- Score ESG MSCI : A-

2.4 RÉPARTITION GÉOGRAPHIQUE DU CHIFFRE D'AFFAIRES (M€)

Europe :                    1 545 M€    (64%)
  - France :                  782 M€    (32%)
  - Allemagne :               385 M€    (16%)
  - Royaume-Uni :             201 M€    (8%)
  - Autres Europe :           177 M€    (7%)

Asie-Pacifique :             531 M€    (22%)
  - Singapour :               198 M€    (8%)
  - Japon :                   156 M€    (6%)
  - Australie :                98 M€    (4%)
  - Autres APAC :              79 M€    (3%)

Amériques :                  241 M€    (10%)
  - États-Unis :              167 M€    (7%)
  - Canada :                   42 M€    (2%)
  - Amérique latine :          32 M€    (1%)

Moyen-Orient & Afrique :      95 M€    (4%)

2.5 ORGANISATION DU GROUPE

Le groupe DigiTech Solutions s'organise autour de 4 divisions opérationnelles :

ENTERPRISE SOLUTIONS DIVISION (ESD)
- CA 2023 : 1 124 M€ (+12%)
- Effectifs : 4 850
- Solutions ERP, CRM, HCM pour grandes entreprises

CLOUD & INFRASTRUCTURE DIVISION (CID)
- CA 2023 : 687 M€ (+34%)
- Effectifs : 2 340
- Services cloud, hébergement, infrastructure as a service

AI & ANALYTICS DIVISION (AAD)
- CA 2023 : 412 M€ (+45%)
- Effectifs : 1 820
- Intelligence artificielle, machine learning, data analytics

CYBERSECURITY DIVISION (CSD)
- CA 2023 : 189 M€ (nouvelle division post-acquisition)
- Effectifs : 780
- Sécurité informatique, SOC, protection des données

FONCTIONS SUPPORT
- Effectifs : 2 757
- Fonctions : Finance, RH, Legal, Marketing, IT corporate
""")

    # 3. GOUVERNANCE
    rapport.append("\n" + "=" * 80)
    rapport.append("3. GOUVERNANCE ET ORGANISATION")
    rapport.append("=" * 80 + "\n")
    rapport.append("""
3.1 COMPOSITION DU CONSEIL D'ADMINISTRATION

Le Conseil d'Administration de DigiTech Solutions S.A. est composé de
12 membres, dont 8 administrateurs indépendants (67%), conformément aux
meilleures pratiques de gouvernance.

PRÉSIDENT-DIRECTEUR GÉNÉRAL
Jean-Philippe MOREAU (58 ans)
- Fondateur et PDG depuis 1998
- Diplômé de l'École Polytechnique et MBA INSEAD
- Détient 8,2% du capital

ADMINISTRATEURS INDÉPENDANTS

Marie LECLERC (62 ans) - Administratrice référente
- Ex-DG France d'Oracle Corporation
- Présidente du Comité d'Audit
- Membre du Comité Stratégie & Innovation

Philippe BERNARD (55 ans)
- Partner chez Accel Partners (fonds d'investissement)
- Président du Comité des Rémunérations
- Membre du Comité d'Audit

Sophie MARTIN (49 ans)
- Professeure d'économie à Sciences Po Paris
- Experte en transformation digitale
- Membre du Comité RSE

David CHEN (51 ans)
- Ex-CTO de SAP EMEA
- Président du Comité Stratégie & Innovation
- Membre du Comité des Rémunérations

Claire DUBOIS (47 ans)
- DRH du Groupe Schneider Electric
- Présidente du Comité RSE
- Membre du Comité des Rémunérations

Thomas ROUX (59 ans)
- PDG de ConsultingTech Partners
- Membre du Comité d'Audit
- Membre du Comité Stratégie & Innovation

Isabelle AUBERT (53 ans)
- CFO du Groupe Atos
- Membre du Comité d'Audit

Laurent PETIT (46 ans)
- Entrepreneur et Business Angel
- Membre du Comité Stratégie & Innovation

ADMINISTRATEURS NON INDÉPENDANTS

Marie DUBOIS (56 ans)
- Co-fondatrice, Directrice Innovation
- Détient 6,8% du capital

Laurent CHEN (57 ans)
- Co-fondateur, CTO Groupe
- Détient 5,4% du capital

Représentant des salariés : Julien MOREAU (42 ans)
- Directeur Technique Division Cloud

Représentant des salariés : Émilie ROUSSEAU (38 ans)
- Responsable RH France

3.2 COMITÉS SPÉCIALISÉS

COMITÉ D'AUDIT (4 réunions en 2023)
Présidente : Marie Leclerc
Membres : Philippe Bernard, Thomas Roux, Isabelle Aubert
Mission : Supervision des comptes, contrôle interne, audit, risques

COMITÉ DES RÉMUNÉRATIONS (3 réunions en 2023)
Président : Philippe Bernard
Membres : David Chen, Claire Dubois
Mission : Politique de rémunération dirigeants et mandataires

COMITÉ RSE & DÉVELOPPEMENT DURABLE (4 réunions en 2023)
Présidente : Claire Dubois
Membres : Sophie Martin, Marie Dubois
Mission : Stratégie RSE, objectifs climat, diversité, éthique

COMITÉ STRATÉGIE & INNOVATION (5 réunions en 2023)
Président : David Chen
Membres : Marie Leclerc, Thomas Roux, Laurent Petit, Marie Dubois
Mission : Orientations stratégiques, M&A, innovation, R&D

3.3 DIRECTION GÉNÉRALE ET COMITÉ EXÉCUTIF

PRÉSIDENT-DIRECTEUR GÉNÉRAL
Jean-Philippe MOREAU

DIRECTEUR GÉNÉRAL DÉLÉGUÉ
Antoine LAMBERT (52 ans)
- Responsable des opérations et de l'exécution stratégique

COMITÉ EXÉCUTIF (COMEX) - 10 membres

CFO - Directeur Financier
Nathalie GIRARD (48 ans)
- Ex-CFO Dassault Systèmes
- Membre du COMEX depuis 2019

COO - Directeur des Opérations
Marc FONTAINE (45 ans)
- Ex-VP Operations Google Cloud EMEA
- Membre du COMEX depuis 2021

CTO - Directeur Technique Groupe
Laurent CHEN (57 ans)
- Co-fondateur
- Membre du COMEX depuis 1998

CSIO - Chief Strategy & Innovation Officer
Marie DUBOIS (56 ans)
- Co-fondatrice
- Membre du COMEX depuis 1998

DRH - Directrice Ressources Humaines Groupe
Valérie RENAUD (51 ans)
- Ex-DRH Capgemini France
- Membre du COMEX depuis 2018

CMO - Directrice Marketing & Communication
Sandrine MOREL (43 ans)
- Ex-VP Marketing ServiceNow EMEA
- Membre du COMEX depuis 2020

EVP Enterprise Solutions Division
François BLANC (49 ans)
- 15 ans d'expérience chez SAP
- Membre du COMEX depuis 2017

EVP Cloud & Infrastructure Division
Karim BEN SALAH (46 ans)
- Ex-VP AWS EMEA South
- Membre du COMEX depuis 2022

EVP AI & Analytics Division
Dr. Lisa WANG (41 ans)
- PhD Stanford, ex-Google Research
- Membre du COMEX depuis 2020

EVP Cybersecurity Division
Robert O'CONNOR (54 ans)
- Ex-CISO Airbus Group
- Membre du COMEX depuis 2023 (post-acquisition)

3.4 RÉMUNÉRATION DES DIRIGEANTS 2023

PRÉSIDENT-DIRECTEUR GÉNÉRAL (Jean-Philippe MOREAU)
- Rémunération fixe :             850 000 €
- Rémunération variable :         1 275 000 € (150% du fixe atteint)
- Avantages en nature :            45 000 €
- Jetons de présence :             35 000 €
- Options/Actions gratuites :     450 000 € (valorisation IFRS2)
TOTAL :                          2 655 000 €

DIRECTEUR GÉNÉRAL DÉLÉGUÉ (Antoine LAMBERT)
- Rémunération fixe :             550 000 €
- Rémunération variable :         715 000 € (130% du fixe atteint)
- Avantages en nature :            28 000 €
- Options/Actions gratuites :     275 000 € (valorisation IFRS2)
TOTAL :                          1 568 000 €

Total rémunération mandataires dirigeants : 4 223 000 €

POLITIQUE DE RÉMUNÉRATION VARIABLE
La part variable est basée sur des critères :
- Quantitatifs (70%) : CA, EBITDA, FCF, NPS client
- Qualitatifs (30%) : Objectifs stratégiques, ESG, innovation

3.5 ACTIONNARIAT AU 31/12/2023

Fondateurs et management :        20,4%
  - Jean-Philippe Moreau           8,2%
  - Marie Dubois                   6,8%
  - Laurent Chen                   5,4%

Investisseurs institutionnels :   62,3%
  - BlackRock Inc.                 8,7%
  - Vanguard Group                 6,4%
  - Amundi Asset Management        5,9%
  - Fidelity Investments           4,8%
  - Autres institutionnels        36,5%

Salariés (actionnariat) :          4,1%

Flottant public :                 13,2%

Nombre total d'actions : 78 456 892 actions
Cours au 31/12/2023 : 87,50 €
Capitalisation boursière : 6,87 Mds €
""")

    # 4. ANALYSE FINANCIÈRE
    rapport.append("\n" + "=" * 80)
    rapport.append("4. ANALYSE FINANCIÈRE DÉTAILLÉE")
    rapport.append("=" * 80 + "\n")
    
    # Générer des tableaux financiers détaillés
    for annee in range(2019, 2024):
        ca = 1450 + (annee - 2019) * 190 + random.randint(-20, 40)
        ebitda = int(ca * 0.19)
        resultat_op = int(ca * 0.13)
        resultat_net = int(ca * 0.09)
        
        rapport.append(f"\nANNÉE {annee}")
        rapport.append(f"Chiffre d'affaires : {ca} M€")
        rapport.append(f"EBITDA : {ebitda} M€ ({int(ebitda/ca*100)}%)")
        rapport.append(f"Résultat opérationnel : {resultat_op} M€")
        rapport.append(f"Résultat net : {resultat_net} M€")
        rapport.append(f"Free cash-flow : {int(resultat_net * 1.3)} M€")
        rapport.append("")
    
    rapport.append("""
4.1 COMPTE DE RÉSULTAT CONSOLIDÉ (en millions d'euros)

                                        2023      2022      Var %
Chiffre d'affaires                    2 412     2 034     +18,5%

  Licences et abonnements             1 254     1 058     +18,5%
  Services professionnels               748       651     +14,9%
  Infrastructure cloud                  410       325     +26,2%

Achats consommés                       (385)     (331)    +16,3%
Charges de personnel                 (1 156)   (1 002)    +15,4%
Autres charges opérationnelles         (415)     (361)    +15,0%

EBITDA                                  456       340     +34,1%
Marge d'EBITDA                        19,0%     16,7%    +230 bp

Dotations aux amortissements           (144)     (120)    +20,0%

RÉSULTAT OPÉRATIONNEL                   312       220     +41,8%
Marge opérationnelle                  12,9%     10,8%    +210 bp

Produits financiers                      18        12     +50,0%
Charges financières                     (32)      (28)    +14,3%

RÉSULTAT AVANT IMPÔTS                   298       204     +46,1%

Impôts sur les sociétés                 (80)      (54)    +48,1%
Taux effectif d'impôt                 26,8%     26,5%

RÉSULTAT NET                            218       150     +45,3%
dont part du groupe                     218       150     +45,3%
dont intérêts minoritaires                0         0

BPA (en euros)                         2,78      1,91     +45,5%
BPA dilué (en euros)                   2,72      1,88     +44,7%

4.2 BILAN CONSOLIDÉ (en millions d'euros)

ACTIF                                 2023      2022
Goodwill                               892       523
Immobilisations incorporelles          456       312
Immobilisations corporelles            287       245
Actifs financiers                       89        67
Impôts différés actifs                  45        38
ACTIFS NON COURANTS                  1 769     1 185

Stocks                                  12        10
Créances clients                       498       412
Autres créances                         87        72
Trésorerie et équivalents              412       358
ACTIFS COURANTS                      1 009       852

TOTAL ACTIF                          2 778     2 037

PASSIF
Capital social                          78        78
Primes et réserves                   1 245       998
Résultat de l'exercice                 218       150
CAPITAUX PROPRES                     1 541     1 226

Dettes financières LT                  675       423
Provisions LT                           67        54
Impôts différés passifs                 34        28
PASSIFS NON COURANTS                   776       505

Dettes financières CT                  160       112
Dettes fournisseurs                    178       134
Dettes fiscales et sociales             87        42
Autres dettes                           36        18
PASSIFS COURANTS                       461       306

TOTAL PASSIF                         2 778     2 037

Dette nette                            423       177
Ratio dette nette / EBITDA           0,93x     0,52x

4.3 TABLEAU DES FLUX DE TRÉSORERIE (M€)

                                      2023      2022
Résultat net                           218       150
Amortissements                         144       120
Variation BFR                          (45)      (32)
Autres ajustements                      21        18
FLUX OPÉRATIONNELS                     338       256

Investissements corporels              (87)      (72)
Investissements incorporels            (45)      (38)
Acquisitions                          (450)      (85)
Autres investissements                 (12)       (8)
FLUX D'INVESTISSEMENT                 (594)     (203)

Augmentation de capital                  0         0
Émission d'emprunts                    350       120
Remboursement d'emprunts               (98)      (76)
Dividendes versés                     (167)     (145)
Rachats d'actions                       (15)       (9)
FLUX DE FINANCEMENT                     70      (110)

Variation trésorerie nette            (186)      (57)
Trésorerie début                       358       415
Trésorerie fin                         172       358

Trésorerie disponible                  412       358
Concours bancaires CT                 (240)        0
Trésorerie nette                       172       358

4.4 ANALYSE PAR DIVISION

ENTERPRISE SOLUTIONS DIVISION (ESD)
CA 2023 :                            1 124 M€    +12%
EBITDA :                               213 M€    19%
Effectifs :                            4 850
Principaux produits : DigiERP, DigiCRM, DigiHCM

Performance 2023 :
+ Croissance soutenue malgré un marché mature
+ Lancement réussi de DigiERP Cloud (migration SaaS)
+ 340 nouveaux clients grands comptes
+ Taux de renouvellement : 96%
- Pression concurrentielle sur les prix
- Ralentissement en Europe du Sud

CLOUD & INFRASTRUCTURE DIVISION (CID)
CA 2023 :                              687 M€    +34%
EBITDA :                               192 M€    28%
Effectifs :                            2 340
Principaux services : DigiCloud, Infrastructure Management

Performance 2023 :
+ Forte croissance portée par la migration cloud
+ Nouveaux datacenters à Singapour et Sydney
+ Partenariats stratégiques AWS et Azure
+ ARR (Annual Recurring Revenue) : 612 M€
- Investissements lourds en infrastructure
- Marges sous pression court terme

AI & ANALYTICS DIVISION (AAD)
CA 2023 :                              412 M€    +45%
EBITDA :                                78 M€    19%
Effectifs :                            1 820
Principaux produits : DigitalCore AI, DigiAnalytics Pro

Performance 2023 :
+ Succès majeur de DigitalCore AI (lancé en mars)
+ 1 200 clients en 9 mois
+ Investissements R&D : 85 M€ (21% du CA division)
+ Recrutement de 450 data scientists
+ Partenariat avec OpenAI et Google Cloud
- Division encore en phase d'investissement
- Marge EBITDA en amélioration

CYBERSECURITY DIVISION (CSD)
CA 2023 :                              189 M€    N/A
EBITDA :                                32 M€    17%
Effectifs :                              780
Principaux services : SOC, Threat Intelligence, Consulting

Performance 2023 :
+ Acquisition CloudSecure réussie (juin 2023)
+ Intégration en cours (8 mois de contribution)
+ Forte demande du marché
+ Pipeline commercial : 245 M€
+ Synergies avec autres divisions
+ Certifications ISO 27001, SOC2

4.5 INDICATEURS CLÉS DE PERFORMANCE (KPI)

INDICATEURS FINANCIERS
- Croissance organique du CA :        +15,2%
- Croissance totale du CA :           +18,5%
- Marge d'EBITDA :                     19,0%
- Marge opérationnelle :               12,9%
- Marge nette :                         9,0%
- ROE (Return on Equity) :             14,2%
- ROCE (Return on Capital Employed) :  16,8%
- Free Cash Flow :                    285 M€
- Conversion FCF / EBITDA :             62%

INDICATEURS OPÉRATIONNELS
- Nombre de clients :                  8 672
- Nouveaux clients :                   1 845
- Taux de rétention :                    94%
- NPS (Net Promoter Score) :             68
- ARR (Annual Recurring Revenue) :   1 854 M€
- CAC (Customer Acquisition Cost) :  48 K€
- LTV (Lifetime Value) :             892 K€
- Ratio LTV/CAC :                      18,6x

INDICATEURS RH
- Effectif total :                    12 547
- Recrutements nets :                  1 657
- Taux de turnover :                   11,2%
- % de femmes cadres :                   45%
- Heures de formation :              187 500
- eNPS (employee NPS) :                  54

INDICATEURS ESG
- Émissions CO2 (scope 1+2) :      18 500 t
- Réduction vs 2022 :                   -32%
- % d'énergies renouvelables :           98%
- Score ESG MSCI :                        A-
- Accidents du travail :               0,12

4.6 TRÉSORERIE ET ENDETTEMENT

STRUCTURE DE LA DETTE (31/12/2023)
Emprunt obligataire 2021-2026 (1,5%) :  300 M€
Crédit syndiqué revolving :             250 M€
Obligations convertibles 2022-2027 :    150 M€
Dettes de loyers IFRS 16 :               85 M€
Autres dettes financières :              25 M€
Concours bancaires CT :                 240 M€
DETTE FINANCIÈRE BRUTE :               1 050 M€

Trésorerie et équivalents :             412 M€
Placements financiers CT :              215 M€
TRÉSORERIE TOTALE :                     627 M€

DETTE NETTE :                           423 M€

Ratio dette nette / EBITDA :           0,93x
Ratio dette nette / capitaux propres : 27,4%
Ratio de couverture des intérêts :     9,8x

NOTATION DE CRÉDIT
Standard & Poor's :     BBB+ (perspective stable)
Moody's :               Baa1 (perspective positive)
Fitch :                 BBB+ (perspective stable)

La structure financière du groupe est saine avec un levier modéré et
une capacité de remboursement confortable. L'émission obligataire de
350 M€ en avril 2023 a permis de financer l'acquisition de CloudSecure
tout en maintenant une flexibilité financière importante.

Le crédit syndiqué revolving de 250 M€ n'est pas tiré au 31/12/2023,
offrant une liquidité additionnelle pour des opérations de croissance
externe opportunistes.

4.7 POLITIQUE D'ALLOCATION DU CAPITAL

Le Conseil d'Administration a défini une politique d'allocation du
capital équilibrée entre :

1. INVESTISSEMENTS ORGANIQUES (40-45% du FCF)
   - R&D et innovation : 193 M€ en 2023
   - Infrastructures IT : 87 M€
   - Développement commercial : 52 M€

2. CROISSANCE EXTERNE (25-30% du FCF)
   - Acquisitions stratégiques ciblées
   - Focus : IA, cybersécurité, expansion géographique
   - Ticket : 50 M€ à 500 M€

3. RÉMUNÉRATION ACTIONNAIRES (30-35% du FCF)
   - Dividende : taux de distribution cible 35% du RN
   - Rachats d'actions opportunistes : 15 M€ en 2023

Cette politique vise à maximiser la création de valeur long terme tout
en maintenant une structure financière solide et flexible.
""")

    # 5. ACTIVITÉS PAR DIVISION
    rapport.append("\n" + "=" * 80)
    rapport.append("5. ACTIVITÉS ET PERFORMANCES PAR DIVISION")
    rapport.append("=" * 80 + "\n")
    
    divisions = [
        "Enterprise Solutions Division",
        "Cloud & Infrastructure Division",
        "AI & Analytics Division",
        "Cybersecurity Division"
    ]
    
    for div in divisions:
        rapport.append(f"\n5.{divisions.index(div)+1} {div.upper()}\n")
        rapport.append(f"{'=' * 60}\n")
        
        # Générer du contenu détaillé pour chaque division
        for i in range(15):
            rapport.append(f"Section {i+1} : Performance détaillée trimestre {(i%4)+1}")
            rapport.append(f"Chiffre d'affaires : {random.randint(80, 350)} M€")
            rapport.append(f"Marge opérationnelle : {random.randint(12, 28)}%")
            rapport.append(f"Nombre de clients : {random.randint(500, 3000)}")
            rapport.append(f"Taux de satisfaction : {random.randint(82, 96)}%")
            rapport.append("")

    # 6-11. Autres sections
    sections = [
        "6. RESSOURCES HUMAINES",
        "7. INNOVATION ET R&D",
        "8. RESPONSABILITÉ SOCIÉTALE (RSE)",
        "9. GESTION DES RISQUES",
        "10. PERSPECTIVES ET STRATÉGIE 2024",
        "11. ANNEXES ET DONNÉES COMPLÉMENTAIRES"
    ]
    
    for section in sections:
        rapport.append("\n" + "=" * 80)
        rapport.append(section)
        rapport.append("=" * 80 + "\n")
        
        # Générer du contenu substantiel
        for paragraphe in range(30):
            rapport.append(f"\n{section.split('.')[1].strip()} - Sous-section {paragraphe + 1}")
            rapport.append("-" * 60)
            
            # Générer plusieurs lignes de contenu
            for ligne in range(random.randint(8, 15)):
                rapport.append(f"Analyse détaillée point {ligne + 1} : Données et métriques")
                rapport.append(f"Indicateur de performance : {random.randint(50, 250)} unités")
                rapport.append(f"Évolution par rapport à N-1 : {random.choice(['+', '-'])}{random.randint(2, 35)}%")
            rapport.append("")
    
    # Footer
    rapport.append("\n" * 3)
    rapport.append("=" * 80)
    rapport.append("FIN DU RAPPORT ANNUEL 2023")
    rapport.append(f"Document généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}")
    rapport.append("DigiTech Solutions S.A. - Tous droits réservés")
    rapport.append("=" * 80)
    
    return "\n".join(rapport)

def main():
    print("Génération du rapport annuel substantiel...")
    print("Cela peut prendre quelques secondes...")
    
    rapport_complet = generer_rapport()
    
    # Sauvegarder le rapport
    fichier_sortie = "data/Rapport_Annuel.txt"
    
    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        f.write(rapport_complet)
    
    # Statistiques
    nb_lignes = rapport_complet.count('\n')
    nb_caracteres = len(rapport_complet)
    nb_mots = len(rapport_complet.split())
    nb_pages_estimees = nb_caracteres // 3000  # ~3000 caractères par page
    
    print(f"\n✅ Rapport généré avec succès !")
    print(f"📄 Fichier : {fichier_sortie}")
    print(f"📊 Statistiques :")
    print(f"   - Lignes : {nb_lignes:,}")
    print(f"   - Caractères : {nb_caracteres:,}")
    print(f"   - Mots : {nb_mots:,}")
    print(f"   - Pages estimées : {nb_pages_estimees}")

if __name__ == "__main__":
    main()
