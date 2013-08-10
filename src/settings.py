# -*- coding: utf-8 -*-
import os
import sys
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


sys.path.append(os.path.join(PROJECT_PATH, 'libs'))
sys.path.append(os.path.join(PROJECT_PATH, 'apps'))
sys.path.insert(0, '/var/www/Dembor')
# Django settings for nanbit project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mateusz', 'mateusz.dargacz@internetprofil.pl'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'debor', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'lipton#321', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.

    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

DEFAULT_CHARSET = 'utf-8'

SITE_ID = 1

#STATICFILES_DIRS = (
#    # Put strings here, like "/home/html/static" or "C:/www/django/static".
#    # Always use forward slashes, even on Windows.
#    # Don't forget to use absolute paths, not relative paths.
#)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'uxrh78ud4i_hlm3rx5(az@x%w78r48jsc4zq$&e7gqnc_0)*fz'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(PROJECT_PATH, "theme/templates"),
#    os.path.join(PROJECT_PATH, "templates"),
)

INSTALLED_APPS = (
    'theme',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'adminsortable',
    'slideshow_parallax',
    'slideshow_roundabout',
    'cms',
    'tagging',
    'mptt',
    'zinnia',
    'cmsplugin_zinnia',
    #'photologue',
    'cmsplugin_contact',
    'menus',
    'easy_thumbnails',
    'inline_ordering',
    'sekizai',
    'cmsplugin_gallery',

    'cmsplugin_plaintext',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',
    'south',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
STATIC_URL = "/static/"


CMS_TEMPLATES = (
    ('cms/site/home.html', 'Template Home'),
    ('cms/site/about.html', 'Template O Firmie'),
    ('cms/site/offer.html', 'Template Oferta'),
    ('cms/site/realizacje.html', 'Template Realizacje'),
    ('cms/site/template-contact.html', 'Template Kontakt'),
    ('cms/site/main.html','Template main'),


)
LANGUAGES = [
    ('pl', 'Polish'),
    ('en', 'English'),
]

ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'
ZINNIA_ENTRY_DETAIL_TEMPLATES = [
    ('zinnia/custom_detail_page.html', 'custom detail template'),
]
ZINNIA_PAGINATION = 3


CMS_REDIRECTS = True
MENU_CACHE_DURATION = 0
CMS_SEO_FIELDS = True
PREPEND_WWW = False
APPEND_SLASH = True

try:
    execfile('%s/local_settings.py' % PROJECT_PATH)
except IOError:
    pass
