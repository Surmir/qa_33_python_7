import allure
import pytest
from api import OrdersApi
from data import OrderData
from data import OrderResponse as correct_r


class TestApiOrders():

    @allure.title("Проверка создания заказа, с разными данными в color")
    @allure.description("Проверка создания заказа при заполнении поля цвет: " \
    "один цвет, два цвета, без цвета")
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_orders_create_success(self, color):
        data = OrderData.PAYLOAD
        data["color"] = color
        r = OrdersApi.create(data)
        assert r.status_code == correct_r.CODE_SUCCESS_CREATE and correct_r.BODY_SUCCESS_CREATE in r.json()

    @allure.title("Проверка получения списка заказов")
    @allure.description("Проверка возвращения списка заказов в ответе")
    def test_orders_get_order_list_success(self):
        r = OrdersApi.get_list_orders()
        assert r.status_code == correct_r.CODE_SUCCESS_GET_LIST and correct_r.BODY_SUCCESS_GET_LIST in r.json()
