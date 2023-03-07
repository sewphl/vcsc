from .base import *
from __future__ import absolute_import, unicode_literals

import os
from dotenv import load_dotenv

#env = os.environ.copy()
load_dotenv()

#SECRET_KEY = env['SECRET_KEY']
SECRET_KEY = os.getenv('SECRET_KEY')

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DEBUG = False


# Allow all host headers for now (TODO: Add correct URL and IP address and remove *)
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbpsql',
        'USER': os.getenv("USER"),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

try:
    from .local import *
except ImportError:
    pass