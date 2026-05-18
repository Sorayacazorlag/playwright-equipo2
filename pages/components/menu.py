from playwright.sync_api import Page, expect

class Menu:

    def __init__(self, page: Page):
        self.page = page
        self.menu_about_us = "Quiénes Somos"
        self.menu_products = "Productos"
        self.menu_contact = "Contacto"
        self.ancho = page.viewport_size['width']

    def visit_menu_about_us(self):
        if self.ancho > 1024:
            self.page.get_by_role("link", name=self.menu_about_us).click()
        else:
            self.page.get_by_role("button", name="Abrir menú principal").click()
            self.page.get_by_role("menuitem", name=self.menu_about_us).click()

    def visit_menu_products(self):        
        if self.ancho > 1024:
            self.page.get_by_role("link", name=self.menu_products).click()
        else:
            self.page.get_by_role("button", name="Abrir menú principal").click()
            self.page.get_by_role("menuitem", name=self.menu_products).click()


    def visit_menu_contact(self):        
        if self.ancho > 1024:
            self.page.get_by_role("link", name=self.menu_contact).click()
        else:
            self.page.get_by_role("button", name="Abrir menú principal").click()
            self.page.get_by_role("menuitem", name=self.menu_contact).click()
        


    

        