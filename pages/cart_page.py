from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/cart"
        self.empty_cart_message = "Tu carrito está vacío"
        
    def open_cart_page(self):
        self.page.goto(self.url)

    def remove_product(self, product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

        self.page.get_by_role("button", name=f"Eliminar {product_name} del").click()

    def verify_product_not_visible(self, product_name):
        expect(self.page.get_by_role("heading", name=product_name)).not_to_be_visible()

    def verify_product_name(self, product_name):
        expect(self.page.locator("#main-content")).to_contain_text(product_name)

    def verify_product_category(self, category):
        expect(self.page.locator("#main-content")).to_contain_text(category)

    def verify_products_price(self, price):
        expect(self.page.locator("dl")).to_contain_text(price)
    
    def verify_one_product_price(self, price):
        expect(self.page.locator("#main-content")).to_contain_text(price)

    def verify_vat(self, vat):
        expect(self.page.get_by_text(vat)).to_be_visible()

    def verify_shipping(self, shipping):
        expect(self.page.get_by_text(shipping)).to_be_visible()

    def verify_total(self, total):
        expect(self.page.get_by_text(total)).to_be_visible()

    def verify_order_summary(self, summary):
        expect(self.page.locator("#cart-summary-title")).to_contain_text(summary)

    def empty_cart(self):
        self.page.get_by_role("button", name="Vaciar Carrito").click() 
    
