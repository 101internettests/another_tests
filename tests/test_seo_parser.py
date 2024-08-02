from time import sleep
from pages.seo.parser_page import SeoPage
import pandas as pd
import random
from pages.url_page import raw_urls


class TestParser:
    def test_parser(self, driver):
            for url in raw_urls:
                try:
                    seo = SeoPage(driver, url)
                    seo.open()
                    seo.seo_func(url)
                except:
                    print(f"site f[{url}] doesn't open")