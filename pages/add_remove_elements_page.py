from selenium.webdriver.common.by import By
class AddRemoveElementsPage:

    TITLE_PAGE_TEXT = (By.CSS_SELECTOR)

    def __init__(self, browser):
        self.browser = browser