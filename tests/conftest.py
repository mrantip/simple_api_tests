import pytest
import requests
from configuration import  SERVICE_URL2


@pytest.fixture(scope='function')
def get_users():
    response = requests.get(SERVICE_URL2)
    return response