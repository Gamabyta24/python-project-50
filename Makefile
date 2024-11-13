lint:
	poetry run flake8
format:
	poetry run black gendiff
install:
	poetry install
pack-install:
	python3 -m pip install --user dist/*.whl
run-stylish:
	poetry run gendiff tests/files/file1.json tests/files/file2.json
run-plain:
	poetry run gendiff tests/files/file1.json tests/files/file2.json --format plain
run-json:
	poetry run gendiff tests/files/file1.json tests/files/file2.json --format json
run-test:
	poetry run pytest
cov-test:
	poetry run pytest --cov=gendiff tests/



