from typing import Required, TypedDict, TypeVar

from django.db import models
from django.http import HttpRequest

from apps.accounts.models import User


class AuthenticatedHttpRequest(HttpRequest):
    user: User


DjangoModelType = TypeVar("DjangoModelType", bound=models.Model)


class UserRegistrationDataType(TypedDict):
    first_name: Required[str]
    last_name: Required[str]
    email: Required[str]
    password: Required[str]
    accepted_terms: Required[bool]


class SocialUserDataType(TypedDict):
    first_name: Required[str]
    last_name: Required[str]
    email: Required[str]
    full_name: str | None
    picture: str | None
    email_verified: bool | None


class EmailDataType(TypedDict):
    to: Required[User]
    subject: Required[str]
    plain_text: str | None
    html: str | None
