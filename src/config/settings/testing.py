import os

from config.settings.base import *  # noqa: F403
from config.settings.base import BASE_DIR, env

DEBUG = env.bool("DEBUG", default=False)


# Email settings
EMAIL_HOST = env("EMAIL_HOST", default="mailpit")
EMAIL_PORT = 1025


MEDIA_URL = "/mediafiles-test/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles-test/")

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
