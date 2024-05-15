import os

from config.env import BASE_DIR, env
from config.settings.base import *  # noqa: F403

DEBUG = env.bool("DEBUG", default=True)


DEVELOP_APPS = [
    "django_extensions",
    "django_browser_reload",
]

INSTALLED_APPS.extend(DEVELOP_APPS)  # noqa: F405
# MIDDLEWARE.extend(["debug_toolbar.middleware.DebugToolbarMiddleware"])  # noqa: F405
MIDDLEWARE.extend(["django_browser_reload.middleware.BrowserReloadMiddleware"])  # noqa: F405


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Email settings
EMAIL_BACKEND = "developmentEmailDashboard.emailbackend.developmentEmailBackend"
DEVELOPMENT_EMAIL_DASHBOARD_SEND_EMAIL_NOTIFICATION = True


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
    # "default": {
    #     "BACKEND": "django.core.cache.backends.redis.RedisCache",
    #     "LOCATION": "redis://127.0.0.1:6379",
    # }
}


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


# Django-debug-toolbar
# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS = INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1"]
# mimetypes.add_type("application/javascript", ".js", True)

# DEBUG_TOOLBAR_PATCH_SETTINGS = False

# DEBUG_TOOLBAR_CONFIG = {
#     "INTERCEPT_REDIRECTS": False,
#     "SHOW_TOOLBAR_CALLBACK": lambda request: True,
#     "INSERT_BEFORE": "</head>",
#     "RENDER_PANELS": True,
# }
