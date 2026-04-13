from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import PyPDF2

app = Flask(__name__)
CORS(app)

# ----------- PATH SETUP -----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------- HOME ROUTE -----------
@app.route('/')
def home():
    file_path = os.path.join(FRONTEND_DIR, 'index.html')
    if not os.path.exists(file_path):
        return "Frontend not found", 404
    return send_from_directory(FRONTEND_DIR, 'index.html')


# ----------- PDF TEXT EXTRACTION -----------
def extract_text(filepath):
    text = ""
    with open(filepath, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
    return text.lower()


# ----------- SKILL DETECTION -----------
def extract_skills(text):
    skills_db = [
        "python", "machine learning", "sql", "flask",
        "html", "css", "javascript", "react",
        "java", "c++", "data analysis"
    ]

    found_skills = []

    text = text.lower()  # ensure case consistency

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill.capitalize() if skill != "c++" else "C++")

    return found_skills


# ----------- JOB RECOMMENDATION -----------
def recommend_jobs(skills):
    skills_lower = [s.lower() for s in skills]

    if "machine learning" in skills_lower:
        return ["Data Scientist", "ML Engineer"]
    elif "html" in skills_lower or "javascript" in skills_lower:
        return ["Frontend Developer"]
    elif "flask" in skills_lower or "python" in skills_lower:
        return ["Backend Developer"]
    elif "java" in skills_lower:
        return ["Java Developer"]
    else:
        return ["Software Engineer"]


# ----------- UPLOAD ROUTE -----------
@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['resume']

    if file.filename == '':
        return jsonify({"error": "Empty file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    text = extract_text(filepath)
    skills = extract_skills(text)
    jobs = recommend_jobs(skills)

    return jsonify({
        "filename": file.filename,
        "skills_found": skills if skills else ["No skills detected"],
        "recommended_jobs": jobs
    })


# ----------- RUN APP -----------
if __name__ == '__main__':
    app.run(debug=True)
