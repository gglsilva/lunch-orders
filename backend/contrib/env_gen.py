"""
Python SECRET_KEY generator.
"""
import random

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*()"
size = 50
secret_key = "".join(random.sample(chars, size))

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%_"
size = 20
password = "".join(random.sample(chars, size))

CONFIG_STRING = '''
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1,.localhost,0.0.0.0


# Ambientes
DJANGO_SETTINGS_MODULE=config.settings.development
#DJANGO_SETTINGS_MODULE=config.settings.production


# Database
DB_NAME=data
DB_USERNAME=postgres
DB_PASSWORD=postgres123
DB_HOSTNAME=db
DB_PORT=5432


# Email
#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=localhost
#EMAIL_PORT=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
#EMAIL_USE_TLS=True


# Celery
CELERY_BROKER_URL=redis://redis:6379/0


# Redis
REDIS_BACKEND=redis://redis:6379/0


# NGINX
NGINX_PORT=80
'''.strip() % (secret_key)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)

print('Success!')
print('Type: cat .env')