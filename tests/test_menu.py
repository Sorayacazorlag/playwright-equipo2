from playwright.sync_api import Page, expect
from pages.about_us_page import AboutUsPage
from pages.components.menu import Menu
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage

def test_menu_links(page: Page):     
     home_page = HomePage(page)
     menu = Menu(page)
     aboutus_page = AboutUsPage(page)
     products_page = ProductsPage(page)
     contact_page = ContactPage(page)

     print("Given the user is on the page Inicio | Vida Verde")
     home_page.open_home_page()

     print("Then the user should see the title Vida Verde")
     home_page.verify_home_page_title()

     print("When the user clicks on About Us")
     menu.visit_menu_about_us()

     print("Then the user should see the title Quiénes somos")
     aboutus_page.verify_about_us_title()

     print("And the URL should be Quiénes Somos | Vida Verde ")
     aboutus_page.verify_about_us_url()

     print("When the user clicks on Products")
     menu.visit_menu_products()

     print("Then the user should see the title Catálogo de Productos")
     products_page.verify_products_title()

     print("And the URL should be Nuestros Productos | Vida Verde")
     products_page.verify_products_url()

     print("When the user clicks on Contact")
     menu.visit_menu_contact()

     print("Then the user should see the title Contáctanos")
     contact_page.verify_contact_title()

     print("And the URL should be Contáctanos | Vida Verde")
     contact_page.verify_contact_url()