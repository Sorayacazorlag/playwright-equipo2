from playwright.sync_api import Page, expect
import re
def test_successful_purchase_with_valid_data(page: Page):
    print("given the users products page 'Products| Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/products")

    print ("user name filter by 'maceta'")
    page.get_by_role("searchbox", name="Nombre").fill("maceta")

    print ("click type of 'maceta colgante'" )
    page.get_by_role("heading", name="Maceta Colgante").click()

    print ("add to cart 'maceta colgante'")
    page.get_by_role("button", name="Añadir Maceta Colgante al").click()
    # Espera a que el resumen sea visible antes de verificar precios
    page.wait_for_selector("text=Resumen del Pedido")

    expect(page.get_by_text("14.75", exact=False)).to_be_visible()
    expect(page.get_by_text("3.10", exact=False)).to_be_visible()
    expect(page.get_by_text("5", exact=False)).to_be_visible()
    expect(page.get_by_text("22.85", exact=False)).to_be_visible()

    print ("checkout purchase")
    page.get_by_role("link", name="Finalizar Compra").click()

    print("click on proceed to payment")
    page.get_by_role("link", name="Proceder al Pago").click()
    page.get_by_role("textbox", name="Nombre Completo *").fill("maria garcia")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    page.get_by_role("textbox", name="Dirección *").fill("calle parmenides,5 Malaga")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("4242 4242 4242 4242")
    page.get_by_role("button", name="Completar Compra").click()

    expect(page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()
    expect(page.get_by_text("14.75")).to_be_visible()
    expect(page.get_by_text("3.10")).to_be_visible()
    expect(page.get_by_text("5")).to_be_visible()
    expect(page.get_by_text("22.85")).to_be_visible()
    page.get_by_role("link", name="Volver a la Tienda").click()
    expect(page).to_have_url("https://web-qa.dev.adalab.es/products")







   









