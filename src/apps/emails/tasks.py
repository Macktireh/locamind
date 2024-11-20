from celery import shared_task
from celery.utils.log import get_task_logger

from apps.emails.models import Email
from apps.emails.repository import email_repository

logger = get_task_logger(__name__)


def _email_send_failure(self, exc, task_id, args, kwargs, einfo) -> None:
    email_id = args[0]
    email = email_repository.get(id=email_id)

    from apps.emails.services import EmailService

    EmailService.email_failed(email)


@shared_task(bind=True, on_failure=_email_send_failure)
def email_send_with_celery(self, email: Email) -> None:
    from apps.emails.services import email_service

    try:
        email_service.email_send(email)
    except Exception as exc:
        logger.warning(f"Exception occurred while sending email: {exc}")
        self.retry(exc=exc, countdown=5)
