from selenium.webdriver.common.by import By

def test_add_cart(browser):
    browser.get('https://magento.softwaretestingboard.com/argus-all-weather-tank.html')
    browser.find_element(By.ID, 'option-label-size-143-item-168').click()
    browser.find_element(By.ID, 'option-label-color-93-item-52').click()
    browser.find_element(By.ID, 'product-addtocart-button').click()





