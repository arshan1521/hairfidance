from PIL import Image, ImageDraw, ImageFont
import os

def draw_actor(draw, x, y, label, font):
    # Head
    r = 18
    draw.ellipse([x - r, y - r, x + r, y + r], outline="black", width=2)
    # Body
    draw.line([x, y + r, x, y + r + 45], fill="black", width=2)
    # Arms
    draw.line([x - 30, y + r + 20, x + 30, y + r + 20], fill="black", width=2)
    # Legs
    draw.line([x, y + r + 45, x - 25, y + r + 95], fill="black", width=2)
    draw.line([x, y + r + 45, x + 25, y + r + 95], fill="black", width=2)
    # Label
    bbox = draw.textbbox((0, 0), label, font=font)
    w = bbox[2] - bbox[0]
    draw.text((x - w / 2, y + r + 105), label, fill="black", font=font)
    return (x, y + r + 20) # Center anchor point

def draw_usecase(draw, x, y, w, h, text, font):
    # Oval
    draw.ellipse([x - w/2, y - h/2, x + w/2, y + h/2], outline="#1e293b", fill="#f8fafc", width=2)
    # Text
    lines = text.split("\n")
    total_h = len(lines) * 18
    start_y = y - total_h / 2 + 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        draw.text((x - tw/2, start_y), line, fill="#0f172a", font=font)
        start_y += 18
    return (x - w/2, y), (x + w/2, y) # left, right edge

def make_usecase_diagram(out_path):
    W, H = 1100, 1350
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 22)
        font_actor = ImageFont.truetype("arialbd.ttf", 16)
        font_uc = ImageFont.truetype("arial.ttf", 14)
    except:
        font_title = ImageFont.load_default()
        font_actor = font_title
        font_uc = font_title

    # System Boundary Box
    bx1, by1, bx2, by2 = 270, 70, 830, 1310
    draw.rectangle([bx1, by1, bx2, by2], outline="#334155", width=2)
    # System Title
    draw.text((bx1 + 25, by1 + 15), "HairFidence System", fill="#0f172a", font=font_title)

    # Use Cases (x, y, w, h, text)
    cx = (bx1 + bx2) / 2
    use_cases = [
        ("Login & Authentication", 140, 240, 46),
        ("Approve / Reject NGOs", 220, 240, 46),
        ("Manage Users & Platform", 300, 240, 46),
        ("Resolve User Complaints", 380, 240, 46),
        ("Create Hair Donation Post", 460, 250, 46),
        ("View Donation Pipeline Status", 540, 260, 46),
        ("Verify Hair Donations", 620, 240, 46),
        ("Browse Available Hair Catalog", 700, 260, 46),
        ("Upload Medical Report", 780, 240, 46),
        ("Submit Hair Request", 860, 240, 46),
        ("Audit Medical Reports &\nApprove Requests", 945, 270, 55),
        ("Create & Manage Campaigns", 1030, 260, 46),
        ("Submit Issues / Grievance", 1110, 250, 46),
        ("View Donation Drives", 1190, 240, 46),
        ("View System Statistics", 1260, 240, 44),
    ]

    uc_anchors = {}
    for text, y, w, h in use_cases:
        left_edge, right_edge = draw_usecase(draw, cx, y, w, h, text, font_uc)
        uc_anchors[text] = (left_edge, right_edge)

    # Actors
    admin_pt = draw_actor(draw, 120, 250, "Admin", font_actor)
    ngo_pt = draw_actor(draw, 120, 800, "NGO", font_actor)
    donor_pt = draw_actor(draw, 980, 360, "Donor", font_actor)
    patient_pt = draw_actor(draw, 980, 880, "Patient", font_actor)

    # Connections
    def connect(pt, edge_pt):
        draw.line([pt[0], pt[1], edge_pt[0], edge_pt[1]], fill="#475569", width=1)

    # Admin connections
    for uc in ["Login & Authentication", "Approve / Reject NGOs", "Manage Users & Platform", "Resolve User Complaints", "View System Statistics"]:
        connect(admin_pt, uc_anchors[uc][0])

    # NGO connections
    for uc in ["Login & Authentication", "Verify Hair Donations", "Audit Medical Reports &\nApprove Requests", "Create & Manage Campaigns", "View Donation Pipeline Status"]:
        connect(ngo_pt, uc_anchors[uc][0])

    # Donor connections
    for uc in ["Login & Authentication", "Create Hair Donation Post", "View Donation Pipeline Status", "View Donation Drives", "Submit Issues / Grievance"]:
        connect(donor_pt, uc_anchors[uc][1])

    # Patient connections
    for uc in ["Login & Authentication", "Browse Available Hair Catalog", "Upload Medical Report", "Submit Hair Request", "View Donation Pipeline Status", "Submit Issues / Grievance"]:
        connect(patient_pt, uc_anchors[uc][1])

    img.save(out_path, dpi=(300, 300))
    print(f"UML Diagram saved to {out_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(base_dir, "use_case_diagram.png")
    make_usecase_diagram(out)
