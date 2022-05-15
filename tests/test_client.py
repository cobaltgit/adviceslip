from random import randint
from re import A

import pytest

import adviceslip

_client = adviceslip.Client()


def test_get_id() -> None:
    _id = 19
    slip = _client.slip_from_id(_id)
    assert slip.id == _id


def test_search() -> None:
    query = "spiders"
    search_obj = _client.search(query)
    assert search_obj.query == query and all(query in slip.advice for slip in search_obj.slips)


def test_closed_session() -> None:
    with adviceslip.Client() as temp_client:
        pass
    with pytest.raises(adviceslip.SessionClosed):
        temp_client.slip_from_id(1)

def test_api_error() -> None:
    out_of_bounds_id = randint(32768, 65536)
    with pytest.raises(adviceslip.APIError):
        _client.slip_from_id(out_of_bounds_id)


def test_http_error() -> None:
    with pytest.raises(adviceslip.HTTPException):
        _client.request("/not-a-real-endpoint")
