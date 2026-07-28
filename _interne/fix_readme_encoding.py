import subprocess

# Récupérer le contenu depuis git avec le bon encodage
result = subprocess.run(
    ['git', 'show', '5198bc0:README.md'],
    cwd=r'c:\Users\s.jaubert\projets\Cours-IA',
    capture_output=True,
    text=False  # Get bytes
)

# Écrire avec UTF-8
with open(r'c:\Users\s.jaubert\projets\Cours-IA\README.md', 'wb') as f:
    f.write(result.stdout)

print("README.md restauré avec encodage UTF-8 correct")
