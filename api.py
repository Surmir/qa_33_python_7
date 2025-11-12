from data import Api
import requests
import allure


class Courier():

    @staticmethod
    @allure.step("Запрос на получение логина курьера в системе")
    def login(data):
        return requests.post(Api.COURUER_LOGIN, data=data)
    
    @staticmethod
    @allure.step("Запрос на создание нового курьера")
    def create(data):
        return requests.post(Api.COURUER_CREATE, data=data)
    
    @staticmethod
    @allure.step("Запрос на удаление курьера по id")
    def delete(id):
        api_with_id = Api.COURUER_DELETE.replace(':id', id)
        return requests.delete(api_with_id)

class Orders():

    @staticmethod
    @allure.step("Запрос на получение списка заказов")
    def get_list_orders():
        return requests.get(Api.ORDERS)
    
    @staticmethod
    @allure.step("Запрос на создание заказа")
    def create(data):
        return requests.post(Api.ORDERS, data=data)
    
    @staticmethod
    @allure.step("Запрос на отмену заказа")
    def cancel(track):
        return requests.put(Api.ORDERS_CANCEL, data=track)
