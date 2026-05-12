
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

    def press_send_payment (self,text)
        self.page.get_by_role("link", name=text).click()

    def fill_complete_name (self,name)
        self.page.get_by_role("textbox", name="Nombre" *"").fill(name)

    def fill_email(self,email)
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def fill_adress(self,adress)
        self.page.get_by_role("textbox", name="direccion").fill(adress)

    def fill_credit_card(self, credit_card)
        self.page.get_by_role("textbox", name= "tarjeta credito").fill(credit_card)

    def press_place_older(self,text)
        self.page.get_by_role("button", name="Completar Compra").click(text)

       