from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_products_cart_view_summary_empty_cart(page: Page):

    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    
    print("When the user visits the page: Nuestros Productos | Vida Verde")
    products_page.open_products_page() 

    print(' And filters by name "Sansevieria" ')
    products_page.filter_by_name("Sansevieria") 
    
    print("And adds the product to the cart")
    products_page.add_product()
    
    print("And clears the filter")
    products_page.clear_filter()
    
    print('And filters by name "maceta de barro"')
    products_page.filter_by_name("Maceta de barro")

    print("And adds the product to the cart")
    products_page.add_product()

    print("And visits the shopping cart")
    cart_page.open_cart_page()

    print('Then they should see the name "Sansevieria"')
    cart_page.verify_product_name("Sansevieria")

    print('And its category "Plantas"')
    cart_page.verify_product_category("Plantas")

    print('And its price "22.00€"')
    cart_page.verify_products_price("22.00 €")

    print('And they should see the product "Maceta de Barro Grande"')
    cart_page.verify_product_name("Maceta de Barro Grande")

    print('And its category "Macetas"')
    cart_page.verify_product_category("Macetas")

    print('And its price "10.50€"')
    cart_page.verify_products_price("10.50 €")

    print("And they should see the order summary with the following details:")
    cart_page.verify_order_summary("Resumen del Pedido")
   
    print('Subtotal, the sum of both products "32.50€"')
    cart_page.verify_products_price("Productos (2)32.50 €")
    
    print('Including 21% VAT "6.83€"')
    cart_page.verify_vat("IVA (21%)6.83 €")
    
    print('And they should see the shipping total "5€"')
    cart_page.verify_shipping("Envío5.00 €")
    
    print('And they should see the total "44.33€"')
    cart_page.verify_total("Total44.33 €")
    
    print("When they click on empty cart")
    cart_page.empty_cart()
    
    print('Then they should see the message "Tu carrito está vacío"')
    cart_page.empty_cart_message("Tu carrito está vacío")

    