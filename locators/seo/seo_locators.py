from selenium.webdriver.common.by import By
from random import randint


class SEOLocators:
    BLOCKS_OF_CITES = (By.XPATH, "//li[@class]")
    LINKS = (By.XPATH, "//div[@class='Path Organic-Path path organic__path']//a[@class]//b")
