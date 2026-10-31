.PHONY: test lint dist upload upload-test clean

TWINE_OPTIONS := --disable-progress-bar --skip-existing

test: .venv/bin/pytest
	@$< -v

lint: .venv/bin/pylint
	@.venv/bin/black --check .
	@.venv/bin/pylint strenum/*.py tests/*.py

dist: test lint .venv/bin/twine
	@.venv/bin/python3 -m build

upload: .venv/bin/twine dist
	@.venv/bin/twine upload \
		$(TWINE_OPTIONS) \
		dist/*

upload-test: .venv/bin/twine dist
	@.venv/bin/twine upload \
		$(TWINE_OPTIONS) \
		--repository-url https://test.pypi.org/legacy/ \
		dist/*

.venv:
	@python3 -m venv .venv
	@.venv/bin/pip3 install --upgrade pip

.venv/bin/pytest: .venv
	@.venv/bin/python3 -m pip install .[test]

.venv/bin/pylint: .venv
	@.venv/bin/python3 -m pip install .[lint]

.venv/bin/twine: .venv
	@.venv/bin/python3 -m pip install .[release]

.venv/bin/sphinx-build: .venv
	@.venv/bin/python3 -m pip install .[docs]

clean:
	@rm -rf .venv/ dist/ build/ *.egg-info .tox/ .eggs/ .pytest_cache/ .coverage
	@rm -rf docs/build pytest.xml cov.xml
	@find -d * -name '*.pyc' -delete -o -name __pycache__ -delete

SPHINX_COMMANDS := html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf latexpdfja text man texinfo info gettext changes xml pseudoxml linkcheck doctest coverage

$(SPHINX_COMMANDS): .venv/bin/sphinx-build
	@cd docs && ../.venv/bin/sphinx-build -M $@ . build
