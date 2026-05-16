from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"
        self.order_summary_label = page.get_by_label("Resumen del Pedido")
        self.price_items = [
            "14.75 €",
            "IVA (21%)3.10 €",
            "5.00 €",
            "22.85 €"
        ]

    def open_products_page(self):
        self.page.goto(self.url) 

    def fill_valid_field(self,name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name)

    def fill_complete_name(self, completename):
        self.page.get_by_role("textbox", name=completename).fill()
 
    def choose_maceta_colgante(self):
        self.page.get_by_role("heading", name="Maceta Colgante").click()  

    def add_maceta_colgante_to_the_cart(self):
        self.page.get_by_role("button", name="Añadir Maceta Colgante al").click()

    def visit_cart_page(self):
        expect(self.page.get_by_role("link", name="Finalizar Compra")).to_be_visible()
        self.page.get_by_role("link", name="Finalizar Compra").click()
        
    def verify_sumary_prices(self):
        self.order_summary_label.get_by_text(self.price_items[0]).click()
        for price in self.price_items[1:]:
            self.page.get_by_text(price).click()

    def proceed_payment(self):
        self.page.get_by_role("link", name="Proceder al Pago").click()

    def fill_valid_email(self,email):
        self.page.get_by_role("textbox", name= email).fill()

    def fill_valid_adress(self,adress):
        self.page.get_by_role("textbox", name=adress).fill()

    def add_valid_credit_card_number(self,creditcard):
        self.page.get_by_role("textbox", name=creditcard).fill()

    def complete_purchase(self):
        self.page.get_by_role("button", name="Completar Compra").click()  

    def see_message_successfull(self, congratulations):
        self.page.wait_for_selector(f"h1:has-text('{congratulations}')", state="visible", timeout=60000)
        expect(self.page.get_by_text(congratulations, exact=False)).to_be_visible()


    def back_products_page(self,backtoshopping):
        self.page.get_by_role("link", name= backtoshopping).click()
        