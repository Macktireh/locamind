from typing import Any

from apps.accounts.models import User
from apps.accounts.repository import user_repository


class UserService:
    def get(self, id: int) -> User | None:
        try:
            return user_repository.get(id=id)
        except User.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> User | None:
        try:
            return user_repository.get(email=email)
        except User.DoesNotExist:
            return None

    def get_by_public_id(self, public_id: str) -> User | None:
        try:
            return user_repository.get(public_id=public_id)
        except User.DoesNotExist:
            return None

    def create(self, first_name: str, last_name: str, email: str, password: str | None, **kwargs) -> User:
        user = user_repository.create(first_name=first_name, last_name=last_name, email=email, **kwargs)
        if password:
            user_repository.set_password(user, password)
        return user

    def update(self, user: User, data: dict[str, Any]) -> User:
        return user_repository.update(user, **data)

    def delete(self, user: User) -> None:
        return user.delete()


user_service = UserService()
