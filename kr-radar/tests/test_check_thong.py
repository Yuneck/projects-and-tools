import pytest
from playwright.async_api import async_playwright, expect

PRODUCT_URL = "https://korneliarataj.com/en/product/thong-dol-stroju-kapielowego-aqua-2025/"

@pytest.mark.asyncio
async def test_xl_and_xxl_are_disabled():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto(PRODUCT_URL, timeout=30000)

        xl = page.locator("li[data-value='xl']")
        xxl = page.locator("li[data-value='xxl']")
        s = page.locator("li[data-value='s']")
        


        # Ensure both exist
        await expect(xl).to_have_count(1)
        await expect(xxl).to_have_count(1)
        await expect(s).to_have_count(1)

        # Read class attribute
        xl_class = await xl.get_attribute("class")
        xxl_class = await xxl.get_attribute("class")
        s_class = await s.get_attribute("class")

        # Assert "disabled" is present
        assert "disabled" in xl_class, f"XL is available!"
        assert "disabled" in xxl_class, f"XXL is available!"
        #assert "disabled" in s_class, f"S is available!"

        await browser.close()
