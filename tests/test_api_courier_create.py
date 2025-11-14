import allure
import pytest
from api import CourierApi
from helpers import CourierData
from data import CourierCreateResponse as correct_r


class TestApiCourier():

    @allure.title("Проверка создания курьера")
    @allure.description("Создается новый курьер если все даннные валидны, обязательные поля заполнены")
    def test_courier_create_success(self, reg_and_del_courier):
        r = reg_and_del_courier
        assert r.status_code == correct_r.CODE_SUCCESS and r.json() == correct_r.BODY_SUCCESS

    @allure.title("Проверка создания курьера с уже существующим логином")
    @allure.description("При создании курьера с уже существующим логином появляется ошибка")
    def test_courier_create_same_login_error(self, reg_and_del_courier):
        r = CourierApi.create(CourierData.PAYLOAD_REGISTR_SAME)
        assert r.status_code == correct_r.CODE_ERROR_SAME_LOGIN and r.json()["message"] == correct_r.BODY_ERROR_SAME_LOGIN
        
    @allure.title("Проверка создания курьера, без логина или пароля")
    @allure.description("При создании курьера появляется ошибка, если одного из обязательных полей нет")
    @pytest.mark.parametrize('num', ["login", "password"])
    def test_courier_create_empty_field_error(self, num):
        data = CourierData.PAYLOAD_REGISTR
        data[num] = ""
        r = CourierApi.create(data)
        assert r.status_code == correct_r.CODE_ERROR_EMPTY_FIELD and r.json()["message"] == correct_r.BODY_ERROR_EMPTY_FIELD
