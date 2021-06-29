from selenium.webdriver.common.by import By

class SearchText():
    SBERTECH_COMPANY = 'Сбертех'
    NAME_SBERTECH_COMPANY = 'АО "СБЕРТЕХ"'
    INN_SBERTECH_COMPANY = '7736632467'
    MENU_NET_ASSET_VALUE = 'Стоимость чистых активов'
    MESSAGE_06559060 = '№06559060 от 25.03.2021'
    NET_ASSET_VALUE_TRUE = '1 923 808 712,07'
    NET_ASSET_VALUE_FALSE = '2 000 000 000,00'

class AuthPageLocators():
    FEDRESURS_PAGE_LINK = 'https://fedresurs.ru/'
    
class SearchPageLocators():
    SEARCH_STRING = (By.XPATH, '//*[@name="searchString"]')
    FIND_BUTTON = (By.XPATH, '//quick-search/div/div/form/button/i')
    
class SearchResultLocators():
    SEARCH_RESULT_COMPANY_BLOCKS = (By.XPATH, '//company-search-result/loader/div[1]/table/tbody/tr/td/*[@class="td_company_name"]')
    SEARCH_RESULT_IDENTIFIER_BLOCKS = (By.XPATH, '//company-search-result/loader/div/table/tbody/tr/td/div/div[@class="field-value"]')
    
class SbertechPageLocators():
    EXPEND_PANEL_ROOT = (By.XPATH, '//*[@label="Существенные факты"]')
    EXPEND_PANEL_SUB = (By.XPATH, '//*[@href="#id6"]')
    MENU_POINT_LINK1 = (By.XPATH, '//*[@id="id6"]/ul/li[1]/a')
    CAPTION_TEXT = (By.XPATH, '//*[contains(text(), MESSAGE_06559060)]')
    LINK_MESSAGE_06559060 = (By.XPATH, '/html/body/fedresurs-app/div[1]/company-card/div/company-publications-statistic/div/div[2]/loader/div[1]/publication-list/div[1]/app-publication-card/div/div[1]/h4[1]/a')
    MESSAGE_ASSET_VALUE = (By.XPATH, '//*[@class="info_table assets"] //tbody/tr/td[contains(text(), NET_ASSET_VALUE_TRUE)]')
    
    