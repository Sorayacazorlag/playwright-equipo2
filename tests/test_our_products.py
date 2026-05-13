from playwright.sync_api import Page
from pages.products_page import ProductsPage


def test_products_page(page: Page):
    products_page = ProductsPage(page);

    print("When the user visits to the products page")
    products_page.open_products_page()

    
    print("Then the user should see the product category 'Plants'")
    products_page.verify_products_category("Plantas")
    

    print("And the user should see the product name 'Ficus Lyrata'")
    products_page.verify_products_name("Ficus Lyrata")


    print("And the user should see the product price '35.00€")
    products_page.verify_products_price("35.00 €")