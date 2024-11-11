lint:
	poetry run flake8
format:
	poetry run black gendiff
install:
	poetry install
pack-install:
	python3 -m pip install --user dist/*.whl
