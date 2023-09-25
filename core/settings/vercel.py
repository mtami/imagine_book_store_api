import os  # noqa

from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = [".vercel.app", ".now.sh", "127.0.0.1", "localhost"]  # adjust to deployment provider base url

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get('DB_NAME'),
        "HOST": os.environ.get('DB_HOST'),
        "PORT": os.environ.get('DB_PORT', 5432),
        "USER": os.environ.get('DB_USER'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
    }
}
