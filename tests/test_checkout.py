from playwright.sync_api import Page, expect
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_successful_purchase_with_valid_data(page: Page): #Teresa

    checkout_page = CheckoutPage(page)

    print("Given user open products page")
    checkout_page.open_products_page()

    print ("When user filter by category")
    checkout_page.filter_by_category("maceta colgante")
    
    print ("then user add maceta colgante to the cart")
    checkout_page.add_maceta_colgante_to_cart()

    print ("and the user visit the cart page")
    checkout_page.visit_cart_page()
    
    print ("verify order sumary prices")
    checkout_page.verify_checkout_price("14.75 €")
    checkout_page.verify_at_amount("IVA (21%)3.10 €")
    checkout_page.verify_shipping_cost("5.00 €")
    checkout_page.verify_total_amount("22.85 €")

    print ("and proceed to payment")
    checkout_page.proceed_payment()


    print ("and fill complete name")
    page.get_by_role("textbox", name="Nombre Completo").fill("maria garcia")

    print ("and fill valid email user ")
    page.get_by_role("textbox", name="Email").fill("test@gmail.com")

    print("and fill valid adress user")
    page.get_by_role("textbox", name="Dirección").fill("parmenides,5,Malaga")

    print ("add valid credit card number")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("4242 4242 4242 4242")

    print ("complete purchse")
    page.get_by_role("button", name="Completar Compra").click()
    expect(page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()

    print("back to products page")
    page.get_by_role("link", name="Volver a la Tienda").click()

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




