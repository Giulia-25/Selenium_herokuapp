from selenium.webdriver.common.by import By


class JsAlerts:
    TITLE_PAGE_TEXT = (By.CSS_SELECTOR, "h3")
    ALERT_BUTTON = (By.CSS_SELECTOR, '[onclick="jsAlert()"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, '[onclick="jsConfirm()"]')
    PROMPT_BUTTON = (By.CSS_SELECTOR, '[onclick="jsPrompt()"]')
    # RESULT = (By.ID, 'result')

    URL = 'https://the-internet.herokuapp.com/javascript_alerts'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_page(self):
        return self.browser.find_element(*self.TITLE_PAGE_TEXT).text

    def click_alert_button(self):
        self.browser.find_element(*self.ALERT_BUTTON).click()

    def click_confirm_button(self):
        self.browser.find_element(*self.CONFIRM_BUTTON).click()

    def click_prompt_button(self):
        self.browser.find_element(*self.PROMPT_BUTTON).click()

    def is_alert_button_displayed(self):
        return self.browser.find_element(*self.ALERT_BUTTON).is_displayed

    def is_confirm_button_displayed(self):
        return self.browser.find_element(*self.CONFIRM_BUTTON).is_displayed

    def is_prompt_button_displayed(self):
        return self.browser.find_element(*self.CONFIRM_BUTTON).is_displayed

    def accept_confirm_button(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def cancel_confirm_button(self):
        alert = self.browser.switch_to.alert
        alert.dismiss()

    def insert_prompt_button(self, text):
        alert = self.browser.switch_to.alert
        alert.send_keys(text)

    # def result(self, text):
    #     rezultat = self.browser.find_element(*self.RESULT).contains(text)




