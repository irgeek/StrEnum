try:
    import aenum as enum
except ImportError:
    import enum

from ._version import get_versions
from ._name_mangler import _NameMangler

__version__ = get_versions()["version"]
__version_info__ = tuple(int(n) for n in __version__.partition("+")[0].split("."))
del get_versions

_name_mangler = _NameMangler()

# The first argument to the `_generate_next_value_` function of the `enum.Enum`
# class is documented to be the name of the enum member, not the enum class:
#
#     https://docs.python.org/3.6/library/enum.html#using-automatic-values
#
# Pylint, though, doesn't know about this so we need to disable it's check for
# `self` arguments.
# pylint: disable=no-self-argument


class StrEnum(str, enum.Enum):
    """
    StrEnum is a Python `enum.Enum` that inherits from `str` to complement
    `enum.IntEnum` in the standard library.
    """

    def __new__(cls, value, *args, **kwargs):
        if not isinstance(value, (str, enum.auto)):
            raise TypeError(
                "Values of StrEnums must be strings: {} is a {}".format(
                    repr(value), type(value)
                )
            )
        return super().__new__(cls, value, *args, **kwargs)

    def __str__(self):
        return str(self.value)

    def _generate_next_value_(name, *_):
        return name


class LowercaseStrEnum(StrEnum):
    """
    A subclass of `StrEnum` that the folds the member name to lowercase for the
    `auto()` value.
    """

    def _generate_next_value_(name, *_):
        return name.lower()


class UppercaseStrEnum(StrEnum):
    """
    A subclass of `StrEnum` that the folds the member name to uppercase for the
    `auto()` value.
    """

    def _generate_next_value_(name, *_):
        return name.upper()


class CamelCaseStrEnum(StrEnum):
    """
    A subclass of `StrEnum` that the converts the member name to camelCase for the
    `auto()` value.
    """

    def _generate_next_value_(name, *_):
        return _name_mangler.camel(name)


class PascalCaseStrEnum(StrEnum):
    """
    A subclass of `StrEnum` that the converts the member name to PascalCase for the
    `auto()` value.
    """

    def _generate_next_value_(name, *_):
        return _name_mangler.pascal(name)


class KebabCaseStrEnum(StrEnum):
    """
    A subclass of `StrEnum` that the converts the member name to kebab-case for the
    `auto()` value.
    """

    def _generate_next_value_(name, *_):
        return _name_mangler.kebab(name)


class SnakeCaseStrEnum(StrEnum):
    """
    A subclass of `StrEnum` that the converts the member name to snake-case for the
    `auto()` value.
    """

    def _generate_next_value_(name, *_):
        return _name_mangler.snake(name)
