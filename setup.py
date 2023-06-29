# pylint:disable=missing-docstring,invalid-name
import setuptools
import versioneer

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="StrEnum",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="James Sinclair",
    author_email="james@nurfherder.com",
    description="An Enum that inherits from str.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/irgeek/StrEnum",
    packages=["strenum"],
    package_data={"strenum": ["*.typed", "*.pyi"]},
    extras_require={
        "test": [
            "pytest",
            "pytest-black",
            "pytest-cov",
            "pytest-pylint",
            "pylint",
        ],
        "docs": [
            "sphinx",
            "sphinx_rtd_theme",
            "myst-parser[linkify]",
        ],
        "release": ["twine"],
    },
    setup_requires=["pytest-runner"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
