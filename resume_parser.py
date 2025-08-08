import fitz  # PyMuPDF
import re

def extract_text_from_pdf(file):
    text = ""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    keywords = [
        'python', 'java', 'c++', 'html', 'css', 'javascript', 'sql',
        'machine learning', 'deep learning', 'data analysis',
        'react', 'node.js', 'cloud', 'aws', 'azure', 'flask', 'django',
        'nlp', 'opencv', 'tensorflow', 'pytorch', 'android'
    ]
    found = [kw for kw in keywords if re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE)]
    return list(set(found))
