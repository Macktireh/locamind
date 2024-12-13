from config.settings.base import env

CELERY_BROKER_URL = env.str("REDIS_URL", "redis://redis:6379/0")

CELERY_RESULT_BACKEND = env.str("REDIS_URL", "redis://redis:6379/0")

CELERY_BEAT_SCHEDULE = {}

CELERY_TIMEZONE = "UTC"

CELERY_TASK_SOFT_TIME_LIMIT = 20  # seconds

CELERY_TASK_TIME_LIMIT = 30  # seconds

CELERY_TASK_MAX_RETRIES = 3
