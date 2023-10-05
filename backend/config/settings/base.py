"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ASSETS_MEDIA_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
APPS_DIR = os.path.join(BASE_DIR, 'apps')

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'debug_toolbar',
    'crispy_forms',
    "crispy_bootstrap5",
    'easy_thumbnails',
]

MY_APPS = [
    'apps.core',
    'apps.product',
    'apps.account',
    'apps.order',
    'apps.menu',
]

INSTALLED_APPS = []

INSTALLED_APPS += DJANGO_APPS + THIRD_APPS + MY_APPS


INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


# Adicione o domínio do ngrok (sem o protocolo https://)
NGROK_DOMAIN = 'https://26c6-131-196-67-132.ngrok-free.app' # Modificar

# Defina as origens confiáveis
CSRF_TRUSTED_ORIGINS = [
    'https://26c6-131-196-67-132.ngrok-free.app', # Modificar
    # 'localhost',  # Se estiver usando localhost
    # Outros domínios confiáveis, se aplicável
]


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================
BUILT_IN_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

THIRD_PARTY_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # django debug toolbar middleware

]
USER_DEFINED_MIDDLEWARE = []
MIDDLEWARE = BUILT_IN_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + USER_DEFINED_MIDDLEWARE

# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": config("DB_NAME"),
#         "USER": config("DB_USERNAME"),
#         "PASSWORD": config("DB_PASSWORD"),
#         "HOST": config("DB_HOSTNAME"),
#         "PORT": config("DB_PORT", cast=int),
#     }
# }


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

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

# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files')  # project/core/static_files
]
STATIC_ROOT = os.path.join(ASSETS_MEDIA_DIR, 'assets')  # project/assets


# REDIRECT
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery
CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = config("REDIS_BACKEND")

# FORMS TEMPLATES
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"