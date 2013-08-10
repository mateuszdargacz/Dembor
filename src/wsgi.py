import os, sys

# path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
#
# if path not in sys.path:
#    sys.path.append(path)
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
#
#
# import django.core.handlers.wsgi
#
# application = django.core.handlers.wsgi.WSGIHandler()


PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PROJECT_ROOT = os.path.join(PROJECT_PATH, 'src')
LIB_ROOT = os.path.join(PROJECT_ROOT, 'libs')
if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
if LIB_ROOT not in sys.path:
    sys.path.insert(0, LIB_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()