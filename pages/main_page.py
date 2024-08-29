from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        coockies = self.browser.find_element(By.TAG_NAME,'svg')
        coockies.click()
        login_link = self.browser.find_element(By.XPATH, '//a[@href="/free-it-consulting"]')
        login_link.click() 

    def should_be_login_link(self):
        coockies = self.browser.find_element(By.TAG_NAME,'svg')
        coockies.click()
        login_link = self.browser.find_element(By.XPATH, '//a[@href="/free-it-consulting"]')
        
