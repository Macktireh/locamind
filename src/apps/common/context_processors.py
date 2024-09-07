from typing import Any

from django.conf import settings


def common_processor(request) -> dict[str, Any]:
    return {
        "APP_NAME": "BienRental",
        "APP_DOMAIN": settings.APP_DOMAIN,
        "DATA_THEME": "light",
        "GOOGLE_OAUTH2_CLIENT_ID": settings.GOOGLE_OAUTH2_CLIENT_ID,
        "GOOGLE_OAUTH2_REDIRECT_URI": settings.GOOGLE_OAUTH2_REDIRECT_URI,
    }
