#!/bin/sh

echo 'Waiting for postgres...'

while ! nc -z $DB_HOSTNAME $DB_PORT; do
    sleep 0.1
done

echo 'PostgreSQL started'

echo 'Checking migrations...'
python manage.py makemigrations

echo 'Running migrations...'
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --no-input

python manage.py runserver 0.0.0.0:8000
exec "$@"
