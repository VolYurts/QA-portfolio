from selenium.webdriver.remote.webdriver import WebDriver
from POM.pages.simple_button import SimpleButtonPage


def test_button1_exist(browser: WebDriver) -> None:
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()

def test_button1_clicked(browser: WebDriver) -> None:
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.click_button()
    assert 'Submitted' == simple_page.result_text
