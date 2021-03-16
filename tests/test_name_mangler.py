# pylint:disable=missing-docstring
import pytest
from strenum import _NameMangler

# Test data consists of a starting string and it's expected representation each
# of the four cases we support:
#   camelCase
#   PascalCase
#   kebab-case
#   snake-case

test_data = [
    ["ONE", "one", "One", "one", "one"],
    ["ONE TWO", "oneTwo", "OneTwo", "one-two", "one_two"],
    ["ONE TWO THREE", "oneTwoThree", "OneTwoThree", "one-two-three", "one_two_three"],
    [
        "fromCamelCase",
        "fromCamelCase",
        "FromCamelCase",
        "from-camel-case",
        "from_camel_case",
    ],
    [
        "FromPascalCase",
        "fromPascalCase",
        "FromPascalCase",
        "from-pascal-case",
        "from_pascal_case",
    ],
    [
        "from-kebab-case",
        "fromKebabCase",
        "FromKebabCase",
        "from-kebab-case",
        "from_kebab_case",
    ],
    [
        "from_snake_case",
        "fromSnakeCase",
        "FromSnakeCase",
        "from-snake-case",
        "from_snake_case",
    ],
]


@pytest.mark.parametrize("name,camel,pascal,kebab,snake", test_data)
def test_name_mangler(name, camel, pascal, kebab, snake):
    name_mangler = _NameMangler()

    assert name_mangler.camel(name) == camel
    assert name_mangler.pascal(name) == pascal
    assert name_mangler.kebab(name) == kebab
    assert name_mangler.snake(name) == snake
