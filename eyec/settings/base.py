"""
Django settings for eyec project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from .import dev,prod
from configparser import RawConfigParser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
config = RawConfigParser()
config.read('settings.ini')
#SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('section','SECRET_KEY')
GOOGLE_RECAPTCHA_SITE_KEY = config.get('section','GOOGLE_RECAPTCHA_SITE_KEY')
GOOGLE_RECAPTCHA_SECRET_KEY = config.get('section','GOOGLE_RECAPTCHA_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#For Dev
#DEBUG = dev.DEBUG
#ALLOWED_HOSTS = dev.ALLOWED_HOSTS

#For Prod
DEBUG = prod.DEBUG
ALLOWED_HOSTS = prod.ALLOWED_HOSTS

#dev.DEBUG
#ALLOWED_HOSTS = ['127.0.0.1','localhost']
#dev.DevelopmentSettings
#prod.ProductionSettings


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'eyec.urls'

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

WSGI_APPLICATION = 'eyec.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.get('section','DBNAME'),
        'USER':config.get('section','DBUSER'),
        'PASSWORD':config.get('section','DBPASSWORD'),
        'HOST':config.get('section','DBHOST'),
        'PORT':''
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES = (
    os.path.join(BASE_DIR,'static'),
)

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR
#Email setup
EMAIL_HOST = config.get('section','HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = config.get('section','HOST_USER')
EMAIL_HOST_PASSWORD = config.get('section','HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False