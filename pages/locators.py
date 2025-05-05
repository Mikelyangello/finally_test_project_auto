from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[contains(@href,"/basket/")]')


class BasketPageLocators:
    BASKET_FORM = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner>p')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    NOTIFICATION_PRODUCT_ADD_TO_BASKET = (By.XPATH, '//div[@class="alertinner "]/strong')
    NOTIFICATION_BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
