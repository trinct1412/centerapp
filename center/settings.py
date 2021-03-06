"""
Django settings for center project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Direction logger save
LOGGER_DIR = os.environ.get('LOGGER_DIR', './logs')

# create location save logging file
if not os.path.exists('django-logging'):
    os.mkdir('django-logging')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5l95p1l-oysw*i-+ukje#g6ied0tbz-4(4w(%^w45upg+_uf3&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '.ngrok.io', '127.0.0.1', 'centerapp-network.herokuapp.com']

# Rest framework definition

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASeSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# Application definition

INSTALLED_APPS = [
    'page.apps.PageConfig',
    'customer',
    'debug_toolbar',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'celery',
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

# config debug toolbar sql
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
]

INTERNAL_IPS = ('127.0.0.1', 'localhost:8000')

DEBUG_TOOLBAR_CONFIG = {
    'SKIP_TEMPLATE_PREFIXES': ('admin/widgets/',),
}

# end

ROOT_URLCONF = 'center.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'center.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dckr4apv7r45u2',
        'USER': 'unzwqysghmsvzk',
        'PASSWORD': 'f0514aee79d9a3c1aba7e95da4f92e7227972d953733cf51b4842c71b5f903d0',
        'HOST': 'ec2-34-194-198-238.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'centerapp',
            'USER': 'root',
            'PASSWORD': 'Corkcrew8542',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
DEBUG_DIRECTED_FILE = "django-logging"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Config celery
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Ho_Chi_Minh'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file", "console", "fetch_api", "user"]},
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "{}/logging.log".format(DEBUG_DIRECTED_FILE),
            "formatter": "verbose",
        },
        "console": {
            "class": "logging.StreamHandler",
        },
        "fetch_api": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "{}/fetch_api.log".format(DEBUG_DIRECTED_FILE),
            "formatter": "simple",
        },
        "user": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "{}/user.log".format(DEBUG_DIRECTED_FILE),
            "formatter": "verbose",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": True,
            "filter": ['require_debug_true'],
        },
        "get_api": {
            "handlers": ["fetch_api", ],
            "level": "WARNING",
            "propagate": True,
            "filter": ['require_debug_true'],
        },
        "user_create": {
            "handlers": ["user", ],
            "level": "ERROR",
            "propagate": True,
            "filter": ['require_debug_true'],
        }
    },
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s %(name)s-%(levelname)s (%(filename)s:%(lineno)s %(funcName)s)]: %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S"},
        "simple": {
            "format": "[%(asctime)s %(name)s-%(levelname)s]: %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S"},
    },
}
