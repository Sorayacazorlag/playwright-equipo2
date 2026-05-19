from tabnanny import check

from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.confirmation_page import ConfirmationPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage


def test_successful_purchase_with_valid_data(page: Page): #Teresa

    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    confirmation_page = ConfirmationPage(page)

    print("Given user open products page")
    products_page.open_products_page()

    print ("When user filter by name maceta colgante")
    products_page.filter_by_name("maceta colgante")

    print ("then user add maceta colgante to the cart")
    products_page.add_product("Añadir Maceta Colgante")

    print ("and the user visit the cart page")
    cart_page.open_cart_page()

    print ("verify order sumary prices")
    cart_page.verify_one_product_price("14.75 €")
    cart_page.verify_vat("IVA (21%)3.10 €")
    cart_page.verify_shipping("5.00 €")
    cart_page.verify_total("22.85 €")
   
    print ("and proceed to payment")
    cart_page.procedd_to_payment()

    print ("and fill complete name")
    checkout_page.fill_complete_name("maria garcia")

    print ("and fill valid email user ")
    checkout_page.fill_email("test@gmail.com")
   
    print("and fill valid adress user")
    checkout_page.fill_adress("parmenides,5,Malaga")

    print ("add valid credit card number")
    checkout_page.fill_credit_card("4242 4242 4242 4242")

    print ("complete purchase")
    checkout_page.complete_payment()

    print("Verify confirmation summary")
    confirmation_page.verify_confirmation_message()

    print("verify products appears")
    confirmation_page.verify_product_name("Maceta Colgante")

    print("verify product price")
    confirmation_page.verify_product_price("Maceta Colgante14.75 €")
    
    print("verify product subototal")
    confirmation_page.verify_product_subtotal("14.75 €")

    print("verify IVA")
    confirmation_page.verify_IVA("3.10 €")
    
    print("verify shipping")
    confirmation_page.verify_shipping("5.00 €")

    print("verify total price")
    confirmation_page.verify_total("22.85 €")
    
    print("back to products page")
    confirmation_page.click_back_to_product()
    
    print ("verify products page")
    products_page.verify_products_url()


    # ---------------------
def  test_successful_purchase_with_invalid_data(page: Page): #Teresa

    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    confirmation_page = ConfirmationPage(page)


    
    print ("Given user visit checkout page")
    products_page.open_products_page()

    print ("the user choose maceta colgante")
    products_page.filter_by_name("Maceta Colgante")

    print ("the user add maceta colgante to the cart")
    products_page.add_product("Añadir Maceta Colgante al")
    
    print ("the user visit the cart page")
    cart_page.open_cart_page()

    print ("proceed to payment")
    cart_page.procedd_to_payment()

    print ("fill complete name")
    checkout_page.fill_complete_name("maria garcia")
    
    print ("fill valid email user ")
    checkout_page.fill_email("test@gmail.com")
    
    print("fill valid adress user")
    checkout_page.fill_adress("parmenides,5,Malaga")
    
    print ("fill invalid credit card number")
    checkout_page.fill_invalid_credit_card("1111 4242")
    
    print("complete purchase")
    checkout_page.complete_payment()
    
    print ("credit card information")
    checkout_page.credit_card_information()

    print ("verify credit card information")
    checkout_page.verify_creditcard_information("El número de tarjeta debe")
    
    print ("back to cart")
    cart_page.open_cart_page()
    

    # ---------------------

def test_purchase_attemp_with_empty_credit_card(page:Page): #Teresa

    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    confirmation_page = ConfirmationPage(page)


    print ("Given user visit products page")
    products_page.open_products_page()

    print ("the user fills the valid field")
    products_page.filter_by_name("maceta")
    
    print ("the user add maceta colgante to the cart")
    products_page.add_product("Añadir Maceta Colgante al")
    
    print ("the user visit the cart page")
    cart_page.open_cart_page()

    print ("proceed to payment")
    cart_page.procedd_to_payment()
    
    print ("fill complete name")
    checkout_page.fill_complete_name("maria garcia")

    print ("fill valid email user ")
    checkout_page.fill_email("test@gmail.com")

    print("fill valid adress user")
    checkout_page.fill_adress("parmenides,5,Malaga")
    
    print("complete purchase")
    checkout_page.complete_payment()

    print ("message that is mandatory a credit card number")
    checkout_page.verify_complete_creditcard("Número de Tarjeta de Crédito *")

    print ("back to cart")
    cart_page.open_cart_page()
    



