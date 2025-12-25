import os
import shutil
import zipfile
import re

KEYWORDS = ['éducation', 'formation', 'pédagogie', 'apprentissage', 'curriculum', 'enseignement']
TARGET_DIR = 'IA-Education'
CURRENT_SCRIPT = os.path.basename(__file__)

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

def file_contains_keywords(filepath):
    # Check filename first (optional, but good for robust sorting if content fails)
    # The prompt says "content", so strictly we should check content, 
    # but often filename is a strong indicator of content "about" something.
    # We will prioritize content check.
    
    content = ""
    ext = os.path.splitext(filepath)[1].lower()
    
    try:
        if ext == '.docx':
            content = extract_text_docx(filepath)
        elif ext == '.pdf':
            # Basic binary check for keywords
            with open(filepath, 'rb') as f:
                raw = f.read()
                # Simple check for utf-8 encoded keywords in binary stream
                # This is not perfect for compressed PDFs but is a "script" attempt without libraries
                for kw in KEYWORDS:
                    if kw.encode('utf-8') in raw:
                        return True
                    # Also check for simple ASCII representation if keywords were not accented
                    # But our keywords have accents. 
                    # Let's try latin-1 too just in case
                    if kw.encode('latin-1', errors='ignore') in raw:
                        return True
            return False
        else:
            # Assume text based
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
    except Exception as e:
        print(f"Skipping {filepath} due to read error: {e}")
        return False

    content_lower = normalize(content)
    for kw in KEYWORDS:
        if normalize(kw) in content_lower:
            return True
            
    return False

def main():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    files_moved = 0
    for filename in os.listdir('.'):
        if filename == CURRENT_SCRIPT or filename.startswith('.'):
            continue
        
        filepath = os.path.join('.', filename)
        
        if not os.path.isfile(filepath):
            continue
            
        if file_contains_keywords(filepath):
            print(f"Moving {filename}...")
            shutil.move(filepath, os.path.join(TARGET_DIR, filename))
            files_moved += 1
            
    print(f"Operation complete. Moved {files_moved} files.")

if __name__ == "__main__":
    main()
