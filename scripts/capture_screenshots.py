import os
import time
from playwright.sync_api import sync_playwright

SCREENSHOT_DIR = r"c:\Users\ARSHAN NIZAR\Downloads\MINI_PROJECT\screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def capture_all():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # 1. Capture Landing Page
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("http://127.0.0.1:8080/index.php")
        time.sleep(1)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "01_home.png"))
        print("Captured 01_home.png")

        # 2. Capture Login Page
        page.goto("http://127.0.0.1:8080/login.php")
        time.sleep(0.5)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "02_login.png"))
        print("Captured 02_login.png")

        # 3. Capture Register Page
        page.goto("http://127.0.0.1:8080/register.php")
        time.sleep(0.5)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "03_register.png"))
        print("Captured 03_register.png")

        # 4. Admin Session & Dashboard
        admin_context = browser.new_context(viewport={"width": 1440, "height": 900})
        admin_page = admin_context.new_page()
        admin_page.goto("http://127.0.0.1:8080/login.php")
        admin_page.fill("input[name='email']", "admin@hairfidence.com")
        admin_page.fill("input[name='password']", "adminpassword")
        admin_page.click("button[type='submit']")
        time.sleep(1.5)
        admin_page.screenshot(path=os.path.join(SCREENSHOT_DIR, "04_admin_dashboard.png"))
        print("Captured 04_admin_dashboard.png")

        # 5. NGO Session & Dashboard
        ngo_context = browser.new_context(viewport={"width": 1440, "height": 900})
        ngo_page = ngo_context.new_page()
        ngo_page.goto("http://127.0.0.1:8080/login.php")
        ngo_page.fill("input[name='email']", "hope@carengo.org")
        ngo_page.fill("input[name='password']", "password123")
        ngo_page.click("button[type='submit']")
        time.sleep(1.5)
        ngo_page.screenshot(path=os.path.join(SCREENSHOT_DIR, "05_ngo_dashboard.png"))
        print("Captured 05_ngo_dashboard.png")

        # 6. Donor Session & Dashboard
        donor_context = browser.new_context(viewport={"width": 1440, "height": 900})
        donor_page = donor_context.new_page()
        donor_page.goto("http://127.0.0.1:8080/login.php")
        donor_page.fill("input[name='email']", "ananya.s@gmail.com")
        donor_page.fill("input[name='password']", "password123")
        donor_page.click("button[type='submit']")
        time.sleep(1.5)
        donor_page.screenshot(path=os.path.join(SCREENSHOT_DIR, "06_donor_dashboard.png"))
        print("Captured 06_donor_dashboard.png")

        # 7. Patient Session & Dashboard
        patient_context = browser.new_context(viewport={"width": 1440, "height": 900})
        patient_page = patient_context.new_page()
        patient_page.goto("http://127.0.0.1:8080/login.php")
        patient_page.fill("input[name='email']", "fatima.b@gmail.com")
        patient_page.fill("input[name='password']", "password123")
        patient_page.click("button[type='submit']")
        time.sleep(1.5)
        patient_page.screenshot(path=os.path.join(SCREENSHOT_DIR, "07_patient_dashboard.png"))
        print("Captured 07_patient_dashboard.png")

        browser.close()
        print("All screenshots successfully captured!")

if __name__ == "__main__":
    capture_all()
