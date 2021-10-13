# pylint:disable=missing-docstring,invalid-name,abstract-method
import sys
from enum import auto
import pytest

from strenum import KebabCaseStrEnum
from strenum.mixins import Comparable


@pytest.mark.skipif(
    sys.version_info < (3, 7, 2), reason="incompatible with Python before 3.7.2"
)
def test_comparable():
    class HttpHeader(Comparable, KebabCaseStrEnum):
        ContentType = auto()
        Host = auto()
        Accept = auto()
        XForwardedFor = auto()

        def _cmp_values(self, other):
            return self.value.lower(), str(other).lower()

    assert HttpHeader.ContentType == "Content-Type"
    assert HttpHeader.ContentType == "content-type"
    assert HttpHeader.ContentType == "coNtEnt-tyPe"

    assert HttpHeader.ContentType != "content-types"

    assert HttpHeader.ContentType < "d"
    assert HttpHeader.ContentType > "b"

    assert HttpHeader.ContentType <= "d"
    assert HttpHeader.ContentType <= "Content-Type"
    assert HttpHeader.ContentType >= "b"
    assert HttpHeader.ContentType >= "Content-Type"


@pytest.mark.skipif(
    sys.version_info < (3, 7, 2), reason="incompatible with Python before 3.7.2"
)
def test_comparable_not_implemented():
    class HttpHeader(Comparable, KebabCaseStrEnum):
        ContentType = auto()
        Host = auto()
        Accept = auto()
        XForwardedFor = auto()

    with pytest.raises(NotImplementedError):
        assert HttpHeader.ContentType == "content-type"
