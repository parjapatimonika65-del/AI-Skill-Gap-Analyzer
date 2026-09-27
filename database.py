
JOB_SKILLS = {

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "power bi",
        "statistics",
        "pandas",
        "numpy"
    ],

    "Full Stack Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "express",
        "mongodb",
        "git"
    ],

    "Data Scientist": [
        "python",
        "sql",
        "statistics",
        "machine learning",
        "pandas",
        "numpy",
        "scikit-learn"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "git"
    ],

    "Backend Developer": [
        "python",
        "java",
        "node.js",
        "sql",
        "mongodb",
        "api",
        "git"
    ]
}


def analyze_skills(target_role, user_skills):

    required_skills = JOB_SKILLS.get(target_role, [])

    user_skills = [
        skill.lower().strip()
        for skill in user_skills
    ]

    matched = []
    missing = []

    for skill in required_skills:

        if skill.lower() in user_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    total = len(required_skills)

    if total > 0:
        percentage = round(
            (len(matched) / total) * 100
        )
    else:
        percentage = 0

    if percentage >= 80:
        level = "Excellent"

    elif percentage >= 60:
        level = "Good"

    elif percentage >= 40:
        level = "Average"

    else:
        level = "Beginner"

    roadmap = create_roadmap(missing)

    return {
        "required": required_skills,
        "matched": matched,
        "missing": missing,
        "percentage": percentage,
        "level": level,
        "roadmap": roadmap
    }


def create_roadmap(missing):

    roadmap = []

    priority = [
        "python",
        "html",
        "css",
        "javascript",
        "sql",
        "excel",
        "statistics",
        "pandas",
        "numpy",
        "power bi",
        "react",
        "node.js",
        "express",
        "mongodb",
        "machine learning",
        "scikit-learn",
        "api",
        "git"
    ]

    for skill in priority:

        if skill in missing:

            roadmap.append(
                f"Learn {skill.title()} and build a small project."
            )

    return roadmap
import re


def extract_skills_from_text(text):
    """
    Detect known technical skills from resume text.
    """

    text = text.lower()

    skill_aliases = {
        "python": ["python"],
        "sql": ["sql"],
        "excel": ["excel", "microsoft excel"],
        "power bi": ["power bi", "powerbi"],
        "statistics": ["statistics", "statistical"],
        "pandas": ["pandas"],
        "numpy": ["numpy"],
        "html": ["html"],
        "css": ["css"],
        "javascript": ["javascript", "java script"],
        "react": ["react", "react.js", "reactjs"],
        "node.js": ["node.js", "nodejs", "node js"],
        "express": ["express", "express.js"],
        "mongodb": ["mongodb", "mongo db"],
        "git": ["git", "github"],
        "java": ["java"],
        "machine learning": [
            "machine learning",
            "machine-learning"
        ],
        "scikit-learn": [
            "scikit-learn",
            "scikit learn",
            "sklearn"
        ],
        "api": ["api", "apis"]
    }

    detected_skills = []

    for skill, aliases in skill_aliases.items():

        for alias in aliases:

            pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

            if re.search(pattern, text):

                detected_skills.append(skill)

                break

    return detected_skills