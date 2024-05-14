from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver
from pages.providers_tests.data import urlsyandex, path_yandex
from pages.seo.seo_page import SeoPage


websites_to_check = ["101internet.ru"]
                     # "piter-online.net","moskvaonline.ru"]


def test_find_competitors_and_website_rank(driver):
    # websites_to_check = ["101internet.ru"]
    for website_to_check in websites_to_check:
        for url, filename in zip(urlsyandex, path_yandex):
            # print(f"Беру ссылку {url}")
            driver.get(url)
            search_results = driver.find_elements(By.CSS_SELECTOR, "li[data-cid]")
            website_rank = None

            for index, result in enumerate(search_results, start=1):
                link = result.find_elements(By.XPATH, "a")
                if link:
                    url = link[0].get_attribute("href")
                    if url is not None and any(website in url for website in websites_to_check):
                        website_rank = index
                        break

            if website_rank:
                print(f"Сайт '{website_to_check}' был на позиции {website_rank} в результатах по запросу '{filename}'.")
            else:
                print(f"Сайт '{website_to_check}' не был найден в результатах по запросу '{filename}'.")

            time.sleep(2)

