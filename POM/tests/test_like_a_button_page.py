from selenium.webdriver.remote.webdriver import WebDriver
from POM.pages.like_a_button import LikeAButton


def test_button2_exist(browser: WebDriver) -> None:
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    assert like_a_button.button_is_displayed

def test_button2_clicked(browser: WebDriver) -> None:
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    like_a_button.button_click()
    assert 'Submitted' == like_a_button.result_text
