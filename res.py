import streamlit as st
import base64

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Mitanshu Patil | MIS Professional",
    page_icon="▣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# BMW-INSPIRED DESIGN SYSTEM
# ============================================================

BMW_BLUE = "#0066B1"
BMW_DARK = "#0B1117"
BMW_NAVY = "#111A24"
BMW_LIGHT = "#F4F6F8"
BMW_TEXT = "#17202A"
BMW_MUTED = "#697586"
WHITE = "#FFFFFF"
BORDER = "#DCE2E8"

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* --------------------------------------------------------
       GLOBAL
    -------------------------------------------------------- */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@500;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    .stApp {{
        background:
            linear-gradient(
                180deg,
                #FFFFFF 0%,
                #F7F9FB 45%,
                #EEF2F5 100%
            );
        color: {BMW_TEXT};
    }}

    .block-container {{
        max-width: 1350px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }}

    /* Remove Streamlit top padding */
    header {{
        visibility: hidden;
        height: 0;
    }}

    /* --------------------------------------------------------
       TOP NAVIGATION
    -------------------------------------------------------- */

    .top-nav {{
        width: 100%;
        height: 68px;

        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 0 26px;

        background: rgba(255,255,255,0.94);
        border: 1px solid #E4E8EC;
        border-radius: 18px;

        box-shadow:
            0 8px 30px rgba(15,23,42,0.06);

        margin-bottom: 28px;
    }}

    .brand {{
        display: flex;
        align-items: center;
        gap: 14px;
    }}

    .brand-mark {{
        width: 40px;
        height: 40px;

        border-radius: 50%;

        background:
            conic-gradient(
                from 0deg,
                #0066B1 0deg 25%,
                #FFFFFF 25% 50%,
                #0066B1 50% 75%,
                #FFFFFF 75% 100%
            );

        border: 3px solid #111111;

        display: flex;
        align-items: center;
        justify-content: center;

        box-shadow: 0 3px 12px rgba(0,0,0,0.12);
    }}

    .brand-text {{
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        letter-spacing: 1.8px;
        font-size: 16px;
        color: #101820;
    }}

    .brand-sub {{
        font-size: 10px;
        letter-spacing: 2px;
        color: {BMW_MUTED};
        margin-top: 2px;
    }}

    .nav-status {{
        display: flex;
        align-items: center;
        gap: 9px;

        font-size: 12px;
        color: #4D5966;
        font-weight: 500;
    }}

    .status-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #21A366;
        box-shadow: 0 0 0 5px rgba(33,163,102,0.10);
    }}

    /* --------------------------------------------------------
       HERO
    -------------------------------------------------------- */

    .hero {{
        position: relative;
        overflow: hidden;

        min-height: 390px;

        border-radius: 28px;

        background:
            radial-gradient(
                circle at 82% 25%,
                rgba(0,102,177,0.30),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #080D12 0%,
                #111A24 55%,
                #172331 100%
            );

        padding: 55px 60px;

        color: white;

        box-shadow:
            0 25px 70px rgba(15,23,42,0.18);

        margin-bottom: 28px;
    }}

    .hero::after {{
        content: "";

        position: absolute;

        width: 420px;
        height: 420px;

        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 50%;

        right: -110px;
        top: -130px;
    }}

    .hero::before {{
        content: "";

        position: absolute;

        width: 280px;
        height: 280px;

        border: 1px solid rgba(0,102,177,0.28);
        border-radius: 50%;

        right: 30px;
        bottom: -180px;
    }}

    .hero-content {{
        position: relative;
        z-index: 3;
        max-width: 850px;
    }}

    .eyebrow {{
        display: inline-flex;
        align-items: center;

        padding: 7px 13px;

        border-radius: 30px;

        background: rgba(0,102,177,0.14);
        border: 1px solid rgba(0,153,255,0.35);

        color: #72B9E9;

        font-size: 11px;
        font-weight: 600;

        letter-spacing: 2px;
        text-transform: uppercase;

        margin-bottom: 22px;
    }}

    .hero-name {{
        font-family: 'Montserrat', sans-serif;

        font-size: clamp(42px, 6vw, 76px);

        line-height: 0.95;

        letter-spacing: -3px;

        font-weight: 700;

        margin: 0 0 18px 0;

        color: #FFFFFF;
    }}

    .hero-role {{
        font-size: 22px;
        color: #D6E2EC;
        font-weight: 400;

        margin-bottom: 18px;
    }}

    .hero-description {{
        max-width: 720px;

        color: #AEBBC7;

        font-size: 14px;

        line-height: 1.8;

        margin-bottom: 25px;
    }}

    .hero-line {{
        height: 2px;
        width: 80px;

        background: {BMW_BLUE};

        margin-bottom: 18px;
    }}

    /* --------------------------------------------------------
       SECTION
    -------------------------------------------------------- */

    .section-title {{
        font-family: 'Montserrat', sans-serif;

        font-size: 26px;

        font-weight: 700;

        color: #111820;

        letter-spacing: -0.6px;

        margin-top: 44px;
        margin-bottom: 6px;
    }}

    .section-subtitle {{
        color: {BMW_MUTED};
        font-size: 13px;
        margin-bottom: 22px;
    }}

    /* --------------------------------------------------------
       KPI CARDS
    -------------------------------------------------------- */

    .metric-card {{
        background: rgba(255,255,255,0.95);

        border: 1px solid #E2E7EC;

        border-radius: 18px;

        padding: 24px;

        min-height: 130px;

        box-shadow:
            0 8px 24px rgba(15,23,42,0.045);

        transition: all 0.2s ease;
    }}

    .metric-card:hover {{
        transform: translateY(-3px);

        border-color: rgba(0,102,177,0.35);

        box-shadow:
            0 15px 35px rgba(0,102,177,0.10);
    }}

    .metric-number {{
        font-family: 'Montserrat', sans-serif;

        font-size: 34px;

        font-weight: 700;

        color: #111820;

        line-height: 1;
    }}

    .metric-label {{
        font-size: 12px;

        color: {BMW_MUTED};

        margin-top: 10px;

        font-weight: 500;
    }}

    .metric-accent {{
        width: 28px;
        height: 3px;

        background: {BMW_BLUE};

        margin-bottom: 15px;

        border-radius: 5px;
    }}

    /* --------------------------------------------------------
       EXPERIENCE CARDS
    -------------------------------------------------------- */

    .experience-card {{
        position: relative;

        background: white;

        border: 1px solid #E2E7EC;

        border-radius: 20px;

        padding: 27px 30px;

        margin-bottom: 18px;

        box-shadow:
            0 7px 25px rgba(15,23,42,0.045);
    }}

    .experience-card::before {{
        content: "";

        position: absolute;

        left: 0;
        top: 22px;
        bottom: 22px;

        width: 4px;

        background: {BMW_BLUE};

        border-radius: 0 5px 5px 0;
    }}

    .company {{
        font-family: 'Montserrat', sans-serif;

        font-size: 19px;

        font-weight: 700;

        color: #151D25;
    }}

    .period {{
        font-size: 12px;
        color: {BMW_BLUE};
        font-weight: 600;

        margin-top: 4px;
        margin-bottom: 16px;
    }}

    .experience-description {{
        font-size: 13px;
        line-height: 1.75;
        color: #586575;
    }}

    .experience-description ul {{
        padding-left: 19px;
        margin-bottom: 0;
    }}

    .experience-description li {{
        margin-bottom: 8px;
    }}

    /* --------------------------------------------------------
       SKILLS
    -------------------------------------------------------- */

    .skill-card {{
        background: white;

        border: 1px solid #E1E6EB;

        border-radius: 15px;

        padding: 16px 17px;

        margin-bottom: 12px;

        display: flex;

        align-items: center;

        justify-content: space-between;
    }}

    .skill-name {{
        font-size: 13px;

        font-weight: 600;

        color: #26313D;
    }}

    .skill-category {{
        font-size: 10px;

        color: {BMW_BLUE};

        text-transform: uppercase;

        letter-spacing: 1px;

        font-weight: 600;
    }}

    /* --------------------------------------------------------
       PROJECT CARDS
    -------------------------------------------------------- */

    .project-card {{
        height: 100%;

        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F7F9FB
            );

        border: 1px solid #DFE5EA;

        border-radius: 20px;

        padding: 26px;

        box-shadow:
            0 8px 24px rgba(15,23,42,0.04);
    }}

    .project-icon {{
        width: 45px;
        height: 45px;

        border-radius: 12px;

        background: rgba(0,102,177,0.09);

        color: {BMW_BLUE};

        display: flex;

        align-items: center;
        justify-content: center;

        font-size: 19px;

        margin-bottom: 17px;
    }}

    .project-title {{
        font-family: 'Montserrat', sans-serif;

        font-size: 16px;

        font-weight: 700;

        margin-bottom: 9px;

        color: #18212A;
    }}

    .project-text {{
        color: #687483;

        font-size: 12px;

        line-height: 1.7;
    }}

    /* --------------------------------------------------------
       EDUCATION
    -------------------------------------------------------- */

    .education-card {{
        background: #111A24;

        color: white;

        border-radius: 20px;

        padding: 27px;

        min-height: 160px;

        box-shadow:
            0 14px 40px rgba(15,23,42,0.12);
    }}

    .education-year {{
        color: #74BCEB;

        font-size: 11px;

        font-weight: 700;

        letter-spacing: 1.4px;

        margin-bottom: 12px;
    }}

    .education-degree {{
        font-family: 'Montserrat', sans-serif;

        font-size: 17px;

        font-weight: 700;

        margin-bottom: 7px;
    }}

    .education-institute {{
        font-size: 12px;

        color: #AEBBC7;
    }}

    /* --------------------------------------------------------
       CONTACT
    -------------------------------------------------------- */

    .contact-box {{
        background:
            linear-gradient(
                135deg,
                #0A1118,
                #142231
            );

        border-radius: 24px;

        padding: 35px;

        color: white;

        margin-top: 45px;
    }}

    .contact-title {{
        font-family: 'Montserrat', sans-serif;

        font-size: 24px;

        font-weight: 700;

        margin-bottom: 8px;
    }}

    .contact-subtitle {{
        color: #AEBBC7;

        font-size: 13px;

        margin-bottom: 25px;
    }}

    .contact-item {{
        padding: 15px 18px;

        border: 1px solid rgba(255,255,255,0.10);

        border-radius: 12px;

        background: rgba(255,255,255,0.04);

        font-size: 12px;

        color: #D9E2EA;
    }}

    .contact-label {{
        color: #6FB9E9;

        font-size: 10px;

        text-transform: uppercase;

        letter-spacing: 1.4px;

        margin-bottom: 5px;

        font-weight: 700;
    }}

    /* --------------------------------------------------------
       FOOTER
    -------------------------------------------------------- */

    .footer {{
        margin-top: 55px;

        padding-top: 22px;

        border-top: 1px solid #D9E0E6;

        text-align: center;

        color: #7A8794;

        font-size: 11px;

        letter-spacing: 0.5px;
    }}

    .footer strong {{
        color: #1C2630;
    }}

    /* --------------------------------------------------------
       STREAMLIT BUTTONS
    -------------------------------------------------------- */

    .stButton > button {{
        border-radius: 10px;

        border: 1px solid #D7DEE5;

        background: white;

        color: #26313D;

        font-weight: 600;

        font-size: 12px;

        padding: 10px 18px;
    }}

    .stButton > button:hover {{
        border-color: {BMW_BLUE};

        color: {BMW_BLUE};
    }}

    /* --------------------------------------------------------
       MOBILE
    -------------------------------------------------------- */

    @media (max-width: 768px) {{

        .hero {{
            padding: 35px 28px;
            min-height: auto;
        }}

        .hero-name {{
            font-size: 46px;
            letter-spacing: -2px;
        }}

        .hero-role {{
            font-size: 17px;
        }}

        .top-nav {{
            padding: 0 17px;
        }}

        .nav-status {{
            display: none;
        }}

        .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# TOP NAVIGATION
# ============================================================

st.markdown(
    """
<div class="top-nav">

<div class="brand">

<div class="brand-mark"></div>

<div>
    <div class="brand-text">MITANSHU PATIL</div>
        <div class="brand-sub">MANAGEMENT INFORMATION SYSTEM</div>
    </div>

</div>

<div class="nav-status">
    <div class="status-dot"></div>
        Available for Professional Opportunities
    </div>

</div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO
# ============================================================

st.markdown(
    """
<div class="hero">

<div class="hero-content">

<div class="eyebrow">
MIS • DATA • AUTOMATION • DASHBOARDS
</div>

<div class="hero-name">
Mitanshu<br>Patil
</div>

<div class="hero-line"></div>

<div class="hero-role">
Management Information System Professional
</div>

<div class="hero-description">
                Results-driven MIS professional focused on reporting,
                dashboard development, automation, data transformation
                and business intelligence. Experienced in converting
                operational data into structured reports and actionable
                business insights.
</div>

</div>

</div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# EXECUTIVE SNAPSHOT
# ============================================================

st.markdown(
    """
<div class="section-title">
    Professional Snapshot
</div>

<div class="section-subtitle">
    A quick view of experience, capabilities and measurable impact.
</div>
    """,
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-accent"></div>
            <div class="metric-number">2+</div>
            <div class="metric-label">Years of Professional Experience</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-accent"></div>
            <div class="metric-number">3</div>
            <div class="metric-label">Professional Organisations</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-accent"></div>
            <div class="metric-number">60%</div>
            <div class="metric-label">Manual Effort Reduced Through Automation</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-accent"></div>
            <div class="metric-number">10+</div>
            <div class="metric-label">MIS, Dashboard & Automation Capabilities</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# PROFILE
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Profile
    </div>

    <div class="section-subtitle">
        Turning operational data into reliable business information.
    </div>
    """,
    unsafe_allow_html=True
)

left, right = st.columns([1.35, 1])

with left:

    st.markdown(
        """
<div class="project-card">

<div class="project-title">
    MIS & Business Reporting
</div>

<div class="project-text">
                Results-driven MIS Executive with experience in MIS
                reporting, dashboard development, data analysis,
                automation and tracker creation. Skilled in Advanced
                Microsoft Excel, Power Query, VBA Macros and Google
                Sheets automation.
                <br><br>
                Experienced in handling large datasets, building
                automated reporting systems and delivering accurate
                business insights to support decision-making.
</div>

</div>
        """,
        unsafe_allow_html=True
    )

with right:

    st.markdown(
        """
<div class="project-card">

<div class="project-title">
    Core Focus
</div>

<div class="project-text">

<b>01</b> &nbsp; Reporting Automation<br><br>

<b>02</b> &nbsp; Dashboard Development<br><br>

<b>03</b> &nbsp; Data Transformation<br><br>

<b>04</b> &nbsp; KPI Tracking<br><br>

<b>05</b> &nbsp; Process Automation

</div>

 </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# PROFESSIONAL EXPERIENCE
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Professional Experience
    </div>

    <div class="section-subtitle">
        Career progression across MIS, reporting, automation and dashboard development.
    </div>
    """,
    unsafe_allow_html=True
)

# ResearchAyU
st.markdown(
    """
<div class="experience-card">

<div class="company">
    RESEACHAYU PVT LTD
</div>

<div class="period">
JAN 2026 — AUG 2026
</div>

<div class="experience-description">

<ul>

<li>
    Created automation of MIS reports including hourly
    and D-1 reports.
</li>

<li>
    Developed automated reporting systems using Excel,
    Power Query and Google Sheets.
</li>

<li>
    Created complex Google Sheets reports for Presales,
    Marketing and Social Media teams.
</li>

<li>
    Handled data transformation and validation while
    ensuring reporting accuracy.
</li>

<li>
    Created a Share Drive using Google for the MIS team.
</li>

</ul>

</div>

 </div>
    """,
    unsafe_allow_html=True
)

# Sterling
st.markdown(
    """
<div class="experience-card">

<div class="company">
STERLING OUTSOURCING PVT LTD
</div>

<div class="period">
JULY 2025 — JAN 2026
</div>

<div class="experience-description">

<ul>

<li>
 Prepared Daily, Monthly and Quarterly performance
 reports for the Sterling Customer Experience team.
</li>

<li>
    Contributed to automation initiatives for Sterling
    Debt Recovery, a Poland-based operation.
</li>

<li>
    Developed user interface dashboards and created
    APR and summary reports.
</li>

<li>
    Supported operational insights and
    decision-making through reporting.
</li>

</ul>

</div>

 </div>
    """,
    unsafe_allow_html=True
)

# KServe
st.markdown(
    """
<div class="experience-card">

<div class="company">
 KSERVE PVT LTD
</div>

<div class="period">
 JULY 2024 — JULY 2025
</div>

<div class="experience-description">

<ul>

<li>
    Automated monthly and weekly reporting processes,
    reducing manual effort by 60%.
</li>

<li>
    Designed dynamic Excel dashboards to visualize
    KPIs and performance metrics.
</li>

<li>
    Developed and maintained macros to streamline
    repetitive tasks across departments.
</li>

<li>
    Utilized Power Query to transform raw datasets
    into structured business reports.
</li>

<li>
    Created UI dashboards for Fortis Hospital,
    Smaaash Entertainment and House of Hiranandani.
</li>

</ul>

 </div>

 </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SKILLS
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Technical Capability
    </div>

    <div class="section-subtitle">
        Core tools and capabilities used across reporting and automation workflows.
    </div>
    """,
    unsafe_allow_html=True
)

skills = [
    ("Advanced Microsoft Excel", "REPORTING"),
    ("Power Query", "DATA"),
    ("Excel Automation", "AUTOMATION"),
    ("Google Sheets & Automation", "AUTOMATION"),
    ("Dashboard Development", "VISUALISATION"),
    ("Tracker Development", "REPORTING"),
    ("MIS Reporting", "MIS"),
    ("Data Transformation", "DATA"),
    ("Data Management", "DATA"),
    ("Data Validation", "DATA"),
    ("Complex Formula", "EXCEL"),
    ("Logical Formula", "EXCEL"),
    ("Report Automation", "AUTOMATION"),
    ("Data Visualization", "VISUALISATION"),
    ("KPI Tracking & Reporting", "KPI"),
    ("Process Automation", "AUTOMATION"),
]

skill_col1, skill_col2 = st.columns(2)

for index, (skill, category) in enumerate(skills):

    target = skill_col1 if index % 2 == 0 else skill_col2

    with target:

        st.markdown(
            f"""
<div class="skill-card">

<div class="skill-name">
    {skill}
</div>

<div class="skill-category">
    {category}
</div>

 </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# SELECTED CAPABILITIES
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Selected Capabilities
    </div>

    <div class="section-subtitle">
        Areas where data, automation and business reporting intersect.
    </div>
    """,
    unsafe_allow_html=True
)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown(
        """
<div class="project-card">

<div class="project-icon">
    ▦
</div>

<div class="project-title">
    MIS Automation
</div>

<div class="project-text">
    Automated recurring reporting processes including
    hourly, D-1, weekly, monthly and quarterly reporting.
</div>

 </div>
        """,
        unsafe_allow_html=True
    )

with p2:
    st.markdown(
        """
<div class="project-card">

<div class="project-icon">
    ◈
</div>

<div class="project-title">
    Dashboard Development
</div>

<div class="project-text">
    Designed dynamic dashboards and UI reporting systems
    for KPI monitoring, operational analysis and
    management visibility.
</div>

</div>
        """,
        unsafe_allow_html=True
    )

with p3:
    st.markdown(
        """
<div class="project-card">

<div class="project-icon">
    ↗
</div>

<div class="project-title">
    Data Transformation
</div>

<div class="project-text">
    Structured raw datasets through Power Query,
    validation and transformation to create reliable
    business-ready reporting.
</div>

 </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# EDUCATION
# ============================================================

st.markdown(
    """
<div class="section-title">
    Education
</div>

<div class="section-subtitle">
    Academic foundation.
</div>
    """,
    unsafe_allow_html=True
)

e1, e2 = st.columns(2)

with e1:

    st.markdown(
        """
<div class="education-card">

<div class="education-year">
    2020 — 2023
</div>

<div class="education-degree">
    Bachelor of Commerce
</div>

<div class="education-institute">
    Mumbai University
</div>

</div>
        """,
        unsafe_allow_html=True
    )

with e2:

    st.markdown(
        """
<div class="education-card">

<div class="education-year">
    2020
</div>

<div class="education-degree">
    HSC
</div>

<div class="education-institute">
    New English School and JR College
</div>

</div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# CONTACT
# ============================================================

st.markdown(
    """
<div class="contact-box">

<div class="contact-title">
    Let's Connect
</div>

<div class="contact-subtitle">
    Open to conversations around MIS, reporting,
    dashboards, automation and data-driven operations.
</div>

<div style="height:10px;"></div>

</div>
    """,
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
<div class="contact-item">

<div class="contact-label">
Email
</div>

    shrxpatil23@gmail.com

</div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
<div class="contact-item">

<div class="contact-label">
    Phone
</div>

    8291427713

</div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
<div class="contact-item">

<div class="contact-label">
    Location
</div>

    Kalwa, Thane

</div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">

<strong>MITANSHU PATIL</strong>
&nbsp; • &nbsp;
MANAGEMENT INFORMATION SYSTEM
&nbsp; • &nbsp;
DATA | AUTOMATION | INSIGHTS

<br><br>

Professional Profile Dashboard

</div>
    """,
    unsafe_allow_html=True
)