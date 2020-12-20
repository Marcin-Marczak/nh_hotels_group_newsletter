from faker import Faker
fake = Faker("pl")

url_main_page = "https://www.nh-hotels.com/"
url_newsletter_page = "https://www.nh-hotels.com/newsletter"
name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
confirm_email = fake.email()
invalid_email = "@" + fake.word()
error_message = "This is required"
error_message_emails_not_match = "The e-mails entered must match"
error_message_invalid_email = 'Not a valid email address'
confirmation_text = "THANK YOU FOR SUBSCRIBING TO OUR NEWSLETTER!"