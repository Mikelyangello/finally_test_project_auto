from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), \
            f"There is NO BASKET BUTTON on page with locator\n{ProductPageLocators.ADD_TO_BASKET[1]}"

    def should_be_add_item_to_basket_notification(self):
        assert self.is_element_present(*ProductPageLocators.NOTIFICATION_PRODUCT_ADD_TO_BASKET), \
            f"There is NO NOTIFICATION of added item to basket on page with locator\n\
                {ProductPageLocators.NOTIFICATION_PRODUCT_ADD_TO_BASKET[1]}"
        product_name_from_card = self.get_product_name()
        product_name_from_notification = self.browser.find_element(*ProductPageLocators.NOTIFICATION_PRODUCT_ADD_TO_BASKET).text
        assert product_name_from_card == product_name_from_notification, \
            f"NAMES of products IS NOT similar\n\
                from card: {product_name_from_card} != {product_name_from_notification} - from notification"

    def should_be_correct_price_of_product(self):
        assert self.is_element_present(*ProductPageLocators.NOTIFICATION_BASKET_PRICE), \
            f"There is NO NOTIFICATION of basket price on page with locator\n\
                {ProductPageLocators.NOTIFICATION_BASKET_PRICE[1]}"
        product_price_from_card = self.get_product_price()
        product_price_from_notification = self.browser.find_element(*ProductPageLocators.NOTIFICATION_BASKET_PRICE).text
        assert product_price_from_card == product_price_from_notification, \
            f"PRICES of products IS NOT similar\n\
                from card: {product_price_from_card} != {product_price_from_notification} - from notification"


