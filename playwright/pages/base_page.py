from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, browser: WebDriver) -> None:
        self.browser: WebDriver = browser

    def find(self, args: Tuple[str, str]) -> WebElement:
        return self.browser.find_element(*args)
