from selenium.webdriver.common.by import By
from random import randint


class SeoLocators:
    H1 = (By.XPATH, "//h1")
    TITLE = (By.XPATH, "(//meta)[1]")
    DESCRIPTION = (By.XPATH, "//meta[@itemprop='description']")