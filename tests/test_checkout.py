from playwright.sync_api import Page, expect


def test_successful_purchase_with_valid_data(page: Page): #Teresa

    print("Given user visit products page")
    checkout_page.open_products_page()

    print ("the user fills the valid field")
    page.get_by_role("searchbox", name="Nombre").fill("maceta")

    print ("the user choose maceta colgante")
    page.get_by_role("heading", name="Maceta Colgante").click()
    
    print ("the user add maceta colgante to the cart")
    page.get_by_role("button", name="Añadir Maceta Colgante al").click()

    print ("the user visit the cart page")
    page.get_by_role("link", name="Finalizar Compra").click()

    print ("verify order sumary prices")
    page.get_by_label("Resumen del Pedido").get_by_text("14.75 €").click()
    page.get_by_text("IVA (21%)3.10 €").click()
    page.get_by_text("5.00 €").click()
    page.get_by_text("22.85 €").click()

    print ("proceed to payment")
    page.get_by_role("link", name="Proceder al Pago").click()

    print ("fill complete name")
    page.get_by_role("textbox", name="Nombre Completo").fill("maria garcia")

    print ("fill valid email user ")
    page.get_by_role("textbox", name="Email").fill("test@gmail.com")

    print("fill valid adress user")
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




