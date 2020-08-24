web: python manage.py runserver
web: gunicorn --pythonpath path_wsgi_application --log-file -
heroku ps:scale web=1