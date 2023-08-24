from selenium.webdriver.common.by import By



class LoginPageLocators:

    EMAIL_BOX = (By.ID, 'txtUserName')
    GIRIS_YAP_BUTTON = (By.ID, 'btnLogin')
    PASSWORD_BOX = (By.ID, 'txtPassword')
    ERROR = (By.CSS_SELECTOR, 'div.hb-fznyBo.btfxMO.sttyttdiwdu')
    GIRIS_YAP_BUTTON2 = (By.ID, 'btnEmailSelect')