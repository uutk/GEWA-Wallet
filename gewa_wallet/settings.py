"""
Django settings for gewa_wallet project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import pymysql

# Import pymysql to connect to mysql server
pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gur)t4($20te9^r+^becc+_-29^ew8=t%%qhpx6*ffxr$aas61'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ['*']

ALLOWED_HOSTS = []  # Set allowed host here when deploying to server


# Application definition

INSTALLED_APPS = [
    'website.apps.WebsiteConfig',
    'auth_system.apps.AuthSystemConfig',
    'users.apps.UsersConfig',
    'paytm_gateway.apps.PaytmGatewayConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gewa_wallet.urls'

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

WSGI_APPLICATION = 'gewa_wallet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'gewa_wallet',
        'USER': 'nonroot',
        'PASSWORD': 'nonroot',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata' # Change this if not from India

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'website-home'

LOGIN_URL = 'login'

ACCOUNT_LOGOUT_REDIRECT_URL = "/"

LOGIN_REDIRECT_URL = "/"

#Email Configration
EMAIL_HOST = 'smtp.gmail.com' # Change this if using some other smtp server

EMAIL_PORT = 465

EMAIL_HOST_USER = 'YOUR_EMAIL_ADDRESS'

EMAIL_HOST_PASSWORD = 'YOUR_EMAIL_PASSWORD'

EMAIL_USE_TLS = False

EMAIL_USE_SSL = True

#paytm_gateway variables configuration
# PAYTM_MERCHANT_KEY = "xxxxxxxxxxxxxxxx"
# PAYTM_MERCHANT_ID = "xxxxxxxxxxxxxxxxxxxx"
# HOST_URL = "http://localhost:8000"
# PAYTM_WEBSITE = 'FROM_PAYTM_DASHBOARD'
INDUSTRY_TYPE_ID = 'Retail'
PAYTM_CALLBACK_URL = "/gateway/paytm/response/"

if DEBUG:
    PAYTM_MERCHANT_KEY = "YOUR_MERCHANT_KEY"
    PAYTM_MERCHANT_ID = "YOUR_MERCHANT_ID"
    PAYTM_WEBSITE = 'WEBSTAGING'
    HOST_URL = 'http://localhost:8000'
    '''
    In sandbox enviornment you can use following wallet credentials to login and make payment.
    Mobile Number : 7777777777
    Password : Paytm12345
    OTP: 489871
    This test wallet is topped-up to a balance of 7000 Rs. every 5 minutes.
    '''

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
