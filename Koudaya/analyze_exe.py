# Script pour extraire les chaines de caracteres lisibles d'un fichier binaire
import re

print("="*80)
print("ANALYSE DE SATEBA.exe")
print("="*80)

# Lire le fichier binaire
with open('SATEBA.exe', 'rb') as f:
    data = f.read()

print(f"\nTaille du fichier: {len(data):,} bytes")

# Extraire les chaines ASCII lisibles (minimum 4 caracteres)
ascii_strings = re.findall(b'[\x20-\x7e]{4,}', data)

print(f"Nombre de chaines trouvees: {len(ascii_strings)}")

# Filtrer les chaines interessantes
keywords = [b'csv', b'CSV', b'excel', b'Excel', b'EXCEL', b'xlsx', b'XLSX',
            b'xls', b'XLS', b'Date', b'Heure', b'Time', b'PMET', b'vis',
            b'cote', b'Cote', b'keyence', b'Keyence', b'KEYENCE',
            b'fichier', b'Fichier', b'file', b'File',
            b'ligne', b'colonne', b'row', b'column']

print("\n" + "="*80)
print("CHAINES PERTINENTES TROUVEES:")
print("="*80)

found_keywords = {}
for keyword in keywords:
    matches = [s for s in ascii_strings if keyword.lower() in s.lower()]
    if matches:
        found_keywords[keyword.decode('ascii', errors='ignore')] = matches

for key, strings in found_keywords.items():
    print(f"\n>>> Mot-cle: '{key}'")
    for s in strings[:10]:  # Limiter a 10 resultats par mot-cle
        decoded = s.decode('ascii', errors='ignore')
        if len(decoded) < 100:  # Eviter les tres longues chaines
            print(f"    - {decoded}")

# Chercher des patterns specifiques
print("\n" + "="*80)
print("PATTERNS SPECIFIQUES:")
print("="*80)

# Chercher des chemins de fichiers
paths = [s for s in ascii_strings if b':\\' in s or b'/' in s]
if paths:
    print("\n>>> Chemins de fichiers detectes:")
    for p in paths[:20]:
        decoded = p.decode('ascii', errors='ignore')
        if len(decoded) < 150:
            print(f"    - {decoded}")

# Chercher des extensions
extensions = [s for s in ascii_strings if b'.csv' in s or b'.xls' in s or b'.xlsx' in s]
if extensions:
    print("\n>>> References a des fichiers:")
    for ext in extensions[:15]:
        decoded = ext.decode('ascii', errors='ignore')
        if len(decoded) < 100:
            print(f"    - {decoded}")

# Chercher des messages d'erreur ou de log
messages = [s for s in ascii_strings if any(word in s.lower() for word in [b'error', b'erreur', b'warning', b'attention'])]
if messages:
    print("\n>>> Messages d'erreur/avertissement:")
    for msg in messages[:10]:
        decoded = msg.decode('ascii', errors='ignore')
        if len(decoded) < 150:
            print(f"    - {decoded}")

# Afficher les longues chaines qui pourraient contenir de l'info
print("\n" + "="*80)
print("CHAINES LONGUES (potentiellement informatives):")
print("="*80)
long_strings = [s for s in ascii_strings if len(s) > 30 and len(s) < 200]
for s in long_strings[:30]:
    decoded = s.decode('ascii', errors='ignore')
    # Filtrer les chaines qui semblent interessantes
    if any(word in decoded.lower() for word in ['csv', 'excel', 'date', 'heure', 'pmet', 'fichier', 'ligne', 'colonne']):
        print(f"    - {decoded}")
