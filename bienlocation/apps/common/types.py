from typing import Required, TypedDict, TypeVar

from django.db import models
from django.http import HttpRequest

from bienlocation.apps.core.models.user_models import User


class AuthenticatedHttpRequest(HttpRequest):
    user: User


DjangoModelType = TypeVar("DjangoModelType", bound=models.Model)


class UserRegistrationDataType(TypedDict):
    first_name: Required[str]
    last_name: Required[str]
    email: Required[str]
    password: Required[str]
