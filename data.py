from urls import Url


class Api():

    url = Url.YANDEX_SCOOTER

    COURUER_LOGIN = f"{url}/api/v1/courier/login"
    COURUER_CREATE = f"{url}/api/v1/courier"
    COURUER_DELETE = f"{url}/api/v1/courier/:id"
    ORDERS = f"{url}/api/v1/orders"

class OrderData():

    PAYLOAD = {
        "firstName": "Madara",
        "lastName": "Uchiha",
        "address": "Konoha, 167 apt.",
        "metroStation": 5,
        "phone": "+7 800 366 56 56",
        "rentTime": 2,
        "deliveryDate": "2025-11-13",
        "comment": "Saske, come back to Uchiha and rest",
        "color": ["GRAY"]
    }

class CourierCreateResponse():

    CODE_SUCCESS = 201
    BODY_SUCCESS = {"ok": True}

    CODE_ERROR_SAME_LOGIN = 409
    BODY_ERROR_SAME_LOGIN = "Этот логин уже используется. Попробуйте другой."

    CODE_ERROR_EMPTY_FIELD = 400
    BODY_ERROR_EMPTY_FIELD = "Недостаточно данных для создания учетной записи"

class CourierLoginResponse():

    CODE_SUCCESS = 200
    BODY_SUCCESS = "id"

    CODE_ERROR_WRONG_DATA = 404
    BODY_ERROR_WRONG_DATA = "Учетная запись не найдена"

    CODE_ERROR_EMPTY_FIELD = 400
    BODY_ERROR_EMPTY_FIELD = "Недостаточно данных для входа"

class OrderResponse():

    CODE_SUCCESS_CREATE = 201
    BODY_SUCCESS_CREATE = "track"

    CODE_SUCCESS_GET_LIST = 200
    BODY_SUCCESS_GET_LIST = "orders"
