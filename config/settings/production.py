from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOST")]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DBname"),
        "USER": os.environ.get("DBuser"),
        "PASSWORD": os.environ.get("DBpassword"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}
