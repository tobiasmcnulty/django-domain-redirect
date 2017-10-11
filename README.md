django-domain-redirect
======================

A very simple Django app to redirect all requests to a new domain, based on https://github.com/readevalprint/mini-django.

You can run it like so:

    $ gunicorn "django.core.handlers.wsgi:WSGIHandler()" \
      --env DJANGO_SETTINGS_MODULE=domain_redirect \
      --log-file - --access-logfile -

This will redirect all requests to for http://localhost:8000 to http://example.com

To configure the domain and scheme used for the redirect, set the `REDIRECT_NETLOC` and `REDIRECT_SCHEME` environment
variables, e.g.:

    $ gunicorn "django.core.handlers.wsgi:WSGIHandler()" \
      --env DJANGO_SETTINGS_MODULE=domain_redirect \
      --env REDIRECT_NETLOC=www.mydomain.com \
      --env REDIRECT_SCHEME=https \
      --log-file - --access-logfile -


Dependencies
============
* python
* django
* gunicorn


Install
=======
1. Clone this repo
2. `pip install requirements.txt`
3. `PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=domain_redirect`


Authors
======
Tim Watts (tim@readevalprint.com)
Tobias McNulty (tobias@caktusgroup.com)
