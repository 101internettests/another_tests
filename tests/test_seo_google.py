from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver
from pages.providers_tests.data import query_new, query_new_spb, query_new_msk
import csv
import time
from selenium.webdriver.common.by import By
import pandas as pd
from tabulate import tabulate
import pandas as pd

def test_find_competitors_and_website_rank(driver):
    websites_to_check = ["101internet", "moskvaonline", "piter-online"]
    results = []
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

            if website_rank is not None:
                results.append([website_to_check, query, website_rank])
            else:
                results.append([website_to_check, query, 'не найдено'])
            time.sleep(2)
    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске'])
    df.to_excel('website_results.xlsx', index=False)

def test_find_competitors_and_website_rank_spb(driver):
    websites_to_check = ["101internet", "moskvaonline", "piter-online"]
    results = []
    for website_to_check in websites_to_check:
        for query in query_new_spb:
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

            if website_rank is not None:
                results.append([website_to_check, query, website_rank])
            else:
                results.append([website_to_check, query, 'не найдено'])
            time.sleep(2)
    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске'])
    df.to_excel('website_results_spb.xlsx', index=False)


def test_find_competitors_and_website_rank_msk(driver):
    websites_to_check = ["101internet", "moskvaonline", "piter-online"]
    results = []
    for website_to_check in websites_to_check:
        for query in query_new_msk:
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

            if website_rank is not None:
                results.append([website_to_check, query, website_rank])
            else:
                results.append([website_to_check, query, 'не найдено'])
            time.sleep(2)
    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске'])
    df.to_excel('website_results_msk.xlsx', index=False)