from playwright.sync_api import Page, expect

def test_submit_form_empty_required_message(page: Page):
    
    print("Given the user is on the contact page Contáctanos | Vida Verde")
    page.goto("https://web-qa.dev.adalab.es/contact")
    
    print("When they fill in the required name field")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Díaz")
    
    print("And they fill in the required email field")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    
    print("And they click on submit")
    page.get_by_role("button", name="Enviar Mensaje").click()
    
    print("Then they should see an error message: El mensaje es obligatorio")
    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()
