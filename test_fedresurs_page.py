import pytest, time

from .pages.main_page import MainPage
from .pages.fedresurs_search_page import FedresursSearchPage
from .pages.fedresurs_sbertech_page import FedresursSbertechPage
from .pages.locators import SearchPageLocators, AuthPageLocators

@pytest.mark.searchpage
def test_fedresurs_search_page(browser):
    link = AuthPageLocators.FEDRESURS_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    fedresurs_search_page = FedresursSearchPage(browser, browser.current_url)
    fedresurs_search_page.should_be_sbertech()
    
@pytest.mark.sbertechpage
def test_fedresurs_sbertech_page(browser):
    link = AuthPageLocators.FEDRESURS_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    fedresurs_sbertech_page = FedresursSbertechPage(browser, browser.current_url)
    fedresurs_sbertech_page.sbertech()

@pytest.mark.xfail(reason='chek')    
def test_fedresurs_sbertech_page_wronge_value(browser): 
    link = AuthPageLocators.FEDRESURS_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    fedresurs_sbertech_page = FedresursSbertechPage(browser, browser.current_url)
    fedresurs_sbertech_page.should_not_be_success_message()