from selenium.webdriver.common.by import By
from random import randint


class WaitCallLocators:
    CHOOSE_THE_REGION = (By.XPATH, "(//a[@href='/select-region'])[1]")
    WRITE_NAME_OF_REGION = (By.XPATH, "//input[@placeholder='Введите первые 3 буквы']")
    CHOOSE_MSK_REGION = (By.XPATH, "(//a[contains(text(), 'Московская область')])[1]")
    TARIFFS_BUTTON = (By.XPATH, "(//a[@datatest='main_tariff_button'])[1]")
    SCROLL = (By.XPATH, "(//a[contains(text(), 'МТС')])[2]")
    BUTTON_WAIT_FOR_CALL = (By.XPATH, "//div[contains(text(), 'жду звонка')]")
    WRITE_TELEPHONE_NUMBER = (By.XPATH, "//input[@id='fix_callback_phone']")
    BUTTON_CALL_ME = (By.XPATH, "//div[contains(text(), 'Жду звонка')]")


class PopUpPhoneNub:
    CHOOSE_MOSCOW = (By.XPATH, "(//a[contains(text(), 'Москва')])[1]")
    BUTTON_SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    NUMBER_INPUT = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    NUMBER_SECOND_INPUT = (By.XPATH, "(//input[@autocomplete='tel'])[2]")
    BUTTON_SHOW_RESULTS = (By.XPATH, "//div[contains(text(), 'Показать результаты')]")
    BUTTON_SUBMIT_APPLICATION = (By.XPATH, "//div[contains(text(), 'Оставить заявку')]")
    POP_UP_TEXT = (By.XPATH, "(//img[@alt='icon']/../div)[1]")
    SOME_TEXT = (By.XPATH, "//div[contains(text(), 'А пока вы можете самостоятельно посмотреть тарифы и почитать отзывы о провайдерах!')]")


class OfficeOrder:
    INTERNET_IN_OFFICE = (By.XPATH, "(//a[contains(text(), 'Интернет в офис')])[1]")
    CHOOSE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_ON_STREET = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    CHOOSE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_ON_HOUSE = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    TENDER_BUTTON = (By.XPATH, "//div[contains(text(), 'Запустить тендер')]")
    PERSON_INPUT = (By.XPATH, "//input[@datatest='business_order_input_person']")
    TELEPHON_INPUT = (By.XPATH, "//input[@datatest='business_order_input_tel']")
    BUTTON_SEND_ORDER = (By.XPATH, "(//div[contains(text(), 'Отправить заявку')])[1]")


class AddreesTariffForm:
    CLOSE_POP_UP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    BUTTON_CONNECT = (By.XPATH, "(//div[@datatest='providers_form_inspect_connect_tariff_button'])[1]")
    INPUT_MOBILE_PHONE = (By.XPATH, "//input[@id='fix_callback_phone']")
    BUTTON_SEND_APPLICATION = (By.XPATH, "//div[contains(text(), 'Отправить заявку')]")
    OPEN_PPOPUP = (By.XPATH, f"(// span[contains(text(), 'Подключить')])[{randint(0, 4)}]")
    TEXT = (By.XPATH, "(//div[contains(text(), 'телефон')])[1]")
    INPUT_NUMBER_SECOND = (By.XPATH, "//input[@datatest='providers_provider_order_input_tel']")
    BUTTON_SEND_APL_SECOND = (By.XPATH, "//div[contains(text(), 'Оставить заявку')]")
    SCROLL = (By.XPATH, "//div[contains(text(), 'Показать все детали тарифа')]")
    TARIFF_POPUP_NUM = (By.XPATH, "//input[@datatest='popup_tariff_order_input_tel']")


class WaitPOLCallLocators:
    CHOOSE_POL_REGION = (By.XPATH, "//a[contains(text(), 'Санкт-Петербург')]")
    SCROLL = (By.XPATH, "//a[contains(text(), 'ВайФаер')]")


class PopUpPhoneNubPOL:
    BUTTON_SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    NUMBER_INPUT = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    BUTTON_SHOW_RESULTS = (By.XPATH, "//div[contains(text(), 'Показать результаты')]")
    POP_UP_TEXT = (By.XPATH, "(//img[@alt='icon']/../div)[1]")
    NUMBER_SECOND_INPUT = (By.XPATH, "(//input[@autocomplete='tel'])[2]")
    BUTTON_SUBMIT_APPLICATION = (By.XPATH, "//div[contains(text(), 'Оставить заявку')]")


class ReferralUrlTariffMOL:
    CHOSE_MOSCOW_REGION = (By.XPATH, "//a[contains(text(), 'Московская область')]")
