from flask import Flask, render_template, request
from database import analyze_skills, extract_skills_from_text
from pypdf import PdfReader

app = Flask(__name__)

# Maximum resume size = 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


def extract_resume_text(file):
    """Extract text from uploaded PDF resume."""

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    name = request.form.get("name", "").strip()

    target_role = request.form.get("target_role", "").strip()

    skills_text = request.form.get("skills", "").strip()

    # -----------------------------
    # Manual skills
    # -----------------------------

    manual_skills = [
        skill.strip().lower()
        for skill in skills_text.split(",")
        if skill.strip()
    ]

    # -----------------------------
    # Resume skills
    # -----------------------------

    resume_skills = []

    resume_file = request.files.get("resume")

    if resume_file and resume_file.filename:

        if not resume_file.filename.lower().endswith(".pdf"):
            return render_template(
                "index.html",
                error="Please upload a PDF resume only."
            )

        try:

            resume_text = extract_resume_text(resume_file)

            resume_skills = extract_skills_from_text(resume_text)

        except Exception:
            return render_template(
                "index.html",
                error="Could not read the PDF. Please upload a valid text-based PDF."
            )

    # -----------------------------
    # Combine manual + resume skills
    # -----------------------------

    user_skills = sorted(
        set(manual_skills + resume_skills)
    )

    # -----------------------------
    # Check if skills are available
    # -----------------------------

    if not user_skills:

        return render_template(
            "index.html",
            error="Please enter your skills or upload a readable PDF resume."
        )

    # -----------------------------
    # Analyze skills
    # -----------------------------

    result = analyze_skills(
        target_role,
        user_skills
    )

    return render_template(
        "result.html",
        name=name,
        target_role=target_role,
        user_skills=user_skills,
        resume_skills=resume_skills,
        result=result
    )


if __name__ == "__main__":
    app.run(
        debug=False,
        use_reloader=False
    )