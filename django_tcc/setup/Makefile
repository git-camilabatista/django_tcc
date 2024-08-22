POETRY_RUN = poetry run

django:
	$(POETRY_RUN) gunicorn -w 1 --bind 0.0.0.0:8000 setup.wsgi:application

#* Formatters
.PHONY: format
format:
	@poetry run ruff format .

#* Linting
.PHONY: lint
lint:
	@poetry run ruff check .
	@poetry run ruff format --check .