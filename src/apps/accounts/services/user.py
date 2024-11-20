from typing import Any

from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.accounts.repository import UserRepository, user_repository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def get(self, **kwargs: dict[str, Any]) -> User | None:
        try:
            return self.user_repository.get(**kwargs)
        except User.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> User | None:
        return self.get(email=email)

    def get_by_public_id(self, public_id: str) -> User | None:
        return self.get(public_id=public_id)

    def create(self, email: str, password: str | None, **extra_fields) -> User:
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self._normalize_email(email)
        user = self.user_repository.create(email=email, **extra_fields)
        if password:
            self.user_repository.set_password(user, password)
        return user

    def update(self, user: User, data: dict[str, Any]) -> User:
        return self.user_repository.update(user, **data)

    def delete(self, user: User) -> None:
        return self.user_repository.delete(user)

    def _normalize_email(self, email) -> str:
        return self.user_repository.model.objects.normalize_email(email)


user_service = UserService(user_repository=user_repository)