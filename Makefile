.PHONY: test lint dist clean

test:
	@uv run pytest -v

lint:
	@uv run black --check .
	@uv run pylint src/strenum/*.py tests/*.py

dist: test lint
	@rm -rf dist/
	@uv build

clean:
	@rm -rf .venv/ dist/ build/ src/*.egg-info .tox/ .eggs/ .pytest_cache/ .coverage
	@rm -rf docs/build pytest.xml cov.xml
	@find -d * -name '*.pyc' -delete -o -name __pycache__ -delete

SPHINX_COMMANDS := html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf latexpdfja text man texinfo info gettext changes xml pseudoxml linkcheck doctest coverage

$(SPHINX_COMMANDS):
	@cd docs && uv run --group docs sphinx-build -M $@ . build
