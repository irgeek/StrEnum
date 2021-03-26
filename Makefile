.PHONY: test dist upload upload-test clean

TWINE_OPTIONS := --disable-progress-bar --skip-existing

test: .venv/bin/pytest
	@$< -v

dist: test
	@.venv/bin/python3 setup.py sdist bdist_wheel

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
	@.venv/bin/pip3 install --upgrade pip setuptools wheel

.venv/bin/pytest: .venv
	@.venv/bin/python3 -m pip install .[test]

.venv/bin/twine: .venv
	@.venv/bin/python3 -m pip install .[test,release]

.venv/bin/sphinx-build: .venv
	@.venv/bin/python3 -m pip install .[docs]

clean:
	@rm -rf .venv/ dist/ build/ *.egg-info .tox/ .eggs/ .pytest_cache/ .coverage
	@find -d * -name '*.pyc' -delete -o -name __pycache__ -delete

SPHINX_COMMANDS := html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf latexpdfja text man texinfo info gettext changes xml pseudoxml linkcheck doctest coverage

$(SPHINX_COMMANDS): .venv/bin/sphinx-build
	@cd docs && ../.venv/bin/sphinx-build -M $@ . build
