from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):


    def add_product_to_basket(self):
        
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click() 

    def solve_quiz_and_get_code(self):
        
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_correct_book_message(self):
        
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        book_message = self.browser.find_element(*ProductPageLocators.BOOK_MESSAGE)
        assert book_title.text == book_message.text, "Book message is not correct"

    def should_be_correct_price_message(self):
        
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)
        assert book_price.text == price_message.text, "Price message is not correct" 

    def should_not_be_success_message(self):

        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    





