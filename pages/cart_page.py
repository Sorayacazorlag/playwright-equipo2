from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/cart"

    def open_cart_page(self):
        self.page.goto(self.url)

    def remove_product(self, product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

        self.page.get_by_role("button", name=f"Eliminar {product_name} del").click()

    def verify_product_not_visible(self, product_name):
        expect(self.page.get_by_role("heading", name=product_name)).not_to_be_visible()

    def verify_products_price(self, price):
        expect(self.page.locator("dt:text-is('Productos (1)') + dd data")).to_have_text(price)

    def verify_vat(self, vat):
        expect(self.page.locator("dt:text-is('IVA (21%)') + dd data")).to_have_text(vat)

    def verify_shipping(self, shipping):
        expect(self.page.locator("dt:text-is('Envío') + dd data")).to_have_text(shipping)

    def verify_total(self, total):
        expect(self.page.locator("dt:text-is('Total') + dd data")).to_have_text(total)