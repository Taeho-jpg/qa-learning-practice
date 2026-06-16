from playwright.sync_api import sync_playwright
import os

def test_login_with_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://practicetestautomation.com/practice-test-login/")

        # กรอก password ผิด
        page.locator("#username").fill("student")
        page.locator("#password").fill("wrongpassword")
        page.locator("#submit").click()
        page.wait_for_load_state("networkidle")

        # ถ่าย screenshot ทันที
        page.screenshot(path="screenshot_fail.png")
        print("ถ่าย screenshot แล้ว!")

        # เช็ค URL
        assert "logged-in-successfully" in page.url

        browser.close()