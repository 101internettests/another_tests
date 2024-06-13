from time import sleep
from pages.seo.parser_page import SeoPage
import pandas as pd
import random


urls = []
class TestParser:
    def test_parser(self, driver):
        urls = ['https://101internet.ru', 'https://piter-online.net/']
        for url in urls:
            seo = SeoPage(driver, url)
            seo.open()
            seo.seo_func()