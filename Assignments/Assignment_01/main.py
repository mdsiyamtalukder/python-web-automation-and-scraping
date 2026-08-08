from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print("Chromium browser launched successfully!")
    browser.close()
    print("Browser closed successfully!")
