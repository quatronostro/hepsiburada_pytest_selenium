from hepsiburada_test.src.pages.locators.HomePageLocators import HomePageLocators
from hepsiburada_test.src.ReusableMethods import ReusableMethods
from hepsiburada_test.src.utils.config_helpers import get_base_url


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.rm = ReusableMethods(self.driver)

    def go_to_home_page(self):
        base_url = get_base_url()
        self.driver.get(base_url)

    def accept_cookies(self):
        self.rm.wait_and_click(self.COOKIES)

    def open_login_page(self):
        self.rm.wait_and_click(self.LOGIN_BUTTON)
        self.rm.wait_and_click(self.GIRIS_YAP_BUTTON)

    def search(self, text):
        self.rm.wait_and_click(self.SEARCH_BOX)
        self.rm.type_and_press_enter_text_box(self.SEARCH_BOX, text)

    def determine_lowest_price_range(self, text):
        self.rm.wait_and_input_text(self.PRICE_RANGE_LOWEST, text)

    def determine_highest_price_range(self, text):
        self.rm.wait_and_input_text(self.PRICE_RANGE_HIGHEST, text)

    def click_price_search_button(self):
        self.rm.wait_and_click(self.PRICE_SEARCH_BUTTON)

    def click_first_product(self):
        self.rm.wait_and_click(self.FIRST_PRODUCT)

    def switch_windows(self):
        self.rm.switch_window()

    def verify_title(self, text):
        title = self.driver.title
        assert title.__contains__(text)

    def click_add_to_cart(self):
        self.rm.wait_and_click(self.ADD_TO_CART)

    def verify_product_in_cart(self):
        self.rm.wait_until_element_visible(self.VERIFY_PRODUCT_IN_CART)


