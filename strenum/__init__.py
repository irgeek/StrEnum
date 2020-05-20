# pylint:disable=missing-module-docstring
import enum


class StrEnum(str, enum.Enum):
    """
    StrEnum is a Python `enum.Enum` that inherits from `str` to complement
    `enum.IntEnum` in the standard library.
    """

    def __str__(self):
        return self.value

    # pylint: disable=no-self-argument
    # The first argument to this function is documented to be the name of the
    # enum member, not `self`:
    # https://docs.python.org/3.6/library/enum.html#using-automatic-values
    def _generate_next_value_(name, *_):
        return name
