from selenium import webdriver

urls = ["https://dominternet.ru/saratov/", "https://dominternet.ru/novosibirsk/providers-to-address/",
        # "https://dominternet.ru/novosibirsk/providers/",
        # "https://dominternet.ru/novosibirsk/tariffs/",
        # "https://dominternet.ru/novosibirsk/rating/",
        # "https://dominternet.ru/novosibirsk/for-house/",
        # "https://dominternet.ru/",
        # "https://dominternet.ru/providers/rostelecom/",
        # "https://dominternet.ru/novosibirsk/providers/rostelecom/reviews/",
        # "https://dominternet.ru/providers/rostelecom/checkaddress/",
        # "https://dominternet.ru/novosibirsk/providers/rostelecom/"
        "https://www.youtube.com/"
        ]

class TestMakeScreens:
    def test_make_screenshot(self, driver):
        driver.set_window_size(1920, 8300)

        for url in urls:
            driver.get(url)
            site_name = url.split("/")[-2]
            screenshot_path = f"screenshot_{site_name}.png"
            driver.save_screenshot(screenshot_path)
