from urls import Url


class CourierData():

    PAYLOAD_REGISTR = {
        "login": 'hokage',
        "password": '098123',
        "firstName": 'naruto'
    }

    PAYLOAD_REGISTR_SAME = {
        "login": 'hokage',
        "password": '345678',
        "firstName": 'madara'
    }

    PAYLOAD_LOGIN = {
        "login": 'hokage',
        "password": '098123'
    }

class Api():

    url = Url.YANDEX_SCOOTER

    COURUER_LOGIN = f"{url}/api/v1/courier/login"
    COURUER_CREATE = f"{url}/api/v1/courier"
    COURUER_DELETE = f"{url}/api/v1/courier/:id"
    ORDERS = f"{url}/api/v1/orders"
    ORDERS_CANCEL = f"{url}/api/v1/orders/cancel"

class OrderData():

    PAYLOAD = {
    "firstName": "Madara",
    "lastName": "Uchiha",
    "address": "Konoha, 167 apt.",
    "metroStation": 2,
    "phone": "+7 800 366 56 56",
    "rentTime": 4,
    "deliveryDate": "2025-11-13",
    "comment": "Saske, come back to Uchiha and rest",
    "color": [
        "GRAY"
    ]
}
