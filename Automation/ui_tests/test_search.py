from selenium.webdriver.common.by import By


def test_search(browser):
    browser.get('https://magento.softwaretestingboard.com/')

    query = "shirt"
    search_input = browser.find_element(By.ID, 'search')
    search_input.send_keys(query)

    search_button = browser.find_element(By.CSS_SELECTOR, 'button.action.search')
    search_button.click()

    product_titles = browser.find_elements(By.CSS_SELECTOR, 'a.product-item-link')
    titles_text = [title.text.lower() for title in product_titles]

    assert any(query in title for title in titles_text), "No products found with the search query"
