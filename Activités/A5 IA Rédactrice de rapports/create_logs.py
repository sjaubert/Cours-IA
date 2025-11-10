import csv
import random
from datetime import datetime, timedelta

# --- Configuration des tendances cachées ---
MACHINES = ["M-001", "M-002", "M-003", "M-004", "M-005"]
# M-003 tombera en panne plus souvent (40% de chances)
MACHINE_WEIGHTS = [0.15, 0.15, 0.40, 0.15, 0.15]

PANNE_TYPES = ["Electrique", "Mecanique", "Hydraulique", "Logiciel", "Usure"]
# L'électrique et le mécanique sont plus fréquents
PANNE_TYPE_WEIGHTS = [0.3, 0.3, 0.15, 0.15, 0.1]

EQUIPES = ["Equipe_Electro", "Equipe_Meca", "Equipe_Hydro", "Equipe_IT"]

# Association entre type de panne et nature/équipe/durée
PANNE_DETAILS = {
    "Electrique": {
        "natures": ["Surchauffe composant", "Court-circuit", "Defaut capteur"],
        "equipe": "Equipe_Electro",
        "duree_min": 60,
        "duree_max": 240 # Pannes longues
    },
    "Mecanique": {
        "natures": ["Casse piece", "Vibration anormale", "Bourrage"],
        "equipe": "Equipe_Meca",
        "duree_min": 30,
        "duree_max": 90 # Pannes rapides
    },
    "Hydraulique": {
        "natures": ["Fuite huile", "Pression faible", "Filtre bouche"],
        "equipe": "Equipe_Hydro",
        "duree_min": 45,
        "duree_max": 120
    },
    "Logiciel": {
        "natures": ["Erreur OS", "Crash application", "Conflit reseau"],
        "equipe": "Equipe_IT",
        "duree_min": 15,
        "duree_max": 60
    },
    "Usure": {
        "natures": ["Remplacement courroie", "Graissage", "Nettoyage"],
        "equipe": "Equipe_Meca",
        "duree_min": 20,
        "duree_max": 45
    }
}

NOMBRE_ENTREES = 500
DATE_DEBUT = datetime.now() - timedelta(days=30)

# --- Génération du Fichier ---
lignes = []
lignes.append(["Date", "MachineID", "DureeArretMinutes", "TypePanne", "NaturePanne", "EquipeIntervention"])

for i in range(NOMBRE_ENTREES):
    # Choisir une machine (biaisé)
    machine = random.choices(MACHINES, weights=MACHINE_WEIGHTS, k=1)[0]
    
    # Choisir un type de panne (biaisé)
    type_panne = random.choices(PANNE_TYPES, weights=PANNE_TYPE_WEIGHTS, k=1)[0]
    
    # Obtenir les détails liés à la panne
    details = PANNE_DETAILS[type_panne]
    
    # Choisir une nature de panne
    nature_panne = random.choice(details["natures"])
    
    # Choisir l'équipe
    equipe = details["equipe"]
    
    # Définir la durée (biaisée par type)
    duree = random.randint(details["duree_min"], details["duree_max"])
    
    # Générer une date aléatoire sur les 30 derniers jours
    date_panne = DATE_DEBUT + timedelta(days=random.randint(0, 29), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    
    lignes.append([
        date_panne.strftime("%Y-%m-%d %H:%M"),
        machine,
        duree,
        type_panne,
        nature_panne,
        equipe
    ])

# Écrire le fichier CSV
with open("maintenance_logs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(lignes)

print(f"Fichier 'maintenance_logs.csv' genere avec {NOMBRE_ENTREES} entrees.")