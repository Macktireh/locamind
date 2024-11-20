from typing import TypeVar

from django.db import models
from django.http import HttpRequest

from apps.accounts.models import User


class AuthenticatedHttpRequest(HttpRequest):
    user: User


DjangoModelType = TypeVar("DjangoModelType", bound=models.Model)
