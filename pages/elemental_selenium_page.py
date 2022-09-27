class ElementalSelenium:

    URL = "http://www.elementalselenium.com/"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)