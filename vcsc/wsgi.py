"""
WSGI config for vcsc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

path = '/users/c/m/cmplxsys/dev.cmplxsys.w3.uvm.edu-root/vcsc'
if path not in sys.path:
    sys.path.append(path)


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vcsc.settings.production")

application = get_wsgi_application()
