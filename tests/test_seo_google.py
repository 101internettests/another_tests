from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver
from pages.providers_tests.data import query_new

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")  # Открывать окно браузера в максимальном размере
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


def test_find_competitors_and_website_rank(driver):
    websites_to_check = ["101internet", "piter-online","moskvaonline"]
    for website_to_check in websites_to_check:
        for query in query_new:
            driver.get(f"https://www.google.com/search?q={query}")
            search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
            website_rank = None

            for index, result in enumerate(search_results, start=1):
                link = result.find_elements(By.CSS_SELECTOR, "a")
                if link:
                    url = link[0].get_attribute("href")
                    if url is not None and any(website in url for website in websites_to_check):
                        website_rank = index
                        break

            if website_rank:
                print(f"Сайт '{website_to_check}' был на позиции {website_rank} в результатах по запросу '{query}'.")
            else:
                print(f"Сайт '{website_to_check}' не был найден в результатах по запросу '{query}'.")

            time.sleep(2)