from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_product_add_confirm_msg(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_MSG), "Сообщение о том, что товар добавлен в корзину, не отображается"

    def should_be_equal_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MSG).text
        assert product_name == product_name_in_msg, "Название товара в сообщении не соответствует названию товара"

    def should_be_cart_cost_msg(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST_MSG), "Сообщение о стоимости товаров, не отображается"

    def should_be_equal_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        cart_price_msg = self.browser.find_element(*ProductPageLocators.CART_PRICE_MSG).text
        assert item_price == cart_price_msg, "Цена товара в сообщении не соответствует цене товара"