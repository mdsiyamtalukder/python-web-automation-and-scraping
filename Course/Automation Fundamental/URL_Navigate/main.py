from playwright.sync_api import sync_playwright
with sync_playwright() as p:
   browser = p.chromium.launch(headless=False)
   page=browser.new_page()

   print("processing....")

   #open learn with rabbil
   page.goto("https://rabbil.com/")
   page.wait_for_timeout(5000)
   print(page.title())

   #open github profile
   page.goto("https://github.com/mdsiyamtalukder")
   page.wait_for_timeout(5000)
   print(page.title())

   #open youtube
   page.goto("https://www.youtube.com/")
   page.wait_for_timeout(5000)
   print(page.title())

   #takes a reload 
   page.reload()
   page.wait_for_timeout(5000)

   #goes back to github
   page.go_back()
   page.wait_for_timeout(5000)
   print(page.title())

   #goes back to learn with rabbil
   page.go_back()
   page.wait_for_timeout(5000)
   print(page.title())

   #going to github again
   page.go_forward()
   page.wait_for_timeout(5000)
   print(page.title())

   #going to youtube again
   page.go_forward()
   page.wait_for_timeout(5000)
   print(page.title())

   browser.close()
   print("Ended Successfully!")






