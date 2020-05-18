from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, offer):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=" + offer
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_correct_book_message()
    product_page.should_be_correct_price_message()
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.is_not_element_present(By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.is_not_element_present(By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.is_disappeared(By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")
    product_page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    basket_page = BasketPage(browser, link)
    basket_page.open() 
    basket_page.go_to_basket_page()
    basket_page.is_not_element_present(By.CSS_SELECTOR, "#basket_formset")
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


