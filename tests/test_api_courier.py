import allure
import pytest
from api import Courier
from data import CourierData


class TestApiCourier():

    @allure.title("Проверка создания курьера")
    @allure.description("Создается новый курьер если все даннные валидны, обязательные поля заполнены")
    def test_courier_create_success(self, del_courier):
        r = Courier.create(del_courier)
        assert r.status_code == 201 and r.json() == {"ok": True}

    @allure.title("Проверка создания курьера с уже существующим логином")
    @allure.description("При создании курьера с уже существующим логином появляется ошибка")
    def test_courier_create_same_login_error(self, del_courier):
        Courier.create(del_courier)
        r = Courier.create(CourierData.PAYLOAD_REGISTR_SAME)
        assert r.status_code == 409 and r.json() == {"message": "Этот логин уже используется"}

    @allure.title("Проверка создания курьера, без логина или пароля")
    @allure.description("При создании курьера появляется ошибка, если одного из обязательных полей нет")
    @pytest.mark.parametrize('num', ["login", "password"])
    def test_courier_create_empty_field_error(self, num):
        data = CourierData.PAYLOAD_REGISTR
        data[num] = None
        r = Courier.create(data)
        assert r.status_code == 400 and r.json() == {"message": "Недостаточно данных для создания учетной записи"}

    @allure.title("Проверка авторизации курьера")
    @allure.description("Курьер авторизуется если все даннные валидны, обязательные поля заполнены")
    def test_courier_login_success(self, registr_and_del_courier):
        r = Courier.login(registr_and_del_courier)
        assert r.status_code == 200 and "id" in r.json()

    @allure.title("Проверка авторизации курьера, с неправильным логином или паролем")
    @allure.description("При авторизации курьера с неправильным логином или паролем появляется ошибка")
    @pytest.mark.parametrize('num', ["login", "password"])
    def test_courier_login_wrong_data_error(self, registr_and_del_courier, num):
        data = registr_and_del_courier
        data[num] = 'error12'
        r = Courier.login(data)
        assert r.status_code == 404 and r.json() == {"message": "Учетная запись не найдена"}

    @allure.title("Проверка авторизации курьера, с пустым логином или паролем")
    @allure.description("При авторизации курьера с пустым логином или паролем появляется ошибка")
    @pytest.mark.parametrize('num', ["login", "password"])
    def test_courier_login_wrong_data_error(self, registr_and_del_courier, num):
        data = registr_and_del_courier
        data[num] = None
        r = Courier.login(data)
        assert r.status_code == 400 and r.json() == {"message":  "Недостаточно данных для входа"}
