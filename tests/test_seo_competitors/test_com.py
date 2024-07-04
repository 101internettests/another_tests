from tests.test_seo_competitors.test_seo_screen_competitors import urls, names
from selenium import webdriver
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('-headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.set_window_size(800, 3375)

screen_shot_path = "C:/Users/Katerina/PycharmProjects/"


def __init__(self):
    for url, filename in zip(urls, names):
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
