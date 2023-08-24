from hepsiburada_test.src.pages.locators.LoginPageLocators import LoginPageLocators
from hepsiburada_test.src.ReusableMethods import ReusableMethods


class LoginPage(LoginPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.rm = ReusableMethods(self.driver)

    def input_user_email(self, user_email):
        self.rm.wait_and_input_text(self.EMAIL_BOX, user_email)

    def click_login_button(self):
        self.rm.wait_and_click(self.GIRIS_YAP_BUTTON)

    def input_user_password(self, user_password):
        self.rm.wait_and_input_text(self.PASSWORD_BOX, user_password)

    def click_login_button2(self):
        self.rm.wait_and_click(self.GIRIS_YAP_BUTTON2)

    def verify_login_error_message(self):
        self.rm.wait_until_element_visible(self.ERROR)
