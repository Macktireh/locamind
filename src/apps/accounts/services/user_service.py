from typing import Any

from django.db import transaction

from apps.accounts.models import User


class UserServices:
    def __init__(self, model: type[User]) -> None:
        self.model = model

    @transaction.atomic
    def create(self, first_name: str, last_name: str, email: str, password: str | None, **kwargs) -> User:
        return self.model.objects.create_user(
            first_name=first_name, last_name=last_name, email=email, password=password, **kwargs
        )

    @transaction.atomic
    def user_create_without_password(self, first_name: str, last_name: str, email: str, **kwargs) -> User:
        return self.model.objects.create_user(first_name=first_name, last_name=last_name, email=email, **kwargs)

    def update(self, user: User, data: dict[str, Any]) -> User:
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user

    def set_password(self, user: User, password: str) -> None:
        user.set_password(password)
        user.save()

    def delete(self, user: User) -> None:
        return user.delete()


user_service = UserServices(model=User)
