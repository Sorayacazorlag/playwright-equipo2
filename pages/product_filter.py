from playwright.sync_api import Page, expect

class ProductFilterPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"
        self.title = "Catálogo de Productos"


    def open_products_page(self):
        self.page.goto(self.url)

    def filter_by_name(self, name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name)
   
    def filter_by_category(self, category):   
        self.page.get_by_label("CategoríaTodas las categorí").select_option(category)   

    def filter_by_min_price(self, min_price):
        self.page.get_by_role("spinbutton", name="Precio mínimo").fill(min_price)   

    def filter_by_max_price(self, max_price):    
        self.page.get_by_role("spinbutton", name="Precio máximo").fill(max_price)   

    def expect_results_visible(self):
        expect(self.page.get_by_role("region", name="Catálogo de productos").get_by_role("list")).to_be_visible()
        




    def filter_by_valid_name_price_and_category_values(self):
        self.page.goto("https://web-qa.dev.adalab.es/products")
        self.page.get_by_role("searchbox", name="Nombre").fill("regadera")
        self.page.get_by_label("CategoríaTodas las categorí").select_option("Herramientas")
        self.page.get_by_role("spinbutton", name="Precio mínimo").fill("20")
        self.page.get_by_role("spinbutton", name="Precio máximo").fill("25")
        expect(self.page.get_by_role("region", name="Catálogo de productos").get_by_role("list")).to_be_visible()


    def filter_by_a_value_with_no_results(self):
        self.page.goto("https://web-qa.dev.adalab.es/products")
        self.page.get_by_role("searchbox", name="Nombre").fill("manzana")
        expect(self.page.get_by_text("No se encontraron productos")).to_be_visible()    
def Filter_by_a_value_with_no_results(self):
    self.page.goto("https://web-qa.dev.adalab.es/products")
    self.page.get_by_role("searchbox", name="Nombre").fill("manzana")
    expect(self.page.get_by_text("No se encontraron productos")).to_be_visible()