from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_BOX = (By.ID, 'txtUserName')
    GIRIS_YAP_BUTTON = (By.ID, 'btnLogin')
    PASSWORD_BOX = (By.ID, 'txtPassword')
    ERROR = (By.XPATH, "//div[@type='ERROR']")
    GIRIS_YAP_BUTTON2 = (By.ID, 'btnEmailSelect')
