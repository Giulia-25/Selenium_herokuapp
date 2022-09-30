import pytest
from assertpy import soft_assertions, assert_that

from pages import secure_page
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@pytest.fixture
def login_page(browser):
    return LoginPage(browser)


def test_check_login_page(browser, login_page):
    login_page.load_page()
    with soft_assertions():
        assert_that(login_page.get_title_page()).is_equal_to("Login Page")
        assert_that(login_page.get_welcome_message()).contains("This is where you can log into the secure area.")
        assert_that(browser.current_url).ends_with("/login")
        assert_that(browser.current_url).is_equal_to(login_page.URL)
        assert_that(login_page.is_login_button_displayed()).is_true()


def test_check_login_successfully(browser,login_page):
    login_page.load_page()
    login_page.insert_username("tomsmith")
    login_page.insert_password("SuperSecretPassword!")
    login_page.click_login_button()
    secure_page = SecurePage(browser)
    assert_that(browser.current_url).is_equal_to(secure_page.URL)
    assert_that(secure_page.is_logout_button_displayed()).is_true()


def test_login_negative_username(browser, login_page):
    login_page.load_page()
    login_page.insert_username("tom")
    login_page.insert_password("SuperSecretPassword!")
    login_page.click_login_button()
    assert_that(login_page.get_flash_error()).contains("Your username is invalid!")


def test_login_negative_password(browser, login_page):
    login_page.load_page()
    login_page.insert_username("tomsmith")
    login_page.insert_password("blaaaa")
    login_page.click_login_button()
    assert_that(login_page.get_flash_error()).contains("Your password is invalid!")