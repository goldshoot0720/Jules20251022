from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    page.goto("http://localhost:3000/food")
    page.screenshot(path="jules-scratch/verification/food-page.png")

    page.goto("http://localhost:3000/subscription")
    page.screenshot(path="jules-scratch/verification/subscription-page.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
