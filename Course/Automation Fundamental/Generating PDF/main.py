from playwright.sync_api import sync_playwright
with sync_playwright() as s:
    browser = s.chromium.launch(headless=False)
    page=browser.new_page()

    print("Starting....")
    page.goto("https://elearn.daffodilvarsity.edu.bd/",wait_until='load')
    page.wait_for_timeout(3000)
    print(page.title())

    #pdf
    page.pdf(path="page.pdf",format="A4",print_background=True)
    browser.close()
