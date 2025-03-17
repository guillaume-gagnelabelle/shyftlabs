from bs4 import BeautifulSoup
import pdfplumber
import io
import re

def extract_text_from_pdf(file_bytes: bytes) -> str:
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages[3:])
    
def extract_text_from_html(file_bytes: bytes) -> str:
    soup = BeautifulSoup(file_bytes, "html.parser")
    return soup.get_text(separator="\n")

def chunk_text(text, max_words=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)
    return chunks

def remove_text_after_references(text: str) -> str:
    pattern = r"\n\s*(References|REFERENCES|Bibliography)\s*\n"
    match = re.search(pattern, text)

    if match:
        return text[:match.start()]
    return text
