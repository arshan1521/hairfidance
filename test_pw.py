import traceback
import sys

with open("py_debug.log", "w", encoding="utf-8") as log:
    log.write("Starting test...\n")
    try:
        from playwright.sync_api import sync_playwright
        log.write("Playwright imported\n")
        with sync_playwright() as p:
            log.write("Playwright context manager entered\n")
            b = p.chromium.launch(headless=True)
            log.write(f"Browser launched: {b}\n")
            page = b.new_page()
            log.write("Page created\n")
            page.goto("http://127.0.0.1:8080/index.php")
            log.write(f"Page loaded: {page.title()}\n")
            page.screenshot(path="screenshots/test_home.png")
            log.write("Screenshot saved!\n")
            b.close()
        log.write("Done successfully!\n")
    except Exception as e:
        log.write(f"Exception: {e}\n")
        traceback.print_exc(file=log)
