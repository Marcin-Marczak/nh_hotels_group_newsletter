from selenium.webdriver.common.by import By


class SignUpNewsletterPage:

    def __init__(self, driver):
        self.driver = driver
        self.confirmation_text = (By.XPATH, "//h2[@class='h3']")

    def get_confirmation_text(self):
        return self.driver.find_element(*self.confirmation_text).text