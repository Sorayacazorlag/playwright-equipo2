from playwright.sync_api import Page, expect

def test_complete_and_submit_the_contact_form_with_mandatory_fields(page: Page):
    print("Given la usuaria abre la página de contacto "Contáctanos | Vida Verde"")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When rellena el nombre")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print("And rellena el email")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    print("And rellena el mensaje")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    print("Then debe ver el mensaje "Mensaje enviado"")
    page.get_by_role("button", name="Enviar Mensaje").click()