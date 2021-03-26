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

"""
StrEnum contains a collection of subclasses of Python's `enum.Enum` that
inherit from `str` to complement `enum.IntEnum` in the standard library.
"""


class StrEnum(str, enum.Enum):
    """
    StrEnum is a Python `enum.Enum` that inherits from `str`.

    Example usage::

        class Example(StrEnum):
            UPPER_CASE = auto()
            lower_case = auto()
            MixedCase = auto()

        assert Example.UPPER_CASE == "UPPER_CASE"
        assert Example.lower_case == "lower_case"
        assert Example.MixedCase == "MixedCase"
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
    A `StrEnum` that the folds values to lowercase.

    Example usage::

        class Example(LowercaseStrEnum):
            UPPER_CASE = auto()
            lower_case = auto()
            MixedCase = auto()

        assert Example.UPPER_CASE == "upper_case"
        assert Example.lower_case == "lower_case"
        assert Example.MixedCase == "mixedcase"

    """

    def _generate_next_value_(name, *_):
        return name.lower()


class UppercaseStrEnum(StrEnum):
    """
    A `StrEnum` that the folds values to UPPERCASE.

    Example usage::

        class Example(UppercaseStrEnum):
            UPPER_CASE = auto()
            lower_case = auto()
            MixedCase = auto()

        assert Example.UPPER_CASE == "UPPER_CASE"
        assert Example.lower_case == "LOWER_CASE"
        assert Example.MixedCase == "MIXEDCASE"
    """

    def _generate_next_value_(name, *_):
        return name.upper()


class CamelCaseStrEnum(StrEnum):
    """
    A `StrEnum` that the converts values to camelCase.

    Example usage::

        class Example(CamelCaseStrEnum):
            UPPER_CASE = auto()
            lower_case = auto()
            MixedCase = auto()

        assert Example.UPPER_CASE == "upperCase"
        assert Example.lower_case == "lowerCase"
        assert Example.MixedCase == "mixedCase"
    """

    def _generate_next_value_(name, *_):
        return _name_mangler.camel(name)


class PascalCaseStrEnum(StrEnum):
    """
    A `StrEnum` that the converts values to PascalCase.

    Example usage::

        class Example(PascalCaseStrEnum):
            UPPER_CASE = auto()
            lower_case = auto()
            MixedCase = auto()

        assert Example.UPPER_CASE == "UpperCase"
        assert Example.lower_case == "LowerCase"
        assert Example.MixedCase == "MixedCase"
    """

    def _generate_next_value_(name, *_):
        return _name_mangler.pascal(name)


class KebabCaseStrEnum(StrEnum):
    """
    A `StrEnum` that the converts values to kebab-case.

    Example usage::

        class Example(KebabCaseStrEnum):
            UPPER_CASE = auto()
            lower_case = auto()
            MixedCase = auto()

        assert Example.UPPER_CASE == "upper-case"
        assert Example.lower_case == "lower-case"
        assert Example.MixedCase == "mixed-case"
    """

    def _generate_next_value_(name, *_):
        return _name_mangler.kebab(name)


class SnakeCaseStrEnum(StrEnum):
    """
    A `StrEnum` that the converts values to snake_case.

    Example usage::

        class Example(SnakeCaseStrEnum):
            UPPER_CASE = auto()
            lower_case = auto()
            MixedCase = auto()

        assert Example.UPPER_CASE == "upper_case"
        assert Example.lower_case == "lower_case"
        assert Example.MixedCase == "mixed_case"
    """

    def _generate_next_value_(name, *_):
        return _name_mangler.snake(name)


class MacroCaseStrEnum(StrEnum):
    """
    A `StrEnum` that the converts values to MACRO_CASE.

    Example usage::

        class Example(MacroCaseStrEnum):
            UPPER_CASE = auto()
            lower_case = auto()
            MixedCase = auto()

        assert Example.UPPER_CASE == "UPPER_CASE"
        assert Example.lower_case == "LOWER_CASE"
        assert Example.MixedCase == "MIXED_CASE"
    """

    def _generate_next_value_(name, *_):
        return _name_mangler.macro(name)
