from selenium.webdriver.common.by import By
from random import randint


class SeoLocators:
    H1 = (By.XPATH, "//h1")
    H2 = (By.XPATH, "(//h2)[1]")
    META = (By.XPATH, "(//meta)[1]")
    TITLE = (By.XPATH, "(//title)[1]")
    DESCRIPTION = (By.XPATH, "//meta[@itemprop='description']")