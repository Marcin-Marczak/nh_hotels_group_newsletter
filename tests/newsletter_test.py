from tests.data_used_in_tests import *
import pytest
from pages.main_page import MainPage
from pages.newsletter_page import NewsletterPage
from pages.successful_sign_up_newsletter_page import SignUpNewsletterPage


@pytest.mark.usefixtures("setup")
class TestNewsletter:

    def test_01_is_newsletter_form_page_displayed(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page(url_main_page)
        main_page.go_to_newsletter_form_page()
        assert self.driver.current_url == url_newsletter_page

    def test_02_blank_name_user_is_not_sign_up(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_form_with_blank_name(last_name, email, email)
        assert error_message == newsletter_page.get_error_message()

    def test_03_blank_last_name_user_is_not_sign_up(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_form_with_blank_last_name(name, email, email)
        assert error_message == newsletter_page.get_error_message()

    def test_04_blank_email_and_confirm_email_user_is_not_sign_up(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_form_with_blank_email_and_confirm_email(name, last_name)
        assert error_message == newsletter_page.get_error_message()

    def test_05_blank_email_user_is_not_sign_up(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_form_with_blank_email(name, last_name, confirm_email)
        assert error_message == newsletter_page.get_error_message_1_if_blank_email()
        assert error_message_emails_not_match == newsletter_page.get_error_message_2_if_blank_mail()

    def test_06_blank_confirm_email_user_is_not_sign_up(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_form_with_blank_confirm_email(name, last_name, email)
        assert error_message_emails_not_match == newsletter_page.get_error_message()

    def test_07_invalid_emails_user_is_not_sign_up(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_form_with_invalid_emails(name, last_name, invalid_email, invalid_email)
        assert error_message_invalid_email == newsletter_page.get_error_message()

    def test_08_emails_not_match_user_is_not_sign_up(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_form_with_emails_not_match(name, last_name, email, confirm_email)
        assert error_message_emails_not_match == newsletter_page.get_error_message()

    def test_09_without_private_policy_agree_user_is_not_sign_up(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_form_without_private_policy_agree(name, last_name, email, email)
        assert error_message == newsletter_page.get_error_message()

    def test_10_blank_form(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_blank_form()
        assert 4 == newsletter_page.get_len_of_error_messages_if_submit_blank_form()
        assert error_message == newsletter_page.get_error_message_if_submit_blank_form()

    def test_11_all_data_valid_user_is_sign_up_to_newsletter(self):
        newsletter_page = NewsletterPage(self.driver)
        newsletter_page.open_newsletter_page(url_newsletter_page)
        newsletter_page.submit_form_with_all_data_valid(name, last_name, email, email)
        successful_page = SignUpNewsletterPage(self.driver)
        assert confirmation_text == successful_page.get_confirmation_text()