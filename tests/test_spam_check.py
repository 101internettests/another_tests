
import time
from pages.spam.spam_page import SpamPage


class TestSpamNumbers:
    def test_wait_call_form(self, driver):
        forms_page = SpamPage(driver, "https://www.sberbank.ru/ru/person/cybersecurity/antifraud")
        forms_page.open()
        forms_page.check_the_spam()