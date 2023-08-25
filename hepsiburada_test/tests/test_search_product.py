import time

from hepsiburada_test.src.pages.HomePage import HomePage

import pytest


@pytest.mark.usefixtures("init_driver")
class TestSearchProduct:

    def test_search_product(self):
        home_page = HomePage(self.driver)

        # Launch the browser and navigate to www.hepsiburada.com.
        home_page.go_to_home_page()
        home_page.accept_cookies()

        # Enter a specific product name in the search bar and search it.
        home_page.search('Samsung')

        # Apply relevant filters, such as price range or customer ratings.
        time.sleep(2)
        home_page.determine_lowest_price_range("7000")
        home_page.determine_highest_price_range("15000")
        home_page.click_price_search_button()

        # Select a product from the search results.
        home_page.click_first_product()
        home_page.switch_windows()
        time.sleep(1)

        # Verify that the product page is displayed.
        home_page.verify_title('Samsung')

        # Add the product to the cart.
        home_page.click_add_to_cart()

        # Verify that the product is successfully added to the cart.
        home_page.verify_product_in_cart()
