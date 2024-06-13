import time
from locators.seo.parser_locators import SeoLocators
from pages.base_page import BasePage
import pandas as pd
results = []


class SeoPage(BasePage):
    def seo_func(self):
        h1 = self.element_is_visible(SeoLocators.H1).text
        title = self.element_is_present(SeoLocators.TITLE).text
        print(h1)
        print(title)
        results.append([h1, title])
        df = pd.DataFrame(results, columns=['h1', 'title'])
        df.to_excel('test.xlsx', index=False)