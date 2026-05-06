from playwright.sync_api import Page, expect

def test_menu_links(page: Page):     
     print("Given the user is on the page Inicio | Vida Verde")
     page.goto("https://web-qa.dev.adalab.es/")

     print("Then the user should see the title Vida Verde")
     expect(page.get_by_role("heading", name="Vida Verde")).to_be_visible()

     print("When the user clicks on About Us")
     page.get_by_role("link", name="Quiénes Somos").click()
     expect(page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()

     print("When the user clicks on Products")
     page.get_by_role("link", name="Productos").click()
     expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()

     print("When the user clicks on Contact")
     page.get_by_role("link", name="Contacto").click()
     expect(page.get_by_role("heading", name="Contáctanos")).to_be_visible()
     
 
