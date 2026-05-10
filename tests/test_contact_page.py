from playwright.sync_api import Page, expect
from pages.contact_page import ContactPage 

def test_complete_and_submit_the_contact_form_with_mandatory_fields(page: Page):

    contact_page = ContactPage(page)

    print("Given la usuaria abre la página de contacto 'Contáctanos | Vida Verde'")
    contact_page.open_contact_page()

    print("When rellena el nombre")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")

    print("And rellena el email")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    print("And rellena el mensaje")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")

    print("And pulsa el boton enviar")
    page.get_by_role("button", name="Enviar Mensaje").click()
    
    print("Then debe ver un mensaje de exito")
    expect(page.get_by_text("heading", name="¡Mensaje enviado con éxito!")).to_be_visible()
    


def test_form_with_required_name_field_left_empty(page: Page):

    contact_page = ContactPage(page)

    print("Given the users enters contact page 'Contact| Vida Verde'")
    contact_page.open_contact_page()

    print ("fills required email")
    contact_page.fill_contact_email("test@gmail.com")
   
    print ("fills required message with")
    contact_page.fill_contact_message("test message")

    print ("clicks send")
    contact_page.press_send_contact()

    print ("user should see the error message 'name is mandatory'")
    contact_page.verify_message_form("name is mandatory")


def test_form_with_required_email_field_left_empty(page: Page):

    contact_page = ContactPage(page)

    print ("given the users contact page 'Contact| Vida Verde'")
    contact_page.open_contact_page()
    
    print ("fills in the required name")
    contact_page.fill_contact_name.fill("ana sanchez")

    print ("fills in the required message")
    contact_page.fill_contact_message.fill("test message")

    print("And they click on submit") 
    contact_page.press_send_contactclick("enviar mensaje")

    print ("they should see an error message")
    contact_page.verify_message_form("el nombre es obligatorio")
           

    
def test_submit_form_empty_required_message(page: Page):

    contact_page = ContactPage(page)
    
    print("Given the user is on the contact page: Contáctanos | Vida Verde")
    contact_page.open_contact_page()

    print("When they fill in the required name field")
    contact_page.fill_contact_name("ana sanchez")
    
    print("And they fill in the required email field")
    contact_page.fill_contact_email("test@gmail.com")
    
    print("And they click on submit")
    contact_page.press_send_contact("enviar mensaje")
    
    print("Then they should see an error message: El mensaje es obligatorio")
    contact_page.verify_message_form("el mensaje es obligatorio")
    




