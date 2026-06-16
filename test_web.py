import pytest
from playwright.sync_api import sync_playwright

def test_wikipedia_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # เปิด Wikipedia
        page.goto("https://www.wikipedia.org")
        
        # พิมพ์ค้นหา
        page.locator('input[name="search"]').fill("Playwright automation")
        
        # กด Enter
        page.keyboard.press("Enter")
        
        # รอโหลด
        page.wait_for_load_state("networkidle")
        
        # เช็ค title หน้าที่เปิดมา
        print(f"Page title: {page.title()}")
        assert "Playwright" in page.title()
        
        page.wait_for_timeout(2000)
        browser.close()