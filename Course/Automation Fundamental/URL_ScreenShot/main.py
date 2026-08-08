from playwright.sync_api import sync_playwright
with sync_playwright() as s:
    browser = s.chromium.launch(headless=False)
    page=browser.new_page()

    print("Starting....")
    page.goto("https://github.com/mdsiyamtalukder",wait_until='load')
    page.wait_for_timeout(3000)
    print(page.title())

    #screenshot
    page.screenshot(path="screenshot.png",full_page=True)

    browser.close()
