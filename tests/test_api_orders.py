import allure
import pytest
from api import Orders
from data import OrderData


class TestApiOrders():

    @allure.title("Проверка создания заказа, с разными данными в color")
    @allure.description("Проверка создания заказа при заполнении поля цвет: " \
    "один цвет, два цвета, без цвета")
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_orders_create_success(self, color):
        data = OrderData.PAYLOAD
        data["color"] = color
        r = Orders.create(data)
        assert r.status_code == 201 and "track" in r.json()

    @allure.title("Проверка получения списка заказов")
    @allure.description("Проверка возвращения списка заказов в ответе")
    def test_orders_get_order_list_success(self):
        r = Orders.get_list_orders()
        assert r.status_code == 200 and "orders" in r.json()
