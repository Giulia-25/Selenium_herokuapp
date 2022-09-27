from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ContextMenu:

    CONTEXT_MENU = (By.ID, "hot-spot")

    URL = 'https://the-internet.herokuapp.com/context_menu'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_context_menu(self):
        action = ActionChains(self.browser)
        action.context_click(self.browser.find_element(*self.CONTEXT_MENU)).perform()