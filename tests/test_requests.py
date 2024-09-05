import requests
import telebot
from links.urls import all_urls
import allure
from config import bot, chat_id




class TestUrl:
    # def test_check_url_response(self):
    #     for url in urls_to_check:
    #         try:
    #             response = requests.get(url)
    #             print(f"Response code for {url}: {response.status_code}")
    #             if response.status_code == 502:
    #                 print("502 Bad Gateway error detected!")
    #
    #         except requests.exceptions.RequestException as e:
    #             print(f"An error occurred while checking {url}: {e}")
    @allure.suite("Проверь статус коды")
    def test_check_url_response(self):
        for url in all_urls:
            try:
                response = requests.get(url)
                status_code = response.status_code
                if 200 >= status_code <= 299:
                    print(f"URL: {url} - Status Code: {status_code} (Success)")
                elif 300 >= status_code <= 399:
                    print(f"URL: {url} - Status Code: {status_code} (Redirection)")
                elif 400 >= status_code <= 499:
                    bot.send_message(chat_id, f"Внимание:  {url} статус-код {status_code}")
                    #bot.send_photo(chat_id, f'http.cat/{status_code}')
                    print(f"URL: {url} - Status Code: {status_code} (Client Error)")
                elif 500 >= status_code <= 599:
                    bot.send_message(chat_id, f"Внимание:  {url} статус-код {status_code}")
                    bot.send_photo(chat_id, f'http.cat/{status_code}')
                    print(f"URL: {url} - Status Code: {status_code} (Server Error)")
                else:
                    print(f"URL: {url} - Status Code: {status_code} (Not in the expected ranges)")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while checking {url}: {e}")


