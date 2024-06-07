from typing import Any

from django.conf import settings


def common_processor(request) -> dict[str, Any]:
    return {
        "APP_NAME": "BienLocation",
        "APP_DOMAIN": settings.APP_DOMAIN,
    }
