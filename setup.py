import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="StrEnum",
    version="0.4.0",
    author="James Sinclair",
    author_email="james@nurfherder.com",
    description="An Enum that inherits from str.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/irgeek/StrEnum",
    packages=setuptools.find_packages(),
    tests_require=["pytest", "pytest-black", "pytest-pylint", "pytest-cov"],
    setup_requires=["pytest-runner"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
