from typing import Required, TypedDict


class UserRegistrationPayloadType(TypedDict):
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