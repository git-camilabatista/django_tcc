How to run?

```sh
poetry run gunicorn --bind 0.0.0.0:8000 setup.wsgi:application
```

or using Makefile

```sh
make django
```