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
def test_successful_purchase_with_invalid_data(page: Page): #Teresa
    
    print ("Given user visit products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print ("the user fills the valid field")
    page.get_by_role("searchbox", name="Nombre").fill("maceta")

    print ("the user choose maceta colgante")
    page.get_by_role("heading", name="Maceta Colgante").click()
    
    print ("the user add maceta colgante to the cart")
    page.get_by_role("button", name="Añadir Maceta Colgante al").click()

    print ("the user visit the cart page")
    page.get_by_role("link", name="Finalizar Compra").click()

    print ("proceed to payment")
    page.get_by_role("link", name="Proceder al Pago").click()

    print ("fill complete name")
    page.get_by_role("textbox", name="Nombre Completo *").fill("maria garcia")

    print ("fill valid email user ")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    print("fill valid adress user")
    page.get_by_role("textbox", name="Dirección *").fill("parmenides,5,Malaga")

    print ("fill invalid credit card number")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("1111 4242")

    print("complete purchase")
    page.get_by_role("button", name="Completar Compra").click()
    expect(page.get_by_text("El número de tarjeta debe")).to_be_visible()

    print ("back to cart")
    page.get_by_role("link", name="Volver al Carrito").click()


    # ---------------------
def test_successful_purchase_with_invalid_data(page: Page): #Teresa
    
    print ("Given user visit products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print ("the user fills the valid field")
    page.get_by_role("searchbox", name="Nombre").fill("maceta")

    print ("the user choose maceta colgante")
    page.get_by_role("heading", name="Maceta Colgante").click()
    
    print ("the user add maceta colgante to the cart")
    page.get_by_role("button", name="Añadir Maceta Colgante al").click()

    print ("the user visit the cart page")
    page.get_by_role("link", name="Finalizar Compra").click()

    print ("proceed to payment")
    page.get_by_role("link", name="Proceder al Pago").click()

    print ("fill complete name")
    page.get_by_role("textbox", name="Nombre Completo *").fill("maria garcia")

    print ("fill valid email user ")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    print("fill valid adress user")
    page.get_by_role("textbox", name="Dirección *").fill("parmenides,5,Malaga")

    print ("fill invalid credit card number")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("1111 4242")

    print("complete purchase")
    page.get_by_role("button", name="Completar Compra").click()
    expect(page.get_by_text("El número de tarjeta debe")).to_be_visible()

    print ("back to cart")
    page.get_by_role("link", name="Volver al Carrito").click()


def test_purchase_attemp_with_empty_credit_card(page:Page): #Teresa

    print ("Given user visit products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print ("the user fills the valid field")
    page.get_by_role("searchbox", name="Nombre").fill("maceta")

    print ("the user choose maceta colgante")
    page.get_by_role("heading", name="Maceta Colgante").click()
    
    print ("the user add maceta colgante to the cart")
    page.get_by_role("button", name="Añadir Maceta Colgante al").click()

    print ("the user visit the cart page")
    page.get_by_role("link", name="Finalizar Compra").click()

    print ("proceed to payment")
    page.get_by_role("link", name="Proceder al Pago").click()

    print ("fill complete name")
    page.get_by_role("textbox", name="Nombre Completo *").fill("maria garcia")

    print ("fill valid email user ")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    print("fill valid adress user")
    page.get_by_role("textbox", name="Dirección *").fill("parmenides,5,Malaga")

    print("complete purchase")
    page.get_by_role("button", name="Completar Compra").click()
    expect(page.get_by_role("button", name="Completar Compra")).to_be_visible()

    print ("message that is mandatory a credit card number")
    expect(page.get_by_role("textbox", name="Número de Tarjeta de Crédito *")).to_be_visible()
    page.get_by_role("button", name="Completar Compra").click()




