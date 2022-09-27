"""
Django settings for poc project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
    "localhost", "127.0.0.1", "poc.local", ".poc.local"
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tenants',
    'accounting'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tenants.middlewares.TenantMiddleware',
]

ROOT_URLCONF = 'poc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'poc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

default_dburl = "sqlite:///" + os.path.join(BASE_DIR, "default.sqlite3")
thor_dburl = "sqlite:///" + os.path.join(BASE_DIR, "thor.sqlite3")
potter_dburl = "sqlite:///" + os.path.join(BASE_DIR, "potter.sqlite3")

DATABASES = {
    "default": config("DATABASE_URL", default=default_dburl, cast=dburl),
    "thor": config("DATABASE_URL", default=thor_dburl, cast=dburl),
    "potter": config("DATABASE_URL", default=potter_dburl, cast=dburl),
}

# SQLITE_SERVICE_INSTANCE = 'django.db.backends.sqlite3'
#
# DATABASES = {
#     'default': {
#         'ENGINE': SQLITE_SERVICE_INSTANCE,
#         'NAME': BASE_DIR / 'default.sqlite3',
#     },
#     'thor': {
#         'ENGINE': SQLITE_SERVICE_INSTANCE, 'NAME': BASE_DIR / 'thor.sqlite3'
#     },
#     'potter': {
#         'ENGINE': SQLITE_SERVICE_INSTANCE, 'NAME': BASE_DIR / 'potter.sqlite3'
#     },
# }

DATABASE_ROUTERS = ['tenants.router.TenantRouter']

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'