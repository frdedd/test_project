from .base_page import BasePage
from .locators import SearchPageLocators, SearchText, SearchResultLocators

import time 

class FedresursSearchPage(BasePage):

    def should_be_sbertech(self):
    
        # Находим строку поиска, вводим значение Сбертех
        self.find_element(*SearchPageLocators.SEARCH_STRING).send_keys(*SearchText.SBERTECH_COMPANY)
        
        #Находим копку найти, вызываем ее
        self.find_element(*SearchPageLocators.FIND_BUTTON).click()
        
        # Собираем все компании на странице поиска в список и проверям наличие интересующей компании.
        assert SearchText.NAME_SBERTECH_COMPANY in self.data_list(*SearchResultLocators.SEARCH_RESULT_COMPANY_BLOCKS), "Компания с нименованием: "+SearchText.NAME_SBERTECH_COMPANY+" не найдена на странице поиска!" 
        
        #Собираем все идентификаторы на странице поиска в список и проверям наличие интересующего ИНН.
        assert SearchText.INN_SBERTECH_COMPANY in self.data_list(*SearchResultLocators.SEARCH_RESULT_IDENTIFIER_BLOCKS), "Компания с ИНН:"+SearchText.INN_SBERTECH_COMPANY+" не найдена на странице поиска!"
        
        #Переходим на страницу компании
        self.find_element_by_link_text(SearchText.NAME_SBERTECH_COMPANY).click()