from playwright.sync_api import Page, expect

def test_complete_and_submit_the_contact_form_with_mandatory_fields(page: Page):
    print("Given la usuaria abre la página de contacto 'Contáctanos | Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When rellena el nombre")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print("And rellena el email")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    print("And rellena el mensaje")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    print("Then debe ver el mensaje 'Mensaje enviado'")
    page.get_by_role("button", name="Enviar Mensaje").click()



def test_form_with_required_name_field_left_empty(page: Page):
    print("Given the users enters contact page 'Contact| Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/contact")

    print ("fills required email with 'test@gmail.com'")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
   
    print ("fills required message with 'test mesage'")
    page.get_by_role("textbox", name="Mensaje *").fill("test message")
    page.get_by_role("textbox", name="Nombre *").click()

    print ("clicks send")
    page.get_by_role("button", name="Enviar Mensaje").click()

    print ("user should see the error message 'name is mandatory'")
    expect(page.get_by_text("El nombre es obligatorio")).to_be_visible()


from playwright.sync_api import Page, expect

def test_form_with_required_email_field_left_empty(page: Page):

    print ("given the users contact page 'Contact| Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/contact")
    
    print ("fills in the required name with 'ANA SANCHEZ'")
    page.get_by_role("textbox", name="Nombre *").fill("ANA SANCHEZ")

    print ("fills in the required message with 'test message'")
    page.get_by_role("textbox", name="Mensaje *").fill("test message")

    print ("fills in the optional telefhone with a number")
    page.get_by_role("textbox", name="Teléfono (Opcional)").fill("682458569")
    
    page.get_by_role("button", name="Enviar Mensaje").click()
    expect(page.get_by_role("textbox", name="Email *")).to_be_visible()
    



    





