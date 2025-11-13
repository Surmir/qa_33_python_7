import pytest
from data import CourierData
from api import Courier


@pytest.fixture
def del_courier():
    payload = CourierData.PAYLOAD_REGISTR

    yield payload

    response = Courier.login(CourierData.PAYLOAD_LOGIN)
    courier_id = response.json().get('id')
    Courier.delete(courier_id)

@pytest.fixture
def reg_and_del_courier():
    Courier.create(CourierData.PAYLOAD_REGISTR)
    payload = CourierData.PAYLOAD_LOGIN

    yield payload

    response = Courier.login(payload)
    courier_id = response.json().get('id')
    Courier.delete(courier_id)
