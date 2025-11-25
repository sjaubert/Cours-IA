import random
from datetime import datetime, timedelta

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

    # Generate Daily Logs
    daily_logs = []
    start_date = datetime(2024, 1, 1)
    
    clients = [f"Client_{i}" for i in range(1, 51)]
    products = ["SuperGadget 3000", "MegaWidget X", "UltraTool Pro", "NanoService", "CloudPack"]
    regions = ["Europe", "Asie", "Amerique", "Afrique"]
    
    daily_logs.append("8. JOURNAL DES OPERATIONS 2024")
    daily_logs.append("Ce journal détaille les opérations quotidiennes significatives pour l'année 2024.")
    daily_logs.append("")

    for i in range(365):
        current_date = start_date + timedelta(days=i)
        date_str = current_date.strftime("%Y-%m-%d")
        
        daily_logs.append(f"--- Date: {date_str} ---")
        
        # Daily Stats
        daily_sales = random.randint(5000, 50000)
        daily_logs.append(f"Ventes journalières totales: {daily_sales} EUR")
        daily_logs.append(f"Taux de satisfaction client: {random.randint(80, 100)}%")
        
        # Random Events (8-15 events per day to generate volume)
        for _ in range(random.randint(8, 15)):
            event_type = random.choice(["VENTE", "SUPPORT", "MAINTENANCE", "RH", "LOGISTIQUE", "MARKETING"])
            
            if event_type == "VENTE":
                client = random.choice(clients)
                product = random.choice(products)
                amount = random.randint(100, 5000)
                region = random.choice(regions)
                daily_logs.append(f"[VENTE] Commande #{random.randint(10000, 99999)} - Client: {client} - Produit: {product} - Région: {region} - Montant: {amount} EUR")
            
            elif event_type == "SUPPORT":
                ticket_id = random.randint(1000, 9999)
                priority = random.choice(['Basse', 'Moyenne', 'Haute', 'Critique'])
                status = random.choice(['Ouvert', 'En cours', 'Résolu', 'Fermé'])
                daily_logs.append(f"[SUPPORT] Ticket #{ticket_id} - Priorité: {priority} - Statut: {status} - Temps de réponse: {random.randint(1, 48)}h")
            
            elif event_type == "MAINTENANCE":
                machine = f"SRV-{random.randint(1, 20)}"
                action = random.choice(["Mise à jour", "Redémarrage", "Remplacement pièce", "Nettoyage logs"])
                daily_logs.append(f"[MAINTENANCE] Système: {machine} - Action: {action} - Technicien: Tech_{random.randint(1, 10)}")
            
            elif event_type == "RH":
                action = random.choice(["Entretien", "Formation", "Réunion équipe", "Teambuilding"])
                daily_logs.append(f"[RH] Activité: {action} - Participants: {random.randint(2, 20)}")

            elif event_type == "LOGISTIQUE":
                action = random.choice(["Réception stock", "Expédition lot", "Inventaire partiel"])
                daily_logs.append(f"[LOGISTIQUE] Opération: {action} - Entrepôt: {random.choice(['Paris', 'Lyon', 'Marseille'])}")
                
            elif event_type == "MARKETING":
                campaign = f"Campagne_{random.randint(1, 12)}"
                daily_logs.append(f"[MARKETING] Lancement {campaign} - Impressions: {random.randint(1000, 50000)} - Clics: {random.randint(50, 2000)}")

        daily_logs.append("") # Empty line separator

    with open("Rapport_Annuel.txt", "w", encoding="utf-8") as f:
        f.write("RAPPORT ANNUEL 2024 - ENTREPRISE FICTIVE\n")
        f.write(f"Généré le : {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("VERSION DETAILLEE - DOCUMENT CONFIDENTIEL\n\n")
        
        # Write static sections
        for title, content in sections:
            f.write(f"{title}\n")
            for line in content:
                f.write(f"{line}\n")
                if random.random() > 0.5:
                     f.write("Note: Analyse approfondie disponible en annexe.\n")
            f.write("\n")
            
        # Write daily logs
        for line in daily_logs:
            f.write(f"{line}\n")

if __name__ == "__main__":
    generate_report()
    print("Rapport_Annuel.txt (version longue) a été régénéré avec succès.")
