from typing import Required, TypedDict

from apps.accounts.models import User


class EmailDataType(TypedDict):
    to: Required[User]
    subject: Required[str]
    plain_text: str | None
    html: str | None
