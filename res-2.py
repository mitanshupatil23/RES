import streamlit as st
from datetime import datetime
from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Mitanshu Patil | Data Analyst & Business Intelligence",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PERSONAL INFORMATION
# ============================================================

NAME = "Mitanshu Patil"
EMAIL = "shrxpatil23@gmail.com"
PHONE = "8291427713"
LOCATION = "Kalwa, Thane"

LINKEDIN_URL = "https://www.linkedin.com/in/mitanshu-patil-394991262"

CURRENT_YEAR = datetime.now().year


# ============================================================
# DESIGN SYSTEM
# ============================================================

BMW_BLUE = "#0066B1"
BMW_LIGHT_BLUE = "#4AA3DF"
BMW_DARK = "#071018"
BMW_NAVY = "#0D1721"
BMW_NAVY_2 = "#142331"

WHITE = "#FFFFFF"
OFF_WHITE = "#F7F9FB"
LIGHT_GREY = "#EEF2F5"
BORDER = "#DDE4EA"

TEXT = "#17212B"
MUTED = "#6B7785"
SOFT = "#9AA6B2"

GREEN = "#21A366"


# ============================================================
# RESUME DATA
# ============================================================

experience = [

    (
        "RESEARCHAYU PVT LTD",
        "Data Analyst / Reporting & Automation",
        "JAN 2026 — AUG 2026",
        [
            "Created automation for MIS reports including hourly and D-1 reporting.",
            "Developed automated reporting systems using Excel, Power Query and Google Sheets.",
            "Created complex Google Sheets reports for Presales, Marketing and Social Media teams.",
            "Handled data transformation and validation while ensuring reporting accuracy.",
            "Created a shared Google Drive structure for the MIS team."
        ]
    ),

    (
        "STERLING OUTSOURCING PVT LTD",
        "Data Analyst",
        "JUL 2025 — JAN 2026",
        [
            "Prepared daily, monthly and quarterly performance reports.",
            "Contributed to automation initiatives for Sterling Debt Recovery operations.",
            "Developed UI dashboards and created APR and summary reports.",
            "Supported operational insights and management decision-making."
        ]
    ),

    (
        "KSERVE PVT LTD",
        "MIS Executive",
        "JUL 2024 — JUL 2025",
        [
            "Automated monthly and weekly reporting processes, reducing manual effort by 60%.",
            "Designed dynamic Excel dashboards for KPI and performance monitoring.",
            "Developed and maintained macros to streamline repetitive tasks.",
            "Used Power Query to transform raw datasets into structured reports.",
            "Created UI dashboards for Fortis Hospital, Smaaash Entertainment and House of Hiranandani."
        ]
    )

]


skills = [
    ("Advanced Microsoft Excel", 95),
    ("Power Query", 90),
    ("MIS Reporting", 94),
    ("Report Automation", 90),
    ("Dashboard Development", 88),
    ("Google Sheets", 88),
    ("Data Transformation", 92),
    ("Data Validation", 91),
    ("KPI Reporting", 90),
    ("Excel Formula & Logic", 94),
    ("Process Automation", 87),
    ("Data Visualisation", 84),
]


# ============================================================
# PDF RESUME GENERATOR
# ============================================================

def generate_resume_pdf():

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm
    )

    styles = getSampleStyleSheet()

    # --------------------------------------------------------
    # COLORS
    # --------------------------------------------------------

    pdf_blue = colors.HexColor("#0066B1")
    pdf_dark = colors.HexColor("#071018")
    pdf_text = colors.HexColor("#17212B")
    pdf_muted = colors.HexColor("#64748B")
    pdf_light = colors.HexColor("#F3F6F8")

    # --------------------------------------------------------
    # STYLES
    # --------------------------------------------------------

    name_style = ParagraphStyle(
        "ResumeName",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=25,
        leading=28,
        textColor=pdf_dark,
        spaceAfter=4
    )

    role_style = ParagraphStyle(
        "ResumeRole",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=pdf_blue,
        spaceAfter=8
    )

    contact_style = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=pdf_muted
    )

    section_style = ParagraphStyle(
        "Section",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=pdf_blue,
        spaceBefore=9,
        spaceAfter=6
    )

    company_style = ParagraphStyle(
        "Company",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=13,
        textColor=pdf_text
    )

    job_style = ParagraphStyle(
        "Job",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=pdf_blue
    )

    date_style = ParagraphStyle(
        "Date",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.5,
        leading=10,
        textColor=pdf_muted,
        alignment=TA_CENTER
    )

    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=13,
        textColor=pdf_text
    )

    bullet_style = ParagraphStyle(
        "Bullet",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=11.5,
        leftIndent=10,
        firstLineIndent=-6,
        textColor=pdf_text
    )

    skill_style = ParagraphStyle(
        "Skill",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=11,
        textColor=pdf_text
    )

    # --------------------------------------------------------
    # DOCUMENT
    # --------------------------------------------------------

    story = []

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    story.append(
        Paragraph(
            NAME,
            name_style
        )
    )

    story.append(
        Paragraph(
            "MIS & BUSINESS INTELLIGENCE PROFESSIONAL",
            role_style
        )
    )

    contact_text = (
        f"{EMAIL} &nbsp;&nbsp; | &nbsp;&nbsp; "
        f"{PHONE} &nbsp;&nbsp; | &nbsp;&nbsp; "
        f"{LOCATION}"
    )

    story.append(
        Paragraph(
            contact_text,
            contact_style
        )
    )

    story.append(Spacer(1, 7))

    story.append(
        HRFlowable(
            width="100%",
            thickness=1,
            color=pdf_blue,
            spaceBefore=2,
            spaceAfter=10
        )
    )

    # --------------------------------------------------------
    # PROFESSIONAL SUMMARY
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "PROFESSIONAL SUMMARY",
            section_style
        )
    )

    story.append(
        Paragraph(
            "Results-driven MIS professional specialising in reporting, "
            "dashboard development, data transformation, process automation "
            "and business intelligence. Experienced in Advanced Microsoft "
            "Excel, Power Query, VBA Macros and Google Sheets automation. "
            "Focused on converting operational data into structured "
            "information that supports faster and better business decisions.",
            body_style
        )
    )

    # --------------------------------------------------------
    # CORE EXPERTISE
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "CORE EXPERTISE",
            section_style
        )
    )

    expertise = (
        "Advanced Excel • Power Query • MIS Reporting • "
        "Dashboard Development • Report Automation • "
        "Google Sheets • Data Transformation • KPI Reporting • "
        "Process Automation • Data Visualisation"
    )

    story.append(
        Paragraph(
            expertise,
            body_style
        )
    )

    # --------------------------------------------------------
    # EXPERIENCE
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "PROFESSIONAL EXPERIENCE",
            section_style
        )
    )

    for company, role, date, bullets in experience:

        company_table = Table(
            [
                [
                    Paragraph(company, company_style),
                    Paragraph(date, date_style)
                ],
                [
                    Paragraph(role, job_style),
                    ""
                ]
            ],
            colWidths=[125 * mm, 45 * mm]
        )

        company_table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 1),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ]
            )
        )

        story.append(company_table)
        story.append(Spacer(1, 3))

        for bullet in bullets:

            story.append(
                Paragraph(
                    f"• {bullet}",
                    bullet_style
                )
            )

        story.append(Spacer(1, 7))

    # --------------------------------------------------------
    # KEY ACHIEVEMENT
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "KEY ACHIEVEMENT",
            section_style
        )
    )

    achievement_table = Table(
        [
            [
                Paragraph(
                    "<b>60%</b><br/>Manual reporting effort reduced",
                    body_style
                ),
                Paragraph(
                    "<b>10+</b><br/>Core technical capabilities",
                    body_style
                ),
                Paragraph(
                    "<b>2+</b><br/>Years professional experience",
                    body_style
                )
            ]
        ],
        colWidths=[58 * mm, 58 * mm, 58 * mm]
    )

    achievement_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), pdf_light),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#DDE4EA")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#DDE4EA")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(achievement_table)

    # --------------------------------------------------------
    # EDUCATION
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "EDUCATION",
            section_style
        )
    )

    education_data = [
        [
            Paragraph(
                "<b>Bachelor of Commerce</b><br/>Mumbai University",
                body_style
            ),
            Paragraph(
                "<b>2020 — 2023</b>",
                date_style
            )
        ],
        [
            Paragraph(
                "<b>HSC</b><br/>New English School and JR College",
                body_style
            ),
            Paragraph(
                "<b>2020</b>",
                date_style
            )
        ]
    ]

    education_table = Table(
        education_data,
        colWidths=[125 * mm, 45 * mm]
    )

    education_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                ("LINEBELOW", (0, 0), (-1, -2), 0.5, colors.HexColor("#E2E8ED")),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    story.append(education_table)

    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    story.append(Spacer(1, 12))

    story.append(
        HRFlowable(
            width="100%",
            thickness=0.5,
            color=colors.HexColor("#DDE4EA"),
            spaceBefore=3,
            spaceAfter=6
        )
    )

    footer_style = ParagraphStyle(
        "Footer",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7,
        textColor=pdf_muted,
        alignment=TA_CENTER
    )

    story.append(
        Paragraph(
            f"{NAME} • MIS | AUTOMATION | BUSINESS INTELLIGENCE • {CURRENT_YEAR}",
            footer_style
        )
    )

    # --------------------------------------------------------
    # BUILD
    # --------------------------------------------------------

    doc.build(story)

    buffer.seek(0)

    return buffer


# ============================================================
# GENERATE PDF
# ============================================================

resume_pdf = generate_resume_pdf()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@500;600;700;800&display=swap');

html,
body,
[class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(0, 102, 177, 0.035),
            transparent 25%
        ),
        linear-gradient(
            180deg,
            #FFFFFF 0%,
            #F8FAFC 50%,
            #EEF2F5 100%
        );

    color: {TEXT};
}}

.block-container {{
    max-width: 1420px;
    padding-top: 1.2rem;
    padding-bottom: 5rem;
}}

header {{
    visibility: hidden;
    height: 0;
}}

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

::-webkit-scrollbar {{
    width: 7px;
}}

::-webkit-scrollbar-track {{
    background: #F1F4F6;
}}

::-webkit-scrollbar-thumb {{
    background: #B8C3CD;
    border-radius: 10px;
}}

::-webkit-scrollbar-thumb:hover {{
    background: {BMW_BLUE};
}}


/* ============================================================
   TOP BAR
============================================================ */

.topbar {{
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(216, 224, 231, 0.9);
    border-radius: 16px;
    box-shadow: 0 10px 35px rgba(15, 23, 42, 0.055);
    backdrop-filter: blur(15px);
    margin-bottom: 22px;
    animation: fadeDown 0.7s ease;
}}

.corp-brand {{
    display: flex;
    align-items: center;
    gap: 13px;
}}

.corp-symbol {{
    width: 38px;
    height: 38px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #17212B;
    overflow: hidden;
    background:
        conic-gradient(
            #0066B1 0deg 90deg,
            #FFFFFF 90deg 180deg,
            #0066B1 180deg 270deg,
            #FFFFFF 270deg 360deg
        );
}}

.corp-name {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 14px;
    letter-spacing: 2px;
    color: #111820;
}}

.corp-sub {{
    font-size: 9px;
    color: {MUTED};
    letter-spacing: 1.7px;
    margin-top: 2px;
}}

.top-right {{
    display: flex;
    align-items: center;
    gap: 16px;
}}

.live-status {{
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 13px;
    background: rgba(33, 163, 102, 0.06);
    border: 1px solid rgba(33, 163, 102, 0.18);
    border-radius: 30px;
    font-size: 10px;
    font-weight: 600;
    color: #337A58;
    letter-spacing: 0.5px;
}}

.live-dot {{
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: {GREEN};
    box-shadow: 0 0 0 4px rgba(33, 163, 102, 0.10);
    animation: pulse 2s infinite;
}}


/* ============================================================
   HERO
============================================================ */

.hero {{
    position: relative;
    min-height: 540px;
    overflow: hidden;
    border-radius: 30px;
    padding: 66px;

    background:
        radial-gradient(
            circle at 78% 25%,
            rgba(0, 102, 177, 0.30),
            transparent 23%
        ),
        radial-gradient(
            circle at 100% 100%,
            rgba(74, 163, 223, 0.12),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #050A0F 0%,
            #0B151F 50%,
            #142432 100%
        );

    color: white;

    box-shadow: 0 30px 80px rgba(8, 20, 30, 0.20);

    animation: fadeUp 0.8s ease;

    margin-bottom: 28px;
}}

.hero-grid {{
    position: absolute;
    inset: 0;
    opacity: 0.08;

    background-image:
        linear-gradient(
            rgba(255, 255, 255, 0.3) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(255, 255, 255, 0.3) 1px,
            transparent 1px
        );

    background-size: 55px 55px;

    animation: gridMove 15s linear infinite;
}}

.hero-ring-one {{
    position: absolute;
    width: 520px;
    height: 520px;
    right: -190px;
    top: -180px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 50%;
    animation: ringRotate 20s linear infinite;
}}

.hero-ring-two {{
    position: absolute;
    width: 350px;
    height: 350px;
    right: -70px;
    top: -100px;
    border: 1px solid rgba(0, 153, 255, 0.20);
    border-radius: 50%;
    animation: ringRotateReverse 14s linear infinite;
}}

.hero-content {{
    position: relative;
    z-index: 10;
    max-width: 880px;
}}

.hero-label {{
    display: inline-flex;
    padding: 8px 14px;
    border-radius: 30px;
    background: rgba(0, 102, 177, 0.14);
    border: 1px solid rgba(83, 176, 237, 0.35);
    color: #7BC4F4;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 25px;
}}

.hero-name {{
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(45px, 6vw, 82px);
    line-height: 0.94;
    letter-spacing: -4px;
    font-weight: 800;
    margin: 0;
    color: white;
}}

.hero-name span {{
    color: #5BB5ED;
}}

.hero-divider {{
    width: 75px;
    height: 3px;
    background: {BMW_BLUE};
    margin: 25px 0 20px;
}}

.hero-role {{
    font-size: 22px;
    font-weight: 400;
    color: #DCE7EF;
    margin-bottom: 18px;
}}

.hero-description {{
    max-width: 760px;
    color: #AAB8C4;
    font-size: 14px;
    line-height: 1.85;
    margin-bottom: 28px;
}}

.hero-tags {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}}

.hero-tag {{
    padding: 7px 11px;
    border-radius: 6px;
    background: rgba(255, 255, 255, 0.055);
    border: 1px solid rgba(255, 255, 255, 0.09);
    color: #C7D4DE;
    font-size: 10px;
    letter-spacing: 0.5px;
}}


/* ============================================================
   AUTOMOTIVE SCENE
============================================================ */

.auto-scene {{
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 215px;
    z-index: 3;
    overflow: hidden;
    pointer-events: none;
}}

.auto-horizon {{
    position: absolute;
    left: 0;
    right: 0;
    bottom: 110px;
    height: 2px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(0, 102, 177, 0.12),
            rgba(0, 153, 255, 0.55),
            rgba(0, 102, 177, 0.12),
            transparent
        );

    filter: blur(1px);
}}

.auto-road {{
    position: absolute;
    left: -5%;
    right: -5%;
    bottom: -35px;
    height: 125px;

    background:
        linear-gradient(
            180deg,
            rgba(4, 9, 14, 0.15),
            rgba(2, 5, 8, 0.88)
        );

    transform: perspective(500px) rotateX(55deg);
    transform-origin: bottom;
}}

.road-line {{
    position: absolute;
    bottom: 22px;
    left: 0;
    right: 0;
    height: 2px;

    background:
        repeating-linear-gradient(
            90deg,
            transparent 0px,
            transparent 35px,
            rgba(92, 173, 223, 0.22) 35px,
            rgba(92, 173, 223, 0.22) 80px,
            transparent 80px,
            transparent 145px
        );

    animation: roadMove 1.3s linear infinite;
}}

.light-streak {{
    position: absolute;
    height: 2px;
    border-radius: 10px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(72, 178, 241, 0.8),
            rgba(255, 255, 255, 0.85),
            transparent
        );

    filter: blur(0.5px);
    opacity: 0;
}}

.streak-one {{
    width: 220px;
    bottom: 132px;
    left: 5%;
    animation: streakMove 4s linear infinite;
}}

.streak-two {{
    width: 160px;
    bottom: 151px;
    left: 35%;
    animation: streakMove 5s linear infinite 1.5s;
}}

.streak-three {{
    width: 260px;
    bottom: 118px;
    left: 60%;
    animation: streakMove 4.5s linear infinite 2s;
}}

.car-wrapper {{
    position: absolute;
    width: 440px;
    height: 155px;
    right: 7%;
    bottom: 45px;

    animation:
        carEnter 2.4s cubic-bezier(.16, .75, .25, 1) forwards,
        carFloat 4s ease-in-out infinite 2.5s;

    z-index: 8;
}}

.car-shadow {{
    position: absolute;
    width: 330px;
    height: 20px;
    left: 50px;
    bottom: 6px;
    background: rgba(0, 0, 0, 0.70);
    border-radius: 50%;
    filter: blur(8px);
    animation: shadowPulse 4s ease-in-out infinite;
}}

.car-body {{
    position: absolute;
    width: 370px;
    height: 65px;
    left: 30px;
    bottom: 37px;

    border-radius:
        75px
        45px
        18px
        14px;

    background:
        linear-gradient(
            180deg,
            #3E4A55 0%,
            #171F26 35%,
            #080D12 100%
        );

    border: 1px solid rgba(173, 210, 231, 0.24);

    box-shadow:
        inset 0 1px 0 rgba(255, 255, 255, 0.18),
        0 15px 35px rgba(0, 0, 0, 0.50);
}}

.car-hood {{
    position: absolute;
    width: 155px;
    height: 42px;
    right: 0;
    top: 20px;

    border-radius: 10px 65px 12px 0;

    background:
        linear-gradient(
            180deg,
            #38444F,
            #10171D
        );

    border-top: 1px solid rgba(255, 255, 255, 0.12);
}}

.car-roof {{
    position: absolute;
    width: 205px;
    height: 72px;
    left: 88px;
    bottom: 58px;

    background:
        linear-gradient(
            145deg,
            #46535E,
            #121A21
        );

    clip-path:
        polygon(
            14% 100%,
            29% 20%,
            44% 0%,
            72% 8%,
            92% 100%
        );

    border-top: 1px solid rgba(255, 255, 255, 0.15);
}}

.car-window {{
    position: absolute;
    left: 116px;
    bottom: 70px;
    width: 165px;
    height: 47px;

    clip-path:
        polygon(
            15% 100%,
            29% 15%,
            45% 0%,
            70% 8%,
            90% 100%
        );

    background:
        linear-gradient(
            135deg,
            rgba(72, 117, 145, 0.75),
            rgba(5, 13, 19, 0.95)
        );

    border: 1px solid rgba(130, 191, 222, 0.25);
}}

.window-divider {{
    position: absolute;
    left: 196px;
    bottom: 71px;
    width: 2px;
    height: 42px;
    background: rgba(202, 224, 236, 0.15);
    transform: rotate(5deg);
}}

.headlight {{
    position: absolute;
    width: 27px;
    height: 12px;
    right: 5px;
    bottom: 58px;
    border-radius: 80% 20% 20% 80%;
    background: #EAF9FF;

    box-shadow:
        0 0 8px #C7F2FF,
        0 0 20px rgba(74, 185, 241, 0.85),
        35px 0 55px rgba(74, 185, 241, 0.18);

    animation: headlightPulse 2s ease-in-out infinite;
}}

.headlight-beam {{
    position: absolute;
    width: 220px;
    height: 65px;
    right: -190px;
    bottom: 30px;

    background:
        linear-gradient(
            90deg,
            rgba(133, 217, 255, 0.17),
            transparent
        );

    clip-path:
        polygon(
            0 35%,
            100% 0,
            100% 100%,
            0 65%
        );

    filter: blur(3px);
    opacity: 0.55;
}}

.grille {{
    position: absolute;
    width: 34px;
    height: 28px;
    right: 38px;
    bottom: 43px;
    border-radius: 5px;

    background:
        repeating-linear-gradient(
            90deg,
            #05090C 0px,
            #05090C 5px,
            #38444D 6px,
            #05090C 8px
        );

    border: 1px solid rgba(255, 255, 255, 0.08);
    transform: skewX(-8deg);
}}

.car-accent {{
    position: absolute;
    width: 220px;
    height: 2px;
    left: 70px;
    bottom: 38px;

    background:
        linear-gradient(
            90deg,
            transparent,
            {BMW_BLUE},
            #75C7F5,
            transparent
        );

    box-shadow:
        0 0 10px rgba(0, 102, 177, 0.8);
}}

.wheel {{
    position: absolute;
    width: 55px;
    height: 55px;
    bottom: 15px;
    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            #111820 0 19%,
            #8B969E 20% 24%,
            #1B242C 25% 47%,
            #05080B 48% 70%,
            #56616A 71% 74%,
            #05080B 75%
        );

    border: 3px solid #202A32;

    box-shadow:
        0 5px 12px rgba(0, 0, 0, 0.55);

    animation: wheelSpin 1.2s linear infinite;
}}

.wheel-left {{
    left: 78px;
}}

.wheel-right {{
    right: 66px;
}}

.wheel::after {{
    content: "";
    position: absolute;
    inset: 11px;
    border-radius: 50%;
    border: 2px dashed rgba(206, 216, 222, 0.35);
}}


/* ============================================================
   SECTION HEADERS
============================================================ */

.section-header {{
    margin-top: 48px;
    margin-bottom: 22px;
    animation: fadeUp 0.6s ease;
}}

.section-number {{
    font-size: 10px;
    color: {BMW_BLUE};
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 6px;
}}

.section-title {{
    font-family: 'Montserrat', sans-serif;
    font-size: 27px;
    font-weight: 800;
    color: #111820;
    letter-spacing: -0.7px;
    margin: 0;
}}

.section-description {{
    color: {MUTED};
    font-size: 12px;
    margin-top: 7px;
}}


/* ============================================================
   KPI
============================================================ */

.kpi-card {{
    position: relative;
    min-height: 145px;

    background:
        linear-gradient(
            145deg,
            #FFFFFF,
            #F8FAFC
        );

    border: 1px solid {BORDER};
    border-radius: 19px;
    padding: 24px;
    overflow: hidden;

    box-shadow:
        0 8px 30px rgba(15, 23, 42, 0.045);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border 0.25s ease;

    animation: fadeUp 0.7s ease;
}}

.kpi-card:hover {{
    transform: translateY(-6px);
    border-color: rgba(0, 102, 177, 0.35);

    box-shadow:
        0 20px 45px rgba(0, 102, 177, 0.10);
}}

.kpi-card::after {{
    content: "";
    position: absolute;
    width: 90px;
    height: 90px;
    right: -30px;
    bottom: -40px;
    border-radius: 50%;
    border: 1px solid rgba(0, 102, 177, 0.08);
}}

.kpi-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}}

.kpi-index {{
    font-size: 10px;
    color: {SOFT};
    font-weight: 700;
    letter-spacing: 1px;
}}

.kpi-icon {{
    width: 30px;
    height: 30px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 102, 177, 0.08);
    color: {BMW_BLUE};
    font-size: 14px;
}}

.kpi-number {{
    font-family: 'Montserrat', sans-serif;
    font-size: 34px;
    font-weight: 800;
    line-height: 1;
    color: #111820;
}}

.kpi-label {{
    color: {MUTED};
    font-size: 11px;
    line-height: 1.5;
    margin-top: 9px;
}}


/* ============================================================
   PROFILE
============================================================ */

.profile-card {{
    height: 100%;
    padding: 28px;
    background: white;
    border: 1px solid {BORDER};
    border-radius: 20px;

    box-shadow:
        0 8px 25px rgba(15, 23, 42, 0.04);

    transition: 0.25s ease;
}}

.profile-card:hover {{
    transform: translateY(-3px);

    box-shadow:
        0 15px 35px rgba(15, 23, 42, 0.07);
}}

.profile-title {{
    font-family: 'Montserrat', sans-serif;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 14px;
    color: #18212A;
}}

.profile-text {{
    color: #627080;
    font-size: 12px;
    line-height: 1.85;
}}

.focus-row {{
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid #EDF1F4;
    color: #374554;
    font-size: 12px;
}}

.focus-row:last-child {{
    border-bottom: none;
}}

.focus-number {{
    color: {BMW_BLUE};
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    width: 22px;
}}


/* ============================================================
   EXPERIENCE
============================================================ */

.timeline {{
    position: relative;
    padding-left: 28px;
}}

.timeline::before {{
    content: "";
    position: absolute;
    left: 7px;
    top: 5px;
    bottom: 5px;
    width: 1px;

    background:
        linear-gradient(
            180deg,
            {BMW_BLUE},
            #DCE4EA
        );
}}

.timeline-item {{
    position: relative;
    margin-bottom: 24px;
    animation: fadeUp 0.7s ease;
}}

.timeline-dot {{
    position: absolute;
    left: -28px;
    top: 25px;
    width: 15px;
    height: 15px;
    border-radius: 50%;
    background: white;
    border: 3px solid {BMW_BLUE};

    box-shadow:
        0 0 0 5px rgba(0, 102, 177, 0.08);
}}

.experience {{
    background: white;
    border: 1px solid {BORDER};
    border-radius: 20px;
    padding: 27px 30px;

    box-shadow:
        0 8px 28px rgba(15, 23, 42, 0.045);

    transition: 0.25s ease;
}}

.experience:hover {{
    transform: translateX(5px);
    border-color: rgba(0, 102, 177, 0.28);

    box-shadow:
        0 15px 35px rgba(15, 23, 42, 0.07);
}}

.exp-top {{
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 15px;
}}

.exp-company {{
    font-family: 'Montserrat', sans-serif;
    font-size: 17px;
    font-weight: 800;
    color: #16202A;
}}

.exp-role {{
    font-size: 11px;
    color: {BMW_BLUE};
    font-weight: 700;
    margin-top: 4px;
}}

.exp-date {{
    white-space: nowrap;
    font-size: 10px;
    font-weight: 700;
    color: #7A8794;
    padding: 7px 10px;
    background: #F4F7F9;
    border-radius: 6px;
}}

.exp-description {{
    color: #667483;
    font-size: 12px;
    line-height: 1.75;
}}

.exp-description ul {{
    padding-left: 18px;
    margin: 0;
}}

.exp-description li {{
    margin-bottom: 7px;
}}


/* ============================================================
   SKILLS
============================================================ */

.skill-box {{
    padding: 18px;
    background: white;
    border: 1px solid {BORDER};
    border-radius: 15px;
    margin-bottom: 12px;
    transition: 0.2s ease;
}}

.skill-box:hover {{
    transform: translateY(-2px);
    border-color: rgba(0, 102, 177, 0.30);
}}

.skill-header {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 9px;
}}

.skill-name {{
    font-size: 12px;
    font-weight: 700;
    color: #273441;
}}

.skill-percent {{
    font-size: 10px;
    font-weight: 700;
    color: {BMW_BLUE};
}}

.skill-track {{
    width: 100%;
    height: 5px;
    background: #E9EEF2;
    border-radius: 20px;
    overflow: hidden;
}}

.skill-fill {{
    height: 100%;

    background:
        linear-gradient(
            90deg,
            {BMW_BLUE},
            {BMW_LIGHT_BLUE}
        );

    border-radius: 20px;

    animation: grow 1.2s ease;
}}


/* ============================================================
   CAPABILITY
============================================================ */

.capability {{
    height: 100%;
    padding: 27px;

    background:
        linear-gradient(
            145deg,
            #FFFFFF,
            #F7F9FB
        );

    border: 1px solid {BORDER};
    border-radius: 20px;

    transition: all 0.25s ease;

    box-shadow:
        0 8px 25px rgba(15, 23, 42, 0.035);
}}

.capability:hover {{
    transform: translateY(-6px);
    border-color: rgba(0, 102, 177, 0.30);

    box-shadow:
        0 20px 45px rgba(0, 102, 177, 0.08);
}}

.capability-icon {{
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 102, 177, 0.08);
    color: {BMW_BLUE};
    border-radius: 13px;
    font-size: 20px;
    margin-bottom: 18px;
}}

.capability-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 16px;
    color: #18212A;
    margin-bottom: 9px;
}}

.capability-text {{
    font-size: 11px;
    line-height: 1.75;
    color: #697685;
}}


/* ============================================================
   EDUCATION
============================================================ */

.edu-card {{
    position: relative;
    overflow: hidden;
    min-height: 170px;
    padding: 27px;

    background:
        linear-gradient(
            135deg,
            #091119,
            #152533
        );

    border-radius: 20px;
    color: white;

    box-shadow:
        0 15px 40px rgba(9, 17, 25, 0.12);

    transition: 0.25s ease;
}}

.edu-card:hover {{
    transform: translateY(-4px);

    box-shadow:
        0 25px 55px rgba(9, 17, 25, 0.18);
}}

.edu-year {{
    color: #70BCEB;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 13px;
}}

.edu-degree {{
    font-family: 'Montserrat', sans-serif;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 7px;
}}

.edu-institute {{
    color: #A9B8C4;
    font-size: 11px;
}}


/* ============================================================
   CONTACT
============================================================ */

.contact {{
    position: relative;
    overflow: hidden;
    padding: 40px;
    margin-top: 50px;

    background:
        radial-gradient(
            circle at 85% 20%,
            rgba(0, 102, 177, 0.25),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #071018,
            #132332
        );

    border-radius: 25px;
    color: white;

    box-shadow:
        0 25px 65px rgba(7, 16, 24, 0.18);
}}

.contact-title {{
    font-family: 'Montserrat', sans-serif;
    font-size: 27px;
    font-weight: 800;
    margin-bottom: 8px;
}}

.contact-subtitle {{
    color: #AAB8C4;
    font-size: 12px;
    line-height: 1.7;
    max-width: 650px;
    margin-bottom: 25px;
}}

.contact-item {{
    background: rgba(255, 255, 255, 0.045);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 13px;
    padding: 15px 17px;
    transition: 0.2s ease;
}}

.contact-item:hover {{
    background: rgba(255, 255, 255, 0.07);
    border-color: rgba(255, 255, 255, 0.18);
}}

.contact-label {{
    color: #70BCEB;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    margin-bottom: 6px;
}}

.contact-value {{
    color: #D9E3EA;
    font-size: 11px;
}}


/* ============================================================
   BUTTONS
============================================================ */

.stButton > button,
.stDownloadButton > button {{
    border-radius: 9px !important;
    border: 1px solid #D5DEE5 !important;
    background: white !important;
    color: #24313D !important;
    font-weight: 700 !important;
    font-size: 11px !important;
    min-height: 40px !important;

    transition:
        all 0.2s ease !important;
}}

.stButton > button:hover,
.stDownloadButton > button:hover {{
    border-color: {BMW_BLUE} !important;
    color: {BMW_BLUE} !important;
    transform: translateY(-2px);
}}


/* ============================================================
   FOOTER
============================================================ */

.footer {{
    margin-top: 60px;
    padding: 24px 0;
    border-top: 1px solid #D9E0E6;
    text-align: center;
    color: #7B8792;
    font-size: 10px;
    letter-spacing: 0.6px;
}}

.footer strong {{
    color: #1A242D;
}}


/* ============================================================
   ANIMATIONS
============================================================ */

@keyframes fadeUp {{
    from {{
        opacity: 0;
        transform: translateY(18px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

@keyframes fadeDown {{
    from {{
        opacity: 0;
        transform: translateY(-15px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

@keyframes pulse {{
    0% {{
        box-shadow:
            0 0 0 0 rgba(33, 163, 102, 0.25);
    }}

    70% {{
        box-shadow:
            0 0 0 7px rgba(33, 163, 102, 0);
    }}

    100% {{
        box-shadow:
            0 0 0 0 rgba(33, 163, 102, 0);
    }}
}}

@keyframes grow {{
    from {{
        width: 0;
    }}
}}

@keyframes gridMove {{
    from {{
        transform: translate(0, 0);
    }}

    to {{
        transform: translate(55px, 55px);
    }}
}}

@keyframes ringRotate {{
    from {{
        transform: rotate(0deg);
    }}

    to {{
        transform: rotate(360deg);
    }}
}}

@keyframes ringRotateReverse {{
    from {{
        transform: rotate(360deg);
    }}

    to {{
        transform: rotate(0deg);
    }}
}}

@keyframes roadMove {{
    from {{
        background-position: 0 0;
    }}

    to {{
        background-position: -160px 0;
    }}
}}

@keyframes streakMove {{
    0% {{
        transform: translateX(-350px);
        opacity: 0;
    }}

    15% {{
        opacity: 0.75;
    }}

    70% {{
        opacity: 0.65;
    }}

    100% {{
        transform: translateX(1200px);
        opacity: 0;
    }}
}}

@keyframes carEnter {{
    0% {{
        transform:
            translateX(650px)
            scale(0.82);

        opacity: 0;
    }}

    65% {{
        opacity: 1;
    }}

    100% {{
        transform:
            translateX(0)
            scale(1);

        opacity: 1;
    }}
}}

@keyframes carFloat {{
    0% {{
        margin-bottom: 0;
    }}

    50% {{
        margin-bottom: 4px;
    }}

    100% {{
        margin-bottom: 0;
    }}
}}

@keyframes wheelSpin {{
    from {{
        transform: rotate(0deg);
    }}

    to {{
        transform: rotate(360deg);
    }}
}}

@keyframes headlightPulse {{
    0% {{
        opacity: 0.75;

        box-shadow:
            0 0 8px #C7F2FF,
            0 0 18px rgba(74, 185, 241, 0.65);
    }}

    50% {{
        opacity: 1;

        box-shadow:
            0 0 12px #FFFFFF,
            0 0 28px rgba(74, 185, 241, 0.95);
    }}

    100% {{
        opacity: 0.75;

        box-shadow:
            0 0 8px #C7F2FF,
            0 0 18px rgba(74, 185, 241, 0.65);
    }}
}}

@keyframes shadowPulse {{
    0% {{
        transform: scaleX(0.95);
        opacity: 0.45;
    }}

    50% {{
        transform: scaleX(1);
        opacity: 0.65;
    }}

    100% {{
        transform: scaleX(0.95);
        opacity: 0.45;
    }}
}}


/* ============================================================
   MOBILE
============================================================ */

@media (max-width: 768px) {{

    .block-container {{
        padding-left: 1rem;
        padding-right: 1rem;
    }}

    .topbar {{
        height: 58px;
        padding: 0 14px;
    }}

    .corp-sub {{
        display: none;
    }}

    .live-status {{
        display: none;
    }}

    .hero {{
        padding: 38px 27px;
        min-height: 535px;
    }}

    .hero-name {{
        font-size: 49px;
        letter-spacing: -2px;
    }}

    .hero-role {{
        font-size: 17px;
    }}

    .hero-description {{
        font-size: 12px;
    }}

    .section-title {{
        font-size: 23px;
    }}

    .exp-top {{
        flex-direction: column;
    }}

    .exp-date {{
        width: fit-content;
    }}

    .timeline {{
        padding-left: 22px;
    }}

    .timeline-dot {{
        left: -22px;
    }}

    .car-wrapper {{
        right: -105px;
        transform: scale(0.75);
        transform-origin: right bottom;
    }}

    .auto-scene {{
        height: 175px;
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
<div class="topbar">

<div class="corp-brand">

<div class="corp-symbol"></div>

<div>

<div class="corp-name">
    MITANSHU PATIL
</div>

<div class="corp-sub">
    MANAGEMENT INFORMATION SYSTEM
</div>

</div>

</div>

<div class="top-right">

<div class="live-status">

<div class="live-dot"></div>

PROFILE ACTIVE

</div>

</div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# HERO + CAR
# ============================================================

st.markdown(
    """
<div class="hero">

<div class="hero-grid"></div>

<div class="hero-ring-one"></div>

<div class="hero-ring-two"></div>

<div class="hero-content">

<div class="hero-label">
Data Analyst • AUTOMATION • BUSINESS INTELLIGENCE
</div>

<div class="hero-name">
Mitanshu<br>
<span>Patil.</span>
</div>

<div class="hero-divider"></div>

<div class="hero-role">
Data Analyst Professional
</div>

<div class="hero-description">

Results-driven Data professional specialising in
reporting, dashboard development, data transformation,
process automation and business intelligence.

Focused on converting operational data into structured
information that supports faster and better business
decisions.

</div>

<div class="hero-tags">

<div class="hero-tag">
ADVANCED EXCEL
</div>

<div class="hero-tag">
POWER QUERY
</div>

<div class="hero-tag">
AUTOMATION
</div>

<div class="hero-tag">
DASHBOARDS
</div>

<div class="hero-tag">
DATA ANALYSIS
</div>

</div>

</div>


<div class="auto-scene">

<div class="auto-horizon"></div>

<div class="auto-road"></div>

<div class="road-line"></div>

<div class="light-streak streak-one"></div>

<div class="light-streak streak-two"></div>

<div class="light-streak streak-three"></div>

<div class="car-wrapper">

<div class="car-shadow"></div>

<div class="car-roof"></div>

<div class="car-window"></div>

<div class="window-divider"></div>

<div class="car-body"></div>

<div class="car-hood"></div>

<div class="car-accent"></div>

<div class="grille"></div>

<div class="headlight"></div>

<div class="headlight-beam"></div>

<div class="wheel wheel-left"></div>

<div class="wheel wheel-right"></div>

</div>

</div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# QUICK ACTIONS
# ============================================================

a1, a2, a3, a4 = st.columns(4)


with a1:

    if st.button(
        "VIEW EXPERIENCE",
        use_container_width=True
    ):
        st.toast("Experience section selected")


with a2:

    if st.button(
        "VIEW SKILLS",
        use_container_width=True
    ):
        st.toast("Skills section selected")


with a3:

    if st.button(
        "CONTACT ME",
        use_container_width=True
    ):
        st.toast("Contact information below")


with a4:

    st.download_button(
        label="DOWNLOAD PROFILE",
        data=resume_pdf,
        file_name="Mitanshu_Patil_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )


# ============================================================
# SECTION HELPER
# ============================================================

def section_header(number, title, description):

    st.markdown(
        f"""
<div class="section-header">

<div class="section-number">
{number}
</div>

<div class="section-title">
{title}
</div>

<div class="section-description">
{description}
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# PROFESSIONAL SNAPSHOT
# ============================================================

section_header(
    "01 / OVERVIEW",
    "Professional Snapshot",
    "A concise view of experience, automation impact and core capabilities."
)


k1, k2, k3, k4 = st.columns(4)


kpis = [
    ("01", "2+", "YEARS EXPERIENCE", "◷"),
    ("02", "3", "ORGANISATIONS", "◆"),
    ("03", "60%", "MANUAL EFFORT REDUCED", "↗"),
    ("04", "10+", "CORE CAPABILITIES", "▦"),
]


for col, (index, number, label, icon) in zip(
    [k1, k2, k3, k4],
    kpis
):

    with col:

        st.markdown(
            f"""
<div class="kpi-card">

<div class="kpi-top">

<div class="kpi-index">
{index}
</div>

<div class="kpi-icon">
{icon}
</div>

</div>

<div class="kpi-number">
{number}
</div>

<div class="kpi-label">
{label}
</div>

</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# PROFILE
# ============================================================

section_header(
    "02 / PROFILE",
    "Professional Profile",
    "Combining operational understanding with reporting, data and automation."
)


left, right = st.columns([1.35, 1])


with left:

    st.markdown(
        """
<div class="profile-card">

<div class="profile-title">
MIS & Business Reporting
</div>

<div class="profile-text">

Results-driven MIS professional with experience in
MIS reporting, dashboard development, data analysis,
automation and tracker creation.

<br><br>

Experienced in Advanced Microsoft Excel,
Power Query, VBA Macros and Google Sheets
automation.

<br><br>

Focused on transforming large operational datasets
into structured reports, dashboards and actionable
business insights.

</div>

</div>
""",
        unsafe_allow_html=True
    )


with right:

    st.markdown(
        """
<div class="profile-card">

<div class="profile-title">
Core Focus
</div>

<div class="focus-row">
<div class="focus-number">01</div>
Reporting Automation
</div>

<div class="focus-row">
<div class="focus-number">02</div>
Dashboard Development
</div>

<div class="focus-row">
<div class="focus-number">03</div>
Data Transformation
</div>

<div class="focus-row">
<div class="focus-number">04</div>
KPI Tracking
</div>

<div class="focus-row">
<div class="focus-number">05</div>
Process Automation
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# PROFESSIONAL EXPERIENCE
# ============================================================

section_header(
    "03 / CAREER",
    "Professional Experience",
    "Career progression across MIS, reporting, automation and dashboard development."
)


st.markdown(
    '<div class="timeline">',
    unsafe_allow_html=True
)


for company, role, date, bullets in experience:

    bullet_html = "".join(
        f"<li>{bullet}</li>"
        for bullet in bullets
    )

    st.markdown(
        f"""
<div class="timeline-item">

<div class="timeline-dot"></div>

<div class="experience">

<div class="exp-top">

<div>

<div class="exp-company">
{company}
</div>

<div class="exp-role">
{role}
</div>

</div>

<div class="exp-date">
{date}
</div>

</div>

<div class="exp-description">

<ul>
{bullet_html}
</ul>

</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# TECHNICAL SKILLS
# ============================================================

section_header(
    "04 / EXPERTISE",
    "Technical Capability",
    "Core tools and capabilities used across reporting, analytics and automation."
)


s1, s2 = st.columns(2)


for i, (skill, percentage) in enumerate(skills):

    target = s1 if i % 2 == 0 else s2

    with target:

        st.markdown(
            f"""
<div class="skill-box">

<div class="skill-header">

<div class="skill-name">
{skill}
</div>

<div class="skill-percent">
{percentage}%
</div>

</div>

<div class="skill-track">

<div
class="skill-fill"
style="width:{percentage}%"
></div>

</div>

</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# SELECTED CAPABILITIES
# ============================================================

section_header(
    "05 / CAPABILITIES",
    "Selected Capabilities",
    "Where reporting, data and automation create measurable operational value."
)


p1, p2, p3 = st.columns(3)


capabilities = [

    (
        p1,
        "▦",
        "MIS Automation",
        "Automated recurring reporting processes including hourly, D-1, weekly, monthly and quarterly reporting."
    ),

    (
        p2,
        "◈",
        "Dashboard Development",
        "Designed dynamic dashboards and UI reporting systems for KPI monitoring, operational analysis and management visibility."
    ),

    (
        p3,
        "↗",
        "Data Transformation",
        "Structured raw datasets through Power Query, validation and transformation to create reliable business-ready reporting."
    )

]


for col, icon, title, description in capabilities:

    with col:

        st.markdown(
            f"""
<div class="capability">

<div class="capability-icon">
{icon}
</div>

<div class="capability-title">
{title}
</div>

<div class="capability-text">
{description}
</div>

</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# BUSINESS IMPACT
# ============================================================

section_header(
    "06 / IMPACT",
    "Business Impact",
    "The objective behind every reporting and automation initiative."
)


i1, i2, i3 = st.columns(3)


impact_data = [

    (
        i1,
        "TIME",
        "Reduce Manual Work",
        "Automating repetitive reporting processes allows teams to spend more time on analysis rather than data preparation."
    ),

    (
        i2,
        "ACCURACY",
        "Improve Data Reliability",
        "Structured transformation and validation processes help create consistent and dependable reporting."
    ),

    (
        i3,
        "VISIBILITY",
        "Enable Better Decisions",
        "Dashboards and KPI reporting provide management with clearer visibility into operational performance."
    )

]


for col, category, title, text in impact_data:

    with col:

        st.markdown(
            f"""
<div class="profile-card">

<div class="section-number">
{category}
</div>

<div class="profile-title">
{title}
</div>

<div class="profile-text">
{text}
</div>

</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# EDUCATION
# ============================================================

section_header(
    "07 / EDUCATION",
    "Academic Foundation",
    "Educational background supporting a business and analytical mindset."
)


e1, e2 = st.columns(2)


with e1:

    st.markdown(
        """
<div class="edu-card">

<div class="edu-year">
2020 — 2023
</div>

<div class="edu-degree">
Bachelor of Commerce
</div>

<div class="edu-institute">
Mumbai University
</div>

</div>
""",
        unsafe_allow_html=True
    )


with e2:

    st.markdown(
        """
<div class="edu-card">

<div class="edu-year">
2020
</div>

<div class="edu-degree">
HSC
</div>

<div class="edu-institute">
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
<div class="contact">

<div class="contact-title">
Let's Connect.
</div>

<div class="contact-subtitle">

Open to professional conversations around MIS,
reporting, dashboards, automation and data-driven
operations.

</div>

</div>
""",
    unsafe_allow_html=True
)


c1, c2, c3 = st.columns(3)


with c1:

    st.markdown(
        f"""
<div class="contact-item">

<div class="contact-label">
Email
</div>

<div class="contact-value">
{EMAIL}
</div>

</div>
""",
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        f"""
<div class="contact-item">

<div class="contact-label">
Phone
</div>

<div class="contact-value">
{PHONE}
</div>

</div>
""",
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        f"""
<div class="contact-item">

<div class="contact-label">
Location
</div>

<div class="contact-value">
{LOCATION}
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# FINAL ACTIONS
# ============================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)


b1, b2, b3 = st.columns(3)


# ============================================================
# EMAIL BUTTON
# ============================================================

with b1:

    st.link_button(
        "EMAIL ME",
        f"mailto:{EMAIL}",
        use_container_width=True
    )


# ============================================================
# LINKEDIN BUTTON
# ============================================================

with b2:

    st.link_button(
        "VIEW LINKEDIN",
        LINKEDIN_URL,
        use_container_width=True
    )


# ============================================================
# DOWNLOAD RESUME BUTTON
# ============================================================

with b3:

    st.download_button(
        "DOWNLOAD RESUME",
        data=resume_pdf,
        file_name="Mitanshu_Patil_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    f"""
<div class="footer">

<strong>MITANSHU PATIL</strong>

&nbsp; • &nbsp;

MANAGEMENT INFORMATION SYSTEM

&nbsp; • &nbsp;

DATA | AUTOMATION | INSIGHTS

<br><br>

Professional Automotive Portfolio

&nbsp; | &nbsp;

{CURRENT_YEAR}

</div>
""",
    unsafe_allow_html=True
)
