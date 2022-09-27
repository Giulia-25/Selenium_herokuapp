from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecurePage:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[class *= 'icon-signout']")
    URL = "https://the-internet.herokuapp.com/secure"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

#cauta elementul timp de 4 secunde (refresh la fiecare 500ms)
    def is_logout_button_displayed(self):
        logout_button = WebDriverWait(self.browser, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class *= 'icon-signout']")))
        return logout_button.is_displayed()