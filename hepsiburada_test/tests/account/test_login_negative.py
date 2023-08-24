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

        # go to login page
        home_page.open_login_page()

        # enter existing email
        login_page.input_user_email('berke.bar@hotmail.com')

        # click "Giriş Yap" button
        login_page.click_login_button()

        # enter incorrect password
        login_page.input_user_password('1234')





