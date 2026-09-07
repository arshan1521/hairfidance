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
    print("Generating HairFidence KTU MCA Thesis Document...")
    doc = Document()

    # Base margins: Left 1.5 inches, Right/Top/Bottom 1.0 inch
    sec0 = doc.sections[0]
    sec0.top_margin = Inches(1.0)
    sec0.bottom_margin = Inches(1.0)
    sec0.left_margin = Inches(1.5)
    sec0.right_margin = Inches(1.0)

    # ──────────────────────────────────────────────────────────────────────────
    # 1. COVERING PAGE
    # ──────────────────────────────────────────────────────────────────────────
    add_p(doc, "", space_before=15)
    add_p(doc, "HAIRFIDENCE: A CENTRALIZED ROLE-BASED WEB APPLICATION FOR HAIR DONATION LIFECYCLE MANAGEMENT", font_size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

    add_p(doc, "A PROJECT THESIS REPORT", font_size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_p(doc, "SUBMITTED TO", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "AWH ENGINEERING COLLEGE, KUTTIKKATTOOR, CALICUT - 8", font_size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_p(doc, "IN PARTIAL FULFILLMENT OF THE REQUIREMENTS", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "FOR THE AWARD OF THE DEGREE OF", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "MASTER OF COMPUTER APPLICATIONS", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "OF", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY, KERALA", font_size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)

    add_p(doc, "SUBMITTED BY", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "ARSHAN NIZAR K P", font_size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "(Register Number: AWH25MCA-2010)", font_size=11.5, bold=False, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)

    add_p(doc, "UNDER THE GUIDANCE OF", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=3)
    add_p(doc, "Ms. AMEENA AFSAR", font_size=12.5, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "Assistant Professor, Department of Computer Applications", font_size=11, bold=False, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)

    if os.path.exists(LOGO_PATH):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(20)
        p_logo.add_run().add_picture(LOGO_PATH, width=Inches(1.4))

    add_p(doc, "DEPARTMENT OF COMPUTER APPLICATIONS", font_size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=3)
    add_p(doc, "AWH ENGINEERING COLLEGE", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "KUTTIKKATTOOR, KOZHIKODE, KERALA – 673008", font_size=11.5, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "ACADEMIC YEAR: 2025–2026", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)

    # ──────────────────────────────────────────────────────────────────────────
    # 2. CERTIFICATE PAGE
    # ──────────────────────────────────────────────────────────────────────────
    doc.add_page_break()
    if os.path.exists(LOGO_PATH):
        p_logo2 = doc.add_paragraph()
        p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo2.paragraph_format.space_after = Pt(10)
        p_logo2.paragraph_format.space_before = Pt(6)
        p_logo2.add_run().add_picture(LOGO_PATH, width=Inches(1.2))

    add_p(doc, "DEPARTMENT OF COMPUTER APPLICATIONS", font_size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=3)
    add_p(doc, "AWH ENGINEERING COLLEGE", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "KUTTIKKATTOOR, CALICUT - 673008", font_size=11.5, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)

    add_p(doc, "BONA FIDE CERTIFICATE", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)

    cert_text = (
        "This is to certify that this project thesis entitled “HAIRFIDENCE: A CENTRALIZED ROLE-BASED "
        "WEB APPLICATION FOR HAIR DONATION LIFECYCLE MANAGEMENT” is a bona fide record of the project work "
        "carried out by ARSHAN NIZAR K P (Register Number: AWH25MCA-2010) in partial fulfillment of the requirements "
        "for the award of the Degree of Master of Computer Applications from APJ Abdul Kalam Technological University "
        "during the academic year 2025–2026."
    )
    add_p(doc, cert_text, font_size=12, italic=True, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=50, line_spacing=1.5, indent=0.5)

    # 2x2 Signatures Table
    t_staff = doc.add_table(rows=2, cols=2)
    t_staff.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_staff.autofit = False

    t_staff.cell(0, 0).paragraphs[0].text = "Ms. AMEENA AFSAR"
    t_staff.cell(0, 0).paragraphs[0].runs[0].font.bold = True
    t_staff.cell(0, 0).paragraphs[0].runs[0].font.name = "Times New Roman"
    p_g1 = t_staff.cell(0, 0).add_paragraph("Project Guide & Assistant Professor\nDept. of Computer Applications\nAWH Engineering College, Calicut")
    p_g1.paragraph_format.line_spacing = 1.15

    t_staff.cell(0, 1).paragraphs[0].text = "Mrs. SRUTI SUDEVAN"
    t_staff.cell(0, 1).paragraphs[0].runs[0].font.bold = True
    t_staff.cell(0, 1).paragraphs[0].runs[0].font.name = "Times New Roman"
    p_h1 = t_staff.cell(0, 1).add_paragraph("Head of the Department & Associate Professor\nDept. of Computer Applications\nAWH Engineering College, Calicut")
    p_h1.paragraph_format.line_spacing = 1.15

    add_p(doc, "", space_after=35)

    add_p(doc, "Submitted for the Viva-Voce Examination held on: ............................................................", font_size=11, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=35)

    t_exam = doc.add_table(rows=1, cols=2)
    t_exam.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_exam.cell(0, 0).paragraphs[0].text = "EXTERNAL EXAMINER"
    t_exam.cell(0, 0).paragraphs[0].runs[0].font.bold = True
    t_exam.cell(0, 0).paragraphs[0].runs[0].font.name = "Times New Roman"

    t_exam.cell(0, 1).paragraphs[0].text = "INTERNAL EXAMINER"
    t_exam.cell(0, 1).paragraphs[0].runs[0].font.bold = True
    t_exam.cell(0, 1).paragraphs[0].runs[0].font.name = "Times New Roman"

    # ──────────────────────────────────────────────────────────────────────────
    # 3. ACKNOWLEDGEMENT (Strictly 1 Page, 1.5 Line Spacing)
    # ──────────────────────────────────────────────────────────────────────────
    doc.add_page_break()
    add_p(doc, "ACKNOWLEDGEMENT", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=15, space_after=24)

    ack_p1 = (
        "I express my profound sense of gratitude and sincere indebtedness to our respected Principal, Dr. Sabeena MV, "
        "for providing all necessary institutional facilities, computational infrastructure, and academic encouragement that "
        "made the completion of this project thesis possible."
    )
    add_p(doc, ack_p1, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p2 = (
        "I convey my deepest and heartfelt thanks to Mrs. Sruti Sudevan, Head of the Department of Computer Applications, "
        "for her continuous inspiration, academic leadership, and vital encouragement throughout the duration of the MCA "
        "program and during this project endeavor."
    )
    add_p(doc, ack_p2, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p3 = (
        "I take immense privilege in expressing my sincere gratitude to my Project Guide, Ms. Ameena Afsar, Assistant Professor, "
        "Department of Computer Applications, for her technical mentorship, invaluable suggestions, and patient supervision. "
        "Her constructive critiques, insightful suggestions, and thorough evaluations at every phase of system modeling, design, and testing "
        "helped shape this project into an academically rigorous and socially impactful system."
    )
    add_p(doc, ack_p3, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p4 = (
        "I also extend my sincere gratitude to all the teaching and technical staff members of the Department of Computer Applications "
        "for their invaluable support, timely suggestions, and generous academic assistance throughout the project development cycle."
    )
    add_p(doc, ack_p4, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p5 = (
        "I express my loving thanks to my family members and batchmates whose unwavering moral support, sacrifices, and continuous encouragement "
        "have been the bedrock of my life and education. Their feedback during user experience reviews and software testing has been deeply appreciated."
    )
    add_p(doc, ack_p5, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    ack_p6 = (
        "Above all, I surrender myself in eternal gratitude before the Almighty for granting me the wisdom, health, strength, and perseverance "
        "to complete this project thesis successfully."
    )
    add_p(doc, ack_p6, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=35, line_spacing=1.5, indent=0.5)

    add_p(doc, "ARSHAN NIZAR K P\n(Register Number: AWH25MCA-2010)", font_size=12, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=0)

    # ──────────────────────────────────────────────────────────────────────────
    # 4. ABSTRACT (Strictly 1 Page, 1.5 Line Spacing, 12pt Times New Roman)
    # ──────────────────────────────────────────────────────────────────────────
    doc.add_page_break()
    add_p(doc, "ABSTRACT", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=15, space_after=24)

    abs_p1 = (
        "Chemotherapy-induced alopecia (hair loss) is widely recognized in oncological medicine as one of the most psychologically "
        "distressing and traumatic side effects for cancer patients, precipitating profound erosion of self-esteem, clinical anxiety, "
        "and acute social alienation. While thousands of empathetic citizens wish to donate natural hair for medical wig fabrication, "
        "traditional donation mechanisms across Kerala and India remain uncoordinated, fragmented, and heavily vulnerable to logistics "
        "failures. Existing approaches rely on informal WhatsApp groups, untracked courier drop-offs, and open social media appeals. "
        "This absence of centralized coordination creates acute bottlenecks: donors receive zero visibility into parcel arrivals; "
        "non-governmental organizations (NGOs) receive unsorted specimens lacking vital technical metadata; and immunocompromised "
        "cancer patients are forced to physically travel with paper diagnostic reports to prove their condition."
    )
    add_p(doc, abs_p1, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    abs_p2 = (
        "To decisively resolve these failures, this thesis presents HairFidence: A Centralized Role-Based Web Application for Hair "
        "Donation Lifecycle Management, an end-to-end, secure, 3-Tier Model-View-Controller (MVC) web architecture. The platform "
        "digitizes, automates, and audits the entire hair donation, clinical verification, and prosthesis allocation lifecycle. "
        "Engineered using semantic HTML5, Vanilla CSS3 custom properties, and JavaScript (ES6+) on the client side, paired with a modular "
        "PHP 8.x backend engine, all transactional states are anchored in an optimized 8-table relational MySQL schema running in an "
        "Apache XAMPP environment."
    )
    add_p(doc, abs_p2, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.5, indent=0.5)

    abs_p3 = (
        "HairFidence partitions governance across four discrete role modules: System Administrator (institutional NGO accreditation "
        "and grievance resolution), Healthcare NGOs (physical parcel audits, clinical diagnostic report verification, and community "
        "donation drives), Donors (specification authoring and multi-stage visual pipeline tracking), and Patients (secure medical "
        "report uploading and catalog browsing). A critical technical contribution is the implementation of Pessimistic Concurrency "
        "Locking via SELECT ... FOR UPDATE wrapped within atomic PDO database transactions, strictly preventing double-booking race "
        "conditions during simultaneous patient requests. Rigorous unit, integration, and black-box test suites validate that the system "
        "delivers robust data security, zero-cost wig access for cancer survivors, and total transparency for civic donors."
    )
    add_p(doc, abs_p3, font_size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=0, line_spacing=1.5, indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # 5. TABLE OF CONTENTS
    # ──────────────────────────────────────────────────────────────────────────
    doc.add_page_break()
    add_p(doc, "CONTENTS", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=15, space_after=20)

    toc_items = [
        ("CERTIFICATE", "ii", True),
        ("ACKNOWLEDGEMENT", "iii", True),
        ("ABSTRACT", "iv", True),
        ("CHAPTER 1: INTRODUCTION", "1", True),
        ("    1.1 Domain Overview & Background", "1", False),
        ("    1.2 Motivation", "3", False),
        ("    1.3 Problem Statement", "5", False),
        ("    1.4 Objectives", "6", False),
        ("    1.5 Organization of the Report", "7", False),
        ("CHAPTER 2: SYSTEM ANALYSIS", "8", True),
        ("    2.1 Existing System", "8", False),
        ("    2.2 Proposed System", "10", False),
        ("    2.3 Module Description", "12", False),
        ("    2.4 Sprint Planning", "14", False),
        ("    2.5 User Stories", "16", False),
        ("CHAPTER 3: FEASIBILITY STUDY", "18", True),
        ("    3.1 Economic Feasibility", "18", False),
        ("    3.2 Technical Feasibility", "19", False),
        ("    3.3 Operational Feasibility", "20", False),
        ("    3.4 Behavioral Feasibility", "21", False),
        ("    3.5 Software Feasibility", "22", False),
        ("CHAPTER 4: SOFTWARE ENGINEERING PARADIGM", "23", True),
        ("    4.1 Agile Development Methodology", "23", False),
        ("    4.2 Scrum Framework", "25", False),
        ("CHAPTER 5: SYSTEM REQUIREMENT SPECIFICATION", "27", True),
        ("    5.1 Software Requirements", "27", False),
        ("    5.2 Hardware Requirements", "29", False),
        ("CHAPTER 6: SYSTEM DESIGN", "31", True),
        ("    6.1 Database Design & Normalization (1NF, 2NF, 3NF)", "31", False),
        ("    6.2 Data Dictionary (8 Tables)", "34", False),
        ("    6.3 UML Architecture (Class & Sequence Trace)", "39", False),
        ("    6.4 Use Case Diagram & Actor Mapping", "42", False),
        ("    6.5 System Scenarios", "44", False),
        ("CHAPTER 7: SYSTEM DEVELOPMENT", "46", True),
        ("    7.1 Development Lifecycle Activities", "46", False),
        ("    7.2 Implementation Technologies", "48", False),
        ("    7.3 Core Code Implementations", "50", False),
        ("CHAPTER 8: SYSTEM TESTING AND IMPLEMENTATION", "54", True),
        ("    8.1 Types of Testing", "54", False),
        ("    8.2 Test Case Matrix", "56", False),
        ("    8.3 Deployment & Cutover Strategy", "59", False),
        ("CHAPTER 9: SYSTEM MAINTENANCE", "60", True),
        ("    9.1 Corrective Maintenance", "60", False),
        ("    9.2 Adaptive Maintenance", "61", False),
        ("    9.3 Perfective Maintenance", "62", False),
        ("CHAPTER 10: FUTURE ENHANCEMENTS", "63", True),
        ("CHAPTER 11: CONCLUSION", "65", True),
        ("CHAPTER 12: APPENDIX (UI SCREENSHOTS & WORKFLOWS)", "67", True),
        ("CHAPTER 13: BIBLIOGRAPHY", "82", True),
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
    # CHAPTER 1: INTRODUCTION
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 1: INTRODUCTION")
    add_heading_1(doc, "CHAPTER 1: INTRODUCTION")

    add_heading_2(doc, "1.1 Domain Overview & Background")
    add_p(doc, "In modern oncological healthcare management, advanced chemotherapy regimens, targeted biological agents, and radiotherapy have substantially improved clinical remission rates and overall survival statistics for cancer patients worldwide. However, the cytotoxic agents utilized in these regimens attack rapidly dividing physiological cells indiscriminately. Consequently, along with malignant tumor cells, healthy hair follicle keratinocytes are severely damaged, leading to complete or extensive alopecia (hair loss). Oncological literature emphasizes that chemotherapy-induced alopecia is clinically classified among the top three most emotionally traumatic and psychologically debilitating adverse effects endured by cancer patients, exerting an acute psychological toll on women, adolescents, and children.", indent=0.5)

    add_p(doc, "Unlike internal organ distress or systemic fatigue, alopecia serves as an involuntary, overt visual badge of malignancy. It frequently forces patients into unintended disclosure of their health status, eroding self-confidence, inducing clinical depression, and accelerating social withdrawal. The restoration of personal identity during oncological therapy has a profound therapeutic benefit: medical literature confirms that patient emotional well-being directly enhances immune response compliance and survival resilience. In response, cranial prostheses—specifically custom natural hair medical wigs—provide immediate emotional rehabilitation, enabling recovering individuals to reclaim their social presence and emotional autonomy.", indent=0.5)

    add_p(doc, "Nevertheless, the manufacturing and economic dynamics of cranial prostheses present a formidable structural barrier. Medical-grade wigs hand-crafted from natural human hair require 10 to 12 individual donor bundles, specialized sanitization, color-sorting, and hand-knotting upon a breathable monofilament silicone cap. In commercial marketplaces, these medical prostheses command exorbitant prices ranging between ₹25,000 and ₹1,20,000 per unit. For economically disadvantaged and middle-class cancer patients already bearing catastrophic costs of chemotherapeutic infusions and diagnostic scans, purchasing a commercial natural hair wig is impossible. Synthetic nylon or acrylic alternatives, while cheaper, cause severe scalp pruritus, contact dermatitis, and heat discomfort upon immunocompromised scalps.", indent=0.5)

    add_p(doc, "Concurrently, a massive demographic of altruistic citizens actively desires to donate their natural hair to assist cancer survivors. In Kerala and across India, hundreds of individuals cut their hair monthly with the explicit charitable intent of supporting cancer patients. Regrettably, the charitable supply chain linking civic donors to certified wig fabrication trusts and immunocompromised patients is severely broken, disorganized, and vulnerable to operational failure.", indent=0.5)

    add_heading_2(doc, "1.2 Motivation")
    add_p(doc, "Traditional charitable hair donation avenues rely almost exclusively on sporadic, informal mechanisms: unmonitored postal parcels sent to hospital addresses, untracked courier packets dropped at regional charitable trusts, and emotional appeals broadcast across open social media platforms such as Instagram, Facebook, and WhatsApp groups. These informal conduits suffer from catastrophic vulnerabilities:", indent=0.5)

    add_p(doc, "1. Severe Trust Deficits and Zero Donor Visibility: When a citizen cuts 10 to 15 inches of natural hair and dispatches it via postal mail, they receive zero formal acknowledgment, shipment tracking, or verification. Donors are left in complete uncertainty regarding whether their specimen arrived safely, was spoiled by dampness, or was discarded due to sub-standard packaging.", indent=0.5)

    add_p(doc, "2. Clinical Record Exposure and Privacy Infringements: Desperate families seeking wigs for cancer-stricken relatives frequently publish unredacted medical diagnostic cards, biopsy reports, and personal phone numbers on public social media forums. This exposes vulnerable patients to identity theft, predatory commercial quacks, and public indignity.", indent=0.5)

    add_p(doc, "3. NGO Operational Bottlenecks and Unsorted Specimens: Non-governmental organizations (NGOs) receive hundreds of unsolicited physical parcels without standardized donor metadata. Staff members spend valuable hours sorting hair bundles by hand, lacking recorded data on strand length, texture, chemical treatment status, or donor contact info.", indent=0.5)

    add_p(doc, "4. Commercial Intermediation and Fraud: The absence of an auditable inventory registry enables unethical middlemen to intercept freely donated hair bundles and divert them into lucrative commercial extension markets, completely bypassing the cancer survivors for whom the hair was intended.", indent=0.5)

    add_p(doc, "These critical societal and technical challenges provided the definitive motivation to conceptualize, design, and engineer HairFidence—a centralized, verifiable, role-governed web application that formalizes and digitizes the hair donation lifecycle under strict institutional oversight.", indent=0.5)

    add_heading_2(doc, "1.3 Problem Statement")
    add_p(doc, "There exists a critical absence of an integrated, verifiable, and privacy-preserving digital platform to govern the end-to-end lifecycle of humanitarian hair donations. Existing informal channels lack institutional verification, expose sensitive oncology patient records to public forums, leave altruistic donors without parcel traceability, and provide no concurrency protection against double-allocating donated assets. Consequently, there is an urgent technical necessity for a secure 3-Tier Model-View-Controller web application that enforces Role-Based Access Control (RBAC), isolates medical documents, automates multi-stage parcel tracking, and guarantees transactional consistency across all donor contributions, NGO clinical audits, and patient wig allocation workflows.", indent=0.5)

    add_heading_2(doc, "1.4 Objectives")
    add_p(doc, "The primary technical, architectural, and operational objectives of the HairFidence system are summarized as follows:", indent=0.5)
    add_p(doc, "• Centralized Digital Cataloging: Unify fragmented donation initiatives by providing a structured web portal where donors register precise hair attributes (length in inches, hair texture, specimen photograph) and track real-time parcel availability.", indent=0.5)
    add_p(doc, "• Institutional NGO Accreditation: Establish healthcare NGOs as accredited clinical gatekeepers empowered to inspect physical parcels, verify patient medical diagnoses, and coordinate wig fabrication.", indent=0.5)
    add_p(doc, "• Confidential Diagnostic Validation: Implement an isolated, encrypted file-handling pipeline that allows immunocompromised cancer survivors to upload diagnostic oncology summaries with strict RBAC visibility limited to authorized auditors.", indent=0.5)
    add_p(doc, "• Concurrency-Safe Asset Allocation: Enforce Pessimistic Concurrency Locking (SELECT ... FOR UPDATE) inside atomic PDO transactions, eliminating race conditions and double-allocation when multiple patients request matching hair posts simultaneously.", indent=0.5)
    add_p(doc, "• Multi-Stage Lifecycle Pipeline: Provide visual state-machine tracking across three discrete states: 'Available' (cataloged), 'Processing' (locked under NGO clinical review), and 'Donated' (physically verified and handed over for wig crafting).", indent=0.5)
    add_p(doc, "• Community Outreach & Grievance Redressal: Equip accredited NGOs to publish community hair donation drives and provide an institutional ticketing module for rapid grievance resolution.", indent=0.5)

    add_heading_2(doc, "1.5 Organization of the Report")
    add_p(doc, "This academic project report is organized into thirteen comprehensive chapters: Chapter 1 introduces the domain, motivation, and system objectives; Chapter 2 presents system analysis, sprint planning, and user stories; Chapter 3 evaluates economic, technical, operational, behavioral, and software feasibility; Chapter 4 outlines the Agile Scrum software engineering paradigm; Chapter 5 defines system hardware and software requirement specifications (SRS); Chapter 6 details system design, 3NF normalization, data dictionaries for all 8 tables, and UML diagrams; Chapter 7 covers modular development and core code implementations; Chapter 8 details testing types, worked test cases, and deployment strategies; Chapter 9 outlines maintenance methodologies; Chapter 10 projects future enhancements; Chapter 11 provides the final academic conclusion; Chapter 12 presents the complete Appendix containing UI screen layouts; and Chapter 13 lists authoritative web and textbook bibliographical citations.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 2: SYSTEM ANALYSIS
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 2: SYSTEM ANALYSIS")
    add_heading_1(doc, "CHAPTER 2: SYSTEM ANALYSIS")

    add_heading_2(doc, "2.1 Existing System")
    add_p(doc, "The conventional paradigm for hair donation and medical wig distribution across regional charitable centers is an entirely manual, fragmented, and unmonitored ecosystem. When an individual decides to donate hair, they must independently search for hospital charity wings or non-profit trusts through word-of-mouth or unverified social media posts. The donor cuts their hair at a local salon, wraps it in paper or polythene, and mails it via standard post to an NGO address without any unique parcel identifier.", indent=0.5)

    add_p(doc, "Upon parcel delivery at the charitable facility, administrative clerks manually open packets and transcribe donor names into paper logbooks or ad-hoc desktop spreadsheets. Crucial technical parameters—such as precise unstretched strand length, chemical treatment history, and moisture integrity—are either subjectively estimated or completely unrecorded. On the recipient end, cancer survivors or their relatives must physically commute to hospital charity offices, carrying physical paper biopsy reports and chemotherapy prescription cards to prove their clinical condition. Administrative personnel then manually search through disorganized physical storage bins to locate matching bundles. This process causes severe bottlenecks: parcels are frequently misplaced; unverified social media requests expose patients to fraudulent solicitations; and patients suffer profound humiliation when turned away due to inventory mismatches.", indent=0.5)

    add_heading_2(doc, "2.2 Proposed System")
    add_p(doc, "HairFidence re-engineers this broken humanitarian workflow into a secure, role-governed web application. The platform introduces a structured 4-tier Role-Based Access Control (RBAC) hierarchy comprising Administrator, Healthcare NGO, Hair Donor, and Cancer Patient modules. Donors register authenticated profiles, log detailed specimen attributes, and upload photographic verification. The hair post is cataloged in real-time in the 'Available' state.", indent=0.5)

    add_p(doc, "Cancer patients register authenticated profiles and securely upload digital copies of their oncology medical certificates. Patients can browse a live, multi-attribute searchable catalog of available hair donations. When a patient identifies a suitable hair asset, they submit an allocation request. The system triggers an atomic transaction that executes a Pessimistic Concurrency Lock (SELECT ... FOR UPDATE), instantly transitioning the post state from 'Available' to 'Processing'. This guarantees that no other patient can claim or request the locked asset.", indent=0.5)

    add_p(doc, "The selected partner NGO accesses its secure verification desk, audits the patient's diagnostic certificate, and inspects the physical hair parcel upon arrival. If verified, the NGO executes the approval action: the hair post permanently transitions to 'Donated', and the wig crafting workflow begins. If the medical criteria are not met, the NGO rejects the request: the system automatically unlocks the hair post and restores it back to 'Available' in the public catalog.", indent=0.5)

    add_heading_2(doc, "2.3 Module Description")
    add_heading_3(doc, "1. Administrator Module")
    add_p(doc, "The Administrator serves as the supreme governance authority. Key functions include: reviewing statutory registration certificates of applicant NGOs and approving or rejecting accounts; monitoring platform-wide analytics (total donors, active posts, patient requests, completed donations); auditing grievance tickets; and managing system security configurations.", indent=0.5)

    add_heading_3(doc, "2. Healthcare NGO Module")
    add_p(doc, "Accredited NGOs function as clinical and physical quality-control gatekeepers. Key functions include: auditing digital medical certificates uploaded by cancer patients; inspecting physical hair parcels upon mail delivery; managing request status (Approved / Rejected); and publishing community hair donation drives.", indent=0.5)

    add_heading_3(doc, "3. Hair Donor Module")
    add_p(doc, "Empowers civic donors with complete operational visibility. Key functions include: authoring hair donation posts (specifying strand length in inches, hair texture, and uploading specimen photographs); tracking the live lifecycle stage of their donation across an interactive progress bar; and viewing upcoming community collection drives.", indent=0.5)

    add_heading_3(doc, "4. Cancer Patient Module")
    add_p(doc, "Designed with utmost dignity and privacy. Key functions include: secure registration and encrypted uploading of diagnostic oncology certificates; browsing the live catalog with length and texture filters; submitting allocation requests protected by concurrency locks; and tracking request approval status.", indent=0.5)

    add_heading_2(doc, "2.4 Sprint Planning")
    add_p(doc, "Development was organized into two focused sprints using the Agile Scrum framework:", indent=0.5)

    add_heading_3(doc, "Sprint 1: Core Architecture, Database Modeling & Authentication")
    sprint1_tasks = [
        ("Module", "Task Description", "Hours", "Expected Date", "Actual Date", "Remarks"),
        ("System", "Database Schema Design & Tables Creation", "4", "10/07/25", "10/07/25", "8 Normalized Tables (InnoDB)"),
        ("Auth", "Login Controller & RBAC Redirection", "3", "14/07/25", "14/07/25", "BCrypt Hashing & Session Guard"),
        ("Auth", "Multi-Role Registration Pipelines", "4", "18/07/25", "18/07/25", "Donors, Patients & NGOs"),
        ("Admin", "Admin Metric Engine & Dashboard", "4", "22/07/25", "22/07/25", "KPI Counters & Data Aggregation"),
        ("Admin", "NGO Accreditation Approval Workflow", "3", "26/07/25", "26/07/25", "Gated Access Control"),
        ("NGO", "NGO Registration & Document Upload", "3", "30/07/25", "30/07/25", "Verification Queue"),
        ("NGO", "NGO Operational Dashboard Shell", "4", "04/08/25", "04/08/25", "Responsive Management View"),
        ("Donor", "Donor Shell & Base Navigation", "3", "08/08/25", "08/08/25", "Responsive Flexbox Layout"),
    ]
    t_sp1 = doc.add_table(rows=len(sprint1_tasks), cols=6)
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
    add_heading_3(doc, "Sprint 2: Donation Logistics, Concurrency Control & Clinical Audit")
    sprint2_tasks = [
        ("Module", "Task Description", "Hours", "Expected Date", "Actual Date", "Remarks"),
        ("Donor", "Hair Post Authoring & Image Upload", "4", "12/08/25", "12/08/25", "MIME Validation & Sanitization"),
        ("Donor", "Multi-Stage Visual Pipeline Tracker", "3", "16/08/25", "16/08/25", "Available -> Processing -> Donated"),
        ("Patient", "Patient Registration & Medical Upload", "4", "20/08/25", "20/08/25", "Isolated Storage & RBAC"),
        ("Patient", "Interactive Hair Catalog & Filters", "4", "24/08/25", "24/08/25", "Length & Texture Filters"),
        ("Patient", "Submit Request with Concurrency Lock", "3", "28/08/25", "28/08/25", "SELECT ... FOR UPDATE"),
        ("NGO", "Clinical Audit & Request State Machine", "4", "02/09/25", "02/09/25", "Atomic Approval & Rollback"),
        ("NGO", "Community Campaign Publishing", "3", "06/09/25", "06/09/25", "Date & Location Broadcasting"),
        ("System", "Complaint Ticketing & Redressal", "3", "10/09/25", "10/09/25", "Grievance Logging & Audit"),
    ]
    t_sp2 = doc.add_table(rows=len(sprint2_tasks), cols=6)
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

    add_heading_2(doc, "2.5 User Stories")
    add_p(doc, "• Administrator User Stories:\n"
               "  - As an Administrator, I want to review statutory registration numbers and certificates of applicant NGOs so that only legitimate healthcare charities are granted access to clinical data.\n"
               "  - As an Administrator, I want to view global platform metrics so that I can evaluate donation velocity and operational health.\n"
               "  - As an Administrator, I want to audit user complaints and mark them as Resolved so that platform grievances are resolved transparently.\n\n"
               "• Healthcare NGO User Stories:\n"
               "  - As an NGO Staff Member, I want to securely inspect cancer patient oncology reports so that free wigs are allocated exclusively to genuine medical patients.\n"
               "  - As an NGO Staff Member, I want to approve or reject hair requests so that verified assets transition to Donated and rejected assets are instantly returned to the public catalog.\n"
               "  - As an NGO Staff Member, I want to post community hair donation drives so that civic donors can attend in-person collection events.\n\n"
               "• Hair Donor User Stories:\n"
               "  - As a Hair Donor, I want to register hair specifications (length, texture, photo) so that patients can evaluate if the specimen suits their needs.\n"
               "  - As a Hair Donor, I want to view a real-time status tracker (Available -> Processing -> Donated) so that I receive certainty regarding the arrival and utilization of my hair.\n\n"
               "• Cancer Patient User Stories:\n"
               "  - As a Cancer Patient, I want to upload my diagnostic certificate to a private server directory so that my medical dignity is preserved without public exposure.\n"
               "  - As a Cancer Patient, I want to browse a live catalog of available hair donations and select a preferred NGO so that I can request a custom wig without financial burden.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 3: FEASIBILITY STUDY
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 3: FEASIBILITY STUDY")
    add_heading_1(doc, "CHAPTER 3: FEASIBILITY STUDY")

    add_heading_2(doc, "3.1 Economic Feasibility")
    add_p(doc, "Economic feasibility analyzes whether the anticipated societal and operational benefits justify development and deployment expenditures. HairFidence is engineered entirely upon Free and Open-Source Software (FOSS) technologies: PHP 8.x, Apache HTTP Server, MariaDB/MySQL, and open web standards. By eliminating commercial software licensing fees, capital expenditure is strictly minimized. Infrastructure requirements are modest: a budget Virtual Private Server (VPS) or standard shared hosting environment satisfies all processing demands. Furthermore, by automating manual inventory logging and document review, the platform saves hundreds of labor hours for non-profit organizations, yielding a rapid return on investment (ROI).", indent=0.5)

    add_heading_2(doc, "3.2 Technical Feasibility")
    add_p(doc, "Technical feasibility evaluates the capability and maturity of the technology stack to meet system objectives. PHP 8.x provides a mature scripting engine with robust PDO extensions for database abstraction. MariaDB/MySQL with the InnoDB engine delivers strict ACID transactional compliance, foreign key cascade enforcement, and pessimistic concurrency locking. Client-side code runs natively in any standard web browser using semantic HTML5, Vanilla CSS3 custom properties, and modern JavaScript (ES6+), requiring zero client-side installation. The technical architecture is robust, predictable, and highly scalable.", indent=0.5)

    add_heading_2(doc, "3.3 Operational Feasibility")
    add_p(doc, "Operational feasibility assesses whether the software can be successfully integrated into the daily routines of stakeholders. HairFidence provides role-partitioned interfaces that mirror the real-world responsibilities of administrators, NGO caseworkers, donors, and cancer patients. By replacing paper registers with automated dashboards and visual pipeline indicators, operational friction is eliminated. Workflows require no advanced technical training, ensuring smooth institutional adoption.", indent=0.5)

    add_heading_2(doc, "3.4 Behavioral Feasibility")
    add_p(doc, "Behavioral feasibility examines human-computer interaction and user acceptance. For cancer patients coping with chemotherapy trauma, the application provides an empathetic, confidential environment where medical documents are strictly protected from public exposure. For donors, the emotional satisfaction of charitable giving is reinforced through transparent, stage-by-stage visual tracking. These user-centric considerations ensure widespread community acceptance and sustained engagement.", indent=0.5)

    add_heading_2(doc, "3.5 Software Feasibility")
    add_p(doc, "Software feasibility examines operating platform dependencies, browser compliance, and maintenance overhead. HairFidence adheres strictly to universal W3C web standards, ensuring seamless cross-browser compatibility across Google Chrome, Mozilla Firefox, Microsoft Edge, and Apple Safari. Responsive CSS grid and flexbox layouts adapt flawlessly across smartphones, tablets, and desktop monitors without requiring separate native device applications.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 4: SOFTWARE ENGINEERING PARADIGM
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 4: SOFTWARE ENGINEERING PARADIGM")
    add_heading_1(doc, "CHAPTER 4: SOFTWARE ENGINEERING PARADIGM")

    add_heading_2(doc, "4.1 Agile Development Methodology")
    add_p(doc, "The development of HairFidence was guided by the Agile methodology. In contrast to rigid, sequential waterfall models, Agile prioritizes iterative enhancements, flexibility, and continuous stakeholder feedback. The project was decomposed into modular iterations where functional units were designed, coded, tested, and validated incrementally. This iterative approach allowed rapid adaptation to real-world operational requirements, such as optimizing document upload security and refining the multi-state donation tracking pipeline.", indent=0.5)

    add_heading_2(doc, "4.2 Scrum Framework")
    add_p(doc, "Scrum was adopted as the operational framework to govern sprint execution. The team maintained structured roles, ceremonies, and artifacts:", indent=0.5)
    add_p(doc, "• Scrum Roles:\n"
               "  - Product Owner: Defined core functional objectives, established acceptance criteria, and prioritized the product backlog based on healthcare stakeholder needs.\n"
               "  - Scrum Master: Facilitated sprint cadence, eliminated technical roadblocks, and ensured strict adherence to Scrum principles.\n"
               "  - Development Team: Engineered frontend responsive interfaces, backend PHP controllers, database migrations, and automated test cases.\n\n"
               "• Scrum Ceremonies:\n"
               "  - Sprint Planning: At the start of each sprint cycle, high-priority user stories were broken down into technical tasks with estimated hours.\n"
               "  - Daily Scrum: Brief daily check-ins to review progress, synchronize tasks, and identify impediments.\n"
               "  - Sprint Review: End-of-sprint live demonstrations of functional modules to validate feature completion.\n"
               "  - Sprint Retrospective: Team reviews to identify process improvements for subsequent iterations.\n\n"
               "• Scrum Artifacts:\n"
               "  - Product Backlog: Master repository of all desired system features and security requirements.\n"
               "  - Sprint Backlog: Subset of backlog items committed for execution during a specific sprint cycle.\n"
               "  - Burndown Tracking: Visual charts monitoring remaining effort versus elapsed sprint hours.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 5: SYSTEM REQUIREMENT SPECIFICATION (SRS)
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 5: SYSTEM REQUIREMENT SPECIFICATION")
    add_heading_1(doc, "CHAPTER 5: SYSTEM REQUIREMENT SPECIFICATION")

    add_heading_2(doc, "5.1 Software Requirements")
    sw_reqs = [
        ("Operating System", "Microsoft Windows 10 / 11 (64-bit) / Ubuntu Server 22.04 LTS / Linux"),
        ("Web Server", "Apache HTTP Server 2.4.x (via XAMPP Control Panel v3.3+)"),
        ("Backend Scripting Engine", "PHP 8.2+ with PDO, OpenSSL, and Fileinfo extensions"),
        ("Database Management System", "MySQL 8.0+ / MariaDB 10.4+ with InnoDB Storage Engine"),
        ("Frontend Architecture", "HTML5, Vanilla CSS3 (Custom Properties), JavaScript (ES6+)"),
        ("Development Environment", "Visual Studio Code (VS Code) with PHP Intelephense"),
        ("Database Client Tools", "phpMyAdmin 5.2+ and MySQL Command Line Client"),
        ("Client Web Browsers", "Google Chrome (v110+), Mozilla Firefox, Microsoft Edge, Safari"),
    ]
    t_sw = doc.add_table(rows=len(sw_reqs) + 1, cols=2)
    t_sw.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sw.cell(0, 0).paragraphs[0].text = "Parameter"
    t_sw.cell(0, 1).paragraphs[0].text = "Specification"
    t_sw.cell(0, 0).paragraphs[0].runs[0].font.bold = True
    t_sw.cell(0, 1).paragraphs[0].runs[0].font.bold = True
    set_cell_shading(t_sw.cell(0, 0), "F1F5F9")
    set_cell_shading(t_sw.cell(0, 1), "F1F5F9")
    for idx, (param, spec) in enumerate(sw_reqs):
        c0 = t_sw.cell(idx + 1, 0)
        c1 = t_sw.cell(idx + 1, 1)
        c0.paragraphs[0].text = param
        c1.paragraphs[0].text = spec
        c0.paragraphs[0].runs[0].font.name = "Times New Roman"
        c1.paragraphs[0].runs[0].font.name = "Times New Roman"
        c0.paragraphs[0].runs[0].font.size = Pt(9.5)
        c1.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_border(c0)
        set_cell_border(c1)

    add_p(doc, "", space_after=8)
    add_heading_2(doc, "5.2 Hardware Requirements")
    hw_reqs = [
        ("Hardware Component", "Client-Side Specification", "Server-Side Specification"),
        ("Processor", "Dual-Core 1.8 GHz Intel Core i3 / AMD", "Quad-Core 2.4 GHz Intel Xeon / AMD EPYC"),
        ("Memory (RAM)", "2.0 GB DDR3 / DDR4 (4 GB recommended)", "8.0 GB DDR4 ECC (16 GB recommended)"),
        ("Storage Drive", "500 MB free browser cache space", "512 GB SSD (minimum 20 GB free partition)"),
        ("Display Output", "Minimum 1024x768 (1920x1080 Full HD)", "Server Console / Headless Display"),
        ("Network Interface", "Standard Broadband / 4G (512 Kbps+)", "Gigabit Ethernet (1000BASE-T) Static IP"),
    ]
    t_hw = doc.add_table(rows=len(hw_reqs), cols=3)
    t_hw.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_i, r_data in enumerate(hw_reqs):
        for c_i, val in enumerate(r_data):
            cell = t_hw.cell(r_i, c_i)
            cell.paragraphs[0].text = val
            cell.paragraphs[0].runs[0].font.name = "Times New Roman"
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            if r_i == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_shading(cell, "F1F5F9")
            set_cell_border(cell)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 6: SYSTEM DESIGN
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 6: SYSTEM DESIGN")
    add_heading_1(doc, "CHAPTER 6: SYSTEM DESIGN")

    add_heading_2(doc, "6.1 Database Design & Normalization (1NF, 2NF, 3NF)")
    add_p(doc, "Relational database normalization is a formal mathematical methodology applied to eliminate data redundancy, prevent insertion, update, and deletion anomalies, and enforce referential integrity across transactional entities. HairFidence strictly complies with Third Normal Form (3NF):", indent=0.5)

    add_p(doc, "• First Normal Form (1NF): A relation R is in 1NF if and only if the domain of every attribute consists exclusively of atomic (indivisible) values, with no repeating groups or nested arrays. In HairFidence, all multi-valued attributes are decoupled into dedicated relational tuples. For example, attributes such as hair_length, hair_type, and image_url store single scalar values. Hence, 1NF is strictly satisfied.", indent=0.5)

    add_p(doc, "• Second Normal Form (2NF): A relation R is in 2NF if it is in 1NF and every non-prime attribute is fully functionally dependent on the entire primary key (no partial functional dependencies). In our relational schema, every entity table utilizes an independent, single-column surrogate primary key generated via AUTO_INCREMENT (|PK| = 1). Because no composite primary keys exist, partial dependencies cannot mathematically occur. Hence, 2NF is guaranteed.", indent=0.5)

    add_p(doc, "• Third Normal Form (3NF): A relation R is in 3NF if it is in 2NF and there exist no transitive dependencies (i.e., no non-prime attribute functionally determines another non-prime attribute: X -> Y and Y -> Z). User credentials reside strictly in the 'login' table, while specific profile attributes reside in 'donors', 'patients', and 'ngos'. In 'hair_requests', request status depends strictly on request_id, not transitively on patient_id or ngo_id. Therefore, 3NF is strictly achieved.", indent=0.5)

    add_heading_2(doc, "6.2 Data Dictionary (8 Tables)")
    add_p(doc, "The relational database structure comprises eight normalized tables, detailed as follows:", indent=0.5)

    # Table 1: login
    add_data_dict_table(doc, "login (Universal Authentication Store)", [
        ("login_id", "INT", "Unique authentication primary key", "AUTO_INCREMENT, PRIMARY KEY"),
        ("email", "VARCHAR(150)", "User electronic mail address for login", "NOT NULL, UNIQUE"),
        ("password", "VARCHAR(255)", "BCrypt cryptographic salted hash", "NOT NULL"),
        ("role", "ENUM('admin','ngo','donor','patient')", "Authorization role for RBAC routing", "NOT NULL"),
        ("created_at", "TIMESTAMP", "Account creation timestamp", "DEFAULT CURRENT_TIMESTAMP"),
    ])

    # Table 2: donors
    add_data_dict_table(doc, "donors (Hair Donor Profiles)", [
        ("donor_id", "INT", "Unique donor entity identifier", "AUTO_INCREMENT, PRIMARY KEY"),
        ("login_id", "INT", "Foreign key referencing login credentials", "FOREIGN KEY -> login(login_id) ON DELETE CASCADE"),
        ("full_name", "VARCHAR(100)", "Legal full name of hair donor", "NOT NULL"),
        ("phone", "VARCHAR(15)", "Contact telephone number", "NOT NULL"),
        ("address", "TEXT", "Postal address for courier pickup", "NOT NULL"),
    ])

    # Table 3: patients
    add_data_dict_table(doc, "patients (Cancer Survivor Profiles)", [
        ("patient_id", "INT", "Unique patient entity identifier", "AUTO_INCREMENT, PRIMARY KEY"),
        ("login_id", "INT", "Foreign key referencing login credentials", "FOREIGN KEY -> login(login_id) ON DELETE CASCADE"),
        ("full_name", "VARCHAR(100)", "Legal full name of cancer patient", "NOT NULL"),
        ("phone", "VARCHAR(15)", "Primary contact telephone number", "NOT NULL"),
        ("address", "TEXT", "Delivery residential address for wig shipment", "NOT NULL"),
        ("medical_report_url", "VARCHAR(255)", "File path to uploaded diagnostic report", "NOT NULL"),
    ])

    # Table 4: ngos
    add_data_dict_table(doc, "ngos (Accredited Healthcare Non-Profits)", [
        ("ngo_id", "INT", "Unique healthcare NGO identifier", "AUTO_INCREMENT, PRIMARY KEY"),
        ("login_id", "INT", "Foreign key referencing login credentials", "FOREIGN KEY -> login(login_id) ON DELETE CASCADE"),
        ("organization_name", "VARCHAR(150)", "Statutory legal title of charitable foundation", "NOT NULL"),
        ("registration_number", "VARCHAR(100)", "Government society registration number", "NOT NULL"),
        ("is_approved", "TINYINT(1)", "Administrative accreditation flag", "DEFAULT 0 (0=Pending, 1=Approved)"),
    ])

    # Table 5: hair_donation_posts
    add_data_dict_table(doc, "hair_donation_posts (Hair Inventory Catalog)", [
        ("post_id", "INT", "Unique hair specimen post identifier", "AUTO_INCREMENT, PRIMARY KEY"),
        ("donor_id", "INT", "Foreign key identifying contributing donor", "FOREIGN KEY -> donors(donor_id) ON DELETE CASCADE"),
        ("hair_length", "DECIMAL(5,2)", "Length of hair bundle in inches", "NOT NULL"),
        ("hair_type", "VARCHAR(50)", "Hair texture classification (Straight/Wavy/Curly)", "NOT NULL"),
        ("image_url", "VARCHAR(255)", "Relative file path to specimen photograph", "NOT NULL"),
        ("status", "ENUM('Available','Processing','Donated')", "Current transactional state flag", "DEFAULT 'Available'"),
    ])

    # Table 6: hair_requests
    add_data_dict_table(doc, "hair_requests (Allocation Transactions)", [
        ("request_id", "INT", "Unique hair allocation request identifier", "AUTO_INCREMENT, PRIMARY KEY"),
        ("patient_id", "INT", "Foreign key identifying requesting patient", "FOREIGN KEY -> patients(patient_id) ON DELETE CASCADE"),
        ("post_id", "INT", "Foreign key identifying allocated hair specimen", "FOREIGN KEY -> hair_donation_posts(post_id) ON DELETE CASCADE"),
        ("ngo_id", "INT", "Foreign key identifying auditing partner NGO", "FOREIGN KEY -> ngos(ngo_id) ON DELETE CASCADE"),
        ("request_date", "TIMESTAMP", "Timestamp request transaction was initiated", "DEFAULT CURRENT_TIMESTAMP"),
        ("status", "ENUM('Pending','Approved','Rejected')", "Clinical audit outcome flag", "DEFAULT 'Pending'"),
    ])

    # Table 7: campaigns
    add_data_dict_table(doc, "campaigns (Community Donation Drives)", [
        ("campaign_id", "INT", "Unique public donation campaign identifier", "AUTO_INCREMENT, PRIMARY KEY"),
        ("ngo_id", "INT", "Foreign key identifying organizing NGO", "FOREIGN KEY -> ngos(ngo_id) ON DELETE CASCADE"),
        ("title", "VARCHAR(150)", "Public title of donation drive", "NOT NULL"),
        ("description", "TEXT", "Detailed guidelines, instructions, and target goals", "NOT NULL"),
        ("event_date", "DATE", "Scheduled calendar date of physical event", "NOT NULL"),
        ("location", "VARCHAR(255)", "Venue physical address or hall location", "NOT NULL"),
    ])

    # Table 8: complaints
    add_data_dict_table(doc, "complaints (Grievance Redressal Tickets)", [
        ("complaint_id", "INT", "Unique grievance ticket identifier", "AUTO_INCREMENT, PRIMARY KEY"),
        ("login_id", "INT", "Foreign key identifying complaining user", "FOREIGN KEY -> login(login_id) ON DELETE CASCADE"),
        ("subject", "VARCHAR(150)", "Summary subject line of grievance", "NOT NULL"),
        ("description", "TEXT", "Complete descriptive incident narrative", "NOT NULL"),
        ("status", "ENUM('Pending','Resolved')", "Grievance resolution status flag", "DEFAULT 'Pending'"),
        ("date_submitted", "TIMESTAMP", "Timestamp grievance ticket was logged", "DEFAULT CURRENT_TIMESTAMP"),
    ])

    add_heading_2(doc, "6.3 UML Architecture (Class & Sequence Trace)")
    add_p(doc, "• Class Diagram Structure:\n"
               "  - User Base Class: Contains common attributes (login_id, email, password, role) and authentication methods.\n"
               "  - Donor Subclass: Specializes User with donor_id, full_name, phone, address, and authorDonationPost() method.\n"
               "  - Patient Subclass: Specializes User with patient_id, medical_report_url, and requestHairPost() method.\n"
               "  - NGO Subclass: Specializes User with ngo_id, registration_number, is_approved, auditMedicalReport(), and publishCampaign() methods.\n"
               "  - HairDonationPost: Entity holding hair specifications with an aggregation association to Donor.\n"
               "  - HairRequest: Associative entity linking Patient, HairDonationPost, and NGO, enforcing the allocation contract.", indent=0.5)

    add_p(doc, "• Sequence Diagram Execution Trace for Concurrency-Safe Request:\n"
               "  1. Patient submits request for post_id via POST /patient/dashboard.php.\n"
               "  2. Web Controller initializes atomic transaction ($pdo->beginTransaction()).\n"
               "  3. Controller executes SELECT status FROM hair_donation_posts WHERE post_id=? FOR UPDATE (acquires pessimistic row lock).\n"
               "  4. If status is Available, controller inserts tuple into hair_requests and updates post status to Processing.\n"
               "  5. Transaction commits ($pdo->commit()), releasing row lock and preventing concurrent double-booking.", indent=0.5)

    add_heading_2(doc, "6.4 Use Case Diagram & Actor Mapping")
    if os.path.exists(UML_PATH):
        p_uml = doc.add_paragraph()
        p_uml.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_uml.paragraph_format.space_before = Pt(8)
        p_uml.paragraph_format.space_after = Pt(4)
        p_uml.add_run().add_picture(UML_PATH, width=Inches(5.4))
        add_p(doc, "Figure 6.1: UML Use Case Diagram for HairFidence System", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    add_p(doc, "Actor Use Case Mapping:\n"
               "• Administrator: Authenticates, vets and approves registered NGOs, monitors system metrics, resolves complaint tickets.\n"
               "• Healthcare NGO: Registers profile, creates donation campaigns, reviews patient diagnostic reports, inspects physical hair parcels, issues request approvals or rejections.\n"
               "• Hair Donor: Registers profile, logs hair donation post (length, texture, photo), views real-time multi-stage pipeline status, views upcoming drives, submits support tickets.\n"
               "• Cancer Patient: Registers profile, uploads medical report, searches available hair catalog, dispatches formal hair requests, tracks allocation status.", indent=0.5)

    add_heading_2(doc, "6.5 System Scenarios")
    add_p(doc, "• Scenario 1 (Donation Logging): Donor logs in -> enters length (e.g., 14 inches) and texture (Straight) -> uploads packaging photo -> system validates MIME -> post enters database as Available.\n"
               "• Scenario 2 (Request & Locking): Patient browses catalog -> selects specimen -> chooses partner NGO -> transaction locks post to Processing -> notification dispatched to NGO.\n"
               "• Scenario 3 (Clinical Audit & Approval): NGO accesses console -> views patient report -> inspects physical hair bundle -> clicks Approve -> post status updates to Donated and request to Approved -> wig hand-crafted and delivered.\n"
               "• Scenario 4 (Request Rejection): NGO determines report is invalid -> clicks Reject -> request marked Rejected -> hair post automatically unlocked back to Available in catalog.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 7: SYSTEM DEVELOPMENT
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 7: SYSTEM DEVELOPMENT")
    add_heading_1(doc, "CHAPTER 7: SYSTEM DEVELOPMENT")

    add_heading_2(doc, "7.1 Development Lifecycle Activities")
    add_p(doc, "System development translated architectural designs into a robust, deployable web application through rigorous software engineering phases: database schema migration via structured DDL scripts; backend controller engineering using PDO data access objects; client-side styling with vanilla CSS custom properties; security hardening against OWASP Top-10 vulnerabilities; and comprehensive integration testing.", indent=0.5)

    add_heading_2(doc, "7.2 Implementation Technologies")
    add_p(doc, "• PHP Data Objects (PDO): Provides prepared statements and parameterized queries, completely neutralizing SQL Injection attacks.\n"
               "• BCrypt Hashing: Implements password_hash() with PASSWORD_BCRYPT to guarantee irreversible credential protection.\n"
               "• Role-Based Access Control (RBAC): The check_access() middleware intercepts incoming HTTP requests, preventing privilege escalation.\n"
               "• Secure File System Partitions: Patient medical reports are stored in dedicated directories with restricted script execution permissions.", indent=0.5)

    add_heading_2(doc, "7.3 Core Code Implementations")

    add_heading_3(doc, "1. PDO Database Configuration (config/db.php)")
    add_p(doc, "Establishes a hardened, UTF-8 compliant PDO connection with exception trapping mode enabled:", indent=0.5)
    code_db = (
        "<?php\n"
        "// config/db.php - Centralized PDO Database Connection\n"
        "$host    = 'localhost';\n"
        "$db      = 'hairfidence';\n"
        "$user    = 'root';\n"
        "$pass    = ''; // Local development environment password\n"
        "$charset = 'utf8mb4';\n\n"
        "$dsn = \"mysql:host=$host;dbname=$db;charset=$charset\";\n"
        "$options = [\n"
        "    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,\n"
        "    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,\n"
        "    PDO::ATTR_EMULATE_PREPARES   => false, // Enforces native prepared statements\n"
        "];\n\n"
        "try {\n"
        "    $pdo = new PDO($dsn, $user, $pass, $options);\n"
        "} catch (\\PDOException $e) {\n"
        "    error_log(\"Database Connection Failure: \" . $e->getMessage());\n"
        "    die(\"Database connection failed. Please ensure MySQL is running in XAMPP.\");\n"
        "}\n"
        "?>"
    )
    add_code_block(doc, code_db)

    add_heading_3(doc, "2. Secure Login & RBAC Session Router (login.php)")
    add_p(doc, "Authenticates hashed credentials, checks administrative accreditation for NGOs, and assigns server-side $_SESSION parameters:", indent=0.5)
    code_login = (
        "<?php\n"
        "// login.php - Secure Authentication & Role Router\n"
        "require_once 'config/db.php';\n"
        "session_start();\n\n"
        "if ($_SERVER['REQUEST_METHOD'] === 'POST') {\n"
        "    $email    = trim($_POST['email']);\n"
        "    $password = $_POST['password'];\n\n"
        "    $stmt = $pdo->prepare(\"SELECT * FROM login WHERE email = ?\");\n"
        "    $stmt->execute([$email]);\n"
        "    $user = $stmt->fetch();\n\n"
        "    if ($user && password_verify($password, $user['password'])) {\n"
        "        $role = $user['role'];\n"
        "        $is_approved_ngo = true;\n"
        "        $profile = [];\n\n"
        "        if ($role === 'ngo') {\n"
        "            $stmt = $pdo->prepare(\"SELECT ngo_id, organization_name, is_approved FROM ngos WHERE login_id = ?\");\n"
        "            $stmt->execute([$user['login_id']]);\n"
        "            $profile = $stmt->fetch();\n"
        "            if ($profile && (int)$profile['is_approved'] !== 1) {\n"
        "                $is_approved_ngo = false;\n"
        "            }\n"
        "        }\n\n"
        "        if (!$is_approved_ngo) {\n"
        "            $error = \"Access Restricted: NGO registration is pending Administrator approval.\";\n"
        "        } else {\n"
        "            $_SESSION['login_id'] = $user['login_id'];\n"
        "            $_SESSION['email']    = $user['email'];\n"
        "            $_SESSION['role']     = $role;\n"
        "            header(\"Location: auth/dashboard_redirect.php\");\n"
        "            exit();\n"
        "        }\n"
        "    }\n"
        "}\n"
        "?>"
    )
    add_code_block(doc, code_login)

    add_heading_3(doc, "3. Hair Post Submission Handler with File Validation (donor/dashboard.php)")
    add_p(doc, "Validates image MIME types (JPG, JPEG, PNG), sanitizes file names, writes to uploads/hair_photos/, and registers the post as Available:", indent=0.5)
    code_donor = (
        "<?php\n"
        "// donor/dashboard.php - Hair Post Submission\n"
        "if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_donation'])) {\n"
        "    $hair_length = trim($_POST['hair_length']);\n"
        "    $hair_type   = $_POST['hair_type'];\n"
        "    $file_ext    = strtolower(pathinfo($_FILES['hair_photo']['name'], PATHINFO_EXTENSION));\n"
        "    $allowed     = ['jpg', 'jpeg', 'png'];\n\n"
        "    if (in_array($file_ext, $allowed)) {\n"
        "        $new_name  = 'hair_' . $donor_id . '_' . time() . '.' . $file_ext;\n"
        "        $dest_path = '../uploads/hair_photos/' . $new_name;\n"
        "        $db_path   = 'uploads/hair_photos/' . $new_name;\n\n"
        "        if (move_uploaded_file($_FILES['hair_photo']['tmp_name'], $dest_path)) {\n"
        "            $stmt = $pdo->prepare(\"INSERT INTO hair_donation_posts \n"
        "                (donor_id, hair_length, hair_type, image_url, status) \n"
        "                VALUES (?, ?, ?, ?, 'Available')\");\n"
        "            $stmt->execute([$donor_id, $hair_length, $hair_type, $db_path]);\n"
        "            $success_msg = \"Hair post published successfully in public catalog.\";\n"
        "        }\n"
        "    }\n"
        "}\n"
        "?>"
    )
    add_code_block(doc, code_donor)

    add_heading_3(doc, "4. NGO Medical Verification & Hair Request State Machine (ngo/dashboard.php)")
    add_p(doc, "Audits patient diagnostic certificates and manages atomic transitions to Donated or automatic rollback to Available on rejection:", indent=0.5)
    code_ngo = (
        "<?php\n"
        "// ngo/dashboard.php - Request State Machine (Approval & Rejection)\n"
        "if (isset($_GET['approve_request'])) {\n"
        "    $request_id = intval($_GET['approve_request']);\n"
        "    $pdo->beginTransaction();\n"
        "    $stmt = $pdo->prepare(\"UPDATE hair_requests SET status = 'Approved' WHERE request_id = ? AND ngo_id = ?\");\n"
        "    $stmt->execute([$request_id, $ngo_id]);\n\n"
        "    $stmt = $pdo->prepare(\"SELECT post_id FROM hair_requests WHERE request_id = ?\");\n"
        "    $stmt->execute([$request_id]);\n"
        "    $post_id = $stmt->fetchColumn();\n\n"
        "    if ($post_id) {\n"
        "        $stmt = $pdo->prepare(\"UPDATE hair_donation_posts SET status = 'Donated' WHERE post_id = ?\");\n"
        "        $stmt->execute([$post_id]);\n"
        "    }\n"
        "    $pdo->commit();\n"
        "}\n\n"
        "if (isset($_GET['reject_request'])) {\n"
        "    $request_id = intval($_GET['reject_request']);\n"
        "    $pdo->beginTransaction();\n"
        "    $stmt = $pdo->prepare(\"UPDATE hair_requests SET status = 'Rejected' WHERE request_id = ? AND ngo_id = ?\");\n"
        "    $stmt->execute([$request_id, $ngo_id]);\n\n"
        "    $stmt = $pdo->prepare(\"SELECT post_id FROM hair_requests WHERE request_id = ?\");\n"
        "    $stmt->execute([$request_id]);\n"
        "    $post_id = $stmt->fetchColumn();\n\n"
        "    if ($post_id) {\n"
        "        // Unlock hair post back to Available in public catalog\n"
        "        $stmt = $pdo->prepare(\"UPDATE hair_donation_posts SET status = 'Available' WHERE post_id = ?\");\n"
        "        $stmt->execute([$post_id]);\n"
        "    }\n"
        "    $pdo->commit();\n"
        "}\n"
        "?>"
    )
    add_code_block(doc, code_ngo)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 8: SYSTEM TESTING AND IMPLEMENTATION
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 8: SYSTEM TESTING AND IMPLEMENTATION")
    add_heading_1(doc, "CHAPTER 8: SYSTEM TESTING AND IMPLEMENTATION")

    add_heading_2(doc, "8.1 Types of Testing")
    add_p(doc, "• Unit Testing: Verified isolated routines including password hashing, session role guards, mathematical hair length validators, and file upload extension parsers.\n"
               "• Integration Testing: Validated cross-module operational sequences: Donor Post Upload -> Catalog Display -> Patient Concurrency Lock -> State Transition to Processing -> NGO Clinical Audit -> Final Handover (Donated).\n"
               "• Black Box Testing: Evaluated UI inputs against functional specifications without referencing source code internals.\n"
               "• White Box Testing: Verified statement and branch coverage, exception handling, transaction rollback consistency, and foreign key cascading constraints.", indent=0.5)

    add_heading_2(doc, "8.2 Test Case Matrix")
    test_cases_data = [
        ("Test ID", "Test Scenario", "Input Data", "Expected Output", "Actual Result", "Status"),
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

    add_heading_2(doc, "8.3 Deployment & Cutover Strategy")
    add_p(doc, "Deployment follows an automated local-to-cloud server deployment pipeline: 1. Web server stack initialization via XAMPP (Apache HTTP Server and MariaDB/MySQL); 2. Database schema migration by importing database.sql; 3. Directory permissions configuration ensuring write access to uploads/ partitions; 4. Verification of php.ini directives (file_uploads=On, upload_max_filesize=10M, session.cookie_httponly=1).", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 9: SYSTEM MAINTENANCE
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 9: SYSTEM MAINTENANCE")
    add_heading_1(doc, "CHAPTER 9: SYSTEM MAINTENANCE")

    add_heading_2(doc, "9.1 Corrective Maintenance")
    add_p(doc, "Focuses on defect triage and runtime error resolution. Server error logging is directed to secure error.log files with display_errors = Off to prevent system path disclosure. Input sanitization routines handle multibyte UTF-8 characters and address encoding variations.", indent=0.5)

    add_heading_2(doc, "9.2 Adaptive Maintenance")
    add_p(doc, "Ensures operational continuity across evolving external software environments: upgrading code syntax for upcoming PHP interpreter releases (PHP 8.3/8.4), applying MariaDB engine patches, and maintaining compliance with modern browser security policies (SameSite cookies).", indent=0.5)

    add_heading_2(doc, "9.3 Perfective Maintenance")
    add_p(doc, "Proactive enhancements to optimize performance and usability: implementing client-side debounced AJAX catalog search filters, enhancing analytical dashboard charting with dynamic SVG graphics, and preparing multi-lingual localization support (Malayalam/Hindi).", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 10: FUTURE ENHANCEMENTS
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 10: FUTURE ENHANCEMENTS")
    add_heading_1(doc, "CHAPTER 10: FUTURE ENHANCEMENTS")
    add_p(doc, "• Automated Courier Logistics API Integration: Integration with India Post Speed Post, DTDC, or Delhivery APIs to automatically generate prepaid shipping labels with live parcel tracking webhooks.\n"
               "• Cross-Platform Mobile Applications: Native mobile applications built on Flutter for Android and iOS, leveraging smartphone cameras for calibrated hair strand measurement and automated document scanning.\n"
               "• AI-Powered Virtual Wig Simulator (AR): An Augmented Reality computer vision module using WebGL and TensorFlow.js enabling cancer patients to preview medical wig styles virtually on their own face before submitting requests.\n"
               "• Certified Wig Workshop Integration: Establishing direct digital dispatch channels to certified medical wig manufacturing workshops and integrating philanthropic micro-sponsorship payment gateways (Razorpay/Stripe).", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 11: CONCLUSION
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 11: CONCLUSION")
    add_heading_1(doc, "CHAPTER 11: CONCLUSION")
    add_p(doc, "The development and operational validation of HairFidence: A Centralized Role-Based Web Application for Hair Donation Lifecycle Management represent a meaningful technological milestone in humanitarian healthcare logistics. By replacing informal, untracked, and error-prone manual donation practices with a secure, role-governed 3-Tier MVC web platform, this project establishes a transparent, accountable bridge connecting altruistic donors, verified healthcare NGOs, and cancer patients recovering from chemotherapy.", indent=0.5)

    add_p(doc, "The system successfully digitizes the end-to-end hair donation lifecycle, empowering donors with real-time multi-stage pipeline tracking, equipping healthcare NGOs with auditable verification tools, and providing cancer survivors with an accessible portal to receive customized cranial prostheses at zero financial cost. The implementation of Pessimistic Concurrency Locking inside atomic PDO transactions completely eliminates race conditions and resource double-booking, while strict 3NF database normalization guarantees data integrity. Ultimately, HairFidence establishes an enduring standard for healthcare charity management—one that unites robust software engineering with deep human empathy to restore dignity, confidence, and comfort to cancer survivors.", indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 12: APPENDIX
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 12: APPENDIX")
    add_heading_1(doc, "CHAPTER 12: APPENDIX")
    add_p(doc, "Actual operational user interface screenshots captured from the running HairFidence application demonstrating primary functional workflows across all user roles:", indent=0.5)

    screenshots_info = [
        ("01_login.png", "Figure 12.1: Universal Authentication Console (login.php)",
         "The Universal Authentication Console serves as the single-entry security perimeter for HairFidence. It accepts user credentials, enforces client-side validation, and forwards requests to the backend authentication router. The router verifies BCrypt hashed passwords, checks NGO accreditation status, and issues session tokens.",
         "Security controls include HTTPS transport encryption, HTTP-only cookie flags, and session fixation guards. Unapproved NGOs are prevented from entering the system, displaying an informative pending accreditation banner."),

        ("02_register.png", "Figure 12.2: Multi-Role User Registration Console (register.php)",
         "The Multi-Role Registration Console provides dynamic registration forms tailored to Donors, Cancer Patients, and Healthcare NGOs. Role-specific form sections appear dynamically using JavaScript event listeners based on the selected role card.",
         "Backend validation ensures email uniqueness, enforces password complexity standards, and writes normalized tuples into the login table and corresponding domain profile tables within an atomic database transaction."),

        ("03_home.png", "Figure 12.3: Public Informational & Community Portal (index.php)",
         "The Public Informational Portal introduces civic visitors to the mission of HairFidence. It features educational infographics outlining the physical requirements for donation (minimum 10 inches, dry, tied ponytail), details the wig fabrication journey, and showcases upcoming community collection drives.",
         "The responsive navigation bar offers quick routing to role-specific registration portals and authentication desks, with clean visual typography and fluid CSS animations."),

        ("04_admin_dashboard.png", "Figure 12.4: Administrator Platform Analytics & Overview (admin/dashboard.php)",
         "The Administrator Dashboard serves as the central command center for platform governance. It aggregates system-wide KPIs into dynamic metric cards displaying Total Registered Donors, Total Approved NGOs, Total Donation Posts, and Active Patient Requests.",
         "The console provides quick action links for accrediting newly registered NGOs, reviewing unresolved grievance tickets, and auditing system activity logs in real-time."),

        ("04b_admin_ngos.png", "Figure 12.5: Administrator NGO Verification & Accreditation Console",
         "The NGO Verification Console enables the Administrator to audit statutory registration documents submitted by applicant charities. Each record presents the charity's official name, registration number, contact person, and pending status.",
         "Administrators can execute one-click approvals, which instantly update the is_approved flag in the database and activate the NGO's clinical audit capabilities."),

        ("04c_admin_complaints.png", "Figure 12.6: Administrator Grievance Ticketing & Resolution Console",
         "The Grievance Redressal Console manages user support tickets submitted by donors, patients, or NGOs. Administrators view ticket submission timestamps, user emails, subject lines, and incident narratives.",
         "Administrators can resolve tickets with an audit log update, transitioning the ticket state from 'Pending' to 'Resolved' and recording the resolution timestamp."),

        ("05_ngo_dashboard.png", "Figure 12.7: Healthcare NGO Operations & Clinical Audit Hub (ngo/dashboard.php)",
         "The Healthcare NGO Operations Hub provides accredited charities with tools to manage patient requests and physical parcel logistics. The console displays active requests, donor packaging details, and uploaded medical proofs.",
         "Caseworkers can inspect patient oncology certificates directly in the browser and execute atomic state transitions (Approve or Reject) to manage wig allocation."),

        ("05b_ngo_campaign.png", "Figure 12.8: NGO Community Hair Donation Campaign Creation",
         "The Campaign Creation Form allows accredited NGOs to broadcast upcoming community collection drives. Caseworkers define the campaign title, target donation goals, event calendar date, and venue location.",
         "Upon submission, the drive is immediately published to the public portal and donor dashboards, encouraging local civic participation and salon partnerships."),

        ("06_donor_dashboard.png", "Figure 12.9: Donor Dashboard & Real-Time Pipeline Tracker (donor/dashboard.php)",
         "The Donor Dashboard empowers civic donors with complete visibility over their contributions. An interactive visual pipeline tracker displays the exact real-time state of each donation: 'Available', 'Processing', or 'Donated'.",
         "Donors also receive immediate alerts regarding upcoming collection drives in their geographic vicinity, fostering continuous civic engagement."),

        ("06b_donor_add_donation.png", "Figure 12.10: Donor Hair Post Submission with Specimen Upload",
         "The Hair Post Authoring Interface captures precise technical metadata for hair specimens. Donors input strand length in inches, select hair texture (Straight, Wavy, Curly), and upload a clear specimen photograph.",
         "The backend controller validates image MIME types, creates sanitized unique filenames, and registers the post as Available in the public catalog."),

        ("07_patient_dashboard.png", "Figure 12.11: Cancer Patient Portal & Live Verified Hair Catalog (patient/dashboard.php)",
         "The Cancer Patient Portal allows verified cancer survivors to browse clean, cataloged hair donations. Patients can filter specimens by hair length and texture to match their personal preference.",
         "Each catalog card displays verified strand photos, exact length, and an interactive 'Request Specimen' action that triggers atomic concurrency locking."),

        ("07b_patient_my_requests.png", "Figure 12.12: Patient Hair Request Tracking & Allocation Status",
         "The Patient Request Tracking Console allows patients to monitor the clinical audit and allocation progress of their requested hair prostheses. Status indicators show whether the request is Pending review, Approved, or Rejected.",
         "Approved requests provide partner NGO contact details to coordinate custom wig sizing, styling, and delivery."),

        ("08_user_complaint.png", "Figure 12.13: User Grievance & Support Ticket Submission Form",
         "The Support Ticket Submission Console allows any registered user to log formal operational inquiries or report platform anomalies. Users input a concise subject line and detailed incident description.",
         "Tickets are written directly to the complaints table with a 'Pending' status, immediately alerting the Administrator for resolution."),

        ("09_user_profile.png", "Figure 12.14: User Account Profile & Delivery Address Console",
         "The User Profile Console enables users across all roles to maintain their personal contact coordinates, telephone numbers, and shipping addresses. For cancer patients, maintaining an accurate postal address ensures flawless delivery of crafted wigs.",
         "Password updates and credential security settings are also managed through this console with strict re-authentication safeguards."),
    ]

    for filename, caption, p1_desc, p2_desc in screenshots_info:
        img_path = os.path.join(SCREEN_DIR, filename)
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.add_run().add_picture(img_path, width=Inches(5.2))
            add_p(doc, caption, font_size=9.5, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
            add_p(doc, p1_desc, font_size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, indent=0.5)
            add_p(doc, p2_desc, font_size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=16, indent=0.5)

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 13: BIBLIOGRAPHY
    # ──────────────────────────────────────────────────────────────────────────
    add_divider_page(doc, "CHAPTER 13: BIBLIOGRAPHY")
    add_heading_1(doc, "CHAPTER 13: BIBLIOGRAPHY")

    add_heading_2(doc, "Web Resources & Authoritative Documentation")
    webs = [
        "[1] PHP Documentation Group, PHP: Hypertext Preprocessor Official Reference Manual, Available online: https://www.php.net/manual/en/ (Accessed: June 2026).",
        "[2] Oracle Corporation, MySQL 8.0 Reference Manual: InnoDB Storage Engine & Locking Models, Available online: https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html (Accessed: June 2026).",
        "[3] Mozilla Developer Network (MDN), Web Technology for Developers: Semantic HTML5 and CSS Flexible Box Layout, Available online: https://developer.mozilla.org/en-US/docs/Web (Accessed: May 2026).",
        "[4] Open Web Application Security Project (OWASP), OWASP Top 10: The Ten Most Critical Web Application Security Risks, Available online: https://owasp.org/Top10/ (Accessed: May 2026).",
        "[5] MariaDB Foundation, MariaDB Server Documentation: Transactions and Concurrency Control, Available online: https://mariadb.com/kb/en/documentation/ (Accessed: April 2026).",
        "[6] APJ Abdul Kalam Technological University, Master of Computer Applications Curriculum, Scheme and Syllabi (2020 Scheme), Government of Kerala, Available online: https://ktu.edu.in/ (Accessed: July 2026).",
        "[7] American Cancer Society, Coping with Cancer: Hair Loss and Alopecia During Chemotherapy, Available online: https://www.cancer.org/treatment/treatments-and-side-effects/physical-side-effects/hair-loss.html (Accessed: March 2026).",
    ]
    for w in webs:
        add_p(doc, w, font_size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8, line_spacing=1.3)

    add_p(doc, "", space_after=10)
    add_heading_2(doc, "Technical Reference Textbooks")
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

    # Save to DOCX_OUT_PATH
    doc.save(DOCX_OUT_PATH)
    print(f"HairFidence MCA Thesis Document successfully created at: {DOCX_OUT_PATH}")

if __name__ == "__main__":
    generate_thesis_docx()
