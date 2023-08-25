
from selenium.webdriver.common.by import By



class HomePageLocators:

    COOKIES = (By.ID, 'onetrust-accept-btn-handler')
    LOGIN_BUTTON = (By.ID, 'myAccount')
    GIRIS_YAP_BUTTON = (By.ID, 'login')

    SEARCH_BOX = (By.XPATH, "//*[@class='sf-OldHeader-MSHyIpigOpMg8jl1slwR']")
    PRICE_RANGE_LOWEST = (By.XPATH, "//*[@id='fiyat']/div/div/div/div[1]/div/div[1]/input")
    PRICE_RANGE_HIGHEST = (By.XPATH, "//*[@id='fiyat']/div/div/div/div[1]/div/div[2]/input")
    PRICE_SEARCH_BUTTON = (By.XPATH, "//*[@id='fiyat']/div/div/div/div[1]/button")
    FIRST_PRODUCT = (By.XPATH, "//*[@data-test-id='product-card-name'][1]")
    ADD_TO_CART = (By.ID, 'addToCart')
    VERIFY_PRODUCT_IN_CART = (By.XPATH, "//span[text()=' Ürün sepetinizde']")

