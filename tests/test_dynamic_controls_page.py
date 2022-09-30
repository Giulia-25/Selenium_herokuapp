import pytest
from assertpy import assert_that

from pages.dynamic_controls_page import DynamicControls


@pytest.fixture
def dynamic_controls_page(browser):
    return DynamicControls(browser)


def test_checkbox(browser, dynamic_controls_page):
    dynamic_controls_page.load_page()
    dynamic_controls_page.click_checkbox()
    assert_that(dynamic_controls_page.is_checkbox_displayed()).is_true()


def test_click_remove_add_button(browser, dynamic_controls_page):
    dynamic_controls_page.load_page()
    dynamic_controls_page.click_remove_add_button()
    assert_that(dynamic_controls_page.is_remove_add_button_displayed()).is_true()
    assert_that(dynamic_controls_page.click_checkbox()).is_not_iterable()

    dynamic_controls_page.load_page()
    dynamic_controls_page.click_remove_add_button()
    assert_that(dynamic_controls_page.is_checkbox_displayed()).is_true()


def test_click_enable_disable_button(browser, dynamic_controls_page):
    dynamic_controls_page.load_page()
    dynamic_controls_page.click_enable_disable_button()
    assert_that(dynamic_controls_page.is_enable_disable_button_displayed()).is_true()


def test_insert_text(browser, dynamic_controls_page):
    dynamic_controls_page.load_page()
    dynamic_controls_page.click_enable_disable_button()
    dynamic_controls_page.insert_text('Hello world!')
    assert_that(dynamic_controls_page.is_text_displayed()).is_true()
