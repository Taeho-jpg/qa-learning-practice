def test_login_success(page_with_screenshot):
    page = page_with_screenshot
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()
    page.wait_for_load_state("networkidle")
    assert "logged-in-successfully" in page.url

def test_login_fail(page_with_screenshot):
    page = page_with_screenshot
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.locator("#username").fill("student")
    page.locator("#password").fill("wrongpassword")
    page.locator("#submit").click()
    page.wait_for_load_state("networkidle")
    assert "logged-in-successfully" in page.url