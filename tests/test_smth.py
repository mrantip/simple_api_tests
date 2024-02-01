import requests
from configuration import SERVICE_URL

from src.schemas.posts import POST_SCHEMA
from src.baseclasses.response import Response


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)
