.PHONY: clean-pyc develop

help:
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with linters"
	@echo "test - run tests with the default Python version"
	@echo "test-all - run tests with all supported Python versions"
	@echo "coverage - check code coverage with the default Python"

clean: clean-deploy clean-tests clean-pyc

clean-deploy:
	find . -name '*.egg-info' -exec rm -fr {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-tests:
	find . -name '.tox' -exec rm -fr {} +
	find . -name '.coverage' -exec rm -f {} +

develop:
	pip install -e .[testing]

lint:
	flake8 bootstrap_ui
	isort --check-only --diff --recursive bootstrap_ui

test:
	python runtests.py

test-all:
	tox

coverage:
	coverage run runtests.py
	coverage report -m
