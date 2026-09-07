import os
from PIL import Image, ImageDraw, ImageFont
from build_appendix_screenshots import base_frame, draw_sidebar, get_fonts, SCREEN_DIR

def make_more():
    f_title, f_h2, f_bold, f_reg, f_sm, f_big = get_fonts()

    # 4b. ADMIN - APPROVE NGOS
    img, draw = base_frame("Admin - NGO Approvals", "http://127.0.0.1:8000/admin/dashboard.php?tab=ngos", role="Administrator")
    draw_sidebar(draw, "Approve NGOs", ["Dashboard", "Approve NGOs", "All Users", "Campaigns", "Complaints", "System Logs"])
    draw.text((280, 160), "Healthcare NGO Partner Approvals", fill="#0f172a", font=f_title)
    draw.text((280, 190), "Review institutional certificates, registration documents, and approve medical access", fill="#64748b", font=f_reg)

    draw.rectangle([280, 230, 1370, 520], fill="white", outline="#cbd5e1", width=1)
    draw.rectangle([280, 230, 1370, 275], fill="#f1f5f9")
    draw.text((300, 248), "NGO Name", fill="#0f172a", font=f_bold)
    draw.text((560, 248), "Registration No", fill="#0f172a", font=f_bold)
    draw.text((780, 248), "Contact Person / Phone", fill="#0f172a", font=f_bold)
    draw.text((1020, 248), "Certificates", fill="#0f172a", font=f_bold)
    draw.text((1200, 248), "Decision", fill="#0f172a", font=f_bold)

    ngos = [
        ("Aarogya Cancer Support Foundation", "REG/KL/2024/9912", "Dr. Manoj Kumar / 9847012345", "Govt_Reg_Cert.pdf [View]", 300),
        ("Malabar Care & Cure Society", "REG/KL/2025/1104", "Mrs. Sunitha Pillai / 9447118822", "Society_Act_80G.pdf [View]", 360),
        ("Karunya Cancer Relief Trust", "REG/KL/2023/4521", "Mr. George Mathew / 9745223344", "Trust_Deed_Cert.pdf [View]", 420),
    ]
    for org, reg, cp, cert, y in ngos:
        draw.text((300, y), org, fill="#334155", font=f_reg)
        draw.text((560, y), reg, fill="#334155", font=f_reg)
        draw.text((780, y), cp, fill="#334155", font=f_reg)
        draw.text((1020, y), cert, fill="#0ea5e9", font=f_bold)
        draw.rectangle([1200, y - 5, 1270, y + 22], fill="#10b981")
        draw.text((1212, y), "Approve", fill="white", font=f_bold)
        draw.rectangle([1280, y - 5, 1340, y + 22], fill="#ef4444")
        draw.text((1292, y), "Reject", fill="white", font=f_bold)
    img.save(os.path.join(SCREEN_DIR, "04b_admin_ngos.png"))

    # 4c. ADMIN - COMPLAINTS
    img, draw = base_frame("Admin - System Complaints", "http://127.0.0.1:8000/admin/dashboard.php?tab=complaints", role="Administrator")
    draw_sidebar(draw, "Complaints", ["Dashboard", "Approve NGOs", "All Users", "Campaigns", "Complaints", "System Logs"])
    draw.text((280, 160), "Public Grievance & Issue Redressal", fill="#0f172a", font=f_title)
    draw.text((280, 190), "Respond to donor inquiries, patient medical audit questions, and platform issues", fill="#64748b", font=f_reg)

    draw.rectangle([280, 230, 1370, 500], fill="white", outline="#cbd5e1", width=1)
    draw.rectangle([280, 230, 1370, 275], fill="#f1f5f9")
    draw.text((300, 248), "Ticket ID", fill="#0f172a", font=f_bold)
    draw.text((420, 248), "Complainant", fill="#0f172a", font=f_bold)
    draw.text((640, 248), "Subject / Issue Summary", fill="#0f172a", font=f_bold)
    draw.text((1060, 248), "Current Status", fill="#0f172a", font=f_bold)
    draw.text((1220, 248), "Action", fill="#0f172a", font=f_bold)

    complaints = [
        ("#TCK-108", "rahul.v@gmail.com", "Courier receipt tracking inquiry for Post #102", "Pending", "#f59e0b", 300),
        ("#TCK-105", "fatima.b@gmail.com", "Hospital discharge summary acceptance confirmation", "Resolved", "#10b981", 360),
        ("#TCK-099", "sneha.m@gmail.com", "Appreciation note & certificate of donation query", "Resolved", "#10b981", 420),
    ]
    for tid, user, sub, st, col, y in complaints:
        draw.text((300, y), tid, fill="#334155", font=f_reg)
        draw.text((420, y), user, fill="#334155", font=f_reg)
        draw.text((640, y), sub, fill="#334155", font=f_reg)
        draw.text((1060, y), st, fill=col, font=f_bold)
        if st == "Pending":
            draw.rectangle([1220, y - 5, 1320, y + 22], fill="#0ea5e9")
            draw.text((1235, y), "Mark Resolved", fill="white", font=f_bold)
        else:
            draw.text((1220, y), "Closed", fill="#94a3b8", font=f_reg)
    img.save(os.path.join(SCREEN_DIR, "04c_admin_complaints.png"))

    # 5b. NGO - CREATE CAMPAIGN
    img, draw = base_frame("NGO - Create Donation Campaign", "http://127.0.0.1:8000/ngo/dashboard.php?action=create_campaign", role="Hope Foundation")
    draw_sidebar(draw, "Campaigns", ["Dashboard", "Hair Requests", "Verify Donations", "Campaigns", "Patient Reports"])
    draw.text((280, 160), "Organize Community Hair Donation Drive", fill="#0f172a", font=f_title)
    draw.text((280, 190), "Publish upcoming collection drives, awareness workshops, and community events", fill="#64748b", font=f_reg)

    draw.rectangle([280, 230, 1100, 780], fill="white", outline="#cbd5e1", width=1)
    fields = [
        ("Campaign Title", "Locks of Hope - Mega Hair Donation Camp 2026", 260),
        ("Target Donors / Participants", "250 Volunteers", 335),
        ("Event Date & Time", "15 August 2026, 09:30 AM to 04:30 PM", 410),
        ("Venue / Location Address", "Tagore Centenary Hall, Red Cross Road, Calicut - 673032", 485),
        ("Campaign Objectives & Hair Guidelines", "Minimum 10 inches ponytail cut. Open to all volunteers. Professional hairstylists provided.", 560),
    ]
    for label, val, y in fields:
        draw.text((310, y), label, fill="#334155", font=f_bold)
        draw.rectangle([310, y + 25, 1070, y + 60], fill="#f8fafc", outline="#cbd5e1", width=1)
        draw.text((325, y + 36), val, fill="#0f172a", font=f_reg)

    draw.rectangle([310, 680, 520, 725], fill="#10b981")
    draw.text((345, 694), "Publish Campaign", fill="white", font=f_bold)
    img.save(os.path.join(SCREEN_DIR, "05b_ngo_campaign.png"))

    # 6b. DONOR - ADD DONATION
    img, draw = base_frame("Donor - Add Hair Donation", "http://127.0.0.1:8000/donor/dashboard.php?action=add", role="Ananya Sharma")
    draw_sidebar(draw, "Donate Hair", ["Dashboard", "Donate Hair", "My Donations", "Community Drives", "Profile"])
    draw.text((280, 160), "Submit New Hair Donation Post", fill="#0f172a", font=f_title)
    draw.text((280, 190), "Log the length and texture specifications of your hair contribution", fill="#64748b", font=f_reg)

    draw.rectangle([280, 230, 1050, 760], fill="white", outline="#cbd5e1", width=1)
    dfields = [
        ("Hair Length (in inches)", "14.5 Inches", 260),
        ("Hair Texture", "Straight Natural Hair (Other options: Wavy, Curly)", 335),
        ("Hair Color & Chemical History", "Natural Dark Black (Virgin hair, 100% dye and bleach free)", 410),
        ("Packaging & Cut Date", "Braided & banded on both ends, cut on 10 July 2026", 485),
        ("Attach Photo of Donated Hair", "hair_sample_14inch.jpg  [Browse File]", 560),
    ]
    for label, val, y in dfields:
        draw.text((310, y), label, fill="#334155", font=f_bold)
        draw.rectangle([310, y + 25, 1020, y + 60], fill="#f8fafc", outline="#cbd5e1", width=1)
        draw.text((325, y + 36), val, fill="#0f172a", font=f_reg)

    draw.rectangle([310, 670, 520, 715], fill="#10b981")
    draw.text((350, 684), "Submit Donation", fill="white", font=f_bold)
    img.save(os.path.join(SCREEN_DIR, "06b_donor_add_donation.png"))

    # 7b. PATIENT - MY REQUESTS
    img, draw = base_frame("Patient - My Hair Requests", "http://127.0.0.1:8000/patient/dashboard.php?tab=requests", role="Fatima Beevi")
    draw_sidebar(draw, "My Requests", ["Dashboard", "Browse Hair", "My Requests", "Medical Documents", "Support"])
    draw.text((280, 160), "My Hair Requests & Custom Wig Status", fill="#0f172a", font=f_title)
    draw.text((280, 190), "Monitor real-time progress of your matched hair and wig dispatch", fill="#64748b", font=f_reg)

    draw.rectangle([280, 230, 1370, 550], fill="white", outline="#cbd5e1", width=1)
    draw.rectangle([280, 230, 1370, 275], fill="#f1f5f9")
    draw.text((300, 248), "Request ID", fill="#0f172a", font=f_bold)
    draw.text((430, 248), "Allocated Hair Asset", fill="#0f172a", font=f_bold)
    draw.text((700, 248), "Assigned Verifying NGO", fill="#0f172a", font=f_bold)
    draw.text((1020, 248), "Status", fill="#0f172a", font=f_bold)
    draw.text((1200, 248), "Delivery Timeline", fill="#0f172a", font=f_bold)

    preqs = [
        ("#REQ-401", "14.5\" Straight Black (#PST-12)", "Hope & Healing Cancer Foundation", "Approved", "#10b981", "Wig Crafting in Progress (ETA: 7 Days)", 300),
        ("#REQ-310", "12.0\" Synthetic Wig Care Kit", "Jeevani Welfare Society", "Delivered", "#0ea5e9", "Handed over on 14 Jan 2026", 370),
    ]
    for rid, asset, ngo, st, col, eta, y in preqs:
        draw.text((300, y), rid, fill="#334155", font=f_reg)
        draw.text((430, y), asset, fill="#334155", font=f_reg)
        draw.text((700, y), ngo, fill="#334155", font=f_reg)
        draw.text((1020, y), st, fill=col, font=f_bold)
        draw.text((1200, y), eta, fill="#1e293b", font=f_reg)
    img.save(os.path.join(SCREEN_DIR, "07b_patient_my_requests.png"))

    # 08. USER - COMPLAINT
    img, draw = base_frame("HairFidence - Support & Grievance", "http://127.0.0.1:8000/complaints.php", role="Rahul Varma (Donor)")
    draw.text((380, 160), "Lodge Grievance or Support Query", fill="#0f172a", font=f_title)
    draw.text((380, 190), "Direct escalation to the platform administrator", fill="#64748b", font=f_reg)

    draw.rectangle([380, 230, 1060, 680], fill="white", outline="#cbd5e1", width=1)
    draw.text((410, 260), "Subject", fill="#334155", font=f_bold)
    draw.rectangle([410, 285, 1030, 325], fill="#f8fafc", outline="#cbd5e1", width=1)
    draw.text((425, 297), "Courier receipt tracking update for Donation Post #HDP-102", fill="#0f172a", font=f_reg)

    draw.text((410, 350), "Description of Issue / Grievance", fill="#334155", font=f_bold)
    draw.rectangle([410, 375, 1030, 520], fill="#f8fafc", outline="#cbd5e1", width=1)
    draw.text((425, 390), "I dispatched my hair parcel via DTDC courier (Docket #KL-99821) on 10 July 2026.\nTracking states it was delivered to Hope Foundation Calicut office on 12 July 2026.\nKindly verify receipt and update status to 'Processing' in my dashboard.", fill="#334155", font=f_reg)

    draw.rectangle([410, 570, 630, 615], fill="#10b981")
    draw.text((450, 584), "Submit Ticket", fill="white", font=f_bold)
    img.save(os.path.join(SCREEN_DIR, "08_user_complaint.png"))

    # 09. USER - PROFILE
    img, draw = base_frame("HairFidence - User Profile", "http://127.0.0.1:8000/profile.php", role="Arshan Nizar K P")
    draw.text((400, 160), "My Account Profile", fill="#0f172a", font=f_title)
    draw.text((400, 190), "Manage personal details, registered address, and security", fill="#64748b", font=f_reg)

    draw.rectangle([400, 230, 1040, 720], fill="white", outline="#cbd5e1", width=1)
    pfields = [
        ("Full Name", "ARSHAN NIZAR K P", 260),
        ("Register Number", "AWH25MCA-2010", 335),
        ("Registered Email", "arshannizarkp@gmail.com", 410),
        ("Contact Phone", "+91 9495638657", 485),
        ("Residential Address", "KAPPATTATTIL(H.O) ,KINALUR(P.O) ,BALUSSERY ,KOZHIKODE ,673612", 560),
    ]
    for label, val, y in pfields:
        draw.text((430, y), label, fill="#334155", font=f_bold)
        draw.rectangle([430, y + 25, 1010, y + 60], fill="#f8fafc", outline="#cbd5e1", width=1)
        draw.text((445, y + 36), val, fill="#0f172a", font=f_reg)

    draw.rectangle([430, 645, 620, 685], fill="#0ea5e9")
    draw.text((465, 655), "Update Profile", fill="white", font=f_bold)
    img.save(os.path.join(SCREEN_DIR, "09_user_profile.png"))

    print("Additional screens generated successfully!")

if __name__ == "__main__":
    make_more()
