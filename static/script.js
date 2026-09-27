* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background: #f4f7fb;
    color: #1f2937;
}


/* =========================
   HEADER
========================= */

header {
    background: #111827;
    color: white;
    padding: 20px 8%;
}

.logo {
    font-size: 24px;
    font-weight: bold;
}


/* =========================
   CONTAINER
========================= */

.container {
    width: 90%;
    max-width: 1050px;
    margin: 40px auto;
}


/* =========================
   RESULT HEADER
========================= */

.result-header {
    text-align: center;
    margin-bottom: 30px;
}

.dashboard-label {
    color: #6b7280;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.result-header h1 {
    font-size: 38px;
    margin-bottom: 8px;
}

.result-header p {
    color: #6b7280;
}

.result-header strong {
    color: #111827;
}


/* =========================
   CARD
========================= */

.card {
    background: white;
    padding: 28px;
    border-radius: 16px;
    margin-bottom: 25px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.07);
}


/* =========================
   SECTION TITLE
========================= */

.section-title {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 18px;
}

.section-title > span {
    font-size: 24px;
}

.section-title h2 {
    font-size: 22px;
    margin-bottom: 5px;
}

.section-title p {
    color: #6b7280;
    font-size: 14px;
}


/* =========================
   DASHBOARD CARDS
========================= */

.dashboard {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 25px;
}

.score-card {
    background: white;
    padding: 28px 20px;
    text-align: center;
    border-radius: 16px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.07);
}

.score-icon {
    font-size: 30px;
    margin-bottom: 10px;
}

.score-card h2 {
    font-size: 34px;
    margin-bottom: 6px;
}

.score-card p {
    color: #6b7280;
    font-size: 14px;
}


/* =========================
   PROGRESS BAR
========================= */

.progress-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 18px;
}

.progress-header h2 {
    font-size: 22px;
    margin-bottom: 5px;
}

.progress-header p {
    color: #6b7280;
    font-size: 14px;
}

.progress-header strong {
    font-size: 28px;
}

.progress-bar {
    width: 100%;
    height: 18px;
    background: #e5e7eb;
    border-radius: 20px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: #111827;
    border-radius: 20px;
    transition: width 0.8s ease;
}


/* =========================
   SKILLS
========================= */

.skills {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.skill {
    padding: 9px 15px;
    border-radius: 20px;
    background: #e5e7eb;
    font-size: 14px;
}

.matched {
    background: #dcfce7;
    color: #166534;
}

.missing {
    background: #fee2e2;
    color: #991b1b;
}


/* =========================
   ROADMAP
========================= */

.roadmap {
    padding-left: 25px;
}

.roadmap li {
    padding: 14px;
    margin-bottom: 10px;
    background: #f3f4f6;
    border-radius: 10px;
    line-height: 1.5;
}


/* =========================
   BUTTON
========================= */

.back-button {
    display: block;
    text-align: center;
    background: #111827;
    color: white;
    padding: 15px;
    text-decoration: none;
    border-radius: 10px;
    font-weight: bold;
    margin-bottom: 30px;
}

.back-button:hover {
    background: #374151;
}


/* =========================
   HOME PAGE
========================= */

.hero {
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 40px;
    margin-bottom: 10px;
}

.hero p {
    color: #6b7280;
    font-size: 18px;
}


/* =========================
   FORM
========================= */

form label {
    display: block;
    margin-top: 20px;
    margin-bottom: 8px;
    font-weight: bold;
}

input,
select,
textarea {
    width: 100%;
    padding: 14px;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    font-size: 16px;
}

textarea {
    height: 120px;
    resize: vertical;
}

small {
    color: #6b7280;
}

button {
    width: 100%;
    margin-top: 25px;
    padding: 15px;
    background: #111827;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 17px;
    cursor: pointer;
}

button:hover {
    background: #374151;
}


/* =========================
   ERROR
========================= */

.error-message {
    background: #fee2e2;
    color: #991b1b;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    text-align: center;
    font-weight: bold;
}

input[type="file"] {
    background: #f9fafb;
    cursor: pointer;
}


/* =========================
   MOBILE RESPONSIVE
========================= */

@media (max-width: 700px) {

    .dashboard {
        grid-template-columns: 1fr;
    }

    .result-header h1 {
        font-size: 30px;
    }

    .hero h1 {
        font-size: 30px;
    }

    .container {
        width: 94%;
        margin: 25px auto;
    }

    .card {
        padding: 20px;
    }

    .progress-header {
        align-items: flex-start;
        gap: 15px;
    }

}