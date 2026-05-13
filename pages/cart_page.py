from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/cart"
        self.summary = "Resumen del pedido"
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
        expect(self.page.locator("dt:text-is('Productos (1)') + dd data")).to_have_text(price)

    def verify_vat(self, vat):
        expect(self.page.locator("dt:text-is('IVA (21%)') + dd data")).to_have_text(vat)

    def verify_shipping(self, shipping):
        expect(self.page.locator("dt:text-is('Envío') + dd data")).to_have_text(shipping)

    def verify_total(self, total):
        expect(self.page.locator("dt:text-is('Total') + dd data")).to_have_text(total)

    def verify_order_summary(self):
        expect(self.page.locator("#cart-summary-title")).to_contain_text(self.summary)

    def empty_cart(self):
        self.page.get_by_role("button", name="Vaciar Carrito").click() 
    
    def empty_cart_message(self):
        expect(self.page.locator("#main-content")).to_contain_text(self.empty_cart_message)