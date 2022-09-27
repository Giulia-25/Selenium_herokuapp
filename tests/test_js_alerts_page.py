import pytest
from assertpy import soft_assertions, assert_that

from pages.js_alerts_page import JsAlerts


@pytest.fixture()
def js_alerts_page(browser):
    return JsAlerts(browser)


@pytest.skip
def test_js_alerts_page(browser,js_alerts_page):
    with soft_assertions():
        js_alerts_page.load_page()
        assert_that(js_alerts_page.get_title_page()).contains("JavaScript Alerts")
        assert_that(browser.current_url).ends_with("/javascript_alerts")
        assert_that(js_alerts_page.is_alert_button_displayed()).is_true()
        assert_that(js_alerts_page.is_confirm_button_displayed()).is_true()
        assert_that(js_alerts_page.is_prompt_button_displayed()).is_true()


@pytest.skip
def test_alert_button(browser, js_alerts_page):
    js_alerts_page.load_page()
    js_alerts_page.click_alert_button()
    js_alerts_page.accept_confirm_button()


def test_accept_confirm_button(browser, js_alerts_page):
    js_alerts_page.load_page()
    js_alerts_page.click_confirm_button()
    js_alerts_page.accept_confirm_button()


def test_cancel_confirm_button(browser, js_alerts_page):
    js_alerts_page.load_page()
    js_alerts_page.click_confirm_button()
    js_alerts_page.cancel_confirm_button()


def test_prompt_button(browser, js_alerts_page):
    js_alerts_page.load_page()
    js_alerts_page.click_prompt_button()
    js_alerts_page.insert_prompt_button('ana are mere')