# pylint:disable=missing-docstring,invalid-name
from enum import auto

import pytest
from pydantic import BaseModel

from strenum import StrEnum


class HttpMethod(StrEnum):
    GET = auto()
    HEAD = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    CONNECT = auto()
    OPTIONS = auto()
    TRACE = auto()
    PATCH = auto()


class DummyModel(BaseModel):
    http_method: HttpMethod


def test_isinstance_str():
    assert isinstance(HttpMethod.GET, str)


def test_value_isinstance_str():
    assert isinstance(HttpMethod.GET.value, str)


def test_str_builtin():
    assert str(HttpMethod.GET) == "GET"


def test_str_equals():
    assert HttpMethod.GET == "GET"


def test_str_hash():
    assert hash(HttpMethod.GET) == hash("GET")


def test_str_cmp():
    assert HttpMethod.GET > "FET"
    assert HttpMethod.GET < "GETA"


def test_list_str_enum():
    assert list(HttpMethod) == [
        "GET",
        "HEAD",
        "POST",
        "PUT",
        "DELETE",
        "CONNECT",
        "OPTIONS",
        "TRACE",
        "PATCH",
    ]


def test_pydantic_model_dump_strenum_field():
    assert DummyModel(http_method=HttpMethod.GET).model_dump() == {"http_method": "GET"}


def test_nonstring_fails():
    # pylint:disable=unused-variable
    with pytest.raises(TypeError):

        class BadEnum(StrEnum):
            ONE = 1
            TWO = 2
