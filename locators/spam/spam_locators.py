from selenium.webdriver.common.by import By


class CheckSpam:
    ASSERT_BUTTON = (By.XPATH, "//button[contains(text(), 'Дополнительные')]")
    GO_TO_SBER = (By.XPATH, "//a[contains(text(), 'Перейти на сайт')]")
    INPUT_NUMBER = (By.XPATH, "//input[@class='dk-sbol-input dk-sbol-input_size_md']")
    BUTTON_CHECK = (By.XPATH, "(//span[@class='dk-sbol-button__content'])[1]")
    TEXT = (By.XPATH, "//div[contains(text(), 'Телефон не найден в базе мошенников')]")
    NEW_NUM = (By.XPATH, "//i[@title='Очистить']")