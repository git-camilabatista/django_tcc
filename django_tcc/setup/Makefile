POETRY_RUN = poetry run

django:
	$(POETRY_RUN) gunicorn --bind 0.0.0.0:8000 setup.wsgi:application