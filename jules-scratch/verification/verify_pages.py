from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:3000")

    page.get_by_role("button", name="中獎頁面").click()
    page.wait_for_url("http://localhost:3000/winning")
    page.screenshot(path="jules-scratch/verification/winning.png")

    page.get_by_role("button", name="個人簡介").click()
    page.wait_for_url("http://localhost:3000/personal-introduction")
    page.screenshot(path="jules-scratch/verification/personal-introduction.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
