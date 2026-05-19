
from playwright.sync_api import Page, expect

class CheckoutPage():

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/checkout"

    def open_chekcout_page(self):
        self.page.goto(self.url)

    def fill_complete_name(self,name):
       self.page.get_by_role("textbox", name="Nombre Completo").fill(name)

    def fill_email(self,email):
        self.page.get_by_role("textbox", name="Email").fill(email)

    def fill_adress(self,adress):
        self.page.get_by_role("textbox", name="Dirección").fill(adress)

    def fill_credit_card(self,creditcard):
        self.page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill(creditcard)

    def complete_payment(self):
        self.page.get_by_role("button", name="Completar Compra").click()

    def verify_total(self,total):
        expect(self.page.get_by_text(total)).to_be_visible()




