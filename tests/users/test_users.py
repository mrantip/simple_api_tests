import pytest

from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list(get_users, make_number):
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)
    # print(make_number)


@pytest.mark.skip('issue 2222')
def test_an():
    assert 1 == 1
