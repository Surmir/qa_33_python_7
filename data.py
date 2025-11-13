from urls import Url
import helpers


class CourierData():

    PAYLOAD_REGISTR = {
        "login": helpers.generate_random_string(7),
        "password": helpers.generate_random_string(7),
        "firstName": helpers.generate_random_string(7)
    }

    PAYLOAD_REGISTR_SAME = {
        "login": PAYLOAD_REGISTR["login"],
        "password": "345678",
        "firstName": "madara"
    }

    PAYLOAD_LOGIN = {
        "login": PAYLOAD_REGISTR["login"],
        "password": PAYLOAD_REGISTR["password"]
    }

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
