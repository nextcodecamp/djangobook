"""
Django settings for eroom project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+n&@lr&+5h@%my8$f$v16i^g_sp90+l#9606@pt*8--^_)g23h"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '93.127.206.75','194.238.18.26']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",    #session databse
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.redirects",
    "django.contrib.sites",
    "rest_framework",  #Rest API
    
    "rest_framework.authtoken",
    'rest_framework_simplejwt',
    'dbbackup',
    "corsheaders",#Rest API
    "vroom",
    "elearning",
   
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",  #for session 
   
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    'corsheaders.middleware.CorsMiddleware', #REST
    'django.middleware.common.CommonMiddleware', #REST

]

CORS_ORIGIN_ALLOW_ALL = True   #REST
REST_FRAMEWORK = { 
	'DEFAULT_AUTHENTICATION_CLASSES': [ 
        		#'rest_framework.authentication.BasicAuthentication',
                # 'rest_framework.authentication.TokenAuthentication', 	
                #'rest_framework.authentication.SessionAuthentication', 
                'rest_framework_simplejwt.authentication.JWTAuthentication',
             
    ],
    'DEFAULT_PERMISSION_CLASSES': (
                 
                  'rest_framework.permissions.IsAuthenticated',
   ),
}

ROOT_URLCONF = "eroom.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR.joinpath("templates"),
            BASE_DIR.joinpath("vroom/templates"),
          
            
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.media',   #For video allow reference in template directory
            ],
        },
    },
]



WSGI_APPLICATION = "eroom.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
USE_TZ = True
#TIME_ZONE = "UTC"

USE_I18N = False
SITE_ID = 2
USE_TZ = False

DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S' 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "vroom/static/"
#os.path.join(BASE_DIR, 'app1/static/'),
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    "vroom/static/",
    "elearning/static/video",
    "elearning/static/img",
   
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
#EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = 'contactnextcodecamp@gmail.com' #Set to your email
EMAIL_HOST_PASSWORD = "xxxx xxxx xxxx xxxx"       #Set to your password 

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#IMG_URL = "img/"
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backup'}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
