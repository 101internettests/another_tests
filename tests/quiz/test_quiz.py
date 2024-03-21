import time
from pages.quiz.quiz_page import FormsPage
from config import bot, chat_id


class TestQuiz:
    def test_popup_number(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        try:
            forms_page.change_region_moscow()
            forms_page.fill_address_on_main_page()
            forms_page.fill_popup_number()
            print("Проверка адреса пройдена")
        except AssertionError:
            bot.send_message(chat_id, "Проверка на Шарикоподшипниковская 11 квиза упала 101 ")
        time.sleep(40)

    def test_popup_number_moscow(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms_page.open()
        try:
            forms_page.change_region_moscow()
            forms_page.fill_address_on_main_page()
            forms_page.fill_popup_number()
            print("Проверка адреса пройдена")
        except AssertionError:
            bot.send_message(chat_id, "Проверка на Шарикоподшипниковская 11 квиза упала МОЛ ")
        time.sleep(40)

    def test_popup_number_pol(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        try:
            forms_page.change_region_on_spb()
            forms_page.fill_address_on_main_page_pol()
            forms_page.fill_popup_number()
            print("Проверка адреса пройдена")
        except AssertionError:
            bot.send_message(chat_id, "Проверка на Энгельса 8 квиза упала ПОЛ ")
        time.sleep(40)

    def test_popup_number_second(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        try:
            forms_page.change_region_moscow()
            forms_page.fill_address_on_main_page_second()
            forms_page.fill_popup_number()
            print("Проверка адреса пройдена")
        except AssertionError:
            bot.send_message(chat_id, "Проверка на Гусятников 9 квиза упала 101 ")
        time.sleep(40)

    def test_popup_number_moscow_second(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms_page.open()
        try:
            forms_page.change_region_moscow_o()
            forms_page.fill_address_on_main_page_second()
            forms_page.fill_popup_number()
            print("Проверка адреса пройдена")
        except AssertionError:
            bot.send_message(chat_id, "Проверка на Гусятников 9 квиза упала МОЛ ")
        time.sleep(40)

    def test_popup_number_pol_second(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        try:
            forms_page.change_region_on_spb()
            forms_page.fill_address_on_main_page_pol_second()
            forms_page.fill_popup_number()
            print("Проверка адреса пройдена")
        except AssertionError:
            bot.send_message(chat_id, "Проверка на Народная 16 квиза упала ПОЛ ")
        time.sleep(40)

    def test_popup_number_third(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        try:
            forms_page.change_region_moscow()
            forms_page.fill_address_on_main_page_third()
            forms_page.fill_popup_number()
            print("Проверка адреса пройдена")
        except AssertionError:
            bot.send_message(chat_id, "Проверка на Ленинградский 12 квиза упала 101 ")
        time.sleep(40)

    def test_popup_number_moscow_third(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms_page.open()
        try:
            forms_page.change_region_moscow_o()
            forms_page.fill_address_on_main_page_mol()
            forms_page.fill_popup_number()
            print("Проверка адреса пройдена")
        except AssertionError:
            bot.send_message(chat_id, "Проверка на Балашиха 16 квиза упала МОЛ ")
        time.sleep(40)

    def test_popup_number_pol_third(self, driver):
        forms_page = FormsPage(driver, "https://piter-online.net/")
        forms_page.open()
        try:
            forms_page.change_region_on_spb()
            forms_page.fill_address_on_main_page_pol_third()
            forms_page.fill_popup_number()
            print("Проверка адреса пройдена")
        except AssertionError:
            bot.send_message(chat_id, "Проверка на Загородный проспект 13 квиза упала ПОЛ ")
