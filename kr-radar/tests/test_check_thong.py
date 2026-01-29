import pytest
from playwright.sync_api import sync_playwright, expect

PRODUCT_URL = "https://korneliarataj.com/en/product/thong-dol-stroju-kapielowego-aqua-2025/"


def test_xl_and_xxl_are_disabled():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(PRODUCT_URL, timeout=60000)

        xl = page.locator("li[data-value='xl']")
        xxl = page.locator("li[data-value='xxl']")
        s = page.locator("li[data-value='s']")
        print("Test started")
        

        if xl.count() == 1:
            xl_class = xl.get_attribute("class")
            assert "disabled" in xl_class, f"XL is available!"
            print("XL not available...")

        if xxl.count() == 1:
            xxl_class = xxl.get_attribute("class")
            assert "disabled" in xxl_class, f"XXL is available!"
            print("XXL not available...")

        if s.count() == 1:
            s_class = s.get_attribute("class")
            #assert "disabled" in s_class, f"S is available!"
            #print("S not available...")
        # Read class attribute


        browser.close()
