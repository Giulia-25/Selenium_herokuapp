import pytest
from assertpy import assert_that, soft_assertions

from pages.forgot_password_page import ForgotPassword


@pytest.fixture
def forgot_password_page(browser):
    return ForgotPassword(browser)


def test_check_forgot_password_page(browser, forgot_password_page):
    forgot_password_page.load_page()
    with soft_assertions():
        assert_that(forgot_password_page.get_title_page()).is_equal_to("Forgot Password")
        assert_that(browser.current_url).ends_with("/forgot_password")
        assert_that(forgot_password_page.is_retrieve_pass_button_displayed()).is_true()


def test_retrieve_password_negative(browser, forgot_password_page):
    forgot_password_page.load_page()
    forgot_password_page.insert_email("bla.gmail.com")
    forgot_password_page.click_retrieve_pass_button()
    assert_that(forgot_password_page.retrieve_password_submit()).contains('Internal Server Error')
