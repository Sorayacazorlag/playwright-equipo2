from playwright.sync_api import Page, expect

def submit_form_invalid_required_email(page: Page):
    
    print("Given the user is on the page: Contáctenos | Vida Verde")
    page.goto("https://web-qa.dev.adalab.es/contact")
    
    print("When they fill in the required name field")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Díaz")
    
    print("And they fill in the required email field with an invalid email")
    page.get_by_role("textbox", name="Email *").fill("email")
    
    print("And they fill in the required message field")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    
    print("And they click on submit")
    page.get_by_role("button", name="Enviar Mensaje").click()

    print("Then they should see an error message")
    expect(page.get_by_text("El formato del email no es vá")).to_be_visible()


