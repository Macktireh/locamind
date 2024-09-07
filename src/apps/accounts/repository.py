from apps.accounts.models import User
from apps.common.repositories.django_base_repository import DjangoBaseRepository


class UserRepository(DjangoBaseRepository[User]):
    def __init__(self, model: User) -> None:
        super().__init__(model)


user_repository = UserRepository(User)
