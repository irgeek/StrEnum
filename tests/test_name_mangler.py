# pylint: disable=missing-docstring,too-many-arguments
import pytest
from strenum import _NameMangler


word_split_test_data = (
    ("one", ["one"]),
    ("one two", ["one", "two"]),
    ("one two three", ["one", "two", "three"]),
    ("ONETwoThree", ["ONE", "Two", "Three"]),
    ("OneTWOThree", ["One", "TWO", "Three"]),
    ("OneTwoTHREE", ["One", "Two", "THREE"]),
    ("fromCamelCase", ["from", "Camel", "Case"]),
    ("FromPascalCase", ["From", "Pascal", "Case"]),
    ("from-kebab-case", ["from", "kebab", "case"]),
    ("from_snake_case", ["from", "snake", "case"]),
    ("FROM_MACRO_CASE", ["FROM", "MACRO", "CASE"]),
    ("from_Camel_Snake_Case", ["from", "Camel", "Snake", "Case"]),
    ("From_Pascal_Snake_Case", ["From", "Pascal", "Snake", "Case"]),
    ("FROM-COBOL-CASE", ["FROM", "COBOL", "CASE"]),
    ("From-Http-Header-Case", ["From", "Http", "Header", "Case"]),
)


@pytest.mark.parametrize("word,expected", word_split_test_data)
def test_word_splitting(word, expected):
    name_mangler = _NameMangler()
    assert list(name_mangler.words(word)) == expected


test_data = [
    ("camel", "oneTwoThree"),
    ("pascal", "OneTwoThree"),
    ("kebab", "one-two-three"),
    ("snake", "one_two_three"),
    ("macro", "ONE_TWO_THREE"),
    ("camel_snake", "one_Two_Three"),
    ("pascal_snake", "One_Two_Three"),
    ("spongebob", "ONE_twO_ThREe"),
    ("cobol", "ONE-TWO-THREE"),
    ("http_header", "One-Two-Three"),
]


@pytest.mark.parametrize("func_name,expected", test_data)
def test_name_mangler(func_name, expected):
    name_mangler = _NameMangler()

    func = getattr(name_mangler, func_name)
    assert func("one two three") == expected
