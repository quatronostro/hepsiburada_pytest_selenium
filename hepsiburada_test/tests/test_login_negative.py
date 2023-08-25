import time

from hepsiburada_test.src.pages.HomePage import HomePage
from hepsiburada_test.src.pages.LoginPage import LoginPage

import pytest


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    def test_login_none_existing_user(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)

        # go to hepsiburada home page
        home_page.go_to_home_page()
        time.sleep(1)

        # accept cookies
        home_page.accept_cookies()
        time.sleep(1)

        # go to login page
        home_page.open_login_page()
        time.sleep(1)

        # enter existing email
        login_page.input_user_email('berke.bar@hotmail.com')
        time.sleep(1)

        # click "Giriş Yap" button
        login_page.click_login_button()
        time.sleep(1)

        # enter incorrect password
        login_page.input_user_password('1234')
        time.sleep(1)

        # click "Giriş Yap" button
        login_page.click_login_button2()
        time.sleep(1)

        # verify login error message
        login_page.verify_login_error_message()
        time.sleep(1)
