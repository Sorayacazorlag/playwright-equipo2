from playwright.sync_api import Page, expect

def test_add_products_cart_view_summary_empty_cart(page: Page):
    
    print("When the user visits the page: Nuestros Productos | Vida Verde")
    page.goto("https://web-qa.dev.adalab.es/products")
    
    print(' And filters by name "Sansevieria" ')
    page.get_by_role("searchbox", name="Nombre").fill("Sansevieria")
    
    print("And adds the product to the cart")
    page.get_by_role("button", name="Añadir Sansevieria al carrito").click()
    
    print("And clears the filter")
    page.get_by_role("button", name="Quitar filtros y ver todos").click()
    
    print('And filters by name "maceta de barro"')
    page.get_by_role("searchbox", name="Nombre").fill("maceta de barro")
    
    print("And adds the product to the cart")
    page.get_by_role("button", name="Añadir Maceta de Barro Grande").click()

    print("And visits the shopping cart")
    page.get_by_role("link", name="Carrito de compra").click()

    print('Then they should see the name "Sansevieria"')
    expect(page.locator("#main-content")).to_contain_text("Sansevieria")

    print('And its category "Plantas"')
    expect(page.locator("#main-content")).to_contain_text("Plantas")

    print('And its price "22.00€"')
    expect(page.locator("#main-content")).to_contain_text("22.00 €")

    print('And they should see the product "Maceta de Barro Grande"')
    expect(page.locator("#main-content")).to_contain_text("Maceta de Barro Grande")

    print('And its category "Macetas"')
    expect(page.locator("#main-content")).to_contain_text("Macetas")

    print('And its price "10.50€"')
    expect(page.locator("#main-content")).to_contain_text("10.50 €")

    print("And they should see the order summary with the following details:")
    expect(page.locator("#cart-summary-title")).to_contain_text("Resumen del Pedido")
   
    print('Subtotal, the sum of both products "32.50€"')
    expect(page.locator("dl")).to_contain_text("Productos (2)32.50 €")
    
    print('Including 21% VAT "6.83€"')
    expect(page.locator("dl")).to_contain_text("IVA (21%)6.83 €")
    
    print('And they should see the shipping total "5€"')
    expect(page.locator("dl")).to_contain_text("Envío5.00 €")
    
    print('And they should see the total "44.33€"')
    expect(page.locator("dl")).to_contain_text("Total44.33 €")
    
    print("When they click on empty cart")
    page.get_by_role("button", name="Vaciar Carrito").click()
    
    print('Then they should see the message "Tu carrito está vacío"')
    expect(page.locator("#main-content")).to_contain_text("Tu carrito está vacío")

    