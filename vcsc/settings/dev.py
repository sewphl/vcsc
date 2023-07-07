from .base import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from dotenv import load_dotenv

#env = os.environ.copy()
load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY_DEV')

# Dropbox:
DROPBOX_OAUTH2_TOKEN = os.getenv('DROPBOX_OAUTH2_TOKEN') 
DROPBOX_APP_KEY = os.getenv('DROPBOX_APP_KEY') 
DROPBOX_APP_SECRET = os.getenv('DROPBOX_APP_SECRET') 
DROPBOX_OAUTH2_REFRESH_TOKEN = os.getenv('DROPBOX_OAUTH2_REFRESH_TOKEN') 

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
