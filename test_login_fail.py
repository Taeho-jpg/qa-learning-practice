from playwright.sync_api import sync_playwright

def test_login_wrong_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.locator("#username").fill("student")
        page.locator("#password").fill("wrongpassword")
        page.locator("#submit").click()
        page.wait_for_load_state("networkidle")

        # เช็ค URL ว่าต้องไปหน้า success
        # ทั้งที่ password ผิด → ควรได้ FAIL
        current_url = page.url
        print(f"URL ปัจจุบัน: {current_url}")
        assert "logged-in-successfully" in current_url

        browser.close()