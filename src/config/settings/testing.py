from config.env import env
from config.settings.base import *  # noqa: F403

DEBUG = env.bool("DEBUG", default=False)


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


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
    # "default": {
    #     "BACKEND": "django.core.cache.backends.redis.RedisCache",
    #     "LOCATION": env("REDIS_URL"),
    # },
}

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


# STORAGES = {
#     "default": {
#         "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
#     },
# }

# CLOUDINARY_STORAGE = {
#     "CLOUD_NAME": env("CLOUDINARY_CLOUD_NAME"),
#     "API_KEY": env("CLOUDINARY_API_KEY"),
#     "API_SECRET": env("CLOUDINARY_API_SECRET"),
# }

print("testing settings")
