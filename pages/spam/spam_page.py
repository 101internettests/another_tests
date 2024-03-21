from locators.spam.spam_locators import CheckSpam
import time
from pages.base_page import BasePage
from config import num_1


class SpamPage(BasePage):
    def check_the_spam(self):
        self.element_is_visible(CheckSpam.ASSERT_BUTTON).click()
        self.element_is_visible(CheckSpam.GO_TO_SBER).click()
        time.sleep(5)
        self.element_is_visible(CheckSpam.INPUT_NUMBER).send_keys(num_1)
        self.element_is_visible(CheckSpam.BUTTON_CHECK).click()
        check_text = self.element_is_visible(CheckSpam.TEXT)
        assert check_text.text == "Телефон не найден в базе мошенников"
        self.element_is_visible(CheckSpam.NEW_NUM).click()