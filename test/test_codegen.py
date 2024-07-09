v#type in console playwright codegen or playwright codegen XX where XX=URL
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.codegen
def test_example(page: Page) -> None:
    page.goto("https://es.wikipedia.org/wiki/Wikipedia:Portada")
    page.get_by_role("link", name="Bienvenidos").click()
    expect(page.locator("#firstHeading")).to_contain_text("Bienvenidos")