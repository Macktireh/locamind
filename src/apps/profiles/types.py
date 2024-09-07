from typing import Required, TypedDict

from apps.accounts.models import User


class ProfilePayloadType(TypedDict):
	user: Required[User]
	phone_number: str | None
