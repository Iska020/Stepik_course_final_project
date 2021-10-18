import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser=browser, url=link)
        # открываем страницу
        page.open()
        # выполняем метод страницы — переходим на страницу логина
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser=browser, url=link)
        page.open()
        page.should_be_login_link()

def test_guest_should_see_login_form_and_registration_form(browser):
    page = MainPage(browser=browser, url=link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser=browser, url=link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page.check_the_basket_is_empty()
    page.check_the_presence_of_message_about_empty_basket()
