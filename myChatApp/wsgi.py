import os, sys

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'myChatApp.settings'

application = get_wsgi_application()

app = application