from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver
from pages.providers_tests.data import urlsyandex, path_yandex, url_ms, path_yandex_msk
import pandas as pd


websites_to_check = ["101internet.ru", "piter-online.net", "moskvaonline.ru"]


def test_find_competitors_and_website_rank(driver):
    results = []
    for website_to_check in websites_to_check:
        for url, filename in zip(urlsyandex, path_yandex):
            driver.get(url)
            search_results = driver.find_elements(By.CSS_SELECTOR, "li[data-cid]")
            website_rank = None
            link = None

            for index, result in enumerate(search_results, start=1):
                link_elements = result.find_elements(By.CSS_SELECTOR, "a")
                if link_elements:
                    url = link_elements[0].get_attribute("href")
                    if url and any(website in url for website in websites_to_check):
                        website_rank = index
                        link = url
                        break

            if website_rank is not None and link is not None:
                results.append([website_to_check, filename, website_rank, link])
            else:
                results.append([website_to_check, filename, 'не найдено', 'нет ссылки'])

            time.sleep(2)

    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске', 'Ссылка'])
    df.to_excel('results.xlsx', index=False)


def test_find_competitors_and_website_rank_msk(driver):
    results = []
    for website_to_check in websites_to_check:
        for url, filename in zip(url_ms, path_yandex_msk):
            driver.get(url)
            search_results = driver.find_elements(By.CSS_SELECTOR, "li[data-cid]")
            website_rank = None
            link = None

            for index, result in enumerate(search_results, start=1):
                link_elements = result.find_elements(By.CSS_SELECTOR, "a")
                if link_elements:
                    url = link_elements[0].get_attribute("href")
                    if url and any(website in url for website in websites_to_check):
                        website_rank = index
                        link = url
                        break

            if website_rank is not None and link is not None:
                results.append([website_to_check, filename, website_rank, link])
            else:
                results.append([website_to_check, filename, 'не найдено', 'нет ссылки'])

            time.sleep(2)

    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске', 'Ссылка'])
    df.to_excel('results_msk.xlsx', index=False)