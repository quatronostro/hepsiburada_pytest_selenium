
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

