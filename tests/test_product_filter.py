from playwright.sync_api import Page
from pages.products_page import ProductsPage

def test_filter_by_valid_name_price_and_category_values(page: Page):
    products_page = ProductsPage(page)

    print("Given: La usuaria abre la página de productos | Vida Verde")
    products_page.open_products_page()

    print("When: La usuaria filtra por nombre 'Regadera'")
    products_page.filter_by_name("Regadera") 

    print("And filtra por categoría 'Herramientas'")  
    products_page.filter_by_category("Herramientas")

    print("And filtra por precio mínimo '20'")
    products_page.filter_by_min_price("20")

    print("And filtrar por precio máximo '25'")
    products_page.filter_by_max_price("25")
  
    print("Then debe ver el producto 'Regadera Metálica'")
    products_page.verify_products_name("Regadera Metálica")



def test_filter_by_a_value_with_no_results(page: Page):
    products_page = ProductsPage(page)

    print("Given la usuaria entra en la página de productos")
    products_page.open_products_page()

    print("When filtra por el nombre 'manzana'")
    products_page.filter_by_name("manzana")

    print("Then debería ver el mensaje 'No se encontraron productos'")
    products_page.expect_no_results_message()   