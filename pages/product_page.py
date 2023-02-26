from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        # добавить продукт в корзину
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_product_add_confirm_msg(self):
        # проверка, что сообщение о добавлении продукта в корзину отобразилось
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_MSG), "Сообщение о том, что товар добавлен в корзину, не отображается"

    def should_be_equal_product_name(self):
        # проверка, что название продукта в сообщении о добавлении совпадает с названием продукта
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MSG).text
        assert product_name == product_name_in_msg, "Название товара в сообщении не соответствует названию товара"

    def should_be_cart_cost_msg(self):
        # проверка отображения сообщения о стоимости товара в корзине
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST_MSG), "Сообщение о стоимости товаров, не отображается"

    def should_be_equal_price(self):
        # проверка, что цена в сообщении о стоимости товара в корзине совпадает с ценой товара
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        cart_price_msg = self.browser.find_element(*ProductPageLocators.CART_PRICE_MSG).text
        assert item_price == cart_price_msg, "Цена товара в сообщении не соответствует цене товара"

    def should_not_be_success_message(self):
        # проверка, что сообщение о добавлении товара в корзину не должно отображаться
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_MSG), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        # проверка, что сообщение о добавлении товара в корзину должно исчезнуть
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_MSG), "Success message is presented, but should disappear"