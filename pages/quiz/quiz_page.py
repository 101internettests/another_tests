import time
from locators.quiz.quiz_locators import ReferralUrlTariffMOL, WaitCallLocators, PopUpPhoneNub, OfficeOrder, AddreesTariffForm, WaitPOLCallLocators, PopUpPhoneNubPOL
from pages.base_page import BasePage


class FormsPage(BasePage):
    def change_region_moscow(self):
        self.element_is_visible(WaitCallLocators.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(WaitCallLocators.WRITE_NAME_OF_REGION).send_keys("Москва")
        time.sleep(1)
        self.element_is_visible(PopUpPhoneNub.CHOOSE_MOSCOW).click()

    def fill_address_on_main_page(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Шарикоподшипниковская")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("11")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(PopUpPhoneNub.BUTTON_SHOW_TARIFFS).click()

    def fill_address_on_main_page_mol(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Балашиха")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("16")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(PopUpPhoneNub.BUTTON_SHOW_TARIFFS).click()

    def fill_address_on_main_page_second(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Гусятников")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("9")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(PopUpPhoneNub.BUTTON_SHOW_TARIFFS).click()


    def fill_address_on_main_page_third(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Ленинградский пр")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("12")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(PopUpPhoneNub.BUTTON_SHOW_TARIFFS).click()

    def fill_popup_number(self):
        if self.element_is_visible(PopUpPhoneNub.POP_UP_TEXT):
            text_in_pop_up = self.element_is_present(PopUpPhoneNub.POP_UP_TEXT).text
            if text_in_pop_up == ("Отлично! Подключение возможно. Введите номер "
                                  "телефона, оператор перезвонит вам в ближайшее "
                                  "время."):
                self.element_is_visible(PopUpPhoneNub.NUMBER_SECOND_INPUT).send_keys('1111111111')
                self.element_is_visible(PopUpPhoneNub.BUTTON_SUBMIT_APPLICATION).click()
                some_text = self.element_is_visible(PopUpPhoneNub.SOME_TEXT)
                assert some_text.text == "А пока вы можете самостоятельно посмотреть тарифы и почитать отзывы о провайдерах!"
                print("Провайдер доступен в этом доме")
            elif text_in_pop_up != ("Отлично! Подключение возможно. Введите номер "
                                    "телефона, оператор перезвонит вам в ближайшее "
                                    "время."):
                self.element_is_visible(PopUpPhoneNub.NUMBER_INPUT).send_keys('1111111111')
                self.element_is_visible(PopUpPhoneNub.BUTTON_SHOW_RESULTS).click()
                some_text = self.element_is_visible(PopUpPhoneNub.SOME_TEXT)
                assert some_text.text == "А пока вы можете самостоятельно посмотреть тарифы и почитать отзывы о провайдерах!"
                print("Провайдер недоступен в этом доме, отправлена заявки на другие")
        else:
            self.element_is_visible(AddreesTariffForm.OPEN_PPOPUP).click()

    def change_region_on_spb(self):
        self.element_is_visible(WaitCallLocators.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(WaitPOLCallLocators.CHOOSE_POL_REGION).click()

    def fill_address_on_main_page_pol(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Энгельса")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("8")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(PopUpPhoneNubPOL.BUTTON_SHOW_TARIFFS).click()

    def fill_address_on_main_page_pol_second(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Народная")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("61")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(PopUpPhoneNubPOL.BUTTON_SHOW_TARIFFS).click()

    def fill_address_on_main_page_pol_third(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Загородный проспект")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("13")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(PopUpPhoneNubPOL.BUTTON_SHOW_TARIFFS).click()

    def change_region_moscow_o(self):
        self.element_is_visible(WaitCallLocators.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(ReferralUrlTariffMOL.CHOSE_MOSCOW_REGION).click()
        time.sleep(3)