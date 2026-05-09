from playwright.sync_api import Page, expect

def test_successful_purchase_with_valid_data(page: Page):
    print("given the users products page 'Products| Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("user name filter by 'maceta'")
    page.get_by_role("searchbox", name="Nombre").fill("maceta")

    print("click type of 'maceta colgante'")
    page.get_by_role("heading", name="Maceta Colgante").click()

    print("add to cart 'maceta colgante'")
    page.get_by_role("button", name="Añadir Maceta Colgante al").click()

    print("checkout purchase")
    page.get_by_role("link", name="Finalizar Compra").click()
    expect(page.get_by_text("Maceta Colgante")).to_be_visible()

    print("click on proceed to payment")
    page.get_by_role("link", name="Proceder al Pago").click()
    page.get_by_role("textbox", name="Nombre Completo *").fill("maria garcia")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    page.get_by_role("textbox", name="Dirección *").fill("calle parmenides, 5 Malaga")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("4242 4242 4242 4242")
    page.get_by_role("button", name="Completar Compra").click()

    # Verificar página de confirmación
    expect(page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()
    expect(page.get_by_text("Maceta Colgante")).to_be_visible()
    expect(page.locator("data.text-gray-900").nth(0)).to_be_visible()  # Product price : 14.75
    expect(page.locator("data.text-gray-900").nth(1)).to_be_visible()  # Subtotal: 14.75
    expect(page.locator("data.text-gray-900").nth(2)).to_be_visible()  # VAT: 3.10
    expect(page.locator("data.text-gray-900").nth(3)).to_be_visible()  # Shipping: 5.00
    expect(page.locator("data.text-green-600")).to_be_visible()        # Total: 22.85


    page.get_by_role("link", name="Volver a la Tienda").click()
    expect(page).to_have_url("https://web-qa.dev.adalab.es/products")




   









