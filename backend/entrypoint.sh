#!/bin/sh

if [ $DATABASE = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
# exclusão dos dados
#python manage.py flush --no-input
python backend/manage.py makemigrations
python backend/manage.py migrate

exec "$@"