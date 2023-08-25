from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ReusableMethods:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10
        self.actions = ActionChains(driver)

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def wait_until_element_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def type_and_press_enter_text_box(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        self.actions.move_to_element(element)
        self.actions.send_keys(text)
        self.actions.send_keys(Keys.ENTER)
        self.actions.perform()

    def switch_window(self):
        all_window_handles = self.driver.window_handles
        self.driver.switch_to.window(all_window_handles[1])



