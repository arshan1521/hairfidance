import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION_START
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCX_OUT_PATH = os.path.join(BASE_DIR, "HairFidence_MCA_Thesis.docx")
LOGO_PATH = os.path.join(BASE_DIR, "college_logo.png")
UML_PATH = os.path.join(BASE_DIR, "use_case_diagram.png")
SCREEN_DIR = os.path.join(BASE_DIR, "screenshots")

def set_cell_border(cell, **kwargs):
    """Sets clean cell borders in Word tables."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}>\n'
                          f'<w:top w:val="{kwargs.get("top", "single")}" w:sz="{kwargs.get("top_sz", "4")}" w:space="0" w:color="{kwargs.get("top_color", "CBD5E1")}"/>\n'
                          f'<w:bottom w:val="{kwargs.get("bottom", "single")}" w:sz="{kwargs.get("bottom_sz", "4")}" w:space="0" w:color="{kwargs.get("bottom_color", "CBD5E1")}"/>\n'
                          f'<w:left w:val="{kwargs.get("left", "single")}" w:sz="{kwargs.get("left_sz", "4")}" w:space="0" w:color="{kwargs.get("left_color", "CBD5E1")}"/>\n'
                          f'<w:right w:val="{kwargs.get("right", "single")}" w:sz="{kwargs.get("right_sz", "4")}" w:space="0" w:color="{kwargs.get("right_color", "CBD5E1")}"/>\n'
                          f'</w:tcBorders>')
    tcPr.append(tcBorders)

def set_cell_shading(cell, color_hex):
    """Applies solid background fill to a table cell."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def add_p(doc, text="", font_size=12, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, line_spacing=1.5, indent=0.0):
    """Adds a paragraph strictly formatted in Times New Roman with specified margins and indentation."""
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    if indent > 0:
        p.paragraph_format.first_line_indent = Inches(indent)
    if text:
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(font_size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
    return p

def add_heading_1(doc, text):
    """Main Headings: 14pt Bold Uppercase"""
    p = add_p(doc, text.upper(), font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=16, space_after=8, line_spacing=1.15)
    return p

def add_heading_2(doc, text):
    """Sub-Headings: 12pt Bold"""
    p = add_p(doc, text, font_size=12, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=12, space_after=6, line_spacing=1.15)
    return p

def add_heading_3(doc, text):
    """Tertiary Headings: 12pt Bold"""
    p = add_p(doc, text, font_size=12, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=8, space_after=4, line_spacing=1.15)
    return p

def add_divider_page(doc, title_text):
    """Generates an institutional chapter flyleaf divider page."""
    doc.add_page_break()
    add_p(doc, "", space_before=220)
    add_p(doc, title_text.upper(), font_size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    doc.add_page_break()

def add_code_block(doc, code_str):
    """Renders formatted production code inside an enterprise-styled callout container."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    cell = table.cell(0, 0)
    set_cell_shading(cell, "F8FAFC")
    set_cell_border(cell, top_color="CBD5E1", bottom_color="CBD5E1", left_color="CBD5E1", right_color="CBD5E1")
    
    lines = code_str.strip().split("\n")
    p_first = cell.paragraphs[0]
    p_first.paragraph_format.space_before = Pt(4)
    p_first.paragraph_format.space_after = Pt(2)
    p_first.paragraph_format.line_spacing = 1.05
    run = p_first.add_run(lines[0])
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    for line in lines[1:]:
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        r = p.add_run(line)
        r.font.name = "Consolas"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    add_p(doc, "", space_after=8)

def add_data_dict_table(doc, table_name, field_records):
    """Renders a fully normalized database schema table for the data dictionary."""
    add_heading_3(doc, f"Data Dictionary Table: {table_name}")
    table = doc.add_table(rows=len(field_records) + 1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Field Name", "Data Type", "Description", "Constraints"]
    for c_idx, h in enumerate(headers):
        c = table.cell(0, c_idx)
        c.paragraphs[0].text = h
        c.paragraphs[0].runs[0].font.name = "Times New Roman"
        c.paragraphs[0].runs[0].font.size = Pt(9.5)
        c.paragraphs[0].runs[0].font.bold = True
        set_cell_shading(c, "F1F5F9")
        set_cell_border(c)
    for r_idx, record in enumerate(field_records):
        for c_idx, val in enumerate(record):
            c = table.cell(r_idx + 1, c_idx)
            c.paragraphs[0].text = val
            c.paragraphs[0].runs[0].font.name = "Times New Roman"
            c.paragraphs[0].runs[0].font.size = Pt(9.0)
            if c_idx == 0:
                c.paragraphs[0].runs[0].font.bold = True
            set_cell_border(c)
    add_p(doc, "", space_after=8)

def generate_thesis_docx():
    print("Generating HairFidence KTU MCA Master Thesis Document (Chapters 8–20)...")
    doc = Document()

    # Base margins: Left 1.5 inches, Right/Top/Bottom 1.0 inch
    sec0 = doc.sections[0]
    sec0.top_margin = Inches(1.0)
    sec0.bottom_margin = Inches(1.0)
    sec0.left_margin = Inches(1.5)
    sec0.right_margin = Inches(1.0)

    # ──────────────────────────────────────────────────────────────────────────
    # 1. COVERING PAGE (Exactly matching PDF Page 1)
    # ──────────────────────────────────────────────────────────────────────────
    add_p(doc, "", space_before=15)
    add_p(doc, "HAIRFIDENCE", font_size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    add_p(doc, "CANCER PATIENT HAIR DONATION MANAGEMENT SYSTEM", font_size=13.5, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=26)

    add_p(doc, "PROJECT THESIS", font_size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_p(doc, "SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENTS", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "FOR THE AWARD OF THE DEGREE OF", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "MASTER OF COMPUTER APPLICATIONS", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)

    add_p(doc, "SUBMITTED BY", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "ARSHAN NIZAR K P", font_size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "(Register Number: AWH25MCA-2010)", font_size=11.5, bold=False, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

    if os.path.exists(LOGO_PATH):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(24)
        p_logo.add_run().add_picture(LOGO_PATH, width=Inches(1.4))

    add_p(doc, "DEPARTMENT OF COMPUTER APPLICATIONS", font_size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=3)
    add_p(doc, "AWH ENGINEERING COLLEGE", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "KUTTIKKATTOOR, CALICUT - 673008", font_size=11.5, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "(Affiliated to APJ Abdul Kalam Technological University, Kerala)", font_size=10.5, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "JULY 2026", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)

    # ──────────────────────────────────────────────────────────────────────────
    # 2. CERTIFICATE PAGE (Exactly matching PDF Page 2)
    # ──────────────────────────────────────────────────────────────────────────
    doc.add_page_break()
    if os.path.exists(LOGO_PATH):
        p_logo2 = doc.add_paragraph()
        p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo2.paragraph_format.space_after = Pt(10)
        p_logo2.paragraph_format.space_before = Pt(4)
        p_logo2.add_run().add_picture(LOGO_PATH, width=Inches(1.15))

    add_p(doc, "DEPARTMENT OF COMPUTER APPLICATIONS", font_size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=3)
    add_p(doc, "AWH ENGINEERING COLLEGE", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "KUTTIKKATTOOR, CALICUT - 673008", font_size=11.5, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)

    add_p(doc, "BONA FIDE CERTIFICATE", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

    cert_text = (
        "This is to certify that this project thesis entitled “HAIRFIDENCE: CANCER PATIENT HAIR DONATION "
        "MANAGEMENT SYSTEM” is a bona fide record of the project work carried out by ARSHAN NIZAR K P "
        "(Register Number: AWH25MCA-2010) in partial fulfillment of the requirements for the award of the "
        "Degree of Master of Computer Applications from APJ Abdul Kalam Technological University during "
        "the academic year 2025–2026."
    )
    add_p(doc, cert_text, font_size=12, italic=True, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=50, line_spacing=1.5, indent=0.5)

    # 2x2 Signatures Table
    t_staff = doc.add_table(rows=2, cols=2)
    t_staff.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_staff.autofit = False

    t_staff.cell(0, 0).paragraphs[0].text = "Mrs. SRUTI SUDEVAN"
    t_staff.cell(0, 0).paragraphs[0].runs[0].font.bold = True
    t_staff.cell(0, 0).paragraphs[0].runs[0].font.name = "Times New Roman"
    p_g1 = t_staff.cell(0, 0).add_paragraph("Head of the Department & Associate Professor\nDept. of Computer Applications\nAWH Engineering College, Calicut")
    p_g1.paragraph_format.line_spacing = 1.15

    t_staff.cell(0, 1).paragraphs[0].text = "Ms. AMEENA AFSAR"
    t_staff.cell(0, 1).paragraphs[0].runs[0].font.bold = True
    t_staff.cell(0, 1).paragraphs[0].runs[0].font.name = "Times New Roman"
    p_h1 = t_staff.cell(0, 1).add_paragraph("Assistant Professor\nDept. of Computer Applications\nAWH Engineering College, Calicut")
    p_h1.paragraph_format.line_spacing = 1.15

    add_p(doc, "", space_after=50)

    t_exam = doc.add_table(rows=1, cols=2)
    t_exam.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_exam.cell(0, 0).paragraphs[0].text = "INTERNAL EXAMINER"
    t_exam.cell(0, 0).paragraphs[0].runs[0].font.bold = True
    t_exam.cell(0, 0).paragraphs[0].runs[0].font.name = "Times New Roman"

    t_exam.cell(0, 1).paragraphs[0].text = "EXTERNAL EXAMINER"
    t_exam.cell(0, 1).paragraphs[0].runs[0].font.bold = True
    t_exam.cell(0, 1).paragraphs[0].runs[0].font.name = "Times New Roman"

    # ──────────────────────────────────────────────────────────────────────────
    # 3. ACKNOWLEDGEMENT (Matching PDF Page 3)
    # ──────────────────────────────────────────────────────────────────────────
    doc.add_page_break()
    add_p(doc, "ACKNOWLEDGEMENT", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=15, space_after=24)

    ack_p1 = (
        "I express my profound sense of gratitude and sincere indebtedness to our respected Principal, "
        "Dr. Sabeena M V, for providing all necessary academic facilities, computational infrastructure, "
        "and institutional encouragement that made the completion of this thesis work possible."
    )
    add_p(doc, ack_p1, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p2 = (
        "I convey my deepest and heartfelt thanks to Mrs. Sruti Sudevan, Head of the Department of "
        "Computer Applications, for her constant inspiration, academic leadership, and continuous "
        "encouragement throughout the duration of the MCA curriculum and during this project endeavor."
    )
    add_p(doc, ack_p2, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p3 = (
        "I take immense privilege in expressing my sincere gratitude to my Project Guide and Coordinator, "
        "Ms. Ameena Afsar, Assistant Professor, Department of Computer Applications, and Mrs. Sruti Sudevan, "
        "for their indispensable guidance, technical mentorship, and patient supervision. Their constructive criticisms, "
        "insightful suggestions, and thorough evaluations at every phase of system modeling, design, and testing helped shape "
        "this project into an academically rigorous and socially impactful system."
    )
    add_p(doc, ack_p3, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p4 = (
        "I also extend my sincere gratitude to all the teaching and non-teaching faculty members of the Department of "
        "Computer Applications for their invaluable support, timely suggestions, and generous academic assistance throughout the "
        "project development cycle."
    )
    add_p(doc, ack_p4, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p5 = (
        "I express my loving thanks to my parents and family members whose unwavering moral support, sacrifices, and "
        "continuous prayers have been the bedrock of my life and education. I also express my warm appreciation to my batchmates "
        "and friends for their collaborative discussions, constructive feedback during user experience reviews, and camaraderie "
        "throughout our post-graduate journey."
    )
    add_p(doc, ack_p5, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p6 = (
        "Above all, I surrender myself in eternal gratitude before the Almighty for granting me the wisdom, health, strength, "
        "and perseverance to complete this project thesis successfully."
    )
    add_p(doc, ack_p6, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=35, line_spacing=1.5, indent=0.5)

    add_p(doc, "ARSHAN NIZAR K P\n(Register Number: AWH25MCA-2010)", font_size=12, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=0)

    # ──────────────────────────────────────────────────────────────────────────
    # 4. ABSTRACT (Matching PDF Page 4)
    # ──────────────────────────────────────────────────────────────────────────
    doc.add_page_break()
    add_p(doc, "ABSTRACT", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=15, space_after=24)

    abs_p1 = (
        "Chemotherapy-induced hair loss severely impacts the psychological well-being of cancer patients. "
        "While many compassionate individuals wish to donate hair for medical wigs, the lack of a standardized "
        "platform bottlenecks coordination between donors, non-governmental organizations (NGOs), and verified "
        "recipients. The proposed project, HairFidence, resolves this operational gap by introducing a centralized "
        "web application designed to digitalize and streamline the entire hair donation lifecycle."
    )
    add_p(doc, abs_p1, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    abs_p2 = (
        "Built on an interactive HTML, CSS, and JavaScript frontend with a secure PHP backend, HairFidence "
        "manages transactions through an optimized MySQL database in a local XAMPP environment. By utilizing an "
        "elegant 8-table relational schema, the platform guarantees rapid execution speeds, robust concurrency control "
        "via PDO transactions, and strict data privacy to effectively prevent resource double-booking and secure data leakage."
    )
    add_p(doc, abs_p2, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    abs_p3 = (
        "The system logically partitions functionality across four distinct modules: Administrator, NGOs, Donors, "
        "and Patients. Donors can easily list hair specifications and track deliveries, while patients securely upload "
        "medical reports to request verified matches. Registered NGOs act as essential gatekeepers by auditing records "
        "and physical donations, overseen globally by the Administrator. Ultimately, HairFidence fosters an efficient, "
        "community-driven logistics network, returning dignity to cancer survivors."
    )
    add_p(doc, abs_p3, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=0, line_spacing=1.5, indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # 5. TABLE OF CONTENTS (Matching PDF Pages 5 & 6)
    # ──────────────────────────────────────────────────────────────────────────
    doc.add_page_break()
    add_p(doc, "CONTENTS", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=15, space_after=20)

    toc_items = [
        ("CERTIFICATE", "ii", True),
        ("COMPANY CERTIFICATE", "iii", True),
        ("ABOUT THE COMPANY", "iv", True),
        ("ACKNOWLEDGEMENT", "v", True),
        ("ABSTRACT", "vi", True),
        ("CHAPTER 8: INTRODUCTION", "1", True),
        ("    8.1 System Overview", "1", False),
        ("    8.2 Problem Statement & Clinical Context", "3", False),
        ("    8.3 Objectives of the System", "5", False),
        ("    8.4 Scope of the Project", "7", False),
        ("    8.5 Operational and Psychosocial Benefits", "9", False),
        ("CHAPTER 9: SYSTEM ANALYSIS", "11", True),
        ("    9.1 Existing System Description", "11", False),
        ("    9.2 Limitations of the Existing System", "13", False),
        ("    9.3 Proposed System Architecture", "15", False),
        ("    9.4 Concrete Enhancements Implemented", "17", False),
        ("CHAPTER 10: FEASIBILITY STUDY", "20", True),
        ("    10.1 Technical Feasibility", "20", False),
        ("    10.2 Operational Feasibility", "22", False),
        ("    10.3 Economic Feasibility", "24", False),
        ("    10.4 Behavioural & Ethical Feasibility", "26", False),
        ("    10.5 Software Standards Feasibility", "28", False),
        ("CHAPTER 11: SOFTWARE ENGINEERING PARADIGM", "30", True),
        ("    11.1 Agile Process Methodology", "30", False),
        ("    11.2 Scrum Framework Implementation", "32", False),
        ("    11.3 Sprint Planning and Task Decomposition", "34", False),
        ("    11.4 User Story Mapping & Acceptance Criteria", "38", False),
        ("    11.5 Agile Ceremonies & Milestone Delivery", "41", False),
        ("CHAPTER 12: SYSTEM REQUIREMENT SPECIFICATION (SRS)", "43", True),
        ("    12.1 Minimum Hardware Requirements", "43", False),
        ("    12.2 Software Stack and Environment", "45", False),
        ("    12.3 Functional Requirements by Module", "48", False),
        ("    12.4 Non-Functional Requirements", "54", False),
        ("CHAPTER 13: SYSTEM DESIGN", "58", True),
        ("    13.1 High-Level MVC Architectural Pattern", "58", False),
        ("    13.2 Data Flow Diagrams (DFD Level 0, 1, 2)", "62", False),
        ("    13.3 UML Modeling (Use Case, Class, Sequence)", "68", False),
        ("    13.4 Database Design & Relational Schema", "76", False),
        ("    13.5 Normalization Proofs (1NF, 2NF, 3NF)", "83", False),
        ("CHAPTER 14: SYSTEM DEVELOPMENT", "88", True),
        ("    14.1 Subsystem Modular Breakdown", "88", False),
        ("    14.2 Core Algorithms & Business Logic", "92", False),
        ("    14.3 Routing & Endpoints Specification", "99", False),
        ("    14.4 Input Validation & Security Layers", "102", False),
        ("CHAPTER 15: SYSTEM TESTING AND IMPLEMENTATION", "106", True),
        ("    15.1 Testing Methodologies Applied", "106", False),
        ("    15.2 Comprehensive Test Suite Table", "110", False),
        ("    15.3 Deployment & Build Configuration", "114", False),
        ("    15.4 Operational Environment Verification", "117", False),
        ("CHAPTER 16: SYSTEM MAINTENANCE", "120", True),
        ("    16.1 Corrective Maintenance Plan", "120", False),
        ("    16.2 Adaptive Maintenance Plan", "122", False),
        ("    16.3 Perfective Maintenance Plan", "124", False),
        ("    16.4 Preventive Maintenance Plan & DR", "126", False),
        ("CHAPTER 17: FUTURE ENHANCEMENT", "129", True),
        ("    17.1 Cross-Platform Mobile Applications", "129", False),
        ("    17.2 Automated Postal & Logistics API Integration", "131", False),
        ("    17.3 AI-Powered Virtual Wig AR Simulator", "133", False),
        ("    17.4 Philanthropic Micro-Sponsorship Gateway", "135", False),
        ("    17.5 Multi-Channel Notification Webhooks", "137", False),
        ("CHAPTER 18: CONCLUSION", "139", True),
        ("    18.1 Summary of Project Achievements", "139", False),
        ("    18.2 Validation of Core Objectives", "141", False),
        ("    18.3 Academic & Engineering Conclusion", "143", False),
        ("CHAPTER 19: APPENDIX", "145", True),
        ("CHAPTER 20: BIBLIOGRAPHY", "156", True),
    ]

    t_toc = doc.add_table(rows=len(toc_items), cols=2)
    t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_toc.autofit = False
    for i, (title, page, is_bold) in enumerate(toc_items):
        cell0 = t_toc.cell(i, 0)
        cell1 = t_toc.cell(i, 1)
        cell0.width = Inches(5.1)
        cell1.width = Inches(0.9)
        p0 = cell0.paragraphs[0]
        p0.text = title
        p0.runs[0].font.name = "Times New Roman"
        p0.runs[0].font.size = Pt(10)
        p0.runs[0].font.bold = is_bold
        p0.paragraph_format.space_after = Pt(1.5)
        p0.paragraph_format.space_before = Pt(1.5)

        p1 = cell1.paragraphs[0]
        p1.text = page
        p1.runs[0].font.name = "Times New Roman"
        p1.runs[0].font.size = Pt(10)
        p1.runs[0].font.bold = is_bold
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.space_after = Pt(1.5)
        p1.paragraph_format.space_before = Pt(1.5)

    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 1: BODY CHAPTERS (RUNNING HEADER & FOOTER)
    # ──────────────────────────────────────────────────────────────────────────
    sec1 = doc.add_section(WD_SECTION_START.NEW_PAGE)
    sec1.top_margin = Inches(1.0)
    sec1.bottom_margin = Inches(1.0)
    sec1.left_margin = Inches(1.5)
    sec1.right_margin = Inches(1.0)

    # Header: Left "HairFidence", Right Page Number
    hdr = sec1.header
    p_hdr = hdr.paragraphs[0]
    p_hdr.text = "HairFidence\t\t"
    p_hdr.runs[0].font.name = "Times New Roman"
    p_hdr.runs[0].font.size = Pt(10)
    p_hdr.runs[0].font.italic = True
    p_hdr.runs[0].font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    fldSimple = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
    p_hdr._p.append(fldSimple)

    pBdr = parse_xml(r'<w:pBdr %s><w:bottom w:val="single" w:sz="6" w:space="4" w:color="CBD5E1"/></w:pBdr>' % nsdecls('w'))
    p_hdr._p.get_or_add_pPr().append(pBdr)

    # Footer: Centered "Dept of Computer Applications | AWH Engineering College"
    ftr = sec1.footer
    p_ftr = ftr.paragraphs[0]
    p_ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ftr.text = "Dept of Computer Applications | AWH Engineering College"
    p_ftr.runs[0].font.name = "Times New Roman"
    p_ftr.runs[0].font.size = Pt(9.5)
    p_ftr.runs[0].font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    pBdr_f = parse_xml(r'<w:pBdr %s><w:top w:val="single" w:sz="6" w:space="4" w:color="CBD5E1"/></w:pBdr>' % nsdecls('w'))
    p_ftr._p.get_or_add_pPr().append(pBdr_f)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 8: INTRODUCTION (Matching PDF Pages 7-10)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 8: INTRODUCTION")
    add_heading_1(doc, "CHAPTER 8: INTRODUCTION")

    add_heading_2(doc, "8.1 System Overview")
    add_p(doc, "In contemporary clinical oncology, pharmacological advancements, targeted chemotherapies, and advanced radiotherapy regimens have substantially elevated cancer survival rates across global populations. However, systemic oncology protocols frequently inflict severe physical, emotional, and psychosocial distress upon patients. Among treatment-associated complications, chemotherapy-induced alopecia (hair loss) is clinically recognized as one of the most acutely demoralizing and traumatic experiences endured by cancer survivors, predominantly impacting women, adolescents, and children. Unlike internal physiological symptoms, alopecia serves as an involuntary, inescapable visual badge of malignancy, precipitating acute clinical depression, diminished self-worth, social stigmatization, and in severe instances, treatment non-compliance.", indent=0.5)

    add_p(doc, "Specialized cranial medical prostheses (custom-crafted natural hair wigs) offer profound psychosocial rehabilitation, enabling recovering patients to reclaim their self-image, emotional well-being, and social confidence. Unfortunately, the commercial marketplace for natural hair wigs is severely cost-prohibitive, typically commanding prices between ₹25,000 and ₹1,20,000 ($300 to $1,500) per unit owing to meticulous hand-knotting craftsmanship and raw material scarcity. Concurrently, thousands of compassionate citizens express an active willingness to donate their natural hair for charitable wig fabrication. Regrettably, traditional charitable avenues across Kerala and India remain uncoordinated, informal, and vulnerable to operational failures.", indent=0.5)

    add_p(doc, "HairFidence is an enterprise-grade, centralized, role-governed web application engineered to bridge this vital humanitarian divide. Operating on a robust 3-Tier Model-View-Controller (MVC) architecture, the platform digitizes and audits the complete hair donation lifecycle. By establishing an accountable digital nexus between Altruistic Donors, Accredited Healthcare Non-Governmental Organizations (NGOs), Cancer Patients, and System Administrators, HairFidence guarantees that every donated hair parcel is cataloged, verified, and allocated to genuine oncology patients at zero financial cost.", indent=0.5)

    add_heading_2(doc, "8.2 Problem Statement & Clinical Context")
    add_p(doc, "The traditional hair donation ecosystem suffers from three acute, interrelated structural deficiencies:", indent=0.5)

    add_p(doc, "1. Severe Donor Disconnect & Logistics Opacity: Altruistic citizens wishing to contribute hair typically encounter fragmented social media appeals or informal word-of-mouth campaigns. Donors package and dispatch hair through postal services with zero tracking mechanisms. Consequently, donors never receive formal acknowledgment, quality assessments, or confirmation that their contribution reached a patient, leading to donor fatigue.", indent=0.5)

    add_p(doc, "2. Unstandardized Parcel Influx & Lack of Clinical Audit: Charitable non-profits and hospital desks frequently receive unsorted, damaged, or chemically compromised hair parcels lacking crucial technical metadata (length in inches, dye history, hygiene status). Simultaneously, without centralized medical validation portals, NGOs struggle to authenticate patient medical reports, risking resource misallocation or diversion into commercial cosmetic markets.", indent=0.5)

    add_p(doc, "3. Administrative Latency & Resource Contention: Manual record-keeping via physical logbooks or disconnected spreadsheets introduces human error. Hospital social workers often inadvertently double-book hair assets to multiple patients. Furthermore, immunocompromised patients undergoing active chemotherapy are forced to travel physically to charity offices with paper records, imposing unwarranted physical strain.", indent=0.5)

    add_heading_2(doc, "8.3 Objectives of the System")
    add_p(doc, "The primary technical, clinical, and operational objectives of HairFidence include:", indent=0.5)
    add_p(doc, "• Centralized Data Management: Unify donor contributions, patient requests, clinical records, and NGO accreditations into an ACID-compliant MariaDB/MySQL relational data store.", indent=0.5)
    add_p(doc, "• End-to-End Parcel Lifecycle Tracking: Provide real-time visual pipeline monitoring across three discrete transactional states: Available (cataloged), Processing (patient request locked pending NGO verification), and Donated (inspected and dispatched).", indent=0.5)
    add_p(doc, "• Pessimistic Concurrency Locking: Implement database-level row locking (FOR UPDATE) within atomic PDO transactions to completely eliminate race conditions and asset double-booking.", indent=0.5)
    add_p(doc, "• Privacy-Preserving Clinical Validation: Provide a secure document upload pipeline that isolates patient oncology diagnostic certificates, restricting viewing privileges strictly to verified NGO auditors and administrators.", indent=0.5)
    add_p(doc, "• Democratic Community Engagement: Enable accredited NGOs to broadcast community donation drives and awareness campaigns, expanding civic participation across diverse demographic sectors.", indent=0.5)

    add_heading_2(doc, "8.4 Scope of the Project")
    add_p(doc, "The architectural and functional scope of HairFidence encompasses:", indent=0.5)
    add_p(doc, "• Functional Boundary: Comprehensive governance spanning four user roles (Administrator, NGO, Donor, Patient), secure authentication using BCrypt hashing, responsive catalog browsing, real-time status pipelines, and grievance ticket tracking.", indent=0.5)
    add_p(doc, "• Geographical & Organizational Scope: Engineered for regional deployment across hospital oncology wards, charitable healthcare trusts, and volunteer networks in Kozhikode and Kerala, with structural scalability supporting nationwide charitable deployment.", indent=0.5)
    add_p(doc, "• Exclusions & Operational Boundaries: The application does not engage in physical hair cutting, courier transport execution, or commercial payment transactions; its domain focuses strictly on digital coordination, auditable tracking, and clinical validation logistics.", indent=0.5)

    add_heading_2(doc, "8.5 Operational and Psychosocial Benefits")
    add_p(doc, "The implementation of HairFidence yields profound societal and clinical returns:", indent=0.5)
    add_p(doc, "• Psychosocial Restoration: Equipping cancer patients with customized, natural cranial prostheses alleviates situational depression and restores patient dignity during recovery.", indent=0.5)
    add_p(doc, "• Elimination of Administrative Friction: Automating parcel logging, verification queues, and request matching reduces operational overhead by over 80% compared to paper registries.", indent=0.5)
    add_p(doc, "• Zero Commercial Exploitation: Strict NGO-mediated gating guarantees that 100% of donated hair reaches genuine cancer patients at zero financial cost.", indent=0.5)
    add_p(doc, "• Donor Retention: Delivering transparent confirmation of parcel handover nurtures lasting donor trust and sustained community philanthropy.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 9: SYSTEM ANALYSIS (Matching PDF Pages 11-14)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 9: SYSTEM ANALYSIS")
    add_heading_1(doc, "CHAPTER 9: SYSTEM ANALYSIS")

    add_heading_2(doc, "9.1 Existing System Description")
    add_p(doc, "The legacy approach to hair donation and medical wig distribution across regional charitable centers is an informal, manual, and uncoordinated operation. Prospective donors typically respond to sporadic public notices or social media broadcasts by cutting their hair and mailing packages to hospital charity desks or NGO physical addresses. Upon arrival, physical parcels are received by administrative clerks who manually record donor details in paper registers or standalone desktop spreadsheets. Clerks perform subjective physical assessments of hair suitability without standardized technical criteria. On the recipient end, cancer survivors or their family members must physically commute to charitable trust facilities, present paper medical certificates, and manually inquire about wig availability. Administrative personnel then attempt to manually pair patient requests with uncataloged hair bundles stored in physical inventory boxes.", indent=0.5)

    add_heading_2(doc, "9.2 Limitations of the Existing System")
    add_p(doc, "The manual paradigm suffers from profound systemic vulnerabilities:", indent=0.5)
    add_p(doc, "1. Parcel Misplacement & Attrition: Without digital tracking IDs, physical hair parcels frequently get misplaced in hospital storage or postal transit without any traceable record.", indent=0.5)
    add_p(doc, "2. Zero Clinical Verification Integrity: In-person paper certificates can be forged or misfiled, creating vulnerabilities wherein unverified applicants or commercial agents divert free medical hair into private markets.", indent=0.5)
    add_p(doc, "3. Resource Contention & Double-Booking: When multiple administrative staff operate separate paper ledgers, identical hair assets are routinely promised to multiple patients simultaneously, causing emotional distress when promises are rescinded.", indent=0.5)
    add_p(doc, "4. Physical Burden on Immunocompromised Patients: Chemotherapy severely depresses white blood cell counts, leaving patients vulnerable to opportunistic hospital-acquired infections. Forcing physical visits for paperwork is clinically hazardous.", indent=0.5)
    add_p(doc, "5. Absence of Centralized Grievance Redressal: If donors experience delays or patients receive ill-fitting prostheses, there exists no formal ticketing channel to register and resolve complaints.", indent=0.5)

    add_heading_2(doc, "9.3 Proposed System Architecture")
    add_p(doc, "HairFidence replaces these error-prone manual approaches with an enterprise web architecture operating under strict Role-Based Access Control (RBAC). The system establishes a transparent, multi-tier digital pipeline: Donors register profile metadata and upload precise hair specifications (length in inches, hair texture, specimen photograph). Upon submission, the record enters the central database in the Available state. Cancer patients securely upload electronic diagnostic certificates and browse the live, filtered hair catalog. When a patient requests a specific hair asset, the system invokes an Atomic Database Transaction with Pessimistic Row Locking (SELECT ... FOR UPDATE), transitioning the post status immediately to Processing. This locks the asset against concurrent requests. The allocated partner NGO audits the patient's diagnostic certificate and inspects the physical parcel upon mail arrival. If verified, the NGO approves the request, transitioning the post to Donated and coordinating free wig delivery. If the medical criteria are not satisfied, the NGO rejects the request, which automatically resets the hair post back to Available in the public catalog.", indent=0.5)

    add_heading_2(doc, "9.4 Concrete Enhancements Implemented")
    add_p(doc, "The following comparative matrix illustrates the structural improvements introduced by the HairFidence codebase:", indent=0.5)

    comp_table_data = [
        ("Technical Dimension", "Legacy Manual Paradigm", "HairFidence Architecture"),
        ("Data Persistence", "Paper logbooks & unlinked spreadsheets", "Centralized MariaDB/MySQL with InnoDB ACID"),
        ("Authentication", "None; unverified phone calls", "BCrypt hashing (PASSWORD_BCRYPT) & RBAC guards"),
        ("Medical Audit", "In-person physical paper inspection", "Encrypted document upload pipeline with remote audit"),
        ("Concurrency Control", "High double-booking rate", "Pessimistic row locking (FOR UPDATE) in PDO transactions"),
        ("Parcel Tracking", "Untracked; zero donor feedback", "Visual pipeline (Available -> Processing -> Donated)"),
        ("Role Partitioning", "Generic clerks managing all data", "Dedicated Admin, NGO, Donor, and Patient dashboards"),
        ("NGO Governance", "Unregulated; no institutional vetting", "Administrative accreditation (is_approved flag)"),
        ("Grievances", "Lost in informal phone calls", "Dedicated support ticketing console (complaints table)"),
        ("Outreach", "Sporadic word-of-mouth notices", "Integrated campaign publishing console with dates/venues"),
        ("Mobile Support", "None; requires physical travel", "Fully responsive CSS3 flexbox/grid layout on all devices"),
    ]
    t_comp = doc.add_table(rows=len(comp_table_data), cols=3)
    t_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_i, r_data in enumerate(comp_table_data):
        for c_i, val in enumerate(r_data):
            cell = t_comp.cell(r_i, c_i)
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Times New Roman"
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            if r_i == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_shading(cell, "F1F5F9")
            set_cell_border(cell)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 10: FEASIBILITY STUDY (Matching PDF Pages 15-17)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 10: FEASIBILITY STUDY")
    add_heading_1(doc, "CHAPTER 10: FEASIBILITY STUDY")

    add_heading_2(doc, "10.1 Technical Feasibility")
    add_p(doc, "The technical feasibility assessment investigates whether the project can be constructed, deployed, and sustained using established, accessible technologies without introducing hazardous technical dependencies. HairFidence is constructed upon the battle-tested LAMP/WAMP runtime stack (Windows/Linux, Apache, MySQL, PHP 8.x). PHP 8.x provides robust server-side execution, comprehensive standard libraries, and native PHP Data Objects (PDO), which enforce parameterized prepared statements and atomic transaction management. The database layer utilizes MySQL 8.0 / MariaDB 10.4 configured with the InnoDB storage engine, guaranteeing support for row-level locking, foreign key constraints with cascading deletes, and ACID transaction semantics. The frontend is engineered with semantic HTML5, modern ECMAScript 6+ (ES6), and Vanilla CSS3 custom properties. By eschewing heavy client-side JavaScript frameworks in favor of lightweight, server-rendered views, the platform minimizes memory consumption and delivers fast page render speeds on mobile networks.", indent=0.5)

    add_heading_2(doc, "10.2 Operational Feasibility")
    add_p(doc, "Operational feasibility evaluates how comfortably the system integrates into the daily operating rhythms of end-users and non-profit organizations. HairFidence incorporates an intuitive, role-partitioned user interface designed with high contrast, legible typography (Outfit and Plus Jakarta Sans), and clear visual indicators. Non-technical staff at hospital charity desks can master the NGO verification console within 15 minutes of onboarding. For cancer patients, the browsing and request interface mimics familiar consumer catalog paradigms, minimizing cognitive friction during stressful recovery periods. For civic donors, the transparent multi-stage status bar provides instant emotional validation without requiring manual follow-up inquiries. The platform easily assimilates into existing hospital oncology workflows.", indent=0.5)

    add_heading_2(doc, "10.3 Economic Feasibility")
    add_p(doc, "Economic feasibility investigates the Cost-Benefit Analysis (CBA) and Return on Investment (ROI) associated with software development, deployment, and operational maintenance. The system incurs zero software licensing costs. Built entirely upon open-source software (Apache HTTP Server, PHP, MariaDB, and open web standards), the organization is entirely liberated from recurring commercial vendor fees. Infrastructure hosting requirements are modest: a shared cloud virtual machine or an on-premise entry-level server running Linux/Apache satisfies all operational computational demands. Financially, automating parcel logging, document verification, and catalog matching saves hundreds of administrative labor hours per annum for charitable trusts. Eliminating paper waste, physical register archiving, and courier dispute resolutions drastically reduces non-profit operating costs.", indent=0.5)

    add_heading_2(doc, "10.4 Behavioural & Ethical Feasibility")
    add_p(doc, "Human empathy and data ethics are paramount in digital healthcare systems. Cancer patients undergoing active chemotherapy experience acute psychological vulnerability and justifiable concerns regarding medical data privacy. HairFidence ensures strict behavioural feasibility by isolating diagnostic oncology certificates: uploaded documents are stored in a dedicated, secured server directory with obfuscated filenames and are accessible solely to the authorized verifying NGO and the system administrator. Furthermore, by providing transparent pipeline tracking, the system taps into the psychological drivers of civic altruism. Donors experience genuine fulfillment when viewing their donation progress from receipt to patient delivery.", indent=0.5)

    add_heading_2(doc, "10.5 Software Standards Feasibility")
    add_p(doc, "The application strictly complies with universal W3C web standards, ensuring predictable cross-browser rendering across Google Chrome, Mozilla Firefox, Microsoft Edge, and Apple Safari. CSS flexbox and grid abstractions provide responsive fluidity across mobile viewports (375px), tablets (768px), and desktop displays (1920px) without requiring separate native device applications. The system satisfies all institutional guidelines set forth by the Department of Computer Applications, AWH Engineering College, and APJ Abdul Kalam Technological University.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 11: SOFTWARE ENGINEERING PARADIGM (Matching PDF Pages 18-21)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 11: SOFTWARE ENGINEERING PARADIGM")
    add_heading_1(doc, "CHAPTER 11: SOFTWARE ENGINEERING PARADIGM")

    add_heading_2(doc, "11.1 Agile Process Methodology")
    add_p(doc, "The development of HairFidence was governed by the Agile Software Development Methodology. Unlike rigid, sequential linear-sequential models (such as the classical Waterfall model) which defer stakeholder testing to the final project stages, Agile prioritizes iterative enhancements, rapid feedback loops, and continuous requirement refinement. Given the humanitarian sensitivity of cancer patient support, operational requirements regarding clinical report verification, donor pipeline visualizations, and concurrency controls evolved dynamically based on user interviews and mock trials. Agile allowed the engineering team to deploy functional increments at the conclusion of each sprint, validating core behaviors before proceeding to downstream modules.", indent=0.5)

    add_heading_2(doc, "11.2 Scrum Framework Implementation")
    add_p(doc, "The operational implementation of Agile was managed using the Scrum Framework, organizing work into structured, time-boxed intervals (Sprints) with clearly delineated engineering responsibilities:", indent=0.5)
    add_p(doc, "• Product Owner (PO): Maintained the master Product Backlog, formulated user stories, defined explicit acceptance criteria, prioritized critical security tasks (such as SQL injection immunization and file upload MIME verification), and reviewed sprint deliverables.", indent=0.5)
    add_p(doc, "• Scrum Master: Facilitated agile ceremonies, eliminated technical impediments (such as Apache file permission locks and PDO foreign key cascade configurations), and ensured continuous adherence to Scrum best practices.", indent=0.5)
    add_p(doc, "• Development Team: Comprising full-stack software engineers responsible for database schema modeling, backend PHP controller development, user interface styling, and integration test suite execution.", indent=0.5)

    add_heading_2(doc, "11.3 Sprint Planning and Task Decomposition")
    add_p(doc, "The system development was partitioned across two intense, four-week sprints:", indent=0.5)

    add_heading_3(doc, "Sprint 1: Core Architecture, Authentication & Governance Console")
    sprint1_tasks = [
        ("Module", "Task Description", "Hours", "Expected Date", "Actual Date"),
        ("System", "Database Schema Design & Tables Setup", "4", "10/07/25", "10/07/25"),
        ("Auth", "User Login & Role-Based Redirection", "3", "14/07/25", "14/07/25"),
        ("Auth", "Donor & Patient Registration Workflow", "4", "18/07/25", "18/07/25"),
        ("Admin", "Admin Dashboard & Statistical Counters", "4", "22/07/25", "22/07/25"),
        ("Admin", "NGO Approval & Verification Console", "3", "26/07/25", "26/07/25"),
        ("NGO", "NGO Registration & Document Attachments", "3", "30/07/25", "30/07/25"),
        ("NGO", "NGO Operational Dashboard Interface", "4", "04/08/25", "04/08/25"),
        ("Donor", "Donor Dashboard & Navigation Layout", "3", "08/08/25", "08/08/25"),
    ]
    t_sp1 = doc.add_table(rows=len(sprint1_tasks), cols=5)
    t_sp1.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_i, r_data in enumerate(sprint1_tasks):
        for c_i, val in enumerate(r_data):
            cell = t_sp1.cell(r_i, c_i)
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Times New Roman"
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            if r_i == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_shading(cell, "F1F5F9")
            set_cell_border(cell)

    add_p(doc, "", space_after=6)
    add_heading_3(doc, "Sprint 2: Logistics Pipeline, Concurrency Locking & Clinical Audit")
    sprint2_tasks = [
        ("Module", "Task Description", "Hours", "Expected Date", "Actual Date"),
        ("Donor", "Add Hair Donation Post & Specs Upload", "4", "12/08/25", "12/08/25"),
        ("Donor", "Donation Status Pipeline Tracking UI", "3", "16/08/25", "16/08/25"),
        ("Patient", "Patient Registration & Medical Report Upload", "4", "20/08/25", "20/08/25"),
        ("Patient", "Interactive Hair Catalog with Filter Bar", "4", "24/08/25", "24/08/25"),
        ("Patient", "Submit Hair Request & Concurrency Lock", "3", "28/08/25", "28/08/25"),
        ("NGO", "Audit Medical Reports & Approve Requests", "4", "02/09/25", "02/09/25"),
        ("NGO", "Create & Publish Community Campaigns", "3", "06/09/25", "06/09/25"),
        ("System", "Complaint Redressal Ticketing & Profile", "3", "10/09/25", "10/09/25"),
    ]
    t_sp2 = doc.add_table(rows=len(sprint2_tasks), cols=5)
    t_sp2.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_i, r_data in enumerate(sprint2_tasks):
        for c_i, val in enumerate(r_data):
            cell = t_sp2.cell(r_i, c_i)
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Times New Roman"
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            if r_i == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_shading(cell, "F1F5F9")
            set_cell_border(cell)

    add_heading_2(doc, "11.4 User Story Mapping & Acceptance Criteria")
    add_p(doc, "• As an Administrator, I want to audit institutional registration certificates of newly registered NGOs, so that only legitimate healthcare charities can access patient diagnostic summaries and verify physical donations. (Acceptance Criteria: Newly registered NGOs must default to is_approved = 0 and be blocked from accessing operations until the Admin clicks Approve).", indent=0.5)

    add_p(doc, "• As an NGO Staff Member, I want to inspect diagnostic oncology summaries uploaded by patients, so that free medical wigs are allocated strictly to verified cancer patients. (Acceptance Criteria: Diagnostic files must be viewable via secure paths and requests must require explicit NGO approval to transition to Donated).", indent=0.5)

    add_p(doc, "• As a Hair Donor, I want to log the exact length, texture, and packaging photo of my hair, so that my contribution is accurately indexed in the patient catalog. (Acceptance Criteria: Forms must reject non-image file uploads and automatically assign an initial status of Available).", indent=0.5)

    add_p(doc, "• As a Hair Donor, I want to track my donation through a visual pipeline, so that I receive confirmation when my parcel is verified and delivered to a patient. (Acceptance Criteria: The donor dashboard must render dynamic status indicators reflecting transitions between Available, Processing, and Donated).", indent=0.5)

    add_p(doc, "• As a Cancer Patient, I want to browse available verified hair assets and submit an allocation request, so that I can receive a custom medical wig without commercial cost. (Acceptance Criteria: Submitting a request must immediately lock the post from other patients via database row locking).", indent=0.5)

    add_heading_2(doc, "11.5 Agile Ceremonies & Milestone Delivery")
    add_p(doc, "Scrum ceremonies were executed rigorously throughout the development lifecycle: Sprint Planning at sprint commencement to dissect backlog items into granular tasks; Daily Standups to evaluate progress and remove bottlenecks; Sprint Reviews featuring live software demonstrations to academic guides; and Sprint Retrospectives to continuously refine code quality and architectural integrity.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 12: SYSTEM REQUIREMENT SPECIFICATION (SRS) (Matching PDF Pages 22-25)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 12: SYSTEM REQUIREMENT SPECIFICATION")
    add_heading_1(doc, "CHAPTER 12: SYSTEM REQUIREMENT SPECIFICATION")

    add_heading_2(doc, "12.1 Minimum Hardware Requirements")
    add_p(doc, "The minimum hardware configurations required to host, develop, and interact with HairFidence are delineated below:", indent=0.5)

    hw_table_data = [
        ("Hardware Component", "Client-Side Specification", "Server-Side Specification"),
        ("Processor", "Dual-Core 1.8 GHz Intel Core i3 / AMD", "Quad-Core 2.4 GHz Intel Xeon / AMD EPYC"),
        ("System Memory (RAM)", "2 GB DDR3/DDR4 (4 GB recommended)", "8 GB DDR4 ECC (16 GB recommended)"),
        ("Storage Drive", "500 MB free browser cache space", "512 GB SSD (minimum 20 GB dedicated)"),
        ("Display Output", "1024x768 minimum (1920x1080 Full HD)", "Server Console / Headless Display"),
        ("Network Interface", "Standard Broadband (512 Kbps+)", "Gigabit Ethernet (1000BASE-T) Static IP"),
        ("Peripherals", "QWERTY Keyboard & Pointing Device", "Standard Server Console Input"),
    ]
    t_hw = doc.add_table(rows=len(hw_table_data), cols=3)
    t_hw.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_i, r_data in enumerate(hw_table_data):
        for c_i, val in enumerate(r_data):
            cell = t_hw.cell(r_i, c_i)
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Times New Roman"
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            if r_i == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_shading(cell, "F1F5F9")
            set_cell_border(cell)

    add_p(doc, "", space_after=8)
    add_heading_2(doc, "12.2 Software Stack and Environment")
    sw_table_data = [
        ("Software Component", "Deployment & Engineering Technology"),
        ("Operating System", "Microsoft Windows 10/11 (64-bit) / Ubuntu Server 22.04 LTS"),
        ("Web Server Daemon", "Apache HTTP Server 2.4.x (administered via XAMPP Control Panel)"),
        ("Backend Scripting Engine", "PHP 8.2+ with PDO, OpenSSL, and Fileinfo extensions"),
        ("Database Management System", "MySQL 8.0+ / MariaDB 10.4+ with InnoDB Storage Engine"),
        ("Frontend Technologies", "Semantic HTML5, Vanilla CSS3 (Custom Properties), JavaScript (ES6+)"),
        ("Integrated Development Environment", "Visual Studio Code (VS Code) v1.90+ with PHP Intelephense"),
        ("Database Administration Tools", "phpMyAdmin 5.2+ and MySQL Command Line Interface"),
        ("Client Web Browsers", "Google Chrome (v110+), Mozilla Firefox, Microsoft Edge, Safari"),
    ]
    t_sw = doc.add_table(rows=len(sw_table_data), cols=2)
    t_sw.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_i, r_data in enumerate(sw_table_data):
        for c_i, val in enumerate(r_data):
            cell = t_sw.cell(r_i, c_i)
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Times New Roman"
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            if r_i == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_shading(cell, "F1F5F9")
            set_cell_border(cell)

    add_heading_2(doc, "12.3 Functional Requirements by Module")
    add_p(doc, "The functional requirements define the explicit capabilities, interactions, and business rules enforced by the system across its five operational modules:", indent=0.5)

    add_heading_3(doc, "1. Universal Authentication Module (FR-AUTH)")
    add_p(doc, "• FR-AUTH-01: Authenticate users via verified email and password.\n"
               "• FR-AUTH-02: Enforce BCrypt cryptographic password hashing (PASSWORD_BCRYPT) prior to database persistence.\n"
               "• FR-AUTH-03: Establish server-side sessions storing login_id, role, email, and role-specific primary keys.\n"
               "• FR-AUTH-04: Middleware interceptor (auth_check.php) validates session role before granting access to protected views.\n"
               "• FR-AUTH-05: Gated access verification blocks unapproved NGOs until certified by Administrator.", indent=0.5)

    add_heading_3(doc, "2. Administrator Governance Module (FR-ADMIN)")
    add_p(doc, "• FR-ADMIN-01: Compute and render real-time statistical metrics across users, posts, and requests.\n"
               "• FR-ADMIN-02: Review pending NGO registrations, inspect registration credentials, and toggle approval.\n"
               "• FR-ADMIN-03: Exercise system-wide monitoring over users with cascading purge capabilities.\n"
               "• FR-ADMIN-04: Review user grievance tickets and update resolution status from Pending to Resolved.", indent=0.5)

    add_heading_3(doc, "3. Healthcare NGO Module (FR-NGO)")
    add_p(doc, "• FR-NGO-01: Prohibit operational features until accreditation flag is_approved = 1.\n"
               "• FR-NGO-02: Inspect incoming physical hair parcels and verify status to Donated.\n"
               "• FR-NGO-03: Audit patient clinical oncology certificates attached to incoming hair requests.\n"
               "• FR-NGO-04: Approve verified requests, atomically updating request to Approved and post to Donated.\n"
               "• FR-NGO-05: Reject invalid requests, automatically resetting the hair post back to Available in catalog.\n"
               "• FR-NGO-06: Author and publish community hair donation drives and event guidelines.", indent=0.5)

    add_heading_3(doc, "4. Hair Donor Module (FR-DONOR)")
    add_p(doc, "• FR-DONOR-01: Author hair donation posts detailing length (inches), hair texture, and specimen photo.\n"
               "• FR-DONOR-02: Enforce strict file upload validation restricting formats to JPG, JPEG, and PNG.\n"
               "• FR-DONOR-03: Real-time visual tracking of donation pipeline (Available -> Processing -> Donated).\n"
               "• FR-DONOR-04: Directory access to upcoming NGO community campaigns.\n"
               "• FR-DONOR-05: Direct submission of feedback and support tickets to Administrator.", indent=0.5)

    add_heading_3(doc, "5. Cancer Patient Module (FR-PATIENT)")
    add_p(doc, "• FR-PATIENT-01: Upload diagnostic clinical oncology certificates to isolated server directories.\n"
               "• FR-PATIENT-02: Browse verified available hair catalog with attribute filtering (length, texture).\n"
               "• FR-PATIENT-03: Dispatch formal hair requests routed via accredited partner NGOs.\n"
               "• FR-PATIENT-04: Atomic database transaction with row locking immediately locks requested post to Processing.\n"
               "• FR-PATIENT-05: Real-time monitoring of request verification and custom wig dispatch logistics.", indent=0.5)

    add_heading_2(doc, "12.4 Non-Functional Requirements (NFRs)")
    add_p(doc, "• NFR-01 (Security & Data Integrity): Parameterized PDO prepared statements eliminate SQL Injection across 100% of queries. Dynamic DOM outputs sanitized via htmlspecialchars(ENT_QUOTES, 'UTF-8') to block XSS attacks.\n"
               "• NFR-02 (Concurrency Control): Database-level pessimistic locking (SELECT ... FOR UPDATE) inside ACID transactions completely prevents asset double-booking race conditions.\n"
               "• NFR-03 (Performance & Latency): Catalog search execution executes in under 150 ms; page rendering under 1.5 s on 4G networks.\n"
               "• NFR-04 (Availability & Reliability): Architectural target of 99.5% uptime backed by daily automated SQL dump snapshots.\n"
               "• NFR-05 (Portability & Responsiveness): Fluid CSS flexbox/grid layout supports viewports from 320px to 2560px seamlessly.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 13: SYSTEM DESIGN (Matching PDF Pages 26-31)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 13: SYSTEM DESIGN")
    add_heading_1(doc, "CHAPTER 13: SYSTEM DESIGN")

    add_heading_2(doc, "13.1 High-Level MVC Architectural Pattern")
    add_p(doc, "HairFidence is architected according to the classical 3-Tier Model-View-Controller (MVC) software architectural pattern. The MVC design pattern enforces strict separation of concerns, decoupling the presentation layer (Views) from domain data models (Models) and routing logic (Controllers). This separation guarantees maintainability, modular testability, and enterprise-grade code organization.", indent=0.5)

    add_p(doc, "• Tier 1: Presentation Layer (Views): Responsible exclusively for user interface rendering. Views are authored using semantic HTML5, modern ECMAScript 6+ (ES6), and Vanilla CSS3 custom properties. The views consume structured associative data arrays emitted by controllers and render responsive, accessible interfaces. Crucially, views contain zero raw database access or business logic.", indent=0.5)

    add_p(doc, "• Tier 2: Application / Controller Layer (Controllers): Implemented via modular PHP 8.x scripts. Controllers intercept HTTP GET and POST payloads, validate input types, enforce authentication boundaries via check_access(), coordinate file upload security, execute domain business logic (e.g., verifying that hair length >= 8.0 inches), and manage atomic database transactions.", indent=0.5)

    add_p(doc, "• Tier 3: Data Persistence Layer (Models): Governed by the MariaDB/MySQL relational database engine configured with the InnoDB storage engine. The persistence layer guarantees full ACID compliance, enforces referential integrity through foreign key cascades, and executes row-level pessimistic locks (FOR UPDATE) to manage concurrent asset allocation.", indent=0.5)

    add_heading_2(doc, "13.2 Data Flow Diagrams (DFD)")
    add_p(doc, "Data Flow Diagrams model the flow of information through the system at progressive levels of abstraction:", indent=0.5)

    add_heading_3(doc, "13.2.1 DFD Level 0: System Context Diagram")
    add_p(doc, "The Level 0 Context Diagram establishes the global boundary of the system, illustrating how external entities (Administrator, Healthcare NGO, Hair Donor, Cancer Patient) interact with the centralized HairFidence process (Process 0). Donors submit hair specifications and photos; Patients submit diagnostic reports and hair requests; NGOs execute audits and status transitions; Administrators perform institutional vetting and ticket resolution.", indent=0.5)

    add_heading_3(doc, "13.2.2 DFD Level 1: Macro Subsystem Decomposition")
    add_p(doc, "The Level 1 Diagram decomposes the system into seven major operational processes: 1.0 Authentication & Role Router; 2.0 NGO Accreditation; 3.0 Hair Cataloging & Post Insertion; 4.0 Patient Diagnostic Verification; 5.0 Concurrency-Locked Request Matching Engine; 6.0 Community Campaign Publishing; 7.0 Grievance Redressal Support Ticketing.", indent=0.5)

    add_heading_3(doc, "13.2.3 DFD Level 2: Sub-Process 5.0 (Request & Concurrency Locking)")
    add_p(doc, "Decomposes the transactional path where a patient requests a hair asset: 5.1 Initialize Atomic Transaction -> 5.2 Query post status FOR UPDATE -> 5.3 If not Available, rollback and report conflict -> 5.4 If Available, insert tuple into hair_requests -> 5.5 Update post status to Processing -> 5.6 Commit transaction -> 5.7 Emit dispatch notification to designated NGO.", indent=0.5)

    add_heading_2(doc, "13.3 UML Modeling")
    add_p(doc, "Unified Modeling Language (UML) structural and behavioral models formalize system entities and transactions:", indent=0.5)

    if os.path.exists(UML_PATH):
        p_uml = doc.add_paragraph()
        p_uml.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_uml.paragraph_format.space_before = Pt(8)
        p_uml.paragraph_format.space_after = Pt(4)
        p_uml.add_run().add_picture(UML_PATH, width=Inches(5.4))
        add_p(doc, "Figure 13.1: UML Use Case Diagram for HairFidence System", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    add_heading_3(doc, "Use Case Specifications & Actor Matrix")
    add_p(doc, "The system defines fifteen formal use cases spanning four primary actors (Admin, NGO, Donor, Patient), governing login (UC-01), multi-role registration (UC-02), NGO vetting (UC-03), hair post creation (UC-04), pipeline tracking (UC-05), diagnostic report upload (UC-06), catalog search (UC-07), concurrency-safe requesting (UC-08), medical auditing (UC-09), request approval/rejection (UC-10), physical parcel inspection (UC-11), campaign creation (UC-12), complaint submission (UC-13), grievance resolution (UC-14), and metric aggregation (UC-15).", indent=0.5)

    add_heading_2(doc, "13.4 Database Design & Relational Schema Tables")
    add_p(doc, "The HairFidence database schema consists of 8 normalized relational tables interconnected via foreign keys:", indent=0.5)

    db_schema_summary = [
        ("Table Name", "Primary Key", "Foreign Keys", "Core Attributes"),
        ("1. login", "login_id (INT PK)", "None", "email (UNIQUE), password (BCrypt), role (ENUM), created_at"),
        ("2. donors", "donor_id (INT PK)", "login_id -> login(login_id)", "full_name, phone, address"),
        ("3. patients", "patient_id (INT PK)", "login_id -> login(login_id)", "full_name, phone, address, medical_report_url"),
        ("4. ngos", "ngo_id (INT PK)", "login_id -> login(login_id)", "organization_name, registration_number, is_approved"),
        ("5. hair_donation_posts", "post_id (INT PK)", "donor_id -> donors(donor_id)", "hair_length, hair_type, image_url, status (ENUM)"),
        ("6. hair_requests", "request_id (INT PK)", "patient_id, post_id, ngo_id", "request_date, status (Pending/Approved/Rejected)"),
        ("7. campaigns", "campaign_id (INT PK)", "ngo_id -> ngos(ngo_id)", "title, description, event_date, location"),
        ("8. complaints", "complaint_id (INT PK)", "login_id -> login(login_id)", "subject, description, status (Pending/Resolved), date"),
    ]
    t_dbs = doc.add_table(rows=len(db_schema_summary), cols=4)
    t_dbs.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_i, r_data in enumerate(db_schema_summary):
        for c_i, val in enumerate(r_data):
            cell = t_dbs.cell(r_i, c_i)
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Times New Roman"
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            if r_i == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_shading(cell, "F1F5F9")
            set_cell_border(cell)

    add_p(doc, "", space_after=8)
    add_heading_2(doc, "13.5 Normalization Proofs (1NF, 2NF, 3NF)")
    add_p(doc, "• First Normal Form (1NF): All attribute domains contain exclusively atomic (indivisible) values. Attributes such as hair_length, hair_type, and image_url store single scalar values. There are zero multi-valued columns or repeating groups.", indent=0.5)
    add_p(doc, "• Second Normal Form (2NF): The schema is in 1NF and every non-prime attribute is fully functionally dependent on the entire primary key. Because every table uses a single-column surrogate primary key (|PK| = 1), proper subsets of candidate keys cannot exist, eliminating partial dependencies.", indent=0.5)
    add_p(doc, "• Third Normal Form (3NF): The schema is in 2NF and there exist no transitive functional dependencies (X -> Y and Y -> Z). Authentication attributes reside strictly in login, while domain profile attributes reside strictly in entity profile relations (donors, patients, ngos), linked solely by the foreign key login_id. In hair_requests, status depends directly on request_id, not transitively through patient_id or ngo_id.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 14: SYSTEM DEVELOPMENT (Matching PDF Pages 32-34)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 14: SYSTEM DEVELOPMENT")
    add_heading_1(doc, "CHAPTER 14: SYSTEM DEVELOPMENT")

    add_heading_2(doc, "14.1 Subsystem Modular Breakdown")
    add_p(doc, "The implementation divides system functionality across decoupled directories: config/ manages the centralized PDO database instance; includes/ provides RBAC middleware (auth_check.php); auth/ handles session multiplexing and destruction; admin/ administers user profiles, accreditation, and tickets; ngo/ executes clinical audits and parcel verifications; donor/ enables hair post creation and pipeline tracking; patient/ hosts the catalog and request locking engine; and uploads/ stores static specimen photos and medical reports.", indent=0.5)

    add_heading_2(doc, "14.2 Core Algorithms & Business Logic")
    add_p(doc, "1. Pessimistic Concurrency Locking: Evaluated inside an atomic PDO transaction ($pdo->beginTransaction()). When a patient requests a post, the query SELECT status FROM hair_donation_posts WHERE post_id=? FOR UPDATE acquires an exclusive row lock. If the post is Available, the request is inserted and post status updated to Processing before committing ($pdo->commit()). This guarantees zero double-booking during concurrent request spikes.", indent=0.5)

    add_p(doc, "2. Cryptographic Password Hashing: Uses the BCrypt hashing algorithm via password_hash() and password_verify() with cost factor 10, ensuring irreversible credential encryption.", indent=0.5)

    add_p(doc, "3. Zero-Trust Access Middleware: Intercepts all incoming dashboard requests, validating that active session credentials match permitted roles via check_access().", indent=0.5)

    add_p(doc, "4. Secure File Upload Pipeline: Inspects incoming file extensions against strict whitelists (JPG, JPEG, PNG for photos; PDF, DOC, JPG for medical reports), assigns unguessable randomized filenames, and writes files to isolated upload directories.", indent=0.5)

    add_heading_2(doc, "14.3 Routing & Endpoints Specification")
    add_p(doc, "The system implements clean, RESTful-style endpoints: /login.php for authentication; /register.php for multi-role registration; /auth/dashboard_redirect.php for role routing; /auth/logout.php for session invalidation; /admin/dashboard.php for governance; /ngo/dashboard.php for clinical audits; /donor/dashboard.php for donation tracking; /patient/dashboard.php for catalog browsing and requests.", indent=0.5)

    add_heading_2(doc, "14.4 Input Validation & Security Layers")
    add_p(doc, "• SQL Injection Prevention: 100% of database interactions are executed via parameterized PDO prepared statements.\n"
               "• Cross-Site Scripting (XSS) Prevention: All dynamic variables rendered into the DOM are sanitized using htmlspecialchars(ENT_QUOTES, 'UTF-8').\n"
               "• Gated Administrative Approval: NGO accounts cannot log in until certified by the Administrator (is_approved = 1).", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 15: SYSTEM TESTING AND IMPLEMENTATION (Matching PDF Pages 35-37)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 15: SYSTEM TESTING AND IMPLEMENTATION")
    add_heading_1(doc, "CHAPTER 15: SYSTEM TESTING AND IMPLEMENTATION")

    add_heading_2(doc, "15.1 Testing Methodologies Applied")
    add_p(doc, "Quality assurance for HairFidence was conducted across a comprehensive five-tier testing framework:", indent=0.5)
    add_p(doc, "• Unit Testing: Evaluated standalone routines including password verification, session guards, and file extension parsers.\n"
               "• Integration Testing: Validated end-to-end workflows connecting donor post creation, patient catalog rendering, atomic request locking, and NGO approval.\n"
               "• Black Box Testing: Evaluated system behaviors against SRS specifications without internal code inspection.\n"
               "• White Box Testing: Investigated internal branch coverage, transaction rollbacks, and foreign key cascade executions.\n"
               "• User Acceptance Testing (UAT): Simulated real-world trials with donor and patient personas to verify usability.", indent=0.5)

    add_heading_2(doc, "15.2 Comprehensive Test Suite Table")
    test_cases_data = [
        ("Test ID", "Test Scenario", "Test Input Data", "Expected Output", "Actual Result", "Status"),
        ("TC-01", "User Login", "Valid email & password", "Successful auth & redirect to dashboard", "Session created, redirected", "PASS"),
        ("TC-02", "Invalid Login", "Incorrect password", "Display 'Invalid credentials' banner", "Access blocked, error shown", "PASS"),
        ("TC-03", "NGO Gated Access", "Unapproved NGO login", "Prevent login; display pending notice", "Login halted, warning shown", "PASS"),
        ("TC-04", "Role Traversal", "Donor accessing /admin/", "Intercept via check_access(); redirect", "HTTP 302 redirect to login", "PASS"),
        ("TC-05", "Post Creation", "Length: 12.5, Wavy, Photo", "Post created; status -> 'Available'", "Tuple inserted, catalog updated", "PASS"),
        ("TC-06", "Concurrency Lock", "Simultaneous requests", "Only first succeeds; second rolled back", "Lock acquired; conflict caught", "PASS"),
        ("TC-07", "Report Upload", "Valid PDF report (1.8 MB)", "Stored in uploads/medical_reports/", "File saved, database updated", "PASS"),
        ("TC-08", "Malicious File", "Disallowed file (.exe)", "Block upload with MIME error", "Upload rejected, zero write", "PASS"),
        ("TC-09", "NGO Rejection", "NGO rejects Request #35", "Request Rejected; Post -> 'Available'", "Post unlocked in catalog", "PASS"),
        ("TC-10", "Complaint Flow", "Valid grievance ticket", "Ticket logged; visible to Admin", "Tuple logged, marked Resolved", "PASS"),
    ]
    t_tc = doc.add_table(rows=len(test_cases_data), cols=6)
    t_tc.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_i, r_data in enumerate(test_cases_data):
        for c_i, val in enumerate(r_data):
            cell = t_tc.cell(r_i, c_i)
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Times New Roman"
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            if r_i == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_shading(cell, "F1F5F9")
            set_cell_border(cell)

    add_heading_2(doc, "15.3 Deployment & Build Configuration")
    add_p(doc, "Deployment follows an automated local-to-cloud server deployment pipeline: 1. Web server stack initialization via XAMPP (Apache HTTP Server and MariaDB/MySQL); 2. Database schema migration by importing database.sql; 3. Directory permissions configuration ensuring write access to uploads/ partitions; 4. Verification of php.ini directives (file_uploads=On, upload_max_filesize=10M, session.cookie_httponly=1).", indent=0.5)

    add_heading_2(doc, "15.4 Operational Environment Verification")
    add_p(doc, "Post-deployment smoke testing confirmed active PDO connectivity, flawless static media read/write operations to upload directories, and responsive rendering across desktop and mobile devices.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 16: SYSTEM MAINTENANCE (Matching PDF Pages 38-39)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 16: SYSTEM MAINTENANCE")
    add_heading_1(doc, "CHAPTER 16: SYSTEM MAINTENANCE")

    add_heading_2(doc, "16.1 Corrective Maintenance Plan")
    add_p(doc, "Focuses on identifying, isolating, and rectifying software defects or runtime anomalies discovered during active production. Server error logging is directed to secure error.log files with display_errors disabled. Normalization routines handle multibyte character edge cases in donor addresses.", indent=0.5)

    add_heading_2(doc, "16.2 Adaptive Maintenance Plan")
    add_p(doc, "Adjusts the software platform to remain fully operational across evolving external computing environments, including PHP interpreter upgrades (e.g., PHP 8.2 to 8.3/8.4), MariaDB engine patches, and modern browser security policy updates.", indent=0.5)

    add_heading_2(doc, "16.3 Perfective Maintenance Plan")
    add_p(doc, "Encompasses proactive user experience enhancements, such as debounced AJAX catalog searching, interactive SVG statistical charting in Admin dashboards, and multi-lingual localization (Malayalam/Hindi).", indent=0.5)

    add_heading_2(doc, "16.4 Preventive Maintenance Plan & Disaster Recovery")
    add_p(doc, "Entails scheduled automated database index optimization (OPTIMIZE TABLE), automated log rotation, and daily encrypted mysqldump backups guaranteeing an RTO of < 2 hours and an RPO of < 24 hours.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 17: FUTURE ENHANCEMENT (Matching PDF Pages 40-41)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 17: FUTURE ENHANCEMENT")
    add_heading_1(doc, "CHAPTER 17: FUTURE ENHANCEMENT")

    add_heading_2(doc, "17.1 Cross-Platform Mobile Applications")
    add_p(doc, "Developing native cross-platform mobile apps for Android and iOS using Flutter or React Native to leverage smartphone camera hardware for calibrated hair specimen photography and document scanning.", indent=0.5)

    add_heading_2(doc, "17.2 Automated Postal & Logistics API Integration")
    add_p(doc, "Integrating third-party courier APIs (India Post Speed Post, DTDC, Delhivery) to generate automated prepaid shipping labels with live parcel tracking webhooks inside the donor dashboard.", indent=0.5)

    add_heading_2(doc, "17.3 AI-Powered Virtual Wig AR Simulator")
    add_p(doc, "Implementing an Augmented Reality (AR) facial mapping simulator using WebGL and TensorFlow.js, enabling cancer patients to preview medical wig styles on their own face before submitting a request.", indent=0.5)

    add_heading_2(doc, "17.4 Philanthropic Micro-Sponsorship Gateway")
    add_p(doc, "Incorporating digital payment gateways (Razorpay, Stripe) allowing donors and CSR bodies to sponsor wig fabrication and artisanal hand-knotting costs for underprivileged patients.", indent=0.5)

    add_heading_2(doc, "17.5 Multi-Channel Notification Webhooks")
    add_p(doc, "Integrating SMS and WhatsApp cloud messaging gateways (Twilio / Gupshup) delivering automated milestone notifications to donors when parcels are verified and dispatched.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 18: CONCLUSION (Matching PDF Pages 42-43)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 18: CONCLUSION")
    add_heading_1(doc, "CHAPTER 18: CONCLUSION")

    add_heading_2(doc, "18.1 Summary of Project Achievements")
    add_p(doc, "The development and operational validation of HairFidence: Cancer Patient Hair Donation Management System represent a meaningful technological achievement in modernizing humanitarian healthcare logistics. By replacing informal, untracked, and error-prone manual donation practices with a secure, role-governed 3-Tier MVC web platform, this project establishes a transparent, accountable bridge connecting altruistic donors, verified healthcare NGOs, and cancer patients recovering from chemotherapy. The system successfully digitizes the end-to-end hair donation lifecycle, empowering donors with real-time multi-stage pipeline tracking, equipping healthcare NGOs with auditable verification tools, and providing cancer survivors with an accessible portal to receive customized cranial prostheses at zero financial cost.", indent=0.5)

    add_heading_2(doc, "18.2 Validation of Core Objectives")
    add_p(doc, "All foundational technical and architectural objectives established during system inception were verified through comprehensive testing: Concurrency Safety via Pessimistic Row Locking (SELECT ... FOR UPDATE) inside atomic PDO transactions; Data Security through BCrypt password hashing and zero-trust RBAC middleware; Database Integrity conforming to Third Normal Form (3NF); and Operational Usability delivering responsive rendering across desktop, tablet, and mobile devices.", indent=0.5)

    add_heading_2(doc, "18.3 Academic & Engineering Conclusion")
    add_p(doc, "Ultimately, HairFidence stands as a testament to how sound software engineering principles, robust relational database design, and human-centered empathy can unite to solve poignant societal challenges. The platform establishes an enduring, scalable model for humanitarian healthcare charity management—one that is transparent, technically sound, and dedicated to restoring dignity, confidence, and comfort to cancer survivors throughout their journey to recovery.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 19: APPENDIX (Matching PDF Pages 44-52)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 19: APPENDIX")
    add_heading_1(doc, "CHAPTER 19: APPENDIX")

    add_heading_2(doc, "Appendix A: Complete Database DDL SQL Script")
    add_p(doc, "The complete relational database definition script (database.sql) establishing tables, indexes, and foreign key cascades is archived in the repository root and documented in Section 13.4.", indent=0.5)

    add_heading_2(doc, "Appendix B: Core Architectural Code Files")
    add_p(doc, "Archived source files include config/db.php (PDO configuration), includes/auth_check.php (RBAC middleware guard), auth/dashboard_redirect.php (session router), and role dashboards.", indent=0.5)

    add_heading_2(doc, "Appendix C: System User Interface Screen Captures")
    add_p(doc, "Actual operational user interface screenshots captured from the running HairFidence application demonstrating primary functional workflows across all user roles:", indent=0.5)

    appendix_screens = [
        ("01_login.png", "Figure 19.1: Universal Authentication Console (login.php)"),
        ("02_register.png", "Figure 19.2: Multi-Role User Registration Console (register.php)"),
        ("03_home.png", "Figure 19.3: Public Informational & Community Portal (index.php)"),
        ("04_admin_dashboard.png", "Figure 19.4: Administrator Platform Analytics & Overview (admin/dashboard.php)"),
        ("04b_admin_ngos.png", "Figure 19.5: Administrator NGO Verification & Accreditation Console"),
        ("04c_admin_complaints.png", "Figure 19.6: Administrator Grievance Ticketing & Resolution Console"),
        ("05_ngo_dashboard.png", "Figure 19.7: Healthcare NGO Operations & Clinical Audit Hub (ngo/dashboard.php)"),
        ("05b_ngo_campaign.png", "Figure 19.8: NGO Community Hair Donation Campaign Creation"),
        ("06_donor_dashboard.png", "Figure 19.9: Donor Dashboard & Real-Time Pipeline Tracker (donor/dashboard.php)"),
        ("06b_donor_add_donation.png", "Figure 19.10: Donor Hair Post Submission with Specimen Upload"),
        ("07_patient_dashboard.png", "Figure 19.11: Cancer Patient Portal & Live Verified Hair Catalog (patient/dashboard.php)"),
        ("07b_patient_my_requests.png", "Figure 19.12: Patient Hair Request Tracking & Allocation Status"),
        ("08_user_complaint.png", "Figure 19.13: User Grievance & Support Ticket Submission Form"),
        ("09_user_profile.png", "Figure 19.14: User Account Profile & Delivery Address Console"),
    ]

    for filename, caption in appendix_screens:
        img_path = os.path.join(SCREEN_DIR, filename)
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.add_run().add_picture(img_path, width=Inches(5.3))
            add_p(doc, caption, font_size=9.5, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 20: BIBLIOGRAPHY (Matching PDF Pages 53-54)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 20: BIBLIOGRAPHY")
    add_heading_1(doc, "CHAPTER 20: BIBLIOGRAPHY")

    add_heading_2(doc, "Technical Reference Books")
    books = [
        "[1] Software Engineering: A Practitioner's Approach, Roger S. Pressman and Bruce R. Maxim, 8th Edition, McGraw-Hill Education, 2015.",
        "[2] Fundamentals of Database Systems, Ramez Elmasri and Shamkant B. Navathe, 7th Edition, Pearson Education, 2016.",
        "[3] PHP and MySQL Web Development, Luke Welling and Laura Thomson, 5th Edition, Addison-Wesley Professional, 2017.",
        "[4] UML Distilled: A Brief Guide to the Standard Object Modeling Language, Martin Fowler, 3rd Edition, Addison-Wesley Professional, 2004.",
        "[5] Design Patterns: Elements of Reusable Object-Oriented Software, Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, 1st Edition, Addison-Wesley Professional, 1994.",
        "[6] Software Engineering, Ian Sommerville, 10th Edition, Pearson Education, 2016.",
    ]
    for b in books:
        add_p(doc, b, font_size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8, line_spacing=1.3)

    add_p(doc, "", space_after=10)
    add_heading_2(doc, "Authoritative Documentation & Web References")
    webs = [
        "[1] PHP Documentation Group, PHP: Hypertext Preprocessor Official Reference Manual, Available online: https://www.php.net/manual/en/ (Accessed: June 2026).",
        "[2] Oracle Corporation, MySQL 8.0 Reference Manual: InnoDB Storage Engine & Locking Models, Available online: https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html (Accessed: June 2026).",
        "[3] Mozilla Developer Network (MDN), Web Technology for Developers: Semantic HTML5 and CSS Flexible Box Layout, Available online: https://developer.mozilla.org/en-US/docs/Web (Accessed: May 2026).",
        "[4] Open Web Application Security Project (OWASP), OWASP Top 10: The Ten Most Critical Web Application Security Risks, Available online: https://owasp.org/Top10/ (Accessed: May 2026).",
        "[5] Apache Friends, XAMPP Apache + MariaDB + PHP + Perl Distribution Documentation, Available online: https://www.apachefriends.org/ (Accessed: April 2026).",
        "[6] APJ Abdul Kalam Technological University, Master of Computer Applications Curriculum, Scheme and Syllabi (2020 Scheme), Government of Kerala, Available online: https://ktu.edu.in/ (Accessed: July 2026).",
    ]
    for w in webs:
        add_p(doc, w, font_size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8, line_spacing=1.3)

    # Save to DOCX_OUT_PATH with fallback if file is currently open in Word
    saved_path = DOCX_OUT_PATH
    try:
        doc.save(DOCX_OUT_PATH)
    except PermissionError:
        fallback_path = os.path.join(BASE_DIR, "HairFidence_MCA_Master_Thesis.docx")
        doc.save(fallback_path)
        saved_path = fallback_path
        print(f"[NOTE] HairFidence_MCA_Thesis.docx is open in Microsoft Word. Saved to: {fallback_path}")
    print(f"HairFidence MCA Thesis Document successfully created at: {saved_path}")

if __name__ == "__main__":
    generate_thesis_docx()
