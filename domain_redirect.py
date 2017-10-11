import os
import random
import string
from urllib.parse import urlunsplit

from django.conf.urls import url
from django.http import HttpResponseRedirect

DEBUG = False
ROOT_URLCONF = 'domain_redirect'
DATABASES = {'default': {}}


def index(request):
    return HttpResponseRedirect(urlunsplit([
        REDIRECT_SCHEME,
        REDIRECT_NETLOC,
        request.get_full_path(),
        '',
        '',
    ]))


urlpatterns = [
    url(r'^.*$', index),  # match all URLs
]

SECRET_KEY = ''.join([
    random.SystemRandom().choice(string.printable)
    for i in range(50)
])

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(';')
REDIRECT_SCHEME = os.getenv('REDIRECT_SCHEME', 'http')
REDIRECT_NETLOC = os.getenv('REDIRECT_NETLOC', 'example.com')
