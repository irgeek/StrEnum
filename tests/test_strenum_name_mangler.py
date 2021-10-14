# pylint:disable=missing-docstring,invalid-name
from enum import auto
from strenum import (
    CamelCaseStrEnum,
    PascalCaseStrEnum,
    KebabCaseStrEnum,
    SnakeCaseStrEnum,
    MacroCaseStrEnum,
    CamelSnakeCaseStrEnum,
    PascalSnakeCaseStrEnum,
    SpongebobCaseStrEnum,
    CobolCaseStrEnum,
    HttpHeaderCaseStrEnum,
)


def test_camel_case_auto():
    class TestEnum(CamelCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "one"
    assert TestEnum.OneTwo == "oneTwo"
    assert TestEnum.OneTwoThree == "oneTwoThree"


def test_pascal_case_auto():
    class TestEnum(PascalCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "One"
    assert TestEnum.OneTwo == "OneTwo"
    assert TestEnum.OneTwoThree == "OneTwoThree"


def test_kebab_case_auto():
    class TestEnum(KebabCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "one"
    assert TestEnum.OneTwo == "one-two"
    assert TestEnum.OneTwoThree == "one-two-three"


def test_snake_case_auto():
    class TestEnum(SnakeCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "one"
    assert TestEnum.OneTwo == "one_two"
    assert TestEnum.OneTwoThree == "one_two_three"


def test_macro_case_auto():
    class TestEnum(MacroCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "ONE"
    assert TestEnum.OneTwo == "ONE_TWO"
    assert TestEnum.OneTwoThree == "ONE_TWO_THREE"


def test_camel_snake_case_auto():
    class TestEnum(CamelSnakeCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "one"
    assert TestEnum.OneTwo == "one_Two"
    assert TestEnum.OneTwoThree == "one_Two_Three"


def test_pascal_snake_case_auto():
    class TestEnum(PascalSnakeCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "One"
    assert TestEnum.OneTwo == "One_Two"
    assert TestEnum.OneTwoThree == "One_Two_Three"


def test_spongebob_case_auto():
    class TestEnum(SpongebobCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "one"
    assert TestEnum.OneTwo == "one_TWo"
    assert TestEnum.OneTwoThree == "one_TWo_thrEE"


def test_cobol_case_auto():
    class TestEnum(CobolCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "ONE"
    assert TestEnum.OneTwo == "ONE-TWO"
    assert TestEnum.OneTwoThree == "ONE-TWO-THREE"


def test_http_header_case_auto():
    class TestEnum(HttpHeaderCaseStrEnum):
        One = auto()
        OneTwo = auto()
        OneTwoThree = auto()

    assert TestEnum.One == "One"
    assert TestEnum.OneTwo == "One-Two"
    assert TestEnum.OneTwoThree == "One-Two-Three"
