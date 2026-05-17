from playwright.sync_api import Page, expect

class CheckoutPage():

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"


    def open_products_page(self):
        self.page.goto(self.url)

    def fill_valid_name(self,name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name)

        