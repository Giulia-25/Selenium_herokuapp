from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls:
    TITLE_PAGE_TEXT = (By.CSS_SELECTOR, "h4")
    REMOVE_ADD_BUTTON = (By.CSS_SELECTOR, '[onclick="swapCheckbox()"]')
    CHECKBOX = (By.ID, "checkbox")
    TEXT_INPUT = (By.CSS_SELECTOR, '[type="text"]')
    ENABLE_DISABLE_BUTTON = (By.CSS_SELECTOR, '[onclick="swapInput()"]')

    URL = 'https://the-internet.herokuapp.com/dynamic_controls'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_remove_add_button(self):
        self.browser.find_element(*self.REMOVE_ADD_BUTTON).click()

    def click_checkbox(self):
        self.browser.find_element(*self.CHECKBOX).click()

    def is_checkbox_displayed(self):
        return self.browser.find_element(*self.CHECKBOX).is_displayed

    def insert_text(self, text):
        text_input = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="text"]')))
        return text_input.send_keys(text)

    def is_text_displayed(self):
        return self.browser.find_element(*self.TEXT_INPUT).is_displayed()

    def click_enable_disable_button(self):
        self.browser.find_element(*self.ENABLE_DISABLE_BUTTON).click()

    def is_remove_add_button_displayed(self):
        return self.browser.find_element(*self.REMOVE_ADD_BUTTON).is_displayed()

    def is_enable_disable_button_displayed(self):
        return self.browser.find_element(*self.ENABLE_DISABLE_BUTTON).is_displayed()

