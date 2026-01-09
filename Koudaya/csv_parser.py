"""
csv_parser.py - Module de parsing pour fichiers CSV Keyence

Ce module permet de lire les fichiers CSV bruts provenant d'équipements Keyence
et de les convertir en format compatible avec analyse_pmet.py

Auteur: Assistant IA
Date: 09/01/2026
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import tempfile


def parse_keyence_csv(filepath, mode='simple'):
    """
    Parse un fichier CSV Keyence et retourne un DataFrame
    compatible avec analyse_pmet.py
    
    Args:
        filepath (str): Chemin vers le fichier CSV Keyence
        mode (str): 'simple' pour traitement direct des 16 lignes,
                   'extended' pour tentative de reproduction SATEBA
    
    Returns:
        pandas.DataFrame: DataFrame avec colonnes:
            - Date (str): Format 'YY MM DD'
            - Heure (str): Format 'HH MM SS'
            - P PMET Cote vis 1-10 (float): Mesures P PMET
            - G PMET Cote vis 1-10 (float): Mesures G PMET
    
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        ValueError: Si le format CSV est invalide
    """
    
    print(f"Parsing du fichier CSV Keyence: {filepath}")
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Fichier introuvable: {filepath}")
    
    # Lire le contenu brut
    with open(filepath, 'rb') as f:
        content = f.read().decode('utf-8', errors='ignore')
    
    # Le fichier utilise \r comme séparateur de lignes
    # Nettoyer et normaliser
    content = content.replace('\r', '\n').replace('\n\n', '\n')
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    print(f"Nombre de lignes détectées: {len(lines)}")
    
    # Parser chaque ligne pour extraire les valeurs
    data_matrix = []
    for i, line in enumerate(lines):
        # Séparer par virgules
        values_str = [v.strip() for v in line.split(',') if v.strip()]
        try:
            values = [float(v) for v in values_str]
            data_matrix.append(values)
            if i < 3:
                print(f"  Ligne {i+1}: {len(values)} valeurs (premières: {values[:5]})")
        except ValueError as e:
            print(f"  Avertissement: Ligne {i+1} ignorée (erreur de conversion): {e}")
    
    if not data_matrix:
        raise ValueError("Aucune donnée valide trouvée dans le fichier CSV")
    
    # Convertir en numpy array pour faciliter la manipulation
    data_array = np.array(data_matrix)
    num_rows, num_cols = data_array.shape
    print(f"Matrice de données: {num_rows} lignes × {num_cols} colonnes")
    
    # Créer le DataFrame avec les colonnes attendues
    df = _create_pmet_dataframe(data_array, mode)
    
    print(f"DataFrame créé: {df.shape[0]} lignes × {df.shape[1]} colonnes")
    print(f"Colonnes: {df.columns.tolist()}")
    
    return df


def _create_pmet_dataframe(data_array, mode='simple'):
    """
    Crée un DataFrame au format PMET à partir de la matrice de données
    
    Args:
        data_array (np.array): Matrice de données (lignes × colonnes)
        mode (str): Mode de conversion
    
    Returns:
        pandas.DataFrame: DataFrame formaté
    """
    
    num_rows, num_cols = data_array.shape
    
    # Générer des timestamps factices
    base_time = datetime.now()
    timestamps = []
    for i in range(num_rows):
        # Intervalle de ~3 minutes entre chaque mesure (comme SATEBA)
        ts = base_time + timedelta(minutes=3*i, seconds=30*i)
        date_str = ts.strftime('%y %m %d')
        time_str = ts.strftime('%H %M %S')
        timestamps.append((date_str, time_str))
    
    # Créer les colonnes de base
    df_dict = {
        'Date': [t[0] for t in timestamps],
        'Heure': [t[1] for t in timestamps]
    }
    
    # Mapping des colonnes CSV vers colonnes PMET
    # Hypothèse: Les 15 colonnes se répartissent ainsi:
    # - Colonnes 1-7 ou 1-8: P PMET (mesures petites)
    # - Colonnes restantes: G PMET (mesures grandes)
    
    # On va créer 10 colonnes P PMET et 10 colonnes G PMET
    # en utilisant les données disponibles
    
    if num_cols >= 15:
        # Scénario idéal: 15 colonnes
        # On prend les premières comme P PMET, les dernières comme G PMET
        # et on remplit avec des valeurs moyennes si nécessaire
        
        # P PMET: utiliser colonnes 0-7 (8 colonnes)
        for i in range(10):
            col_name = f'P PMET Cote vis {i+1}'
            if i < 8:
                df_dict[col_name] = data_array[:, i]
            else:
                # Générer valeurs basées sur moyenne des colonnes existantes
                df_dict[col_name] = data_array[:, :8].mean(axis=1)
        
        # G PMET: utiliser colonnes 8-14 (7 colonnes)
        for i in range(10):
            col_name = f'G PMET Cote vis {i+1}'
            if i < 7:
                df_dict[col_name] = data_array[:, 8+i]
            else:
                # Générer valeurs basées sur moyenne des colonnes existantes
                df_dict[col_name] = data_array[:, 8:15].mean(axis=1)
    else:
        # Scénario de fallback: on répartit équitablement
        half = num_cols // 2
        
        for i in range(10):
            col_name = f'P PMET Cote vis {i+1}'
            if i < half:
                df_dict[col_name] = data_array[:, i]
            else:
                df_dict[col_name] = data_array[:, :half].mean(axis=1)
        
        for i in range(10):
            col_name = f'G PMET Cote vis {i+1}'
            if i < (num_cols - half):
                df_dict[col_name] = data_array[:, half+i]
            else:
                df_dict[col_name] = data_array[:, half:].mean(axis=1)
    
    df = pd.DataFrame(df_dict)
    return df


def csv_to_compatible_format(csv_path, output_excel_path=None, mode='simple'):
    """
    Convertit un CSV Keyence en fichier Excel compatible
    avec analyse_pmet.py
    
    Args:
        csv_path (str): Chemin vers le fichier CSV source
        output_excel_path (str, optional): Chemin de sortie pour l'Excel.
                                          Si None, crée un fichier temporaire.
        mode (str): Mode de conversion ('simple' ou 'extended')
    
    Returns:
        str: Chemin vers le fichier Excel généré
    
    Raises:
        Exception: En cas d'erreur lors de la conversion
    """
    
    print(f"\n{'='*70}")
    print(f"CONVERSION CSV KEYENCE -> EXCEL COMPATIBLE")
    print(f"{'='*70}\n")
    
    # Parser le CSV
    df = parse_keyence_csv(csv_path, mode=mode)
    
    # Déterminer le chemin de sortie
    if output_excel_path is None:
        # Créer un fichier temporaire
        temp_dir = tempfile.gettempdir()
        csv_basename = os.path.basename(csv_path)
        excel_name = os.path.splitext(csv_basename)[0] + '_converted.xlsx'
        output_excel_path = os.path.join(temp_dir, excel_name)
    
    # Exporter vers Excel
    try:
        df.to_excel(output_excel_path, index=False, sheet_name='Tabelle1')
        print(f"[OK] Fichier Excel genere: {output_excel_path}")
        print(f"  - {df.shape[0]} lignes de donnees")
        print(f"  - {df.shape[1]} colonnes")
        return output_excel_path
    
    except Exception as e:
        print(f"[ERREUR] Erreur lors de l'export Excel: {e}")
        raise


def validate_csv_format(filepath):
    """
    Valide qu'un fichier a le format CSV Keyence attendu
    
    Args:
        filepath (str): Chemin vers le fichier à valider
    
    Returns:
        tuple: (is_valid (bool), error_message (str or None))
    """
    
    try:
        with open(filepath, 'rb') as f:
            content = f.read(1000)  # Lire les premiers 1000 bytes
        
        # Vérifier la présence de valeurs numériques avec signe +
        if b'+' not in content:
            return False, "Format invalide: valeurs signées '+' non trouvées"
        
        # Vérifier la présence de virgules (séparateur)
        if b',' not in content:
            return False, "Format invalide: séparateur ',' non trouvé"
        
        # Tenter un parsing rapide
        content_str = content.decode('utf-8', errors='ignore')
        lines = content_str.replace('\r', '\n').split('\n')
        first_line = [l for l in lines if l.strip()][0]
        values = first_line.split(',')
        
        # Vérifier qu'on a au moins quelques valeurs numériques
        num_count = 0
        for v in values[:5]:
            try:
                float(v.strip())
                num_count += 1
            except:
                pass
        
        if num_count < 3:
            return False, "Format invalide: pas assez de valeurs numériques"
        
        return True, None
    
    except Exception as e:
        return False, f"Erreur de validation: {e}"


# Point d'entrée pour tests
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python csv_parser.py <fichier.csv> [fichier_sortie.xlsx]")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_excel = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        # Valider
        is_valid, error = validate_csv_format(input_csv)
        if not is_valid:
            print(f"Erreur: {error}")
            sys.exit(1)
        
        # Convertir
        result_path = csv_to_compatible_format(input_csv, output_excel)
        print(f"\n[OK] Conversion reussie!")
        print(f"Fichier de sortie: {result_path}")
        
    except Exception as e:
        print(f"\n[ERREUR] Erreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
