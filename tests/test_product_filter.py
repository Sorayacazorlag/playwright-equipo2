from playwright.sync_api import Page, expect

def test_product_filter(page: Page):
    page.goto("https://web-qa.dev.adalab.es/products")
    page.get_by_role("searchbox", name="Nombre").fill("regadera")
    page.get_by_label("CategoríaTodas las categorí").select_option("Herramientas")
    page.get_by_role("spinbutton", name="Precio mínimo").fill("20")
    page.get_by_role("spinbutton", name="Precio máximo").fill("25")
    expect(page.get_by_role("region", name="Catálogo de productos").get_by_role("list")).to_be_visible()
    