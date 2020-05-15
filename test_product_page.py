from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, offer):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=" + offer
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_correct_book_message()
    product_page.should_be_correct_price_message()
    