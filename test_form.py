import pytest
from playwright.sync_api import sync_playwright

def test_login_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # เปิดเว็บ test form สำเร็จรูป
        page.goto("https://practicetestautomation.com/practice-test-login/")

        # กรอก username
        page.locator("#username").fill("student")

        # กรอก password
        page.locator("#password").fill("Password123")

        # คลิกปุ่ม Submit
        page.locator("#submit").click()

        # รอหน้าโหลด
        page.wait_for_load_state("networkidle")

        # เช็คว่า login สำเร็จ
        assert "Congratulations" in page.content()
        print("Login สำเร็จ! ✓")

        page.wait_for_timeout(2000)
        browser.close()