from apps.common.repositories.django_repository import DjangoRepository
from apps.emails.models import Email


class EmailRepository(DjangoRepository[Email]):
    def __init__(self, model: Email = Email) -> None:
        super().__init__(model)


email_repository = EmailRepository(Email)
