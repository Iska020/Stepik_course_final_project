from .base_page import BasePage
#from .locators import MainPageLocators

class MainPage(BasePage):
    pass
    #def go_to_login_page(self):
        #print(f"Current url is {self.browser.current_url}")
        #login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #login_link.click()

    #def should_be_login_link(self):
        # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        #assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"