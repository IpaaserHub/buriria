
import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def extract_text(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as z:
            xml_content = z.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # Namespaces
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            text_parts = []
            for p in tree.findall('.//w:p', ns):
                p_text = []
                for t in p.findall('.//w:t', ns):
                    if t.text:
                        p_text.append(t.text)
                if p_text:
                    text_parts.append(''.join(p_text))
            
            return '\n'.join(text_parts)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    import os
    path = r"c:\Users\tsryu\Downloads\ブリリア\LP\ブリリア様 オプトLP草案.docx"
    print(f"Checking if file exists: {os.path.exists(path)}")
    try:
        content = extract_text(path)
        print(f"Content length: {len(content)}")
        output_path = r"c:\Users\tsryu\Downloads\ブリリア\LP\extracted_content.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Content written to {output_path}")
    except Exception as e:
        print(f"Top level error: {e}")
