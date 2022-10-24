"""
Django settings for bigday project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os
from datetime import datetime

from decouple import config
import pytz

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
GENERATE_STATIC = config('GENERATE_STATIC', default=False, cast=bool)

ALLOWED_HOSTS = [
    '*',
    '127.0.0.1',
    'localhost',
    'soeren-thu-wedding.com',
    'www.soeren-thu-wedding.com',
    config('SERVER', default='127.0.0.1'),
]

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'guests.apps.GuestsConfig',
    'django_distill',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bigday.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join('bigday', 'templates'),
        ],
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

DEFAULT_CACHE = 'django.core.cache.backends.locmem.LocMemCache'
CACHES = {
    'default': {
        'BACKEND': config('CACHE_BACKEND', default=DEFAULT_CACHE),
        'LOCATION': 'unique-snowflake',
    }
}

WSGI_APPLICATION = 'bigday.wsgi.application'

if not (DEBUG or GENERATE_STATIC):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'bigday', 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# This is used in a few places where the names of the couple are used
BRIDE_AND_GROOM = 'Søren and Thu'
# base address for all emails
DEFAULT_WEDDING_EMAIL = 'shmulvad@gmail.com'
# the address your emails (save the dates/invites/etc.) will come from
DEFAULT_WEDDING_FROM_EMAIL = f'{BRIDE_AND_GROOM} <{DEFAULT_WEDDING_EMAIL}>'

# the default reply-to of your emails
DEFAULT_WEDDING_REPLY_EMAIL = DEFAULT_WEDDING_EMAIL # change to 'address@domain.tld'
# the location of your wedding
WEDDING_LOCATION = 'Phu Yen, Vietnam'
# the date of your wedding
WEDDING_DATE = 'October 19th, 2022'

VN_TIMEZONE = pytz.timezone('Asia/Ho_Chi_Minh')
WEDDING_DATE_DATETIME = datetime(2022, 10, 19, 10, tzinfo=VN_TIMEZONE)
WEDDING_DATE_DATETIME_UTC = WEDDING_DATE_DATETIME.astimezone(pytz.utc)

# When sending test emails it will use this address
DEFAULT_WEDDING_TEST_EMAIL = DEFAULT_WEDDING_FROM_EMAIL

# This is used in links in save the date / invitations
WEDDING_WEBSITE_URL = 'https://soeren-thu-wedding.com'
WEDDING_CC_LIST = ['shmulvad@gmail.com', 'tranthituyetthu95@gmail.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# python manage.py distill-local --force --collectstatic
DISTILL_DIR = os.path.join(BASE_DIR, 'build')
