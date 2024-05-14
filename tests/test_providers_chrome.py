from selenium import webdriver
from pages.providers_tests.data import query_new
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-headless')
chrome_options.add_argument('-private')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.set_window_size(1280, 3885)

screen_shot_path = "C:/Users/Katerina/Desktop/screens/"

driver.get("https://www.google.ru/")


class TestSearChrome:
    def test_check_search_chrome(self, driver):
        for item in query_new:
            try:
                print(f"Выполняю поиск {item}")
                poisk = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@aria-label='Найти']")))
                poisk.clear()
                poisk.send_keys(item)
                poisk.send_keys(Keys.ENTER)
                sleep(4)
                driver.save_screenshot(screen_shot_path + item + ".png")
                print("Screenshot saved at:", screen_shot_path + item + ".png")
            except Exception as e:
                print(f"Не смог выполнить поиск по {item}, ошибка {e}")
        print("ГОТОВО!")
        driver.quit()