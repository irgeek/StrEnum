# pylint:disable=missing-docstring,invalid-name
from enum import auto
from strenum import (
    CamelCaseStrEnum,
    PascalCaseStrEnum,
    KebabCaseStrEnum,
    SnakeCaseStrEnum,
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
