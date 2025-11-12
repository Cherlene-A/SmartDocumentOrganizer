from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from docx import Document
import os, shutil, tempfile

app = Flask(__name__)

# --- Load keywords from text files ---
def load_keywords(filename):
    if not os.path.exists(filename):
        return set()
    with open(filename, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f if line.strip())

important_keywords = load_keywords("important_keywords.txt")
junk_keywords = load_keywords("junk_keywords.txt")
spam_keywords = load_keywords("spam_keywords.txt")

# --- Extract text from files ---
def extract_text(file_path):
    try:
        if file_path.endswith(".pdf"):
            reader = PdfReader(file_path)
            return " ".join([page.extract_text() or "" for page in reader.pages])
        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            return " ".join([para.text for para in doc.paragraphs])
        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return ""

# --- Categorize files based on keywords ---
def categorize_files(file_paths):
    results = []
    categorized_folder = os.path.join(os.getcwd(), "categorized")
    os.makedirs(categorized_folder, exist_ok=True)

    for file_path in file_paths:
        filename = os.path.basename(file_path)
        text = extract_text(file_path).lower()
        category = "uncategorized"

        if any(word in text for word in important_keywords):
            category = "important"
        elif any(word in text for word in spam_keywords):
            category = "spam"
        elif any(word in text for word in junk_keywords):
            category = "junk"

        category_path = os.path.join(categorized_folder, category)
        os.makedirs(category_path, exist_ok=True)
        shutil.copy2(file_path, os.path.join(category_path, filename))

        results.append((filename, category))
    return results

# --- Flask Routes ---
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_files = request.files.getlist("files")
        if not uploaded_files or uploaded_files[0].filename == "":
            return render_template("index.html", error="❌ Please upload at least one file.")

        with tempfile.TemporaryDirectory() as tmpdir:
            file_paths = []
            for file in uploaded_files:
                if not file.filename.lower().endswith((".pdf", ".docx", ".txt")):
                    continue
                file_path = os.path.join(tmpdir, file.filename)
                file.save(file_path)
                file_paths.append(file_path)

            if not file_paths:
                return render_template("index.html", error="❌ Only PDF, DOCX, and TXT files are supported.")

            results = categorize_files(file_paths)
            return render_template("result.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
