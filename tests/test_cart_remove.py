from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pages.product_filter import ProductFilterPage
from pages.products_page import ProductsPage

def test_cart_remove(page: Page): 
    products_page = ProductsPage(page)
    products_filter = ProductFilterPage(page)
    cart_page = CartPage(page)

    print("When the user vitits the products page Nuestros Productos | Vida Verde") 
    products_page.open_products_page()

    print("And filters by name Ficus") 
    products_filter.filter_by_name("ficus")

    print("And adds the product to the cart")
    products_filter.add_product("Ficus Lyrata")

    print("And clears the filter")    
    products_filter.clear_filter()

    print("And filters by name Tijeras")
    products_filter.filter_by_name("tijeras")

    print("And adds the product to the cart")
    products_filter.add_product("Tijeras de podar")

    print("When the user visits the cart page")
    cart_page.open_cart_page()

    print("When the user removes the product Ficus from the cart page")
    cart_page.remove_product("Ficus Lyrata")

    print("Then the user should not see the product Ficus")
    cart_page.verify_product_not_visible("Ficus Lyrata")

    print("Then the user should see the updated order summary")
    cart_page.verify_products_price("18.50 €")
    cart_page.verify_vat("3.88 €")
    cart_page.verify_shipping("5.00 €")
    cart_page.verify_total("27.38 €")

    
   