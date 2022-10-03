from selenium.webdriver.common.by import By


class ForgotPassword:

    TITLE_PAGE_TEXT = (By.CSS_SELECTOR, "h2")
    SUBHEADER = (By.CLASS_NAME, "subheader")
    EMAIL_INPUT = (By.ID, "email")
    RETRIEVE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    INTERNAL_ERROR = (By.CSS_SELECTOR, "h1")

    URL = 'https://the-internet.herokuapp.com/forgot_password'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_page(self):
        return self.browser.find_element(*self.TITLE_PAGE_TEXT).text

    def get_subheader(self):
        return self.browser.find_element(*self.SUBHEADER).text

    def insert_email(self, email):
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_retrieve_pass_button(self):
        self.browser.find_element(*self.RETRIEVE_PASSWORD_BUTTON).click()

    def is_retrieve_pass_button_displayed(self):
        return self.browser.find_element(*self.RETRIEVE_PASSWORD_BUTTON).is_displayed()

    def retrieve_password_submit(self):
        return self.browser.find_element(*self.INTERNAL_ERROR).text

