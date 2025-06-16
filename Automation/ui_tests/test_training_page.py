from selenium.webdriver.common.by import By

def test_training(browser):
    browser.get('https://magento.softwaretestingboard.com/')
    training_link = browser.find_element(By.ID, 'ui-id-7')
    training_link.click()

    title = browser.find_element(By.TAG_NAME, 'h1')
    assert title.text == 'Training'
