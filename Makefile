.PHONY: test dist upload upload-test clean

TWINE_OPTIONS := --disable-progress-bar --skip-existing

test: .venv/bin/pytest
	@$< -v

dist: test .venv
	@.venv/bin/python3 setup.py sdist bdist_wheel

upload: dist .venv
	@.venv/bin/twine upload \
		$(TWINE_OPTIONS) \
		dist/*

upload-test: dist .venv
	@.venv/bin/twine upload \
		$(TWINE_OPTIONS) \
		--repository-url https://test.pypi.org/legacy/ \
		dist/*

.venv:
	@python3 -m venv .venv
	@.venv/bin/pip3 install --upgrade pip setuptools wheel
	@.venv/bin/pip3 install --upgrade twine

.venv/bin/pytest: .venv
	@.venv/bin/python3 -m pip install .[test]

clean:
	@rm -rf .venv/ dist/ build/ *.egg-info .tox/ .eggs/ .pytest_cache/ .coverage
	@find -d * -name '*.pyc' -delete -o -name __pycache__ -delete
