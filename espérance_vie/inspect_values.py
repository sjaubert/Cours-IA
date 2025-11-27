import pandas as pd

file_path = r"c:\Users\s.jaubert\projets\Cours-IA\espérance_vie\Long-run life expectancy at birth.xlsx"

try:
    df = pd.read_excel(file_path)
    countries = df['country'].unique()
    print("Contains 'World':", 'World' in countries)
    print("Contains 'Monde':", 'Monde' in countries)
    print("Contains 'Europe':", 'Europe' in countries)
    print("Contains 'Asia':", 'Asia' in countries)
    print("Contains 'Americas':", 'Americas' in countries)
    print("Sample countries:", countries[:10])
except Exception as e:
    print(f"Error: {e}")
