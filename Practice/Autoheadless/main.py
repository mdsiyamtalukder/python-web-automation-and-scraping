from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    print("Processing....")
    page.goto("https://fedoraproject.org/")
    page.wait_for_timeout(3000)
    print(page.title())
    print("Done!")
    browser.close()
