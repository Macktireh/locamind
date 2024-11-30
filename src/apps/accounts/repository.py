from apps.accounts.models import User
from apps.common.repositories.django_repository import DjangoRepository


class UserRepository(DjangoRepository[User]):
    def __init__(self, model: User) -> None:
        super().__init__(model)

    def create_superuser(self, **kwargs) -> User:
        return self.model.objects.create_superuser(**kwargs)

    def set_password(self, user: User, password: str) -> None:
        user.set_password(password)
        user.save()


user_repository = UserRepository(User)
