# pylint:disable=missing-docstring,invalid-name
import setuptools
import versioneer

with open("README.md", "r") as fh:
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
    packages=setuptools.find_packages(),
    extras_require={
        "test": [
            "pytest",
            "pytest-black",
            "pytest-cov",
            "pytest-pylint",
            "pylint",
        ],
        "release": ["twine"],
    },
    setup_requires=["pytest-runner"],
    install_requires=["aenum;python_version<'3.6'"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
