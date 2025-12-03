"""
Script de génération de données GMAO pour l'activité pédagogique
Génère un fichier CSV de 5000 interventions de maintenance avec données intentionnellement "sales"
"""

import csv
import random
from datetime import datetime, timedelta

# Configuration
NB_LIGNES = 5000
FICHIER_SORTIE = "interventions_2024.csv"

# Référentiels
MACHINES = [
    # Pompes
    *[f"PMP-{str(i).zfill(3)}" for i in range(1, 11)],
    # Convoyeurs
    *[f"CVY-{str(i).zfill(3)}" for i in range(1, 11)],
    # Compresseurs
    *[f"CMP-{str(i).zfill(3)}" for i in range(1, 11)],
    # Machines CNC
    *[f"CNC-{str(i).zfill(3)}" for i in range(1, 11)],
    # Moteurs
    *[f"MOT-{str(i).zfill(3)}" for i in range(1, 11)],
]

TYPES_PANNES = [
    "Panne Mécanique",
    "Panne Électrique", 
    "Panne Pneumatique",
    "Panne Hydraulique",
    "Défaut Lubrification",
    "Surchauffe",
    "Vibrations Anormales",
    "Fuite",
    "Défaut Capteur",
    "Usure Normale",
]

# Variantes avec fautes de frappe (10% des cas)
TYPES_PANNES_SALES = [
    "Panne Mecanique",  # sans accent
    "Panne Electrique",  # sans accent
    "panne pneumatique",  # minuscule
    "PANNE HYDRAULIQUE",  # majuscule
    "Def. Lubrification",  # abrégé
    "surchauffe",  # minuscule
    "Vibration Anormale",  # singulier
    "Fuites",  # pluriel
    "Défaut capteur",  # minuscule partielle
    "Usure normale",  # minuscule partielle
]

TECHNICIENS = [
    "Martin Dupont",
    "Sophie Bernard",
    "Alexandre Petit",
    "Julie Moreau",
    "Thomas Laurent",
    "Marie Simon",
    "Nicolas Michel",
    "Isabelle Garcia",
    "Pierre Rodriguez",
    "Céline Lefebvre",
]

# Variantes avec fautes
TECHNICIENS_SALES = [
    "M. Dupont",
    "S.Bernard",
    "A. PETIT",
    "julie moreau",
    "T.Laurent",
    "Marie SIMON",
    "N.Michel",
    "I. Garcia",
    "RODRIGUEZ",
    "Celine Lefebvre",  # sans accent
]

PIECES = [
    "Roulement SKF 6205",
    "Courroie HTD 800-8M",
    "Filtre hydraulique HF35",
    "Joint torique NBR 40x3",
    "Contacteur LC1D09",
    "Vérin pneumatique ISO 6432",
    "Capteur inductif M12",
    "Huile ISO VG 68",
    "Fusible 10A",
    "Relais temporisé",
    "Variateur ATV320",
    "Electrovanne 5/2",
    "Graisse lithium NLGI 2",
    "Câble 3G2.5",
    "Disjoncteur C16",
]

def generer_date_aleatoire():
    """Génère une date aléatoire en 2024"""
    debut = datetime(2024, 1, 1)
    fin = datetime(2024, 12, 31)
    delta = fin - debut
    jours = random.randint(0, delta.days)
    date = debut + timedelta(days=jours)
    
    # 5% de formats hétérogènes
    if random.random() < 0.05:
        formats = [
            date.strftime("%d/%m/%Y"),  # format français
            date.strftime("%Y-%m-%d"),  # format ISO
            date.strftime("%d-%m-%Y"),  # tirets
            date.strftime("%d.%m.%Y"),  # points
        ]
        return random.choice(formats)
    
    return date.strftime("%Y-%m-%d")

def generer_duree_arret():
    """Génère une durée d'arrêt avec formats variés"""
    heures = random.randint(0, 48)
    minutes = random.choice([0, 15, 30, 45])
    
    # 10% de formats hétérogènes
    if random.random() < 0.10:
        formats = [
            f"{heures}h{minutes:02d}",
            f"{heures}:{minutes:02d}",
            f"{heures}.{minutes/60:.2f}",
            f"{heures + minutes/60:.1f}",
            f"{heures} heures {minutes} min",
        ]
        return random.choice(formats)
    
    return f"{heures + minutes/60:.2f}"

def choisir_type_panne():
    """Choisit un type de panne avec 10% de fautes"""
    if random.random() < 0.10:
        return random.choice(TYPES_PANNES_SALES)
    return random.choice(TYPES_PANNES)

def choisir_technicien():
    """Choisit un technicien avec 15% de variations"""
    if random.random() < 0.15:
        return random.choice(TECHNICIENS_SALES)
    return random.choice(TECHNICIENS)

def generer_pieces():
    """Génère 0 à 3 pièces changées"""
    nb_pieces = random.choices([0, 1, 2, 3], weights=[10, 50, 30, 10])[0]
    
    if nb_pieces == 0:
        # 5% de données manquantes représentées différemment
        return random.choice(["", "N/A", "-", "Aucune"])
    
    pieces = random.sample(PIECES, nb_pieces)
    # 5% avec séparateur différent
    if random.random() < 0.05:
        sep = random.choice([" | ", " / ", "; ", " - "])
    else:
        sep = ", "
    
    return sep.join(pieces)

def generer_ligne(id_intervention):
    """Génère une ligne d'intervention"""
    date = generer_date_aleatoire()
    machine = random.choice(MACHINES)
    type_panne = choisir_type_panne()
    duree_arret = generer_duree_arret()
    technicien = choisir_technicien()
    pieces = generer_pieces()
    
    # 5% de données complètement manquantes pour certains champs
    if random.random() < 0.05:
        pieces = ""
    if random.random() < 0.02:
        type_panne = ""
    
    return {
        "ID_Intervention": f"INT-{str(id_intervention).zfill(5)}",
        "Date": date,
        "ID_Machine": machine,
        "Type_Panne": type_panne,
        "Duree_Arret_h": duree_arret,
        "Technicien": technicien,
        "Pieces_Changees": pieces,
    }

def main():
    """Fonction principale"""
    print(f"Génération de {NB_LIGNES} interventions...")
    
    # Entêtes
    colonnes = ["ID_Intervention", "Date", "ID_Machine", "Type_Panne", 
                "Duree_Arret_h", "Technicien", "Pieces_Changees"]
    
    # Génération des données
    with open(FICHIER_SORTIE, 'w', newline='', encoding='utf-8') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()
        
        for i in range(1, NB_LIGNES + 1):
            ligne = generer_ligne(i)
            writer.writerow(ligne)
            
            if i % 500 == 0:
                print(f"  {i} lignes générées...")
    
    print(f"\n✓ Fichier '{FICHIER_SORTIE}' créé avec succès !")
    print(f"  Nombre de lignes : {NB_LIGNES}")
    print(f"  Machines différentes : {len(MACHINES)}")
    print(f"  Types de pannes : {len(TYPES_PANNES)}")
    print(f"\nCaractéristiques des données 'sales' :")
    print(f"  - ~10% de fautes de frappe dans les types de pannes")
    print(f"  - ~15% de variations dans les noms de techniciens")
    print(f"  - ~5% de formats de dates hétérogènes")
    print(f"  - ~10% de formats de durées variés")
    print(f"  - ~5% de données manquantes")

if __name__ == "__main__":
    main()
