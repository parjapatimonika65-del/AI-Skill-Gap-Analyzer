import re
import streamlit as st
from PyPDF2 import PdfReader

from database import (
    JOB_SKILLS,
    analyze_skills,
    extract_skills_from_text
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    [data-testid="stAppViewContainer"] {
        background: #f5f7fb;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    /* Main container */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #172033;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #667085;
        margin-bottom: 30px;
    }

    /* Cards */
    .card {
        background: white;
        border-radius: 18px;
        padding: 25px;
        margin-bottom: 20px;
        border: 1px solid #e8ebf0;
        box-shadow: 0 5px 18px rgba(20, 30, 50, 0.06);
    }

    .card-title {
        font-size: 23px;
        font-weight: 700;
        color: #172033;
        margin-bottom: 12px;
    }

    .small-text {
        color: #667085;
        font-size: 15px;
    }

    /* Metric cards */
    .metric-card {
        background: white;
        border-radius: 18px;
        padding: 25px 15px;
        text-align: center;
        border: 1px solid #e8ebf0;
        box-shadow: 0 5px 18px rgba(20, 30, 50, 0.06);
    }

    .metric-value {
        font-size: 32px;
        font-weight: 800;
        color: #2563eb;
    }

    .metric-label {
        font-size: 14px;
        color: #667085;
        margin-top: 5px;
    }

    /* Skill tags */
    .skill-tag {
        display: inline-block;
        background: #eaf7ef;
        color: #247044;
        padding: 8px 15px;
        margin: 5px 5px 5px 0;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 500;
    }

    .missing-tag {
        display: inline-block;
        background: #fff0f0;
        color: #c0392b;
        padding: 8px 15px;
        margin: 5px 5px 5px 0;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 500;
    }

    .roadmap-item {
        background: #f8faff;
        border-left: 4px solid #2563eb;
        padding: 12px 15px;
        margin: 10px 0;
        border-radius: 8px;
        color: #344054;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🎯 AI Skill Gap Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze your skills and discover what you need to learn for your target career.'
    '</div>',
    unsafe_allow_html=True
)
# =========================================================
# USER NAME
# =========================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-title">👤 Your Details</div>',
    unsafe_allow_html=True
)

user_name = st.text_input(
    "Enter your name",
    placeholder="Example: Monika"
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# TARGET ROLE
# =========================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-title">🎯 Choose Your Target Role</div>',
    unsafe_allow_html=True
)

target_role = st.selectbox(
    "Select the job role you want to prepare for:",
    list(JOB_SKILLS.keys())
)

st.markdown(
    f"""
    <div class="small-text">
    Required skills for <b>{target_role}</b>:
    {", ".join(JOB_SKILLS[target_role])}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# INPUT METHOD
# =========================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-title">📥 Add Your Skills</div>',
    unsafe_allow_html=True
)

st.write(
    "Don't have a resume? No problem! You can enter your skills manually."
)

input_method = st.radio(
    "Choose an option:",
    [
        "📄 Upload Resume",
        "✍️ Enter Skills Manually"
    ],
    horizontal=True
)


# =========================================================
# RESUME INPUT
# =========================================================

uploaded_file = None
manual_skills = []

if input_method == "📄 Upload Resume":

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file:
        st.success("Resume uploaded successfully! ✅")


# =========================================================
# MANUAL INPUT
# =========================================================

else:

    manual_input = st.text_area(
        "Enter your skills",
        placeholder=(
            "Example:\n"
            "Python, SQL, Pandas, HTML, CSS, JavaScript, React"
        ),
        height=130
    )

    if manual_input.strip():

        manual_skills = [
            skill.strip().lower()
            for skill in re.split(r"[,\n]+", manual_input)
            if skill.strip()
        ]


st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze_button = st.button(
    "🔍 Analyze My Skills",
    use_container_width=True
)


# =========================================================
# ANALYSIS
# =========================================================

if analyze_button:

    try:

        user_skills = []

        # -------------------------------------------------
        # RESUME
        # -------------------------------------------------

        if input_method == "📄 Upload Resume":

            if uploaded_file is None:
                st.warning(
                    "Please upload a resume first, or choose "
                    "'Enter Skills Manually'."
                )
                st.stop()

            reader = PdfReader(uploaded_file)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            user_skills = extract_skills_from_text(text)

        # -------------------------------------------------
        # MANUAL SKILLS
        # -------------------------------------------------

        else:

            user_skills = manual_skills

        # -------------------------------------------------
        # CHECK SKILLS
        # -------------------------------------------------

        if not user_skills:

            st.warning(
                "No skills found. Please upload a resume "
                "or enter at least one skill."
            )
            st.stop()

        # -------------------------------------------------
        # ANALYZE
        # -------------------------------------------------

        result = analyze_skills(
            target_role,
            user_skills
        )

        matched = result["matched"]
        missing = result["missing"]
        percentage = result["percentage"]
        level = result["level"]
        roadmap = result["roadmap"]


        # =================================================
        # RESULT HEADER
        # =================================================

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="card">
                <div style="font-size:30px;font-weight:800;color:#172033;">
    Hello {user_name} 👋
</div>
                </div>

                <div style="font-size:18px;color:#667085;">
                    Target Role: <b>{target_role}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


        # =================================================
        # DETECTED SKILLS
        # =================================================

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">🛠️ Skills Detected</div>',
            unsafe_allow_html=True
        )

        skills_html = ""

        for skill in user_skills:

            skills_html += (
                f'<span class="skill-tag">{skill}</span>'
            )

        st.markdown(
            skills_html,
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)


        # =================================================
        # METRICS
        # =================================================

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">
                        {percentage}%
                    </div>
                    <div class="metric-label">
                        Skill Match
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">
                        {level}
                    </div>
                    <div class="metric-label">
                        Current Level
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">
                        {len(missing)}
                    </div>
                    <div class="metric-label">
                        Skills Missing
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # =================================================
        # PROGRESS
        # =================================================

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">📊 Overall Skill Match</div>',
            unsafe_allow_html=True
        )

        st.progress(
            percentage / 100
        )

        st.write(
            f"You currently match **{percentage}%** "
            f"of the required skills for **{target_role}**."
        )

        st.markdown('</div>', unsafe_allow_html=True)


        # =================================================
        # MATCHED SKILLS
        # =================================================

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">✅ Matched Skills</div>',
            unsafe_allow_html=True
        )

        if matched:

            html = ""

            for skill in matched:

                html += (
                    f'<span class="skill-tag">{skill}</span>'
                )

            st.markdown(
                html,
                unsafe_allow_html=True
            )

        else:

            st.write("No required skills matched yet.")

        st.markdown('</div>', unsafe_allow_html=True)


        # =================================================
        # MISSING SKILLS
        # =================================================

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">❌ Skill Gap</div>',
            unsafe_allow_html=True
        )

        if missing:

            html = ""

            for skill in missing:

                html += (
                    f'<span class="missing-tag">{skill}</span>'
                )

            st.markdown(
                html,
                unsafe_allow_html=True
            )

        else:

            st.success(
                "🎉 You have all the required skills!"
            )

        st.markdown('</div>', unsafe_allow_html=True)


        # =================================================
        # GRAPH
        # =================================================

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">📈 Skill Gap Visualization</div>',
            unsafe_allow_html=True
        )

        chart_data = {
            "Skill Type": [
                "Matched Skills",
                "Missing Skills"
            ],
            "Number of Skills": [
                len(matched),
                len(missing)
            ]
        }

        st.bar_chart(
            chart_data,
            x="Skill Type",
            y="Number of Skills",
            use_container_width=True
        )

        st.markdown('</div>', unsafe_allow_html=True)


        # =================================================
        # ROADMAP
        # =================================================

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">🛣️ Recommended Learning Roadmap</div>',
            unsafe_allow_html=True
        )

        if roadmap:

            for index, item in enumerate(
                roadmap,
                start=1
            ):

                st.markdown(
                    f"""
                    <div class="roadmap-item">
                        <b>Step {index}</b> — {item}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success(
                "No additional skills are required. Great job! 🎉"
            )

        st.markdown('</div>', unsafe_allow_html=True)


        # =================================================
        # DETAILED RESULT
        # =================================================

        with st.expander("🔎 View Detailed Analysis"):

            st.json(result)


    except Exception as e:

        st.error(
            f"Something went wrong: {e}"
        )