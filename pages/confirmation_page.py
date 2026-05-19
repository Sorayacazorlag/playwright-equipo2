from playwright.sync_api import Page, expect

class ConfirmationPage():

    def __init__(self, page: Page):
        self.page = page
        

    def verify_confirmation_message(self):
      expect(self.page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()   
    
    def verify_product_name(self,name):
       expect(self.page.get_by_text(name)).to_be_visible()

    def verify_product_price(self,price):
       expect(self.page.get_by_role("listitem").filter(has_text= price).locator("data")).to_be_visible()

    def verify_product_subtotal(self,subtotal):
       expect(self.page.get_by_role("definition").filter(has_text=subtotal).locator("data")).to_be_visible()

    def verify_IVA(self,iva):
       expect(self.page.get_by_text(iva)).to_be_visible()
       
    def verify_shipping(self,shipping):
       expect(self.page.get_by_text(shipping)).to_be_visible()

    def verify_total(self,total):
       expect(self.page.get_by_text(total)).to_be_visible()

    def click_back_to_product(self):
       self.page.get_by_role("link", name="Volver a la Tienda").click()