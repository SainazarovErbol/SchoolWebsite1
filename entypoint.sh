#!/usr/bin/sh bash

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn core.wsgi:application -c gunicorn_config.py