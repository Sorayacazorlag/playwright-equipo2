from playwright.sync_api import Page
from pages.products_page import ProductsPage

def Filter_by_valid_name_price_and_category_values(page: Page):
     productos_page= ProductsPage(page)

    print("Given: La usuaria abre la página de productos | Vida Verde")
    productos_page.open_products_page()

    print("When: La usuaria filtra por nombre 'Regadera'")
    productos_page.filtrar_por_nombre("Regadera") 

    print("And filtra por categoría 'Herramientas'")  
    productos_page.filtrar_por_categoria("Herramientas")

    print("And filtra por precio mínimo '20'")
    productos_page.filtrar_por_precio_minimo("20")

    print("And filtrar por precio máximo '25'")
    productos_page.filtrar_por_precio_maximo("25")
  
    print("Then debe ver el producto 'Regadera Metálica'")
    productos_page.verify_products_name("Regadera Metálica")



def Filter_by_a_value_with_no_results(page: Page):
    productos_page = ProductsPage(page)

    print("Given la usuaria entra en la página de productos")
    productos_page.open_products_page()

    print("When filtra por el nombre 'manzana'")
    productos_page.filtrar_por_nombre("manzana")

    print("Then debería ver el mensaje 'No se encontraron productos'")
    productos_page.verificar_mensaje_no_resultados()   