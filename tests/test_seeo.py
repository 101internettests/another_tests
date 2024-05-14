import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.providers_tests.data import urlsyandex, path_yandex

websites_to_check = ["101internet.ru"]



def test_find_website_rank_on_yandex(website, search_query, driver):
    driver.get(urlsyandex)

    search_input = driver.find_element(By.NAME, "text")
    search_input.clear()
    search_input.send_keys(search_query)
    search_input.submit()

    time.sleep(3)  # Даем странице время загрузить результаты поиска

    search_results = driver.find_elements(By.CSS_SELECTOR, "li.serp-item")

    website_rank = None

    for index, result in enumerate(search_results, start=1):
        try:
            link = result.find_element(By.CSS_SELECTOR, "a.organic__url")
            if website in link.get_attribute("href"):
                website_rank = index
                break
        except Exception as e:
            print(e)
            continue

    return website_rank


driver = webdriver.Chrome()
for website, query in zip(websites_to_check, path_yandex):
    rank = test_find_website_rank_on_yandex(website, query, driver)
    if rank:
        print(f"Сайт '{website}' был на позиции {rank} в результатах по запросу '{query}'.")
    else:
        print(f"Сайт '{website}' не был найден в результатах по запросу '{query}'.")

driver.quit()