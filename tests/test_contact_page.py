from playwright.sync_api import Page, expect
from pages.contact_page import ContactPage

def test_complete_and_submit_the_contact_form_with_mandatory_fields(page: Page):

    contact_page = ContactPage(page)

    print("Given la usuaria abre la página de contacto 'Contáctanos | Vida Verde'")
    contact_page.open_contact_page()

    print("When rellena el nombre")
    contact_page.fill_contact_name("Marta Diaz")
    
    print("And rellena el email")
    contact_page.fill_contact_email("test@gmail.com")

    print("And rellena el mensaje")
    contact_page.fill_contact_message("test mensaje")

    print("And pulsa el boton enviar")
    contact_page.press_send_contact()

    print("Then debería ver un mensaje de éxito")
    contact_page.verify_message_form("¡Mensaje enviado con éxito!")


def test_form_with_required_name_field_left_empty(page: Page):
    contact_page = ContactPage(page)
    print("Given the users enters contact page 'Contact| Vida Verde'")
    contact_page.open_contact_page()

    print ("fills required email with 'test@gmail.com'")
    contact_page.fill_contact_email("test@gmail.com")
   
    print ("fills required message with 'test mesage'")
    contact_page.fill_contact_message("test mensaje")

    print ("clicks send")
    contact_page.press_send_contact()

    print ("user should see the error message 'name is mandatory'")
    contact_page.verify_message_form("El nombre es obligatorio")
  

def test_form_with_required_email_field_left_empty(page: Page):

    print ("given the users contact page 'Contact| Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/contact")
    
    print ("fills in the required name with 'ANA SANCHEZ'")
    page.get_by_role("textbox", name="Nombre *").fill("ANA SANCHEZ")

    print ("fills in the required message with 'test message'")
    page.get_by_role("textbox", name="Mensaje *").fill("test message")

    print ("fills in the optional telefhone with a number")
    page.get_by_role("textbox", name="Teléfono (Opcional)").fill("682458569")
    
    print("Press send form button")
    page.get_by_role("button", name="Enviar Mensaje").click()
    page.pause()
    
    print("Then an error message is displayed")
    expect(page.get_by_text("El email es obligatorio")).to_be_visible()
    
   
def test_submit_form_empty_required_message(page: Page):
    
    print("Given the user is on the contact page: Contáctanos | Vida Verde")
    page.goto("https://web-qa.dev.adalab.es/contact")
    
    print("When they fill in the required name field")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Díaz")
    
    print("And they fill in the required email field")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    
    print("And they click on submit")
    page.get_by_role("button", name="Enviar Mensaje").click()
    
    print("Then they should see an error message: El mensaje es obligatorio")
    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()
    

def test_form_invalid_required_email(page: Page):
    
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
    expect(page.get_by_text("El formato del email no es válido")).to_be_visible()