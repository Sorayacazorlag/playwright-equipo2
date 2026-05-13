from playwright.sync_api import Page, expect
from pages.purchase_page import PurchasePage


def test_successful_purchase_with_valid_data(page: Page):


    purchase_page = PurchasePage(page)


    print("given the users products page 'Products| Vida Verde'")
    purchase_page.open_purchase_page()

    print("user name filter by 'maceta'")
    purchase_page.filter_product_name.fill("maceta")

    print("click type of 'maceta colgante'")
    purchase_page.type_of_product.click("maceta colgante")

    print("add to cart 'maceta colgante'")
    purchase_page.add_to_cart.click("añadir maceta colgante al carrito")
    
    print("checkout purchase")
    purchase_page.press_send_checkout_purchase.click("finalizar compra")
    purchase_page.checkout_purchase.click("maceta colgante")

    print("click on proceed to payment")
    purchase_page.press_send_payment.click("proceder al pago")
    purchase_page.fill_complete_name.fill("maria garcia")
    purchase_page.fill_email.fill("test@gmail.com")
    purchase_page.fill_adress("calle parmenides,5 Malaga")
    purchase_page.fill_credit_card("4242 4242 4242 4242")
    purchase_page.press_place_older.click("completar compra")    


    # Verificar página de confirmación

    purchase_page.verify_message_form("¡Compra realizada con éxito!")
    purchase_page.verify_see_message("maceta colgante")
    purchase_page.verify_product_price("14.75") # Product price : 14.75
    purchase_page.verify_subtotal("14.75")      # Subtotal: 14.75
    purchase_page.verify_vat("3.10")            # VAT: 3.10
    purchase_page.verify_shipping("5.00")       # Shipping: 5.00
    purchase_page.verify_total("22.85")         # Total: 22.85

    
    purchase_page.click("volver a la tienda")
    purchase_page.verify_open_website("https://web-qa.dev.adalab.es/products")
    

def test_unsuccessful_purchase_with_invalid_data(page: Page):

     

    purchase_page = PurchasePage(page)

    print("given the users products page 'Products| Vida Verde'")
    purchase_page.open_purchase_page("https://web-qa.dev.adalab.es/products")

    print("user name filter by 'maceta'")
    purchase_page.filter_product_name("maceta")

    print("click type of 'maceta colgante'")
    purchase_page.type_of_product.click("maceta colgante")

    print("add to cart 'maceta colgante'")
    purchase_page.add_to_cart.click("maceta colgante")

    print("checkout purchase")
    purchase_page.press_send_checkout_purchase.click("finalizar compra")
    purchase_page.checkout_purchase.click("maceta colgante")

    print("click on proceed to payment")
    purchase_page.press_send_payment.click("Proceder al Pago")
    purchase_page.fill_complete_name.click("maria garcia")
    purchase_page.fill_email.fill("test@gmail.com")
    purchase_page.fill_adress("calle parmenides,5 Malaga")
    purchase_page.fill_credit_card("4242 4242 4242 4242")
    purchase_page.press_place_older.click("completar compra")
    purchase_page.verify_see_message("tarjeta de credito invalida")
    purchase_page.back_shopping.click("volver al carrito")



    purchase_page = PurchasePage(page)
 
    print("given the users products page 'Products| Vida Verde'")
    purchase_page.open_purchase_page("https://web-qa.dev.adalab.es/products")
    
    print("user name filter by 'maceta'")
    purchase_page.filter_product_name("maceta")

    print("click type of 'maceta colgante'")
    purchase_page.type_of_product.click("maceta colgante")

    print("add to cart 'maceta colgante'")
    purchase_page.add_to_cart.click("maceta colgante")

    print("checkout purchase")
    purchase_page.press_send_checkout_purchase.click("finalizar compra")
    purchase_page.checkout_purchase.click("maceta colgante")

    print("click on proceed to payment")
    purchase_page.press_send_payment.click("Proceder al Pago")
    purchase_page.fill_complete_name.click("maria garcia")
    purchase_page.fill_email.fill("test@gmail.com")
    purchase_page.fill_adress("calle parmenides,5 Malaga")
    purchase_page.press_place_older.click("completar compra")
    purchase_page.verify_see_message("tarjeta de credito invalida")
    purchase_page.back_shopping.click("https://web-qa.dev.adalab.es/products")


   
 


   









