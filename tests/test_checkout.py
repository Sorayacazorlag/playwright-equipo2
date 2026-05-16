from playwright.sync_api import Page,expect


def test_successful_purchase_with_valid_data(page: Page):
    print("Given user visit homepage")
    page.goto("https://web-qa.dev.adalab.es/products")

    print ("When user filters by the name")
    page.get_by_role("heading", name="Maceta Colgante").click()
    expect(page.get_by_role("heading", name="Maceta Colgante")).to_be_visible()

    print ("and visits the cart page")
    page.get_by_role("button", name="Añadir Maceta Colgante al").click()
    
    print ("send click to checkout")
    page.get_by_role("link", name="Proceder al Pago").click()

    print ("fills the valid field with  maria garcia")
    page.get_by_role("textbox", name="Nombre Completo *").fill("maria garcia")
    
    print ("fills the valid field with test@gmail.com")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    
    print ("fills the valid adrees with calle parmenides,5,Malaga")
    page.get_by_role("textbox", name="Dirección *").fill("calle parmenides,5, Malaga")

    print ("enter the valid card number")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("4242 4242 4242 4242")

    print ("clicks on complete purchase")

    # Espera a que el botón esté visible antes de hacer clic
    page.get_by_role("button", name="Completar Compra").wait_for(state="visible")

    # Ahora sí, clic seguro sin timeout
    page.get_by_role("button", name="Completar Compra").click()

    print ("see the message compra realizada con exito")
    expect(page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()

    print ("back to catalogo de productos")
    page.get_by_role("heading", name="Catalogo de productos").click()
    expect(page.get_by_role("heading", name="Catalogo de Productos")).to_be_visible()

