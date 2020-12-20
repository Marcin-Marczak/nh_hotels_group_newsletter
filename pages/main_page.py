from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.cookies_accept_button = (By.ID, "consent-prompt-submit")
        self.go_to_newsletter_form_page_button = (By.LINK_TEXT, "Newsletter")

    def open_main_page(self, url_main_page):
        self.driver.get(url_main_page)
        WebDriverWait(self.driver, 15, 0.5).until(ec.url_to_be, url_main_page)
        self.driver.maximize_window()

    def go_to_newsletter_form_page(self):
        self.driver.find_element(*self.cookies_accept_button).click()
        self.driver.find_element(*self.go_to_newsletter_form_page_button).click()
        WebDriverWait(self.driver, 10, 0.5).until(ec.url_changes)