from playwright.sync_api import Page, expect

def test_view_the_Our_Products_page(page: Page):
    print("When el usuario abre la página de productos 'Nuestros Productos | Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/products")
    print("Then el usuario ve la categoría del producto 'Plantas'")
    page.get_by_label("CategoríaTodas las categorí").select_option("Plantas")
    print("And el usuario ve el nombre del producto 'Ficus Lyrata'")
    page.get_by_role("heading", name="Ficus Lyrata").click()
    print("And el usuario ve el precio del producto '35.00 €'")
    page.get_by_text("35.00 €").click()