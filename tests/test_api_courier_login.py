import allure
import pytest
from api import CourierApi
from data import CourierLoginResponse as correct_r
from helpers import CourierData


class TestApiCourierLogin():

    @allure.title("Проверка авторизации курьера")
    @allure.description("Курьер авторизуется если все даннные валидны, обязательные поля заполнены")
    def test_courier_login_success(self, reg_and_del_courier):
        data = CourierData.PAYLOAD_LOGIN
        r = CourierApi.login(data)
        assert r.status_code == correct_r.CODE_SUCCESS and correct_r.BODY_SUCCESS in r.json()

    @allure.title("Проверка авторизации курьера, с неправильным логином или паролем")
    @allure.description("При авторизации курьера с неправильным логином или паролем появляется ошибка")
    @pytest.mark.parametrize('data', CourierData.TEST_WRONG_DATA)
    def test_courier_login_wrong_data_error(self, reg_and_del_courier, data):
        data = data
        r = CourierApi.login(data)
        assert r.status_code == correct_r.CODE_ERROR_WRONG_DATA and r.json()["message"] == correct_r.BODY_ERROR_WRONG_DATA

    @allure.title("Проверка авторизации курьера, с пустым логином или паролем")
    @allure.description("При авторизации курьера с пустым логином или паролем появляется ошибка")
    @pytest.mark.parametrize('data', CourierData.TEST_EMPTY_FIELD)
    def test_courier_login_empty_field_error(self, reg_and_del_courier, data):
        data = data
        r = CourierApi.login(data)
        assert r.status_code == correct_r.CODE_ERROR_EMPTY_FIELD and r.json()["message"] == correct_r.BODY_ERROR_EMPTY_FIELD
