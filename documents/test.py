from PyPDF2 import PdfReader
from docx import Document

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return " ".join([page.extract_text() or "" for page in reader.pages])
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return " ".join([para.text for para in doc.paragraphs])
    elif file_path.endswith(".txt"):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()

print("PDF text:", extract_text("invoice.pdf")[:200])
print("DOCX text:", extract_text("resume.docx")[:200])
print("TXT text:", extract_text("meeting notes.txt")[:200])
