import random
import string


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

class CourierData():

    PAYLOAD_REGISTR = {
        "login": generate_random_string(7),
        "password": generate_random_string(7),
        "firstName": generate_random_string(7)
    }

    PAYLOAD_REGISTR_SAME = {
        "login": PAYLOAD_REGISTR["login"],
        "password": generate_random_string(7),
        "firstName": generate_random_string(7)
    }

    PAYLOAD_LOGIN = {
        "login": PAYLOAD_REGISTR["login"],
        "password": PAYLOAD_REGISTR["password"]
    }

    TEST_WRONG_DATA = [
        {"login": "error12",
         "password": PAYLOAD_REGISTR["password"]},
        {"login": PAYLOAD_REGISTR["login"],
         "password": "error12"}
                        ]
    
    TEST_EMPTY_FIELD = [
        {"login": "",
         "password": PAYLOAD_REGISTR["password"]},
        {"login": PAYLOAD_REGISTR["login"],
         "password": ""}
                        ]
