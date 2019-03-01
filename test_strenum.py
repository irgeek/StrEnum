from enum import auto
from strenum import StrEnum


class HttpMethod(StrEnum):
    GET = auto()
    HEAD = auto
    POST = auto()
    PUT = auto()
    DELETE = auto()
    CONNECT = auto()
    OPTIONS = auto()
    TRACE = auto()
    PATCH = auto()


def test_isinstance_str():
    assert isinstance(HttpMethod.GET, str)


def test_value_isinstance_str():
    assert isinstance(HttpMethod.GET.value, str)


def test_str_builtin():
    assert str(HttpMethod.GET) == "GET"
