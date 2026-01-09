# Script pour chercher les noms de colonnes et details de transformation
import re

with open('SATEBA.exe', 'rb') as f:
    data = f.read()

# Extraire toutes les chaines
all_strings = re.findall(b'[\x20-\x7e]{3,}', data)

print("="*80)
print("RECHERCHE DES NOMS DE COLONNES")
print("="*80)

# Chercher specifiquement "P PMET" et "G PMET"
pmet_strings = [s for s in all_strings if b'PMET' in s or b'pmet' in s or b'Pmet' in s]
print(f"\n>>> Chaines contenant 'PMET': {len(pmet_strings)}")
for s in pmet_strings[:30]:
    decoded = s.decode('ascii', errors='ignore')
    print(f"    - {decoded}")

# Chercher "Cote" ou "cote"
cote_strings = [s for s in all_strings if b'ote' in s and len(s) < 50]
print(f"\n>>> Chaines contenant 'ote' (pour Cote): {len(cote_strings)}")
for s in cote_strings[:30]:
    decoded = s.decode('ascii', errors='ignore')
    if 'ote' in decoded.lower():
        print(f"    - {decoded}")

# Chercher les noms de colonnes complets
column_patterns = [b'P PMET', b'G PMET', b'Cote vis', b'Date', b'Heure']
print(f"\n>>> Recherche de patterns de colonnes:")
for pattern in column_patterns:
    matches = [s for s in all_strings if pattern in s]
    if matches:
        print(f"\n  Pattern '{pattern.decode()}': {len(matches)} correspondances")
        for m in matches[:10]:
            decoded = m.decode('ascii', errors='ignore')
            if len(decoded) < 100:
                print(f"      - {decoded}")

# Chercher des nombres specifiques pour comprendre la logique
print(f"\n" + "="*80)
print("INDICES DE TRANSFORMATION")
print("="*80)

# Chercher des indices numeriques (10, 15, 20, 40, etc.)
number_context = []
for i, s in enumerate(all_strings):
    decoded = s.decode('ascii', errors='ignore')
    # Si contient des chiffres interessants
    if any(num in decoded for num in ['10', '15', '16', '20', '22', '40', '41', '225', '240']):
        # Regarder le contexte (chaines avant et apres)
        if i > 0:
            prev_str = all_strings[i-1].decode('ascii', errors='ignore')
            if len(prev_str) > 3 and len(prev_str) < 50:
                number_context.append((prev_str, decoded))

print("\n>>> Contexte numerique (peut indiquer dimensions):")
seen = set()
for prev, curr in number_context[:40]:
    pair = f"{prev} -> {curr}"
    if pair not in seen and not any(c in prev.lower() for c in ['@', '\\x', 'vb', 'tk']):
        seen.add(pair)
        print(f"    {prev} -> {curr}")

# Chercher des formules ou operations
print(f"\n" + "="*80)
print("OPERATIONS ET FORMULES")
print("="*80)

calc_strings = [s for s in all_strings if any(op in s for op in [b'+', b'-', b'*', b'/', b'='])]
print("\n>>> Chaines avec operateurs mathematiques:")
for s in calc_strings[:30]:
    decoded = s.decode('ascii', errors='ignore')
    if len(decoded) > 5 and len(decoded) < 80:
        # Filtrer les chaines qui ressemblent a du code
        if not decoded.startswith('http') and decoded.count('=') < 5:
            print(f"    - {decoded}")
