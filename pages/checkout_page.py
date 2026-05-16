from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"



    def open_products_page(self):
        self.page.goto(self.url) 
        





