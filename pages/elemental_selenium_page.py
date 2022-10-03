from selenium.webdriver.common.by import By


class ElementalSelenium:
    # SELENIUM_URL = (By.CSS_SELECTOR, '[target="_blank"]')
    SELENIUM_URL = (By.LINK_TEXT, "Elemental Selenium")

    URL2 = "http://www.elementalselenium.com/"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.SELENIUM_URL)

    # def get_selenium_url(self):
    #     return self.browser.find_element(*self.SELENIUM_URL).