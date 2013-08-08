import os, sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

if path not in sys.path:
   sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

