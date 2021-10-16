import pytest
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

bugged_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7'

@pytest.mark.skip
@pytest.mark.parametrize('link_of_the_site_with_promo_action',
         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
           pytest.param(bugged_link, marks=pytest.mark.xfail),
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link_of_the_site_with_promo_action):
    page = ProductPage(browser=browser, url=link_of_the_site_with_promo_action)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_be_name_of_the_product_on_the_product_page()
    page.should_be_price_of_the_product_on_the_product_page()
    page.add_the_product_to_the_basket()
    page.solve_quiz_and_get_code()
    page.check_the_product_was_successfully_added_to_the_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_the_product_to_the_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_the_product_to_the_basket()
    page.should_not_be_success_message_after_some_time()

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