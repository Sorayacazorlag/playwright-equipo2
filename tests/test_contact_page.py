from playwright.sync_api import Page, expect

def test_complete_and_submit_the_contact_form_with_mandatory_fields(page: Page):
    print("Given la usuaria abre la página de contacto 'Contáctanos | Vida Verde'")
    
    print("When rellena el nombre")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print("And rellena el email")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    print("And rellena el mensaje")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    print("Then debe ver el mensaje 'Mensaje enviado'")
    page.get_by_role("button", name="Enviar Mensaje").click()

    from playwright.sync_api import Page, expect


def test_submit_form_with_required_name_field_left_empty(page: Page):
    print("Given the users enters contact page 'Contact| Vida Verde ")
    page.goto("https://web-qa.dev.adalab.es/contact")

    print ("fills required email with 'test@gmail.com'")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
   
    print ("fills required message with 'test mesage'")
    page.get_by_role("textbox", name="Mensaje *").fill("test message")
    page.get_by_role("textbox", name="Nombre *").click()
    page.get_by_role("textbox", name="Nombre *").click()

    print ("clicks send")
    page.get_by_role("button", name="Enviar Mensaje").click()
    
    print ("user should see the error message 'message is mandatory'")
    expect(page.get_by_text("El nombre es obligatorio")).to_be_visible()





