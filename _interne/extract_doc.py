from docx import Document
import json

doc = Document(r'c:\Users\s.jaubert\projets\Cours-IA\00-Formation\The 7 Secret Knobs That Control Every AI Response.docx')

content = []
for p in doc.paragraphs:
    if p.text.strip():
        content.append(p.text)

# Save to JSON file
with open('doc_content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("Content extracted successfully!")
print(f"Total paragraphs: {len(content)}")
