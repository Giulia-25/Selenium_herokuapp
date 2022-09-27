import pytest
from assertpy import assert_that

from pages import elemental_selenium_page
from pages.add_remove_elements_page import AddRemoveElementsPage
from time import sleep

@pytest.fixture
def add_remove_page(browser):
    return AddRemoveElementsPage(browser)

@pytest.mark.add
def test_check_add_remove_page(browser, add_remove_page):
    add_remove_page.load_page()
    assert add_remove_page.get_title_page() == "Add/Remove Elements", "Check url is ok"
    assert add_remove_page.is_add_button_displayed(), "Check Add Button is displayed"

@pytest.mark.add
def test_add_and_remove_buttons_functionality(browser, add_remove_page):
    print("hellooolo")
    add_remove_page.load_page()
    add_remove_page.click_add_element_button()
    assert add_remove_page.is_delete_button_displayed()
    add_remove_page.click_delete_button()
    assert add_remove_page.get_number_of_delete_buttons() == 0
    for i in range(10):
        add_remove_page.click_add_element_button()
        assert add_remove_page.get_number_of_delete_buttons() == i+1
    for i in range(10,1,-1):
        add_remove_page.click_delete_button()
        assert add_remove_page.get_number_of_delete_buttons() == i-1


def test_url(browser, add_remove_page):
    add_remove_page.load_page()

    assert browser.current_url == add_remove_page.URL, "Check url is ok"


def test_selenium_link(browser, add_remove_page):
    add_remove_page.load_page()
    add_remove_page.click_selenium_link()
    # assert_that(browser.current_url == elemental_selenium_page.URL).is_true()