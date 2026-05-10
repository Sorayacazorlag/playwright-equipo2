from playwright.sync_api import Page, expect
 


url = 'https://web-qa.dev.adalab.es/products'

def test_view_the_Our_Products_page(page: Page):
    print("When el usuario abre la página de productos 'Nuestros Productos | Vida Verde'")
    page.goto(url)

    print("Then el usuario ve la categoría del producto 'Plantas'")
    expect(page.get_by_text("Plantas").nth(2)).to_be_visible()

    print("And el usuario ve el nombre del producto 'Ficus Lyrata'")
    expect(page.get_by_role("heading", name="Ficus Lyrata")).to_be_visible()

    print("And el usuario ve el precio del producto '35.00€'")
    expect(page.get_by_text("35.00 €")).to_be_visible()
