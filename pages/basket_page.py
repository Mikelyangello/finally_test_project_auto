from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.is_a_needed_word_in_page_link('basket')

    def should_be_a_basket_form(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FORM), \
            f"Basket form with locator '{BasketPageLocators.BASKET_FORM[1]}' NOT FOUND"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), \
            f"Basket form with locator '{BasketPageLocators.BASKET_FORM[1]}' IS ON PAGE"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            f"Empty basket message locator '{BasketPageLocators.EMPTY_BASKET_TEXT[1]}' NOT FOUND"
        message_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text.split('.')[0]
        assert message_text in self.mc.empty_basket_texts, \
            f"The empty basket message with '{message_text}' NOT FOUND in site dictionary: {self.mc.empty_basket_texts}"

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            f"Empty basket message is on page, locator:{BasketPageLocators.EMPTY_BASKET_TEXT[1]}"
