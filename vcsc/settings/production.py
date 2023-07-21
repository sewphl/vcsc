from __future__ import absolute_import, unicode_literals
##exec('from __future__ import absolute_import, unicode_literals')

from .base import *

import os
from dotenv import load_dotenv
import dropbox

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

# Dropbox:
DROPBOX_OAUTH2_TOKEN = os.getenv('DROPBOX_OAUTH2_TOKEN') 
DROPBOX_APP_KEY = os.getenv('DROPBOX_APP_KEY') 
DROPBOX_APP_SECRET = os.getenv('DROPBOX_APP_SECRET') 
DROPBOX_OAUTH2_REFRESH_TOKEN = os.getenv('DROPBOX_OAUTH2_REFRESH_TOKEN') 

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DEBUG = False


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
## SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers for now (TODO: Add correct URL and IP address and remove *)
ALLOWED_HOSTS = ['afternoon-reef-17256.herokuapp.com']


# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'dbpsql',
#        'USER': os.getenv('DB_USER'),
#        'PASSWORD': os.getenv('DB_PASSWORD'),
#        'HOST': '',
#        'PORT': '',
#    }
#}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://c0d9ad3bccda447c8947060b835823ba@o4504798573232128.ingest.sentry.io/4504798581096448",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass