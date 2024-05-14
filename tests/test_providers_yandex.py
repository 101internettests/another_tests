from selenium import webdriver
import time
from pages.providers_tests.data import urlsyandex, path_yandex


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('-headless')
# firefox_options.add_argument('--start-maximized')
driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()
driver.set_window_size(800, 3375)

screen_shot_path = "C:/Users/Katerina/Desktop/screens/"


class TestSearchYandex:
    def test_check_search_yandex(self, driver):
        for url, filename in zip(urlsyandex, path_yandex):
            try:
                print(f"Беру ссылку {url}")
                driver.get(url)
                time.sleep(4)
                driver.save_screenshot(screen_shot_path + f"{filename}.png")
                print("Снимок экрана сохранен как:", screen_shot_path + f"{filename}.png")
            except Exception as e:
                print(f"Не удалось выполнить поиск по {url}, ошибка {e}")

        print("ГОТОВО!")
        driver.quit()