import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser=browser, url=link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = MainPage(browser=browser, url=link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_form_and_registration_form(browser):
    page = LoginPage(browser=browser, url=link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()