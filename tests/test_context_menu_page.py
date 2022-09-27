import pytest

from pages.context_menu_page import ContextMenu


@pytest.fixture
def context_menu_page(browser):
    return ContextMenu(browser)


def test_click_context_menu(browser, context_menu_page):
    context_menu_page.load_page()
    context_menu_page.click_context_menu()
