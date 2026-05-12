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
    expect(page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()
    expect(page.get_by_text("Maceta Colgante")).to_be_visible()
    expect(page.locator("data.text-gray-900").nth(0)).to_be_visible()  # Product price : 14.75
    expect(page.locator("data.text-gray-900").nth(1)).to_be_visible()  # Subtotal: 14.75
    expect(page.locator("data.text-gray-900").nth(2)).to_be_visible()  # VAT: 3.10
    expect(page.locator("data.text-gray-900").nth(3)).to_be_visible()  # Shipping: 5.00
    expect(page.locator("data.text-green-600")).to_be_visible()        # Total: 22.85


    page.get_by_role("link", name="Volver a la Tienda").click()
    expect(page).to_have_url("https://web-qa.dev.adalab.es/products")


def test_unsuccessful_purchase_with_invalid_data(page: Page):
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
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("1111 4242 4242 4242 4242")
    page.get_by_role("button", name="Completar Compra").click()
    expect(page.get_by_text("Tarjeta de crédito no válida.")).to_be_visible()
    page.get_by_role("link", name="Volver al Carrito").click()


def test_unsuccessful_purchase_with_empty_credit_card_field(page: Page):

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
    page.get_by_role("button", name="Completar Compra").click()
    expect(page).to_have_url("https://web-qa.dev.adalab.es/checkout")
 


   









