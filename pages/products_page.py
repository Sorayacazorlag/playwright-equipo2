from playwright.sync_api import Page, expect

class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"
        self.title = "Catálogo de Productos"

    def open_products_page(self):
        self.page.goto(self.url)

    def verify_products_category(self, category):
        expect(self.page.get_by_text(category).nth(2)).to_be_visible()

    def verify_products_name(self, product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

    def verify_products_price(self, product_price):
        expect(self.page.get_by_text(product_price)).to_be_visible()

    def verify_products_title(self):
        expect(self.page.locator("h1")).to_contain_text(self.title)

    def verify_products_url(self):
        expect(self.page).to_have_url(self.url)
    
    def filter_by_name(self, name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name)

    def filter_by_category(self, category):   
        self.page.get_by_label("CategoríaTodas las categorías").select_option(category)   

    def filter_by_min_price(self, min_price):
        self.page.get_by_role("spinbutton", name="Precio mínimo").fill(min_price)   

    def filter_by_max_price(self, max_price):    
        self.page.get_by_role("spinbutton", name="Precio máximo").fill(max_price)  

    def expect_no_results_message(self):    
        expect(self.page.get_by_text("No se encontraron productos")).to_be_visible()

       
    def add_product(self, product):
        self.page.get_by_role("button", name=product).click()

    def clear_filter(self):
        self.page.get_by_role("button", name="Quitar filtros y ver todos").click()

    

