import selenium.webdriver
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def browser():
    #before tests
    global driver
    # initializam un browser
    options = Options()
    # options.add_argument('--headless')
    s = Service(ChromeDriverManager().install())