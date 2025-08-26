from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


button_selector: Tuple[str, str] = (By.ID, 'submit-id-submit')
result_selector: Tuple[str, str] = (By.ID, 'result-text')


class SimpleButtonPage(BasePage):
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)

    def open(self) -> None:
        self.browser.get('https://www.qa-practice.com/elements/button/simple')

    def button(self) -> WebElement:
        return self.find(button_selector)

    def button_is_displayed(self) -> bool:
        return self.button().is_displayed()

    def click_button(self) -> None:
        self.button().click()

    def result(self) -> WebElement:
        return self.find(result_selector)

    @property
    def result_text(self) -> str:
        return self.result().text

