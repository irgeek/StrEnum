# StrEnum

StrEnum is a Python `enum.Enum` that inherits from `str` to complement
`enum.IntEnum` in the standard library.

## Installation

You can use [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install StrEnum
```

## Usage

```python
from enum import auto
from strenum import StrEnum


class HttpMethod(StrEnum):
    GET = auto()
    HEAD = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    CONNECT = auto()
    OPTIONS = auto()
    TRACE = auto()
    PATCH = auto()


print(f"An HTTP method: {HttpMethod.GET}")  # prints "An HTTP method: GET"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

Please ensure tests pass before submitting a PR. This repository uses
[Black](https://black.readthedocs.io/en/stable/) and
[Pylint](https://www.pylint.org/) for consistency. Both are run automatically
as part of the test suite.

## Running the tests

Tests can be run using `setup.py`:

```
python3 setup.py test
```

Or inside a virtualenv:

```
python3 -m venv .venv
.venv/bin/python3 setup.py test
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
