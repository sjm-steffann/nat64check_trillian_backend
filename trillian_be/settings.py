"""
Django settings for trillian_be project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _

ADMINS = [
    ('Sander Steffann', 'sander@nat64check.org'),
    ('Jan Žorž', 'jan@nat64check.org'),
]

MANAGERS = ADMINS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get('DJANGO_DEBUG', '0') == '1'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['localhost', '::1', '127.0.0.1']

MY_HOSTNAME = os.environ.get('MY_HOSTNAME')
if MY_HOSTNAME:
    ALLOWED_HOSTS.insert(0, MY_HOSTNAME)

INTERNAL_IPS = [
    '127.0.0.1',
    '::1',
]

# Application definition
# noinspection PyUnresolvedReferences
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'generic',
    'instances',
    'measurements',

    'prettyjson',
    'django_countries',
    'django_extensions',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_filters',
    'rest_framework_swagger',

    # TODO: Consider OTP for Admin site
    # 'django_otp',
    # 'django_otp.plugins.otp_totp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # TODO: Consider OTP for Admin site
    # 'django_otp.middleware.OTPMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trillian_be.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'generic.context_processors.uwsgi_context',
                'trillian_be.context_processors.app_version',
            ],
        },
    },
]

WSGI_APPLICATION = 'trillian_be.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': os.environ.get('PGHOST', ''),
        'NAME': os.environ.get('PGDATABASE', 'trillian'),
        'USER': os.environ.get('PGUSER', 'trillian'),
        'PASSWORD': os.environ.get('PGPASSWORD', ''),
        'CONN_MAX_AGE': 900,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    }
}

# Use cache as a front-end for database cache storage
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('nl', _('Dutch')),
    ('sl', _('Slovenian')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# noinspection PyUnresolvedReferences
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

RUNSERVERPLUS_SERVER_ADDRESS_PORT = '[::]:8000'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_filters.backends.DjangoFilterBackend',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'URL_FIELD_NAME': '_url',
    'SERIALIZER_EXTENSIONS': {
        'AUTO_OPTIMIZE': True,
        'QUERY_PARAMS_ENABLED': False,
    }
}

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'list',
    'JSON_EDITOR': True,
}

# Dump email to console for testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_TIMEOUT = 30
EMAIL_SUBJECT_PREFIX = '[NAT64Check] '

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

# Enable these when running over TLS
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Tell browsers not to guess content-types but to trust us
SECURE_CONTENT_TYPE_NOSNIFF = True

# Tell browsers to (try to) detect XSS attacks
SECURE_BROWSER_XSS_FILTER = True

# Refuse to be framed
X_FRAME_OPTIONS = 'DENY'

try:
    # Override default setting with local settings
    from .local_settings import *
except ImportError:
    pass

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
