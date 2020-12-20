from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class NewsletterPage:

    def __init__(self, driver):
        self.driver = driver
        self.cookies_accept_button = (By.ID, "consent-prompt-submit")
        self.name_input = (By.ID, "name")
        self.last_name_input = (By.ID, "lastname")
        self.email_input = (By.ID, "email")
        self.confirm_email_input = (By.ID, "confmail")
        self.country_language_button = (By.XPATH, "//div[@class='col-sm-6 col-md-4']")
        self.select_country_button = (By.XPATH, "//li[@data-original-index='171']")
        self.select_language_button = (By.XPATH, "//li[@data-original-index='4']")
        self.private_policy_accept_button = (By.XPATH, "//label[@for='GDPR_flag_6']")
        self.send_button = (By.XPATH, "//input[@value='Send']")
        self.error_message = (By.XPATH, "//ul[@role='alert']/li")

    def open_newsletter_page(self, url_newsletter_page):
        self.driver.get(url_newsletter_page)
        self.driver.maximize_window()
        self.driver.find_element(*self.cookies_accept_button).click()

    def submit_form_with_blank_name(self, last_name, email, confirm_email):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.confirm_email_input).send_keys(confirm_email)
        self.driver.find_elements(*self.country_language_button)[0].click()
        self.driver.find_element(*self.select_country_button).click()
        self.driver.find_elements(*self.country_language_button)[1].click()
        self.driver.find_elements(*self.select_language_button)[1].click()
        self.driver.find_element(*self.private_policy_accept_button).click()
        time.sleep(1)
        self.driver.find_element(*self.send_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def submit_form_with_blank_last_name(self, name, email, confirm_email):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.confirm_email_input).send_keys(confirm_email)
        self.driver.find_elements(*self.country_language_button)[0].click()
        self.driver.find_element(*self.select_country_button).click()
        self.driver.find_elements(*self.country_language_button)[1].click()
        self.driver.find_elements(*self.select_language_button)[1].click()
        self.driver.find_element(*self.private_policy_accept_button).click()
        time.sleep(1)
        self.driver.find_element(*self.send_button).click()

    def submit_form_with_blank_email_and_confirm_email(self, name, last_name):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_elements(*self.country_language_button)[0].click()
        self.driver.find_element(*self.select_country_button).click()
        self.driver.find_elements(*self.country_language_button)[1].click()
        self.driver.find_elements(*self.select_language_button)[1].click()
        self.driver.find_element(*self.private_policy_accept_button).click()
        time.sleep(1)
        self.driver.find_element(*self.send_button).click()

    def submit_form_with_blank_email(self, name, last_name, confirm_email):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.confirm_email_input).send_keys(confirm_email)
        time.sleep(1)
        self.driver.find_elements(*self.country_language_button)[0].click()
        self.driver.find_element(*self.select_country_button).click()
        self.driver.find_elements(*self.country_language_button)[1].click()
        self.driver.find_elements(*self.select_language_button)[1].click()
        self.driver.find_element(*self.private_policy_accept_button).click()
        time.sleep(1)
        self.driver.find_element(*self.send_button).click()

    def get_error_message_1_if_blank_email(self):
        return self.driver.find_elements(*self.error_message)[0].text

    def get_error_message_2_if_blank_mail(self):
        return self.driver.find_elements(*self.error_message)[1].text

    def submit_form_with_blank_confirm_email(self, name, last_name, email):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        time.sleep(1)
        self.driver.find_elements(*self.country_language_button)[0].click()
        self.driver.find_element(*self.select_country_button).click()
        self.driver.find_elements(*self.country_language_button)[1].click()
        self.driver.find_elements(*self.select_language_button)[1].click()
        self.driver.find_element(*self.private_policy_accept_button).click()
        time.sleep(1)
        self.driver.find_element(*self.send_button).click()

    def submit_form_with_invalid_emails(self, name, last_name, email, confirm_email):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.confirm_email_input).send_keys(confirm_email)
        self.driver.find_elements(*self.country_language_button)[0].click()
        self.driver.find_element(*self.select_country_button).click()
        self.driver.find_elements(*self.country_language_button)[1].click()
        self.driver.find_elements(*self.select_language_button)[1].click()
        self.driver.find_element(*self.private_policy_accept_button).click()
        time.sleep(1)
        self.driver.find_element(*self.send_button).click()

    def submit_form_with_emails_not_match(self, name, last_name, email, confirm_email):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.confirm_email_input).send_keys(confirm_email)
        self.driver.find_elements(*self.country_language_button)[0].click()
        self.driver.find_element(*self.select_country_button).click()
        self.driver.find_elements(*self.country_language_button)[1].click()
        self.driver.find_elements(*self.select_language_button)[1].click()
        self.driver.find_element(*self.private_policy_accept_button).click()
        time.sleep(1)
        self.driver.find_element(*self.send_button).click()

    def submit_form_without_private_policy_agree(self, name, last_name, email, confirm_email):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.confirm_email_input).send_keys(confirm_email)
        self.driver.find_elements(*self.country_language_button)[0].click()
        self.driver.find_element(*self.select_country_button).click()
        self.driver.find_elements(*self.country_language_button)[1].click()
        self.driver.find_elements(*self.select_language_button)[1].click()
        time.sleep(1)
        self.driver.find_element(*self.send_button).click()

    def submit_blank_form(self):
        self.driver.find_element(*self.send_button).click()

    def get_len_of_error_messages_if_submit_blank_form(self):
        return len(self.driver.find_elements(*self.error_message))

    def get_error_message_if_submit_blank_form(self):
        return self.driver.find_elements(*self.error_message)[0-3].text

    def submit_form_with_all_data_valid(self, name, last_name, email, confirm_email):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.confirm_email_input).send_keys(confirm_email)
        self.driver.find_elements(*self.country_language_button)[0].click()
        self.driver.find_element(*self.select_country_button).click()
        self.driver.find_elements(*self.country_language_button)[1].click()
        self.driver.find_elements(*self.select_language_button)[1].click()
        self.driver.find_element(*self.private_policy_accept_button).click()
        self.driver.find_element(*self.send_button).click()
        WebDriverWait(self.driver, 15, 0.5).until(ec.url_changes)