from playwright.sync_api import Page, expect

class AboutUsPage():

    def __init__(self, page: Page):
        self.page = page
        self.title = "Quiénes Somos"
        self.url = "https://web-qa.dev.adalab.es/about"

    def verify_about_us_title(self):
        expect(self.page.get_by_role("heading", name=self.title)).to_be_visible()

    def verify_about_us_url(self):
        expect(self.page).to_have_url(self.url)