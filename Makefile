IMAGE_NAME=python_api_project_template

.PHONY: shell build format_code lint test run push create/deploy create/service update/deploy update/service

shell:
	docker run --rm -ti $(IMAGE_NAME) bash

build:
	docker build -t $(IMAGE_NAME) .

format_code:
	poetry run isort .
	poetry run black .

lint:
	poetry run black --check .
	poetry run flake8 --max-line-length=99 --exclude .git,__pycache__,.venv
	poetry run mypy app --allow-untyped-decorators

test:
	docker run --rm $(IMAGE_NAME) poetry run pytest --html=test_report.html

run:
	docker run --rm $(IMAGE_NAME) poetry run uvicorn main:app --host 0.0.0.0 --reload

push: build
	docker image tag $(IMAGE_NAME) $(REGISTRY_HOST)/$(IMAGE_NAME)
	docker push $(REGISTRY_HOST)/$(IMAGE_NAME)

create/deploy:
	kubectl create -f kubernetes/deployment.yaml

create/service:
	kubectl create -f kubernetes/service.yaml

update/deploy:
	kubectl apply -f kubernetes/deployment.yaml

update/service:
	kubect; apply -f kubernetes/service.yaml

clean:
	docker rmi $(IMAGE_NAME)