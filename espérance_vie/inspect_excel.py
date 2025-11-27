import pandas as pd
import os

file_path = r"c:\Users\s.jaubert\projets\Cours-IA\espérance_vie\Long-run life expectancy at birth.xlsx"

try:
    # Read the Excel file
    df = pd.read_excel(file_path)
    print("Columns:", df.columns.tolist())
    print("First 5 rows:")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)
except Exception as e:
    print(f"Error reading Excel file: {e}")
