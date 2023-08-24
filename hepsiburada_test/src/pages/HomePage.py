
from hepsiburada_test.src.pages.locators import HomePageLocators
from hepsiburada_test.src.ReusableMethods import ReusableMethods

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.rm = ReusableMethods(self.driver)


    def go_to_login_page(self):
        pass


    def verify_user(self):
        pass