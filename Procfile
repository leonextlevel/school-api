release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
web: gunicorn school_api.wsgi --log-file -
