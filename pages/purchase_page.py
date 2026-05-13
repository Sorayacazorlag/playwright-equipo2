
from playwright.sync_api import Page, expect

class PurchasePage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"
        self.title = "Catálogo de productos"

    def open_purchase_page(self):
        self.page.goto(self.url)

    def filter_product_name(self, name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name)

    def type_of_product(self):
         self.page.get_by_role("heading", name="Maceta Colgante").click()

    def add_to_cart(self,text):
        self.page.get_by_role("button", name=text).click()

    def press_send_checkout_purchase(self,text):
        self.page.get_by_role("link", name=text).click()

    def checkout_purchase(self,name):
        expect(self.page.get_by_text(name)).to_be_visible()

    def press_send_payment (self,text):
        self.page.get_by_role("link", name=text).click()

    def fill_complete_name (self,name):
        self.page.get_by_role("textbox", name="Nombre" *"").fill(name)

    def fill_email(self,email):
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def fill_adress(self,adress):
        self.page.get_by_role("textbox", name="direccion").fill(adress)

    def fill_credit_card(self, credit_card):
        self.page.get_by_role("textbox", name= "tarjeta credito").fill(credit_card)

    def press_place_older(self,text):
        self.page.get_by_role("button", name="Completar Compra").click(text)

    def verify_message_form(self,text):
        expect(self.page.get_by_role("heading", name= text)).to_be_visible()  

    def verify_see_message(self,name):
        expect(self.page.get_by_text(name)).to_be_visible()

    def verify_product_price(self, price):
        expect(self.page.locator("data.text-gray-900").nth(0)).to_have_text(price)

    def verify_subtotal(self, subtotal):
        expect(self.page.locator("data.text-gray-900").nth(1)).to_have_text(subtotal)

    def verify_vat(self, vat):
        expect(self.page.locator("data.text-gray-900").nth(2)).to_have_text(vat)

    def verify_shipping(self, shipping):
        expect(self.page.locator("data.text-gray-900").nth(3)).to_have_text(shipping)

    def verify_total(self, total):
        expect(self.page.locator("data.text-green-600")).to_have_text(total)

    def back_shopping(self,text):
        self.page.get_by_role("link", name=text).click()
   
    def verify_open_website(self,url):
        expect(self.page).to_have_url(url)

def test_unsuccessful_purchase_with_invalid_credit_card(page: Page):
   
   from playwright.sync_api import Page, expect

   class PurchasePage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"
        self.title = "Catálogo de productos"

    def open_purchase_page(self):
        self.page.goto(self.url)
        
    def filter_product_name(self,name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name) 

    def type_of_product(self,text):
      self.page.get_by_role("heading", name= text).click()

    def add_to_cart(self,text):
        self.page.get_by_role("button", name=text).click()

    def checkout_purchase(self,name):
        expect(self.page.get_by_text(name)).to_be_visible()

    def press_send_payment (self,text):
        self.page.get_by_role("link", name=text).click()

    def fill_complete_name (self,name):
        self.page.get_by_role("textbox", name="Nombre" *"").fill(name)

    def fill_email(self,email):
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def fill_adress(self,adress):
        self.page.get_by_role("textbox", name="direccion").fill(adress)

    def fill_credit_card(self, credit_card):
        self.page.get_by_role("textbox", name= "tarjeta credito").fill(credit_card)

    def verify_see_message(self,name):
        expect(self.page.get_by_text(name)).to_be_visible()


def test_unsuccessful_purchase_with_empty_credit_card_field(page: Page):
     
   from playwright.sync_api import Page, expect

   class PurchasePage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"
        self.title = "Catálogo de productos"


    def open_purchase_page(self):
        self.page.goto(self.url)

    def filter_product_name(self,name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name) 

    def type_of_product(self,text):
      self.page.get_by_role("heading", name= text).click()

    def add_to_cart(self,text):
        self.page.get_by_role("button", name=text).click()

    def checkout_purchase(self,name):
        expect(self.page.get_by_text(name)).to_be_visible()

    def press_send_payment (self,text):
        self.page.get_by_role("link", name=text).click()

    def fill_complete_name (self,name):
        self.page.get_by_role("textbox", name="Nombre" *"").fill(name)

    def fill_email(self,email):
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def fill_adress(self,adress):
        self.page.get_by_role("textbox", name="direccion").fill(adress)

    def verify_see_message(self,name):
        expect(self.page.get_by_text(name)).to_be_visible()
   
    def back_shopping(self):
        self.page.get_by_role("link", name=self.title).click()
   