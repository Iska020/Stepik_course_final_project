from selenium.webdriver.common.by import By

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
   ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
   SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")
   NAME_OF_THE_PRODUCT_AFTER_ADDITION = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")
   NAME_OF_THE_PRODUCT_ON_THE_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main h1")
   BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner p:nth-child(1)")
   PRICE_OF_THE_PRODUCT_ON_THE_PRODUCT_PAGE =(By.CSS_SELECTOR, "p.price_color")
   PRICE_OF_THE_BASKET_AFTER_ADDITION = (By.CSS_SELECTOR, ".alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
