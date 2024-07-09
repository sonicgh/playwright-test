import re
from playwright.sync_api import Page, expect, sync_playwright

def test_has_tittle(page: Page):
    #This normally will run in headless mode, but in pytest.ini file is set to headed
    page.goto("https://playwright.dev/python/")

    #Expect title contains substring.
    expect(page).to_have_title(re.compile("Playwright"))