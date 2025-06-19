from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions


def test_search(browser):
    browser.get('https://magento.softwaretestingboard.com/')

    query = "shirt"
    search_input = browser.find_element(By.ID, 'search')
    search_input.send_keys(query)

    search_button = browser.find_element(By.CSS_SELECTOR, 'button.action.search')
    search_button.click()

    WebDriverWait(browser, 10).until(
        expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a.product-item-link'))
    )

    product_titles = browser.find_elements(By.CSS_SELECTOR, 'a.product-item-link')
    titles_text = [title.text.lower() for title in product_titles]

    assert any(query in title for title in titles_text), "No products found with the search query"

