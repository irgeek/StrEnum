# pylint:disable=missing-module-docstring
try:
    import aenum as enum
except ImportError:
    import enum


__version__ = "0.4.0"
__version_info__ = tuple(int(n) for n in __version__.split("."))


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
        return self.value

    # pylint: disable=no-self-argument
    # The first argument to this function is documented to be the name of the
    # enum member, not `self`:
    # https://docs.python.org/3.6/library/enum.html#using-automatic-values
    def _generate_next_value_(name, *_):
        return name
