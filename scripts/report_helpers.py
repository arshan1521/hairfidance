import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC_PATH = os.path.join(BASE_DIR, "HairFidence_MCA_Thesis.docx")
SCREEN_DIR = os.path.join(BASE_DIR, "screenshots")
LOGO_PATH = os.path.join(BASE_DIR, "college_logo.png")
UML_PATH = os.path.join(BASE_DIR, "use_case_diagram.png")

# Helper XML styling
def set_cell_border(cell, **kwargs):
    """
    kwargs: top, bottom, left, right
    values: dict(sz=12, val='single', color='000000')
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}>\n'
                          f'<w:top w:val="{kwargs.get("top", "single")}" w:sz="{kwargs.get("top_sz", "4")}" w:space="0" w:color="{kwargs.get("top_color", "CCCCCC")}"/>\n'
                          f'<w:bottom w:val="{kwargs.get("bottom", "single")}" w:sz="{kwargs.get("bottom_sz", "4")}" w:space="0" w:color="{kwargs.get("bottom_color", "CCCCCC")}"/>\n'
                          f'<w:left w:val="{kwargs.get("left", "single")}" w:sz="{kwargs.get("left_sz", "4")}" w:space="0" w:color="{kwargs.get("left_color", "CCCCCC")}"/>\n'
                          f'<w:right w:val="{kwargs.get("right", "single")}" w:sz="{kwargs.get("right_sz", "4")}" w:space="0" w:color="{kwargs.get("right_color", "CCCCCC")}"/>\n'
                          f'</w:tcBorders>')
    tcPr.append(tcBorders)

def set_cell_shading(cell, color_hex):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_para_font(p, name="Times New Roman", size=12, bold=False, italic=False, color_rgb=None, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, line_spacing=1.15):
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    for r in p.runs:
        r.font.name = name
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        if color_rgb:
            r.font.color.rgb = color_rgb

def add_p(doc, text="", font_size=12, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, line_spacing=1.15):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(font_size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
    return p

def add_heading_1(doc, text):
    p = add_p(doc, text, font_size=16, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=14, space_after=8)
    return p

def add_heading_2(doc, text):
    p = add_p(doc, text, font_size=13.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=10, space_after=6)
    return p

def add_heading_3(doc, text):
    p = add_p(doc, text, font_size=12, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=8, space_after=4)
    return p

def add_divider_page(doc, title_text):
    """Clean chapter separation page like friend's report"""
    doc.add_page_break()
    p_pre = add_p(doc, "", space_before=220)
    p = add_p(doc, title_text, font_size=20, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    doc.add_page_break()

print("Helper functions defined.")
