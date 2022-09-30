from selenium.webdriver.common.by import By


class LoginPage:

    TITLE_PAGE_TEXT = (By.CSS_SELECTOR, "h2")
    WELCOME_TEXT = (By.CSS_SELECTOR, "h4")
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "radius")
    FLASH_ERROR = (By.ID, "flash")

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_page(self):
        return self.browser.find_element(*self.TITLE_PAGE_TEXT).text

    def get_welcome_message(self):
        return self.browser.find_element(*self.WELCOME_TEXT).text

    def insert_username(self, username):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)

    def insert_password(self, password):
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def is_login_button_displayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()

    def get_flash_error(self):
        return self.browser.find_element(*self.FLASH_ERROR).text
