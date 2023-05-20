.ONESHELL:
.PHONY: init install install-tests tests tests-cov clean terminate

init:
	python3 -m venv venv

install: 
	python3 -m pip install -r requirements.txt

install-tests: 
	python3 -m pip install -r requirements-tests.txt

tests:
	python3 -m pytest --verbose --cov=tests

tests-cov:
	pytest --cov=src --cov-report term-missing --cov-report=html

clean:
	find src -type d -name '__pycache__' -exec rm -r {} +
	find tests -type d -name '__pycache__' -exec rm -r {} +

terminate:
	echo "Test"