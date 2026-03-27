from flask import Flask, request, jsonify, render_template_string
import PyPDF2
import io

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- Skill & Job Data ---
SKILLS = ["python", "java", "sql", "html", "css", "javascript", "machine learning", "excel", "django", "react"]

JOBS = {
    "python":           ["Backend Developer", "Data Scientist", "ML Engineer"],
    "java":             ["Software Engineer", "Android Developer"],
    "sql":              ["Database Administrator", "Data Analyst"],
    "html":             ["Frontend Developer", "Web Designer"],
    "css":              ["Frontend Developer", "UI Designer"],
    "javascript":       ["Frontend Developer", "Full Stack Developer"],
    "machine learning": ["ML Engineer", "AI Researcher"],
    "excel":            ["Business Analyst", "Data Analyst"],
    "django":           ["Backend Developer", "Full Stack Developer"],
    "react":            ["Frontend Developer", "Full Stack Developer"],
}

# --- Helper Functions ---
def extract_text_from_pdf(file_bytes):
    """Extract text from uploaded PDF bytes."""
    reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_skills(text):
    """Return list of matched skills from text."""
    text_lower = text.lower()
    return [skill for skill in SKILLS if skill in text_lower]

def recommend_jobs(skills):
    """Return unique job recommendations based on skills."""
    result = []
    for skill in skills:
        if skill in JOBS:
            result.extend(JOBS[skill])
    return list(set(result))  # remove duplicates

# --- Routes ---
@app.route("/")
def home():
    return "<h2>Resume Analyzer API is running ✅</h2>"

@app.route("/upload", methods=["POST"])
def upload():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_bytes = file.read()
    text = extract_text_from_pdf(file_bytes)

    if not text.strip():
        return jsonify({"error": "Could not extract text from PDF"}), 400

    skills_found    = extract_skills(text)
    jobs_recommended = recommend_jobs(skills_found)

    return jsonify({
        "filename":      file.filename,
        "skills_found":  skills_found,
        "recommended_jobs": jobs_recommended
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
