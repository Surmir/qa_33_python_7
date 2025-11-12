import pytest
from data import CourierData, OrderData
from api import Courier, Orders


@pytest.fixture
def del_courier():
    payload = CourierData.PAYLOAD_REGISTR

    yield payload

    response = Courier.login(CourierData.PAYLOAD_LOGIN)
    courier_id = response.json().get('id')
    Courier.delete(courier_id)

@pytest.fixture
def registr_and_del_courier():
    Courier.create(CourierData.PAYLOAD_REGISTR)
    payload = CourierData.PAYLOAD_LOGIN

    yield payload

    response = Courier.login(payload)
    courier_id = response.json().get('id')
    Courier.delete(courier_id)

@pytest.fixture
def cancel_order():
    payload = OrderData.PAYLOAD

    yield payload

    r = Orders.get_list_orders()
    if r["orders"]["comment"] == payload["comment"]:
        track = r["orders"]["track"]
        Orders.cancel(track)
