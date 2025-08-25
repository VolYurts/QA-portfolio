from playwright.sync_api import expect
from .base_page import BasePage


class SimplePage(BasePage):
    url = 'https://www.qa-practice.com/elements/button/simple'

    def __init__(self, page, button_selector='#submit-id-submit', result_selector='#result-text'):
        super().__init__(page)
        self.button_selector = button_selector
        self.result_selector = result_selector

    def _button(self):
        return self.page.locator(self.button_selector)

    def _result(self):
        return self.page.locator(self.result_selector)

    def check_button_exists(self):
        expect(self._button()).to_be_visible()

    def click_button(self):
        self._button().click()

    def check_result_text(self, text):
        expect(self._result()).to_have_text(text)
