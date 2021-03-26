# pylint:disable=missing-docstring,invalid-name
from enum import auto
from strenum import LowercaseStrEnum, UppercaseStrEnum


def test_lowercase_auto():
    class BeamType(LowercaseStrEnum):
        START = auto()
        STOP = auto()
        PARTIAL = auto()

    assert BeamType.START == "start"
    assert BeamType.STOP == "stop"
    assert BeamType.PARTIAL == "partial"


def test_uppercase_auto():
    class HttpMethod(UppercaseStrEnum):
        Get = auto()
        Head = auto()
        Post = auto()
        Put = auto()
        Delete = auto()
        Connect = auto()
        Options = auto()
        Trace = auto()
        Patch = auto()

    assert HttpMethod.Get == "GET"
    assert HttpMethod.Head == "HEAD"
    assert HttpMethod.Post == "POST"
    assert HttpMethod.Put == "PUT"
    assert HttpMethod.Delete == "DELETE"
    assert HttpMethod.Connect == "CONNECT"
    assert HttpMethod.Options == "OPTIONS"
    assert HttpMethod.Trace == "TRACE"
    assert HttpMethod.Patch == "PATCH"
