import html.parser
import re

class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.current_tag = ""

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag == "img":
            # Extract image src to know where they are supposed to be
            src = dict(attrs).get("src")
            if src:
                self.text_parts.append(f"\n[IMAGE: {src}]\n")

    def handle_data(self, data):
        clean_data = data.strip()
        if clean_data:
            self.text_parts.append(clean_data)

input_file = r"c:\Users\tsryu\Downloads\ブリリア\セールスレター\index.html"
output_file = r"c:\Users\tsryu\Downloads\ブリリア\セールスレター\extracted_content.md"

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

parser = MyHTMLParser()
parser.feed(content)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(parser.text_parts))

print(f"Extracted content to {output_file}")
