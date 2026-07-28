import zipfile
import re
import sys
import os

def extract_text_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as zf:
            xml_content = zf.read('word/document.xml').decode('utf-8')
            # Simple regex to extract text from <w:t> tags
            # This is a basic extraction, it might not preserve all formatting but should get the content.
            text_parts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml_content)
            return "".join(text_parts)
    except Exception as e:
        return f"Error reading docx: {e}"

if __name__ == "__main__":
    file_path = "Integrating Google Antigravity Unlocking the Google Workspace Extension for Gemini CL.docx"
    if os.path.exists(file_path):
        text = extract_text_from_docx(file_path)
        with open("extracted_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Text extracted to extracted_text.txt")
    else:
        print(f"File not found: {file_path}")
