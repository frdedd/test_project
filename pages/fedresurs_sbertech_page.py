from .base_page import BasePage
from .locators import SearchPageLocators, SearchText, SbertechPageLocators

import time 

class FedresursSbertechPage(BasePage):

    def sbertech(self):
    
        # Находим строку поиска, вводим значение Сбертех
        self.find_element(*SearchPageLocators.SEARCH_STRING).send_keys(*SearchText.SBERTECH_COMPANY)
        
        #Находим копку найти, вызываем ее
        self.find_element(*SearchPageLocators.FIND_BUTTON).click()

        #Переходим на страницу компании
        self.find_element_by_link_text(SearchText.NAME_SBERTECH_COMPANY).click()
        
        #Переклюаемся в новое окно браузера
        self.switch_to_window()
        
        #Находим и кликаем элемент: раздел «Существенные факты»
        self.find_element_scroll(*SbertechPageLocators.EXPEND_PANEL_ROOT).click()
        
        #Находим и кликаем элемент: раздел «Активы и аудит»
        self.find_element_scroll(*SbertechPageLocators.EXPEND_PANEL_SUB).click()
 
        #Проверяем, что есть подменю «Стоимость чистых активов»
        assert SearchText.MENU_NET_ASSET_VALUE in self.ec_visibility_of_element_located(*SbertechPageLocators.MENU_POINT_LINK1).text, "Подменю : "+SearchText.MENU_NET_ASSET_VALUE+" не найдено на странице!"
        
        #Кликаем на пункт «Стоимость чистых активов»
        self.find_element(*SbertechPageLocators.MENU_POINT_LINK1).click()
        
        #Найти сообщение «Сообщение №06559060 от 25.03.2021»
        self.ec_visibility_of_element_located(*SbertechPageLocators.CAPTION_TEXT)
        
        #Переходим на страницу с сообщением о стоимости чистых активов
        self.find_element(*SbertechPageLocators.LINK_MESSAGE_06559060).click()
        
        #Переклюаемся в новое окно браузера
        self.switch_to_window()
        
        #Прокручиваем окно браузера до необходимого сообщения и проверяем стоимость чистых активов        
        assert SearchText.NET_ASSET_VALUE_TRUE == self.find_element_scroll(*SbertechPageLocators.MESSAGE_ASSET_VALUE).text, "Стоимость чистых активов: "+SearchText.NET_ASSET_VALUE_TRUE+" не найдена на странице!"
    
    def should_not_be_success_message(self):
        # Находим строку поиска, вводим значение Сбертех
        self.find_element(*SearchPageLocators.SEARCH_STRING).send_keys(*SearchText.SBERTECH_COMPANY)
        
        #Находим копку найти, вызываем ее
        self.find_element(*SearchPageLocators.FIND_BUTTON).click()
        
        #Переходим на страницу компании
        self.find_element_by_link_text(SearchText.NAME_SBERTECH_COMPANY).click()
        
        #Переклюаемся в новое окно браузера
        self.switch_to_window()
        
        #Находим и кликаем элемент: раздел «Существенные факты»
        self.find_element_scroll(*SbertechPageLocators.EXPEND_PANEL_ROOT).click()
        
        #Находим и кликаем элемент: раздел «Активы и аудит»
        self.find_element_scroll(*SbertechPageLocators.EXPEND_PANEL_SUB).click()
        
        #Кликаем на пункт «Стоимость чистых активов»
        self.ec_visibility_of_element_located(*SbertechPageLocators.MENU_POINT_LINK1).click()
        
        #Найти сообщение «Сообщение №06559060 от 25.03.2021»
        self.ec_visibility_of_element_located(*SbertechPageLocators.CAPTION_TEXT)
        
        #Переходим на страницу с сообщением о стоимости чистых активов
        self.find_element(*SbertechPageLocators.LINK_MESSAGE_06559060).click()
        
        #Переклюаемся в новое окно браузера
        self.switch_to_window()
        
        #Проверка на срабатывании ошибки
        assert SearchText.NET_ASSET_VALUE_FALSE == self.find_element_scroll(*SbertechPageLocators.MESSAGE_ASSET_VALUE).text, "Стоимость чистых активов: "+SearchText.NET_ASSET_VALUE_FALSE+" не найдена на странице!"