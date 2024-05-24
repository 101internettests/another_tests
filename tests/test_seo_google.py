from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver
from pages.providers_tests.data import query_new, query_new_spb, query_new_msk, query_new_ekb, query_new_ufa, query_new_krasnodar, query_new_novosibirsk
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
                results.append([website_to_check, query, website_rank, link])
            else:
                results.append([website_to_check, query, 'не найдено', 'нет ссылки'])
            time.sleep(2)

    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске', 'Ссылка'])
    df.to_excel('google.xlsx', index=False)


def test_find_competitors_and_website_rank_spb(driver):
    websites_to_check = ["101internet", "moskvaonline", "piter-online"]
    results = []
    for website_to_check in websites_to_check:
        for query in query_new_spb:
            driver.get(f"https://www.google.com/search?q={query}")
            search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
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
                results.append([website_to_check, query, website_rank, link])
            else:
                results.append([website_to_check, query, 'не найдено', 'нет ссылки'])
            time.sleep(2)

    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске', 'Ссылка'])
    df.to_excel('google_spb.xlsx', index=False)


def test_find_competitors_and_website_rank_msk(driver):
    websites_to_check = ["101internet", "moskvaonline", "piter-online"]
    results = []
    for website_to_check in websites_to_check:
        for query in query_new_msk:
            driver.get(f"https://www.google.com/search?q={query}")
            search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
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
                results.append([website_to_check, query, website_rank, link])
            else:
                results.append([website_to_check, query, 'не найдено', 'нет ссылки'])
            time.sleep(2)

    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске', 'Ссылка'])
    df.to_excel('google_msk.xlsx', index=False)


# def test_find_competitors_and_website_rank_ekb(driver):
#     websites_to_check = ["101internet", "moskvaonline", "piter-online"]
#     results = []
#     for website_to_check in websites_to_check:
#         for query in query_new_ekb:
#             driver.get(f"https://www.google.com/search?q={query}")
#             search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
#             website_rank = None
#             link = None
#
#             for index, result in enumerate(search_results, start=1):
#                 link_elements = result.find_elements(By.CSS_SELECTOR, "a")
#                 if link_elements:
#                     url = link_elements[0].get_attribute("href")
#                     if url and any(website in url for website in websites_to_check):
#                         website_rank = index
#                         link = url
#                         break
#
#             if website_rank is not None and link is not None:
#                 results.append([website_to_check, query, website_rank, link])
#             else:
#                 results.append([website_to_check, query, 'не найдено', 'нет ссылки'])
#             time.sleep(2)
#
#     df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске', 'Ссылка'])
#     df.to_excel('google_ekb.xlsx', index=False)


def test_find_competitors_and_website_rank_ufa(driver):
    websites_to_check = ["101internet", "moskvaonline", "piter-online"]
    results = []
    for website_to_check in websites_to_check:
        for query in query_new_ufa:
            driver.get(f"https://www.google.com/search?q={query}")
            search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
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
                results.append([website_to_check, query, website_rank, link])
            else:
                results.append([website_to_check, query, 'не найдено', 'нет ссылки'])
            time.sleep(2)

    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске', 'Ссылка'])
    df.to_excel('google_ufa.xlsx', index=False)


def test_find_competitors_and_website_rank_kransnodar(driver):
    websites_to_check = ["101internet", "moskvaonline", "piter-online"]
    results = []
    for website_to_check in websites_to_check:
        for query in query_new_krasnodar:
            driver.get(f"https://www.google.com/search?q={query}")
            search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
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
                results.append([website_to_check, query, website_rank, link])
            else:
                results.append([website_to_check, query, 'не найдено', 'нет ссылки'])
            time.sleep(2)

    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске', 'Ссылка'])
    df.to_excel('google_kransnodar.xlsx', index=False)


def test_find_competitors_and_website_rank_novosibirsk(driver):
    websites_to_check = ["101internet", "moskvaonline", "piter-online"]
    results = []
    for website_to_check in websites_to_check:
        for query in query_new_novosibirsk:
            driver.get(f"https://www.google.com/search?q={query}")
            search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
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
                results.append([website_to_check, query, website_rank, link])
            else:
                results.append([website_to_check, query, 'не найдено', 'нет ссылки'])
            time.sleep(2)

    df = pd.DataFrame(results, columns=['Сайт', 'Запрос', 'Место в поиске', 'Ссылка'])
    df.to_excel('google_novosibirsk.xlsx', index=False)