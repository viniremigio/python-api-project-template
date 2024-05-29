# Python API Project Template

![Build Workflow](https://github.com/viniremigio/python-api-project-template/actions/workflows/build.yml/badge.svg)

This project bootstraps a template to create toy Python API.


## Requirements
- Docker
- Python > 3.10
- [Poetry](https://python-poetry.org/) as dependency management tool. If you need to change some library version from *pyproject.toml*, run `poetry lock`.

Then run `poetry env info -p` to make sure the environment setup was done properly.


## Commands
- `make format_code`: rewrites source code using *black* and *isort* to keep it in the standard format
- `make lint`: checks the source code for syntax violations
- `make test`: Run unit tests 
- `make run`: FastAPI will be up at http://localhost:8000/

## Documentation
- The project OpenAPI is available at http://localhost:8000/docs
- Further documentation can be placed in the [docs](docs/) folder.
