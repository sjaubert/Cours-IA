"""
Script de lancement - Génère les données et lance l'analyse
Usage : python run_activity.bat
"""
import subprocess
import sys
import os

def check_dependencies():
    """Vérifie que les bibliothèques nécessaires sont installées"""
    required = ['pandas', 'matplotlib', 'numpy']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"❌ Bibliothèques manquantes : {', '.join(missing)}")
        print(f"\nInstallez-les avec :")
        print(f"pip install {' '.join(missing)}")
        return False
    
    return True

def main():
    print("="*60)
    print("Activité 1 : Analyse de Données GMAO")
    print("="*60)
    
    # Vérifier les dépendances
    if not check_dependencies():
        sys.exit(1)
    
    # Générer les données
    print("\n[1/2] Génération des données...")
    result = subprocess.run([sys.executable, "generer_donnees_gmao.py"], 
                          capture_output=False)
    
    if result.returncode != 0:
        print("❌ Erreur lors de la génération des données")
        sys.exit(1)
    
    # Proposer de lancer la solution exemple
    print("\n" + "="*60)
    print("Données générées avec succès !")
    print("="*60)
    print("\nPrêt à commencer l'activité.")
    print("Consultez le fichier 'instructions_apprenant.md' pour les consignes détaillées.")
    
if __name__ == "__main__":
    main()
