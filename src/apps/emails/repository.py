from apps.common.repositories.django_base_repository import DjangoBaseRepository
from apps.emails.models import Email


class EmailRepository(DjangoBaseRepository[Email]):
    def __init__(self, model: Email = Email) -> None:
        super().__init__(model)


email_repository = EmailRepository(Email)
