from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_the_basket_is_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "The basket is empty"

    def check_the_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "The basket is not empty"

    def check_the_presence_of_message_about_empty_basket(self):
        print(self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET).text.split(".")[0])
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET).text.split(".")[0], \
            "The basket is not empty"