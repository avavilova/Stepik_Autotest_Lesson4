from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_msg(self):
        #проверка наличия текста об отсутствии товаров в корзине
        assert self.is_element_present(*BasketPageLocators.CART_EMPTY_MSG), "'Cart is empty' message is not presented, but should be"

    def should_goods_not_present(self):
        # проверка отсутствия товаров в пустой корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket contains items, but shouldn't"