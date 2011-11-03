# Django settings for cc42 project.
import sys
import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_PATH = os.path.dirname(__file__)


def join_with_proj_path(part_path):
    return os.path.join(PROJECT_PATH, part_path)


ADMINS = (
          ('admin', 'admin@admin.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'sqlite.db'),
        'USER': '', 'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST_NAME': ':memory:'
    }
}

TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = join_with_proj_path('media')
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

LOGIN_REDIRECT_URL = '/'

STATICFILES_DIRS = (
                    MEDIA_ROOT,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'l+b28zbkg3=h*s1@iv0kd=3$v-skjd#u2ogy(gnupg9x$&-1we'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'store_requests.middleware.SaveEveryIncomingRequestToDB',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    join_with_proj_path('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'contacts',
    'store_requests',
    'templatelib',
    'extra_commands',
    'model_spectator',
    'south',
    'django_nose',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "context_processors.settings_context_processor"
)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/'

FIXTURE_DIRS = (
   join_with_proj_path('fixtures'),
   join_with_proj_path('contacts/fixtures'),
)

TEST_RUNNER = 'tddspry.django.runner.TestSuiteRunner'

import logging

logging.disable(logging.CRITICAL)
