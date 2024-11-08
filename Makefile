lint:
	poetry run flake8
format:
	poetry run black script
install:
	poetry install
pack-install:
	python3 -m pip install --user dist/*.whl
