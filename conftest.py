import pytest
from helpers import CourierData
from api import CourierApi


@pytest.fixture
def reg_and_del_courier():
    payload = CourierData.PAYLOAD_REGISTR
    create = CourierApi.create(payload)
    
    yield create

    response = CourierApi.login(CourierData.PAYLOAD_LOGIN)
    courier_id = response.json().get('id')
    CourierApi.delete(courier_id)
