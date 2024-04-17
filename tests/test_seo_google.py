from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")  # Открывать окно браузера в максимальном размере
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


def test_find_competitors_and_website_rank(browser):
    search_queries = ["101интернет", "мтс подключить", "питер онлайн"]
    website_to_check = "101internet.ru"  # ваш веб-сайт, позицию которого вы хотите найти

    for query in search_queries:
        browser.get(f"https://www.google.com/search?q={query}")

        search_results = browser.find_elements(By.CSS_SELECTOR, "div.g")

        competitors = []
        website_rank = None
        for index, result in enumerate(search_results, start=1):
            link = result.find_elements(By.CSS_SELECTOR, "a")
            if link:
                url = link[0].get_attribute("href")
                if url:  # Добавим дополнительную проверку на наличие URL
                    title = link[0].text
                    if website_to_check in url:
                        website_rank = index
                    competitors.append(title)

        assert competitors, f"No search results found for query '{query}'"

        if website_rank:
            print(f"Ваш сайт '{website_to_check}' был на позиции {website_rank} в результатах по запросу '{query}'.")
        else:
            print(f"Сайт '{website_to_check}' не был найден в результатах по запросу '{query}'.")

        time.sleep(2)  # Добавим паузу между запросами, чтобы не нагружать сервер Google слишком частыми запросами