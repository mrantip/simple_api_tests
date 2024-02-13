import pytest
import requests
import configuration


@pytest.fixture(scope='function')
def get_users():
    response = requests.get(configuration.Link.SERVICE_URL)
    return response
