from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .locators import SearchText



class BasePage():
    def __init__(self,browser,url,timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)
    
    def find_element(self, how, what):
        return self.browser.find_element(how, what)
        
    def find_elements(self, how, what):
        return self.browser.find_elements(how, what)

    def data_list(self, how, what):
        return [element.text for element in self.find_elements(how, what)]
        
    def find_element_by_link_text(self, what):
        link = self.browser.find_element_by_link_text(what)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)      
        return link
        
    def switch_to_window(self):
        handles = self.browser.window_handles
        for x in range(len(handles)):
            if handles[x] != self.browser.current_window_handle:
                self.browser.close()
                self.browser.switch_to.window(handles[x])
    
    def find_element_scroll(self, how, what):
        element = self.browser.find_element(how, what)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        return element
        
    def ec_visibility_of_element_located(self,how,what):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((how,what)))
        
    def is_elements_present(self, how, what):
        try:
            self.browser.find_elements(how, what)
        except (NoSuchElementException):
            return False
            
        return True
        
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    