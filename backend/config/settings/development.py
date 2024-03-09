from config.settings.base import *
import os
import dj_database_url


DEBUG = True


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(ASSETS_MEDIA_DIR, 'db.sqlite3'),
#     }
# }

# local
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": config("DB_NAME"),
#         "USER": config("DB_USERNAME"),
#         "PASSWORD": config("DB_PASSWORD", cast=str),
#         "HOST": "db",
#         "PORT": 5432,
#     }
# }


DATABASES = {
    'default': {
        dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
}



# database_url = os.environ.get("DATABASE_URL")
# DATABASES["default"] = dj_database_url.parse(database_url)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"