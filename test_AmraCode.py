from pages.main_page import MainPage
from selenium.webdriver.common.by import By




def test_guest_can_go_to_login_page(browser):
    link = "https://amracode.com"
    page = MainPage(browser, link) 
    page.open()            
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "https://amracode.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


