import requests
from configuration import SERVICE_URL

from src.schemas.posts import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)


def test_getting_posts_2():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(Post)
