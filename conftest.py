import pytest
import os

@pytest.fixture
def page_with_screenshot(request):
    from playwright.sync_api import sync_playwright
    
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    yield page  # ส่ง page ให้ test ใช้งาน
    
    # หลัง test จบ เช็คว่า FAIL มั้ย
    if request.node.rep_call.failed:
        # สร้างโฟลเดอร์ screenshots ถ้ายังไม่มี
        os.makedirs("screenshots", exist_ok=True)
        # ถ่าย screenshot ชื่อตาม test ที่ FAIL
        filename = f"screenshots/{request.node.name}.png"
        page.screenshot(path=filename)
        print(f"\n📸 Screenshot saved: {filename}")
    
    browser.close()
    playwright.stop()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)