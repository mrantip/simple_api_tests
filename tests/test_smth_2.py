import requests
from configuration import SERVICE_URL2
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list(get_users):
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)
