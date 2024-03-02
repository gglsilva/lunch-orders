from config.settings.base import *

DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(ASSETS_MEDIA_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USERNAME"),
        "PASSWORD": config("DB_PASSWORD", cast=str),
        "HOST": "db",
        "PORT": 5432,
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"