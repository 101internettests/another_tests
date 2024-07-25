import time
from locators.seo.parser_locators import SeoLocators
from pages.base_page import BasePage
import pandas as pd
results = []


class SeoPage(BasePage):
    results = []  # Переменная класса для хранения результатов

    def seo_func(self):
        url_before_redirect = self.driver.current_url

        try:
            if self.element_is_visible(SeoLocators.H1):
                h1 = self.element_is_visible(SeoLocators.H1).text
            else:
                h1 = "заголовка нет"  # Если H1 не найден, записываем текст

            self.results.append([h1, url_before_redirect])

            # Сохраняем результаты в DataFrame и экспортируем в Excel
            df = pd.DataFrame(self.results, columns=['h1', 'url_before_redirect'])
            df.to_excel('test.xlsx', index=False)

        except Exception as e:
            print(f"Ошибка: {e}. Пошел дальше.")

