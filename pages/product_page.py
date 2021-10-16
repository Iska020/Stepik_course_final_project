from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert add_to_basket_button, "There is not the add to basket button"

    def add_the_product_to_the_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_name_of_the_product_on_the_product_page(self):
        name_of_the_product_on_the_product_page = self.browser.find_element\
            (*ProductPageLocators.NAME_OF_THE_PRODUCT_ON_THE_PRODUCT_PAGE)
        assert name_of_the_product_on_the_product_page, "There is no name of the product on the product page"
        self.name_of_the_product_on_the_product_page_text = name_of_the_product_on_the_product_page.text
        print(f"Название книги на странице покупки {self.name_of_the_product_on_the_product_page_text}")

    def should_be_price_of_the_product_on_the_product_page(self):
        price_of_the_product_on_the_product_page = self.browser.find_element \
            (*ProductPageLocators.PRICE_OF_THE_PRODUCT_ON_THE_PRODUCT_PAGE)
        assert price_of_the_product_on_the_product_page, "There is no price of the product on the product page"
        self.price_of_the_product_on_the_product_page_text = price_of_the_product_on_the_product_page.text
        print(f"Цена книги на странице покупки {self.price_of_the_product_on_the_product_page_text}")

    def check_the_product_was_successfully_added_to_the_basket(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        print(success_message.text)
        basket_price_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE)
        print(basket_price_message.text)
        name_of_the_product = self.browser.find_element(*ProductPageLocators.NAME_OF_THE_PRODUCT_AFTER_ADDITION)
        print(f"Название книги {name_of_the_product.text}")
        assert name_of_the_product.text == self.name_of_the_product_on_the_product_page_text, \
            'Names of the product are different'
        price_of_the_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_BASKET_AFTER_ADDITION)
        print(f"Цена корзины {price_of_the_basket.text}")
        assert price_of_the_basket.text == self.price_of_the_product_on_the_product_page_text, \
            'Prices of the basket and the product are not equal'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_some_time(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
