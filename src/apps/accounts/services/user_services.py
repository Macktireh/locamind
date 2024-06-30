from apps.accounts.models import User
from apps.common.services import model_update


class UserServices:
    def user_create(self, first_name: str, last_name: str, email: str, password: str | None, **kwargs) -> User:
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, **kwargs)
        return user

    def user_update(self, user: User, data: dict) -> User:
        non_side_effect_fields = ["first_name", "last_name"]
        user, has_updated = model_update(instance=user, fields=non_side_effect_fields, data=data)
        return user

    def user_set_password(self, user: User, password: str) -> None:
        user.set_password(password)
        user.save()

    def user_delete(self, user: User) -> None:
        user.delete()
