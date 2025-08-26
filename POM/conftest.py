from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from typing import Generator


@pytest.fixture()
def browser() -> Generator[WebDriver, None, None]:
    chrome_browser: WebDriver = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()
