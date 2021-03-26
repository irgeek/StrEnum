# pylint: disable=missing-docstring,too-many-arguments
import pytest
from strenum import _NameMangler

# Test data consists of a starting string and it's expected representation each
# of the five cases we support:
#   camelCase
#   PascalCase
#   kebab-case
#   snake-case
#   MACRO_CASE

test_data = [
    ["ONE", "one", "One", "one", "one", "ONE"],
    ["ONE TWO", "oneTwo", "OneTwo", "one-two", "one_two", "ONE_TWO"],
    [
        "ONE TWO THREE",
        "oneTwoThree",
        "OneTwoThree",
        "one-two-three",
        "one_two_three",
        "ONE_TWO_THREE",
    ],
    [
        "fromCamelCase",
        "fromCamelCase",
        "FromCamelCase",
        "from-camel-case",
        "from_camel_case",
        "FROM_CAMEL_CASE",
    ],
    [
        "FromPascalCase",
        "fromPascalCase",
        "FromPascalCase",
        "from-pascal-case",
        "from_pascal_case",
        "FROM_PASCAL_CASE",
    ],
    [
        "from-kebab-case",
        "fromKebabCase",
        "FromKebabCase",
        "from-kebab-case",
        "from_kebab_case",
        "FROM_KEBAB_CASE",
    ],
    [
        "from_snake_case",
        "fromSnakeCase",
        "FromSnakeCase",
        "from-snake-case",
        "from_snake_case",
        "FROM_SNAKE_CASE",
    ],
    [
        "FROM_MACRO_CASE",
        "fromMacroCase",
        "FromMacroCase",
        "from-macro-case",
        "from_macro_case",
        "FROM_MACRO_CASE",
    ],
]


@pytest.mark.parametrize("name,camel,pascal,kebab,snake,macro", test_data)
def test_name_mangler(name, camel, pascal, kebab, snake, macro):
    name_mangler = _NameMangler()

    assert name_mangler.camel(name) == camel
    assert name_mangler.pascal(name) == pascal
    assert name_mangler.kebab(name) == kebab
    assert name_mangler.snake(name) == snake
    assert name_mangler.macro(name) == macro
