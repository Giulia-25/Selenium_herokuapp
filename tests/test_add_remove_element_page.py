import pytest
from assertpy import assert_that

from pages import elemental_selenium_page
from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.elemental_selenium_page import ElementalSelenium


@pytest.fixture
def add_remove_page(browser):
    return AddRemoveElementsPage(browser)


def test_check_add_remove_page(browser, add_remove_page):
    add_remove_page.load_page()
    # assert add_remove_page.get_title_page() == "Add/Remove Elements", "Check url is ok"
    # assert add_remove_page.is_add_button_displayed(), "Check Add Button is displayed"

    assert_that(add_remove_page.get_title_page()).is_equal_to("Add/Remove Elements")
    assert_that(add_remove_page.is_add_button_displayed()).is_true()

# cum adaugi in assert_that "Check url is ok" si "Check Add Button is displayed"?


def test_add_and_remove_buttons_functionality(browser, add_remove_page):
    # add_remove_page.load_page()
    # add_remove_page.click_add_element_button()
    # assert add_remove_page.is_delete_button_displayed()
    # add_remove_page.click_delete_button()
    # assert add_remove_page.get_number_of_delete_buttons() == 0
    # for i in range(10):
    #     add_remove_page.click_add_element_button()
    #     assert add_remove_page.get_number_of_delete_buttons() == i+1
    # for i in range(10,1,-1):
    #     add_remove_page.click_delete_button()
    #     assert add_remove_page.get_number_of_delete_buttons() == i-1

    add_remove_page.load_page()
    add_remove_page.click_add_element_button()
    assert_that(add_remove_page.is_delete_button_displayed()).is_true()
    add_remove_page.click_delete_button()
    assert_that(add_remove_page.get_number_of_delete_buttons()).is_equal_to(0)
    for i in range(10):
        add_remove_page.click_add_element_button()
        assert_that(add_remove_page.get_number_of_delete_buttons()).is_equal_to(i+1)
    for i in range(10,1,-1):
        add_remove_page.click_delete_button()
        assert_that(add_remove_page.get_number_of_delete_buttons()).is_equal_to(i-1)


def test_url(browser, add_remove_page):
    add_remove_page.load_page()
    # assert browser.current_url == add_remove_page.URL, "Check url is ok"
    assert_that(add_remove_page.URL).is_equal_to("https://the-internet.herokuapp.com/add_remove_elements/")


def test_selenium_url(browser, add_remove_page):
    add_remove_page.load_page()
    add_remove_page.click_selenium_link()
    elemental_selenium_page = ElementalSelenium(browser)
    elemental_selenium_page.load_page()
    assert_that(elemental_selenium_page.SELENIUM_URL).is_equal_to("http://www.elementalselenium.com/")

# InvalidArgumentException: Message: invalid argument: 'url' must be a string


# am transformat totul in assert_that