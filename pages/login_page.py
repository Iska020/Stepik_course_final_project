from .base_page import BasePage
from .locators import LoginPageLocators
import time, random

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        print(f"Current url is {self.browser.current_url}")
        assert 'login' in self.browser.current_url, "There is not the correct url address"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def create_email_for_user_registration(self):
        email = str(time.time()) + "@fakemail.org"
        return email

    def create_password_for_user_registration(self):
        password = [str(random.randint(0, 9)) for i in range(10)]
        password = ''.join(password)
        return password

    def register_new_user(self, email, password):
        print(f"Email is {email}")
        print(f"Password is {password}")
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FIELD)
        repeat_password_field.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()