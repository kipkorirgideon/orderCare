"""
Django settings for orderCare project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import environ
import os
from pathlib import Path

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# Take environment variables from .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'ordercare-3759a549b02f.herokuapp.com',
]

# Application definition

INSTALLED_APPS = [
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'rest_framework',
    'orderCare',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

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

OAUTH2_PROVIDER = {
    "OIDC_ENABLED": True,
    "PKCE_REQUIRED": False,
    "OAUTH2_VALIDATOR_CLASS": "custom_oauth_validator.OpenIDOAuth2Validator",
    "OIDC_RP_INITIATED_LOGOUT_ENABLED": True,
    "OIDC_RP_INITIATED_LOGOUT_ALWAYS_PROMPT": True,
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        "openid": "OpenID Connect scope"
    },
    'DEFAULT_SCOPES': ['read', 'write', 'openid'],
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
}

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

REDIS_URL = env.cache_url('REDIS_URL')
REDIS_OPTIONS = {}

if 'localhost' not in REDIS_URL['LOCATION'] and '127.0.0.1' not in REDIS_URL['LOCATION']:
    REDIS_OPTIONS = {
        'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        'CONNECTION_POOL_KWARGS': {
            'ssl_cert_reqs': None
        },
        'REDIS_CLIENT_KWARGS': {
            'ssl': True,
            'ssl_cert_reqs': None
        },
    }

CACHES = {
    # Read os.environ['CACHE_URL'] and raises
    # ImproperlyConfigured exception if not found.
    #
    # The cache() method is an alias for cache_url().
    'default': {
        **REDIS_URL,
        'OPTIONS': {**REDIS_OPTIONS}
    },

    'redis': {
        **REDIS_URL,
        'OPTIONS': {**REDIS_OPTIONS}
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

GRAPPELLI_ADMIN_TITLE = 'OrderCare Admin'
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

LOGIN_URL = "/admin/login/"
#
# LOGIN_REDIRECT_URL = "/accounts/profile/"
#
# LOGOUT_REDIRECT_URL = None


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'django_static')

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AFRICAS_TALKING_USERNAME = env('AFRICAS_TALKING_USERNAME', default='sandbox')
AFRICAS_TALKING_API_KEY = env('AFRICAS_TALKING_API_KEY', default='')
AFRICAS_TALKING_SENDER_ID = env('AFRICAS_TALKING_SENDER_ID', default='')
CUSTOMER_SERVICE_NUMBER = env('CUSTOMER_SERVICE_NUMBER', default='')
