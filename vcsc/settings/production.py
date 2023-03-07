from .base import *
from __future__ import absolute_import, unicode_literals

import os

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DEBUG = False

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

# Allow all host headers for now (TODO: Add correct URL and IP address and remove *)
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbpsql',
        'USER': env['USER'],
        'PASSWORD': env['DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '*',
    }
}

try:
    from .local import *
except ImportError:
    pass