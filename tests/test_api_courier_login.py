import allure
import pytest
from api import Courier
from data import CourierData


class TestApiCourierLogin():

    @allure.title("Проверка авторизации курьера")
    @allure.description("Курьер авторизуется если все даннные валидны, обязательные поля заполнены")
    def test_courier_login_success(self, reg_and_del_courier):
        data = reg_and_del_courier
        r = Courier.login(data)
        assert r.status_code == 200 and "id" in r.json()

    @allure.title("Проверка авторизации курьера, с неправильным логином или паролем")
    @allure.description("При авторизации курьера с неправильным логином или паролем появляется ошибка")
    @pytest.mark.parametrize('num', ["login", "password"])
    def test_courier_login_wrong_data_error(self, reg_and_del_courier, num):
        data = reg_and_del_courier
        data[num] = "error12"
        r = Courier.login(data)
        assert r.status_code == 404 and r.json()["message"] == "Учетная запись не найдена"

    @allure.title("Проверка авторизации курьера, с пустым логином или паролем")
    @allure.description("При авторизации курьера с пустым логином или паролем появляется ошибка")
    @pytest.mark.parametrize('num', ["login", "password"])
    def test_courier_login_empty_field_error(self, reg_and_del_courier, num):
        data = reg_and_del_courier
        data[num] = ""
        r = Courier.login(data)
        assert r.status_code == 400 and r.json()["message"] == "Недостаточно данных для входа"
