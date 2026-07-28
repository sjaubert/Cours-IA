import base64

# Lire le logo
with open(r'c:\Users\s.jaubert\projets\Cours-IA\logo_uimm_placeholder.jpg', 'rb') as f:
    logo_data = f.read()

# Convertir en base64
logo_base64 = base64.b64encode(logo_data).decode()

# Sauvegarder
with open('logo_base64.txt', 'w') as f:
    f.write(logo_base64)

print(f"Logo converti : {len(logo_base64)} caracteres")
print(f"Debut : {logo_base64[:100]}...")
