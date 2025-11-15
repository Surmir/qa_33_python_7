from data import Api
import requests
import allure


class CourierApi():

    @staticmethod
    @allure.step("Запрос на авторизацию курьера в системе")
    def login(data):
        return requests.post(Api.COURUER_LOGIN, json=data, timeout=5)
    
    @staticmethod
    @allure.step("Запрос на создание нового курьера")
    def create(data):
        return requests.post(Api.COURUER_CREATE, json=data, timeout=10)
    
    @staticmethod
    @allure.step("Запрос на удаление курьера по id")
    def delete(id):
        id_str = str(id)
        api_with_id = Api.COURUER_DELETE.replace(':id', id_str)
        return requests.delete(api_with_id)

class OrdersApi():

    @staticmethod
    @allure.step("Запрос на получение списка заказов")
    def get_list_orders():
        return requests.get(Api.ORDERS)
    
    @staticmethod
    @allure.step("Запрос на создание заказа")
    def create(data):
        return requests.post(Api.ORDERS, json=data, timeout=5)
