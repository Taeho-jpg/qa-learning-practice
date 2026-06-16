from playwright.sync_api import sync_playwright

def test_login_correct():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.locator("#username").fill("student")
        page.locator("#password").fill("Password123")
        page.locator("#submit").click()
        page.wait_for_load_state("networkidle")

        assert "Congratulations" in page.content()
        print("Login สำเร็จ! ✓")

        page.wait_for_timeout(2000)
        browser.close()