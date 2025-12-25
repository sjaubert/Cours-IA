import os
import zipfile
import re

KEYWORDS = ['éducation', 'formation', 'pédagogie', 'apprentissage', 'curriculum', 'enseignement']
TARGET_DIR = 'IA-Education'

def normalize(text):
    return text.lower()

def extract_text_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as zf:
            xml_content = zf.read('word/document.xml').decode('utf-8')
            text_parts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml_content)
            return " ".join(text_parts)
    except Exception:
        return ""

def verify_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    content = ""
    
    try:
        if ext == '.docx':
            content = extract_text_docx(filepath)
        elif ext == '.pdf':
            with open(filepath, 'rb') as f:
                raw = f.read()
                for kw in KEYWORDS:
                    if kw.encode('utf-8') in raw or kw.encode('latin-1', errors='ignore') in raw:
                        return True
            return False
        else:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
    except Exception:
        return False

    content_lower = normalize(content)
    for kw in KEYWORDS:
        if normalize(kw) in content_lower:
            return True
    return False

def main():
    if not os.path.exists(TARGET_DIR):
        print(f"Directory {TARGET_DIR} does not exist.")
        return

    files = os.listdir(TARGET_DIR)
    if not files:
        print("Directory is empty.")
        return

    valid_count = 0
    invalid_files = []

    for filename in files:
        filepath = os.path.join(TARGET_DIR, filename)
        if verify_file(filepath):
            valid_count += 1
        else:
            invalid_files.append(filename)

    print(f"Verification Complete.")
    print(f"Total files in {TARGET_DIR}: {len(files)}")
    print(f"Validated files (contain keywords): {valid_count}")
    if invalid_files:
        print(f"Files without detected keywords (check manually): {invalid_files}")

if __name__ == "__main__":
    main()
