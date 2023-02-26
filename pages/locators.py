from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    CONFIRM_REGISTER_PASSWORD = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_ADD_MSG = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_NAME_IN_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_COST_MSG = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in")
    ITEM_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    CART_PRICE_MSG = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")