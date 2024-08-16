import os

from config.env import BASE_DIR, env
from config.settings.base import *  # noqa: F403
from config.settings.base import INSTALLED_APPS, MIDDLEWARE

DEBUG = env.bool("DEBUG", default=True)


DEVELOP_APPS = [
    "django_extensions",
    "django_browser_reload",
    "debug_toolbar",
]
INSTALLED_APPS.extend(DEVELOP_APPS)

DEVELOP_MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
MIDDLEWARE.extend(DEVELOP_MIDDLEWARE)


# Database
TYPE_DATABASE = env.str("TYPE_DATABASE", default="sqlite")
if TYPE_DATABASE == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASSWORD"),
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT"),
        }
    }

# Email settings
EMAIL_HOST = env("EMAIL_HOST", default="mailpit")
EMAIL_PORT = 1025


MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles/")

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
}


from config.settings.packages.celery import *  # noqa: F403, E402
from config.settings.packages.debug_toolbar import *  # noqa: F403, E402
