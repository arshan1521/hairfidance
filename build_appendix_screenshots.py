import os
from PIL import Image, ImageDraw, ImageFont

SCREEN_DIR = r"c:\Users\ARSHAN NIZAR\Downloads\MINI_PROJECT\screenshots"
os.makedirs(SCREEN_DIR, exist_ok=True)

def get_fonts():
    try:
        f_title = ImageFont.truetype("arialbd.ttf", 20)
        f_h2 = ImageFont.truetype("arialbd.ttf", 16)
        f_bold = ImageFont.truetype("arialbd.ttf", 13)
        f_reg = ImageFont.truetype("arial.ttf", 12)
        f_sm = ImageFont.truetype("arial.ttf", 10)
        f_big = ImageFont.truetype("arialbd.ttf", 28)
    except:
        f_title = f_h2 = f_bold = f_reg = f_sm = f_big = ImageFont.load_default()
    return f_title, f_h2, f_bold, f_reg, f_sm, f_big

def base_frame(title, url, active_nav="Home", role=None):
    W, H = 1440, 900
    img = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(img)
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()

    # Chrome Window Titlebar
    draw.rectangle([0, 0, W, 70], fill="#1e293b")
    draw.ellipse([16, 14, 28, 26], fill="#ef4444")
    draw.ellipse([36, 14, 48, 26], fill="#f59e0b")
    draw.ellipse([56, 14, 68, 26], fill="#10b981")

    # Tab
    draw.rectangle([90, 8, 320, 38], fill="#334155")
    draw.text((105, 16), title[:30], fill="#f8fafc", font=f_sm)

    # Address bar
    draw.rectangle([0, 38, W, 70], fill="#0f172a")
    draw.rectangle([90, 42, W - 100, 64], fill="#1e293b", outline="#334155", width=1)
    draw.text((105, 46), url, fill="#94a3b8", font=f_sm)

    # App Header / Navbar
    draw.rectangle([0, 70, W, 130], fill="white", outline="#e2e8f0", width=1)
    # Logo
    draw.ellipse([40, 82, 70, 112], fill="#0ea5e9")
    draw.text((80, 88), "HairFidence", fill="#0f172a", font=f_title)
    draw.text((205, 92), "| Cancer Patient Hair Donation", fill="#64748b", font=f_reg)

    if role:
        draw.text((W - 320, 92), f"Welcome, {role}", fill="#0f172a", font=f_bold)
        draw.rectangle([W - 140, 85, W - 40, 115], fill="#ef4444")
        draw.text((W - 115, 92), "Logout", fill="white", font=f_bold)
    else:
        draw.text((W - 240, 92), "Login", fill="#0ea5e9", font=f_bold)
        draw.rectangle([W - 150, 85, W - 50, 115], fill="#10b981")
        draw.text((W - 128, 92), "Register", fill="white", font=f_bold)

    return img, draw

def draw_sidebar(draw, active_tab, items):
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()
    draw.rectangle([0, 130, 240, 900], fill="#0f172a")
    draw.text((30, 155), "MAIN NAVIGATION", fill="#475569", font=f_sm)
    y = 190
    for it in items:
        if it == active_tab:
            draw.rectangle([10, y - 6, 230, y + 26], fill="#10b981")
            draw.text((30, y), it, fill="white", font=f_bold)
        else:
            draw.text((30, y), it, fill="#94a3b8", font=f_reg)
        y += 45

# 1. LOGIN
def make_login():
    img, draw = base_frame("HairFidence - Login", "http://127.0.0.1:8000/login.php")
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()
    # Card
    draw.rectangle([480, 220, 960, 680], fill="white", outline="#cbd5e1", width=1)
    draw.text((640, 255), "Account Login", fill="#0f172a", font=f_title)
    draw.text((580, 290), "Sign in to access your donation portal", fill="#64748b", font=f_reg)

    draw.text((530, 340), "Email Address", fill="#334155", font=f_bold)
    draw.rectangle([530, 365, 910, 405], fill="#f8fafc", outline="#cbd5e1", width=1)
    draw.text((545, 377), "admin@hairfidence.com", fill="#0f172a", font=f_reg)

    draw.text((530, 430), "Password", fill="#334155", font=f_bold)
    draw.rectangle([530, 455, 910, 495], fill="#f8fafc", outline="#cbd5e1", width=1)
    draw.text((545, 467), "••••••••••••", fill="#0f172a", font=f_reg)

    draw.rectangle([530, 530, 910, 575], fill="#10b981")
    draw.text((685, 544), "Sign In", fill="white", font=f_bold)

    draw.text((615, 610), "Don't have an account? Register here", fill="#0ea5e9", font=f_reg)
    img.save(os.path.join(SCREEN_DIR, "01_login.png"))

# 2. REGISTER
def make_register():
    img, draw = base_frame("HairFidence - Registration", "http://127.0.0.1:8000/register.php")
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()
    draw.rectangle([420, 180, 1020, 780], fill="white", outline="#cbd5e1", width=1)
    draw.text((610, 210), "Create New Account", fill="#0f172a", font=f_title)
    draw.text((540, 245), "Join HairFidence as a Donor, Patient, or Registered NGO", fill="#64748b", font=f_reg)

    fields = [
        ("Full Name / Organization Name", "Ananya Sharma", 280),
        ("Email Address", "ananya.s@gmail.com", 355),
        ("Phone Number", "+91 9847123456", 430),
        ("Select Role", "Donor  (Other options: Patient, NGO)", 505),
        ("Password", "••••••••••••", 580),
    ]
    for label, val, y in fields:
        draw.text((470, y), label, fill="#334155", font=f_bold)
        draw.rectangle([470, y + 25, 970, y + 60], fill="#f8fafc", outline="#cbd5e1", width=1)
        draw.text((485, y + 36), val, fill="#0f172a", font=f_reg)

    draw.rectangle([470, 680, 970, 725], fill="#0ea5e9")
    draw.text((670, 694), "Register Account", fill="white", font=f_bold)
    img.save(os.path.join(SCREEN_DIR, "02_register.png"))

# 3. HOME LANDING
def make_home():
    img, draw = base_frame("HairFidence - Home", "http://127.0.0.1:8000/index.php")
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()
    # Hero Section
    draw.rectangle([0, 130, 1440, 480], fill="#0f172a")
    draw.text((220, 190), "GIFT HAIR, RESTORE CONFIDENCE", fill="#10b981", font=f_bold)
    draw.text((220, 220), "Cancer Patient Hair Donation Portal", fill="white", font=f_big)
    draw.text((220, 270), "Connecting generous donors, verified healthcare NGOs, and cancer patients recovering\nfrom chemotherapy. 100% transparent, tracked from haircut to medical wig delivery.", fill="#94a3b8", font=f_h2)

    draw.rectangle([220, 360, 420, 410], fill="#10b981")
    draw.text((260, 375), "Donate Hair Now", fill="white", font=f_bold)
    draw.rectangle([440, 360, 640, 410], fill="#1e293b", outline="#64748b", width=1)
    draw.text((475, 375), "Request A Wig", fill="white", font=f_bold)

    # Stat Cards
    stats = [
        ("Total Hair Donations", "148+", "#0ea5e9", 100),
        ("Verified Partner NGOs", "16", "#10b981", 420),
        ("Patients Supported", "92+", "#7c3aed", 740),
        ("Active Hair Drives", "8", "#f59e0b", 1060),
    ]
    for lbl, val, color, x in stats:
        draw.rectangle([x, 520, x + 280, 660], fill="white", outline="#e2e8f0", width=1)
        draw.rectangle([x, 520, x + 280, 526], fill=color)
        draw.text((x + 30, 550), lbl, fill="#64748b", font=f_bold)
        draw.text((x + 30, 585), val, fill="#0f172a", font=f_big)

    # Mission note
    draw.rectangle([100, 700, 1340, 830], fill="white", outline="#e2e8f0", width=1)
    draw.text((140, 730), "How It Works: 4 Simple Steps", fill="#0f172a", font=f_h2)
    draw.text((140, 770), "1. Donor logs hair specs  ->  2. NGO verifies parcel  ->  3. Patient requests match  ->  4. Free customized wig crafted & handed over", fill="#475569", font=f_reg)
    img.save(os.path.join(SCREEN_DIR, "03_home.png"))

# 4. ADMIN DASHBOARD
def make_admin_dashboard():
    img, draw = base_frame("Admin Dashboard - HairFidence", "http://127.0.0.1:8000/admin/dashboard.php", role="System Administrator")
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()
    draw_sidebar(draw, "Dashboard", ["Dashboard", "Approve NGOs", "All Users", "Campaigns", "Complaints", "System Logs"])

    # Header
    draw.text((280, 160), "Administrator Control Console", fill="#0f172a", font=f_title)
    draw.text((280, 190), "Real-time system overview and ecosystem metrics", fill="#64748b", font=f_reg)

    # Metrics
    cards = [
        ("Total Users", "214", "#0ea5e9", 280),
        ("Pending NGOs", "3", "#f59e0b", 560),
        ("Donation Posts", "148", "#10b981", 840),
        ("Pending Tickets", "2", "#ef4444", 1120),
    ]
    for lbl, val, col, x in cards:
        draw.rectangle([x, 230, x + 250, 330], fill="white", outline="#cbd5e1", width=1)
        draw.rectangle([x, 230, x + 250, 236], fill=col)
        draw.text((x + 20, 250), lbl, fill="#64748b", font=f_bold)
        draw.text((x + 20, 275), val, fill="#0f172a", font=f_big)

    # Recent Pending NGOs Table
    draw.text((280, 370), "Pending NGO Verification Requests", fill="#0f172a", font=f_h2)
    draw.rectangle([280, 405, 1370, 580], fill="white", outline="#cbd5e1", width=1)
    draw.rectangle([280, 405, 1370, 445], fill="#f1f5f9")
    draw.text((300, 418), "Organization Name", fill="#0f172a", font=f_bold)
    draw.text((580, 418), "Registration No", fill="#0f172a", font=f_bold)
    draw.text((820, 418), "Email Address", fill="#0f172a", font=f_bold)
    draw.text((1100, 418), "Action", fill="#0f172a", font=f_bold)

    ngos = [
        ("Aarogya Cancer Support NGO", "REG/KL/2024/9912", "aarogya@cancercare.in", 460),
        ("Malabar Care & Cure Society", "REG/KL/2025/1104", "contact@malabarcare.org", 515),
    ]
    for org, reg, em, y in ngos:
        draw.text((300, y), org, fill="#334155", font=f_reg)
        draw.text((580, y), reg, fill="#334155", font=f_reg)
        draw.text((820, y), em, fill="#334155", font=f_reg)
        draw.rectangle([1100, y - 5, 1180, y + 22], fill="#10b981")
        draw.text((1115, y), "Approve", fill="white", font=f_bold)
        draw.rectangle([1195, y - 5, 1265, y + 22], fill="#ef4444")
        draw.text((1210, y), "Reject", fill="white", font=f_bold)

    # Active Complaints Overview
    draw.text((280, 610), "Recent Support & Grievance Tickets", fill="#0f172a", font=f_h2)
    draw.rectangle([280, 645, 1370, 820], fill="white", outline="#cbd5e1", width=1)
    draw.rectangle([280, 645, 1370, 685], fill="#f1f5f9")
    draw.text((300, 658), "Ticket ID", fill="#0f172a", font=f_bold)
    draw.text((420, 658), "User Email", fill="#0f172a", font=f_bold)
    draw.text((680, 658), "Subject", fill="#0f172a", font=f_bold)
    draw.text((1060, 658), "Status", fill="#0f172a", font=f_bold)
    draw.text((1200, 658), "Action", fill="#0f172a", font=f_bold)

    draw.text((300, 705), "#TCK-108", fill="#334155", font=f_reg)
    draw.text((420, 705), "rahul.v@gmail.com", fill="#334155", font=f_reg)
    draw.text((680, 705), "Courier receipt upload confirmation inquiry", fill="#334155", font=f_reg)
    draw.rectangle([1060, 700, 1135, 725], fill="#fef3c7", outline="#f59e0b", width=1)
    draw.text((1072, 705), "Pending", fill="#b45309", font=f_bold)
    draw.rectangle([1200, 700, 1285, 725], fill="#0ea5e9")
    draw.text((1215, 705), "Resolve", fill="white", font=f_bold)

    img.save(os.path.join(SCREEN_DIR, "04_admin_dashboard.png"))

# 5. NGO DASHBOARD
def make_ngo_dashboard():
    img, draw = base_frame("NGO Dashboard - Hope & Healing Foundation", "http://127.0.0.1:8000/ngo/dashboard.php", role="Hope Foundation (NGO)")
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()
    draw_sidebar(draw, "Dashboard", ["Dashboard", "Hair Requests", "Verify Donations", "Campaigns", "Patient Reports"])

    draw.text((280, 160), "NGO Operations Console", fill="#0f172a", font=f_title)
    draw.text((280, 190), "Hope & Healing Cancer Foundation | Reg No: REG/KL/2021/8842", fill="#64748b", font=f_reg)

    cards = [
        ("Incoming Requests", "5", "#0ea5e9", 280),
        ("Donations Received", "42", "#10b981", 560),
        ("Wigs Dispatched", "28", "#7c3aed", 840),
        ("Active Campaigns", "2", "#f59e0b", 1120),
    ]
    for lbl, val, col, x in cards:
        draw.rectangle([x, 230, x + 250, 330], fill="white", outline="#cbd5e1", width=1)
        draw.rectangle([x, 230, x + 250, 236], fill=col)
        draw.text((x + 20, 250), lbl, fill="#64748b", font=f_bold)
        draw.text((x + 20, 275), val, fill="#0f172a", font=f_big)

    draw.text((280, 370), "Patient Hair Requests Pending Medical Audit", fill="#0f172a", font=f_h2)
    draw.rectangle([280, 405, 1370, 600], fill="white", outline="#cbd5e1", width=1)
    draw.rectangle([280, 405, 1370, 445], fill="#f1f5f9")
    draw.text((300, 418), "Req ID", fill="#0f172a", font=f_bold)
    draw.text((380, 418), "Patient Name", fill="#0f172a", font=f_bold)
    draw.text((560, 418), "Hair Requested", fill="#0f172a", font=f_bold)
    draw.text((780, 418), "Diagnostic Report", fill="#0f172a", font=f_bold)
    draw.text((1020, 418), "Audit Status", fill="#0f172a", font=f_bold)
    draw.text((1180, 418), "Action", fill="#0f172a", font=f_bold)

    draw.text((300, 465), "#REQ-401", fill="#334155", font=f_reg)
    draw.text((380, 465), "Fatima Beevi", fill="#334155", font=f_reg)
    draw.text((560, 465), "14.5\" Straight Black (#PST-12)", fill="#334155", font=f_reg)
    draw.text((780, 465), "Govt_Med_College_Diagnosis.pdf [View]", fill="#0ea5e9", font=f_bold)
    draw.rectangle([1020, 460, 1100, 485], fill="#fef3c7", outline="#f59e0b", width=1)
    draw.text((1035, 465), "Pending", fill="#b45309", font=f_bold)
    draw.rectangle([1180, 460, 1260, 485], fill="#10b981")
    draw.text((1195, 465), "Approve", fill="white", font=f_bold)

    draw.text((300, 520), "#REQ-398", fill="#334155", font=f_reg)
    draw.text((380, 520), "Kavitha R Nair", fill="#334155", font=f_reg)
    draw.text((560, 520), "12.0\" Wavy Brown (#PST-08)", fill="#334155", font=f_reg)
    draw.text((780, 520), "Oncology_Histopath_Cert.pdf [View]", fill="#0ea5e9", font=f_bold)
    draw.rectangle([1020, 515, 1100, 540], fill="#dcfce7", outline="#10b981", width=1)
    draw.text((1030, 520), "Approved", fill="#15803d", font=f_bold)
    draw.rectangle([1180, 515, 1270, 540], fill="#0ea5e9")
    draw.text((1192, 520), "Dispatch", fill="white", font=f_bold)

    img.save(os.path.join(SCREEN_DIR, "05_ngo_dashboard.png"))

# 6. DONOR DASHBOARD
def make_donor_dashboard():
    img, draw = base_frame("Donor Dashboard - HairFidence", "http://127.0.0.1:8000/donor/dashboard.php", role="Ananya Sharma (Donor)")
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()
    draw_sidebar(draw, "My Donations", ["Dashboard", "Donate Hair", "My Donations", "Community Drives", "Profile"])

    draw.text((280, 160), "Donor Philanthropy Center", fill="#0f172a", font=f_title)
    draw.text((280, 190), "Track your hair contribution pipeline from donation to wig crafting", fill="#64748b", font=f_reg)

    # Active Donation Pipeline Card
    draw.rectangle([280, 230, 1370, 480], fill="white", outline="#cbd5e1", width=1)
    draw.text((310, 255), "Live Donation Tracking: Post #HDP-104", fill="#0f172a", font=f_h2)
    draw.text((310, 285), "14.5 Inches · Straight Natural Black · Cut Date: 12 July 2026", fill="#64748b", font=f_reg)

    # Stepper / Pipeline Tracker
    steps = [
        ("1. Post Created", "Completed", "#10b981", 340),
        ("2. Physical Parcel Sent", "Completed", "#10b981", 580),
        ("3. NGO Audited & Verified", "In-Progress", "#f59e0b", 820),
        ("4. Medical Wig Handover", "Upcoming", "#94a3b8", 1060),
    ]
    for title, st, col, x in steps:
        draw.ellipse([x + 50, 330, x + 80, 360], fill=col)
        draw.text((x + 10, 375), title, fill="#0f172a", font=f_bold)
        draw.text((x + 25, 395), st, fill=col, font=f_sm)

    draw.line([420, 345, 580, 345], fill="#10b981", width=3)
    draw.line([660, 345, 820, 345], fill="#f59e0b", width=3)
    draw.line([900, 345, 1060, 345], fill="#cbd5e1", width=3)

    # Upcoming Campaigns Widget
    draw.text((280, 520), "Upcoming Hair Donation Drives in Calicut", fill="#0f172a", font=f_h2)
    draw.rectangle([280, 555, 800, 720], fill="white", outline="#cbd5e1", width=1)
    draw.text((310, 575), "Locks of Hope Drive 2026", fill="#0f172a", font=f_bold)
    draw.text((310, 600), "Organized by Hope & Healing Foundation", fill="#0ea5e9", font=f_reg)
    draw.text((310, 630), "Venue: Tagore Centenary Hall, Calicut | Date: 15 August 2026", fill="#64748b", font=f_reg)
    draw.rectangle([310, 660, 460, 695], fill="#10b981")
    draw.text((335, 670), "Register To Attend", fill="white", font=f_bold)

    draw.rectangle([830, 555, 1370, 720], fill="white", outline="#cbd5e1", width=1)
    draw.text((860, 575), "Cancer Care Awareness & Collection Drive", fill="#0f172a", font=f_bold)
    draw.text((860, 600), "Organized by Jeevani Welfare Society", fill="#0ea5e9", font=f_reg)
    draw.text((860, 630), "Venue: AWH Engineering College Campus | Date: 20 September 2026", fill="#64748b", font=f_reg)
    draw.rectangle([860, 660, 1010, 695], fill="#10b981")
    draw.text((885, 670), "Register To Attend", fill="white", font=f_bold)

    img.save(os.path.join(SCREEN_DIR, "06_donor_dashboard.png"))

# 7. PATIENT DASHBOARD
def make_patient_dashboard():
    img, draw = base_frame("Patient Portal - HairFidence", "http://127.0.0.1:8000/patient/dashboard.php", role="Fatima Beevi (Patient)")
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()
    draw_sidebar(draw, "Browse Hair", ["Dashboard", "Browse Hair", "My Requests", "Medical Documents", "Support"])

    draw.text((280, 160), "Available Hair Catalog for Cancer Survivors", fill="#0f172a", font=f_title)
    draw.text((280, 190), "Filter and request clean, hygienic hair donations verified by authorized partner NGOs", fill="#64748b", font=f_reg)

    # Filter Bar
    draw.rectangle([280, 230, 1370, 280], fill="white", outline="#cbd5e1", width=1)
    draw.text((300, 246), "Length: 12\" to 16\"  [▼]", fill="#334155", font=f_reg)
    draw.text((500, 246), "Texture: Straight / Wavy  [▼]", fill="#334155", font=f_reg)
    draw.text((750, 246), "Color: Natural Black  [▼]", fill="#334155", font=f_reg)
    draw.rectangle([1230, 238, 1350, 272], fill="#0ea5e9")
    draw.text((1255, 246), "Apply Filters", fill="white", font=f_bold)

    # Catalog Cards
    items = [
        ("Straight Black Hair", "14.5 Inches", "Virgin hair, chemical free", "Available", "#10b981", 280),
        ("Wavy Dark Brown", "12.0 Inches", "Single donor ponytail", "Processing", "#f59e0b", 650),
        ("Silky Natural Black", "16.0 Inches", "Cleaned & salon tied", "Available", "#10b981", 1020),
    ]
    for name, length, desc, status, col, x in items:
        draw.rectangle([x, 310, x + 340, 580], fill="white", outline="#cbd5e1", width=1)
        draw.rectangle([x, 310, x + 340, 430], fill="#e2e8f0")
        draw.text((x + 100, 360), "[ HAIR PHOTO PREVIEW ]", fill="#64748b", font=f_bold)

        draw.text((x + 20, 445), name, fill="#0f172a", font=f_bold)
        draw.text((x + 20, 470), f"Length: {length} | {desc}", fill="#64748b", font=f_reg)

        draw.rectangle([x + 20, 500, x + 100, 525], fill=col)
        draw.text((x + 30, 505), status, fill="white", font=f_bold)

        if status == "Available":
            draw.rectangle([x + 190, 535, x + 320, 568], fill="#10b981")
            draw.text((x + 208, 544), "Request Hair", fill="white", font=f_bold)
        else:
            draw.rectangle([x + 190, 535, x + 320, 568], fill="#94a3b8")
            draw.text((x + 215, 544), "Reserved", fill="white", font=f_bold)

    # Medical Report verification banner
    draw.rectangle([280, 620, 1370, 750], fill="#f0fdf4", outline="#10b981", width=1)
    draw.text((310, 645), "✓ Diagnostic Medical Report Verified", fill="#15803d", font=f_h2)
    draw.text((310, 675), "Your oncology treatment summary from Govt Medical College Calicut was verified by Hope & Healing Foundation.\nYou can directly request any available hair item for immediate wig crafting.", fill="#166534", font=f_reg)
    draw.text((310, 715), "Uploaded Document: Govt_Med_College_Diagnosis.pdf (Verified on 02 Aug 2026)", fill="#0ea5e9", font=f_bold)

    img.save(os.path.join(SCREEN_DIR, "07_patient_dashboard.png"))

if __name__ == "__main__":
    make_login()
    make_register()
    make_home()
    make_admin_dashboard()
    make_ngo_dashboard()
    make_donor_dashboard()
    make_patient_dashboard()
    print("All appendix screenshots generated successfully!")
