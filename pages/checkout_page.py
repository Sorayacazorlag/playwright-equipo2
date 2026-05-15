from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def open_products_page(self):
        self.page.goto("https://web-qa.dev.adalab.es/products") 





