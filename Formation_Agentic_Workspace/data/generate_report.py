import random
from datetime import datetime

def generate_report():
    sections = [
        ("1. INTRODUCTION", [
            "L'année 2024 a été une année charnière pour notre entreprise.",
            "Nous avons su naviguer dans un environnement économique complexe tout en maintenant nos objectifs de croissance.",
            "La résilience de nos équipes et la fidélité de nos clients ont été les piliers de notre succès.",
            "Ce rapport détaille nos performances financières, opérationnelles et sociales."
        ]),
        ("2. FAITS MARQUANTS", [
            "- Lancement réussi du produit 'SuperGadget 3000' en octobre, dépassant les prévisions de vente de 20%.",
            "- Expansion internationale avec l'ouverture de notre nouvelle filiale en Espagne, renforçant notre présence en Europe du Sud.",
            "- Recrutement de 20 nouveaux collaborateurs talentueux pour soutenir notre croissance.",
            "- Obtention de la certification ISO 9001, gage de notre engagement envers la qualité.",
            "- Partenariat stratégique signé avec TechGiant Corp pour le développement de solutions IA."
        ]),
        ("3. ANALYSE FINANCIERE", [
            "Le chiffre d'affaires a atteint 12 millions d'euros, soit une augmentation de 15% par rapport à l'année précédente.",
            "Le résultat net s'établit à 1.5 million d'euros, témoignant d'une gestion rigoureuse des coûts.",
            "L'EBITDA a progressé de 12%, atteignant 2.8 millions d'euros.",
            "Les investissements en R&D ont représenté 10% du CA, soulignant notre volonté d'innover.",
            "La trésorerie reste saine avec un flux de trésorerie disponible positif de 500k euros.",
            "Le ratio d'endettement a été réduit à 0.4, offrant une plus grande flexibilité financière."
        ]),
        ("4. RESSOURCES HUMAINES", [
            "L'effectif total est passé à 150 employés, avec une parité hommes-femmes améliorée (45% de femmes).",
            "Nous avons investi 50k euros dans la formation continue, avec un focus sur les compétences numériques.",
            "Le taux de turnover a diminué de 2 points pour s'établir à 8%.",
            "Un nouveau plan d'épargne entreprise a été mis en place pour associer les salariés aux résultats.",
            "L'enquête de satisfaction interne révèle un taux d'engagement de 85%."
        ]),
        ("5. OPERATIONS & IT", [
            "La modernisation de notre chaîne de production a permis de réduire les délais de livraison de 15%.",
            "La migration vers le cloud de 80% de nos infrastructures a amélioré la sécurité et la disponibilité des services.",
            "Nous avons déployé un nouvel ERP pour optimiser la gestion des stocks et des commandes.",
            "Le taux de disponibilité de nos services en ligne a atteint 99.95%.",
            "Un audit de cybersécurité a été réalisé avec succès, sans faille critique détectée."
        ]),
        ("6. RSE (Responsabilité Sociétale des Entreprises)", [
            "Nous avons réduit notre empreinte carbone de 5% grâce à l'optimisation des transports et au télétravail.",
            "100% de nos emballages sont désormais recyclables ou biodégradables.",
            "Nous avons soutenu 3 associations locales œuvrant pour l'éducation et l'insertion professionnelle.",
            "Un comité éthique a été créé pour veiller au respect de nos valeurs dans toutes nos activités.",
            "Nous visons la neutralité carbone à l'horizon 2030."
        ]),
        ("7. PERSPECTIVES 2025", [
            "Nous prévoyons de consolider nos positions en Europe avec l'ouverture prévue d'un bureau en Allemagne.",
            "Le lancement d'une nouvelle gamme de services B2B est programmé pour le second trimestre.",
            "L'objectif de croissance du chiffre d'affaires est fixé à 10% pour l'année à venir.",
            "Nous continuerons d'investir dans l'IA pour améliorer notre efficacité opérationnelle.",
            "La satisfaction client restera au cœur de nos priorités stratégiques."
        ])
    ]

    with open("Rapport_Annuel.txt", "w", encoding="utf-8") as f:
        f.write("RAPPORT ANNUEL 2024 - ENTREPRISE FICTIVE\n")
        f.write(f"Généré le : {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        
        for title, content in sections:
            f.write(f"{title}\n")
            for line in content:
                f.write(f"{line}\n")
                # Add some random filler text to make it look even longer if needed
                if random.random() > 0.7:
                     f.write("Note: Ce point a fait l'objet d'une attention particulière du comité de direction.\n")
            f.write("\n")

if __name__ == "__main__":
    generate_report()
    print("Rapport_Annuel.txt a été régénéré avec succès.")
