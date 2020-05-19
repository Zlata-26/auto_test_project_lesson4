from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty, but should be"

    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        expected_msg = "Your basket is empty"
        real_msg = empty_basket_message.text
        assert expected_msg in real_msg, f"No '{expected_msg}' message in '{real_msg}'"        
