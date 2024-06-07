from typing import Required, TypedDict, TypeVar

from django.db import models
from django.http import HttpRequest

from bienlocation.apps.core.models import User


class AuthenticatedHttpRequest(HttpRequest):
    user: User


DjangoModelType = TypeVar("DjangoModelType", bound=models.Model)


class UserRegistrationDataType(TypedDict):
    first_name: Required[str]
    last_name: Required[str]
    email: Required[str]
    password: Required[str]
    accepted_terms: Required[bool]


class EmailDataType(TypedDict):
    to: Required[User]
    subject: Required[str]
    plain_text: str | None
    html: str | None

