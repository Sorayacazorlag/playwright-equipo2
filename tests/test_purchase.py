from playwright.sync_api import Page, expect

def test_successful_purchase_with_valid_data(page: Page):
    print("given the users products page 'Products| Vida Verde'")
    page.goto("https://bootcampqa.com")
    
