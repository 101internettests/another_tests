import time
from locators.seo.parser_locators import SeoLocators
from pages.base_page import BasePage
import pandas as pd
results = []


class SeoPage(BasePage):
    results = []  # Переменная класса для хранения результатов

    def seo_func(self, url: str):
        url_after_redirect = self.driver.current_url

        try:
            if self.element_is_visible(SeoLocators.H1):
                h1 = self.element_is_visible(SeoLocators.H1).text
            else:
                h1 = "заголовка нет"

            if self.element_is_visible(SeoLocators.META):
                meta = self.element_is_visible(SeoLocators.META).text
            else:
                meta = "описания нет"

            if self.element_is_visible(SeoLocators.H2):
                h2 = self.element_is_visible(SeoLocators.H2).text
            else:
                h2 = "заголовка 2 нет"

            if self.element_is_visible(SeoLocators.TITLE):
                title = self.element_is_visible(SeoLocators.TITLE).text
            else:
                title = "описания нет"

            self.results.append([h1, h2, meta, title, url,  url_after_redirect])
            df = pd.DataFrame(self.results, columns=['h1', 'h2', 'meta',  'title', 'url', 'url_after_redirect' ])
            df.to_excel('test.xlsx', index=False)

        except Exception as e:
            print(f"Ошибка: {e}. Пошел дальше.")

