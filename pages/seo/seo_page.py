import time
from locators.seo.seo_locators import SEOLocators
from pages.base_page import BasePage


class SeoPage(BasePage):
    def seo_func(self):
        element = self.elements_are_visible(SEOLocators.LINKS)
        if element is not None:
            # text = element.text
            print(element)
        else:
            print("Элемент не найден или не видим")
