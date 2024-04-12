IMAGE_NAME=spark_etl_template

.PHONY: format_code lint run_etl start shell test

shell:
	docker-compose exec -ti $(IMAGE_NAME) bash

start:
	docker-compose up --build --remove-orphans --force-recreate -d

format_code:
	make start
	docker-compose exec $(IMAGE_NAME) poetry run isort . && \
	docker-compose exec $(IMAGE_NAME) poetry run black .

lint:
	make start
	docker-compose exec $(IMAGE_NAME) poetry run black --check . && \
	docker-compose exec $(IMAGE_NAME) poetry run flake8 --max-line-length=99 --exclude .git,__pycache__,.venv
	docker-compose exec $(IMAGE_NAME) poetry run mypy app --allow-untyped-decorators

test:
	make start
	docker-compose exec $(IMAGE_NAME) poetry run pytest

run:
	make start
	docker-compose exec $(IMAGE_NAME) poetry run uvicorn main:app --host 0.0.0.0 --reload
