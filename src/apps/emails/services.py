from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.template.loader import get_template
from django.utils import timezone

from apps.common.exceptions import ApplicationError
from apps.common.types import EmailDataType
from apps.emails.enum import Status
from apps.emails.models import Email
from apps.emails.repository import EmailRepository, email_repository
from apps.emails.tasks import email_send_with_celery


class EmailService:
    def __init__(self, email_repository: EmailRepository) -> None:
        self.email_repository = email_repository

    @transaction.atomic
    def create(
        self,
        payload: EmailDataType,
        template_name: str | None = None,
        context: dict | None = None,
    ) -> Email:
        if not template_name:
            email, _ = self.email_repository.get_or_create(**payload)
            return email
        htmlContent = get_template(template_name).render(context)
        payload["html"] = htmlContent
        email, _ = self.email_repository.get_or_create(**payload)
        return email

    @transaction.atomic
    def email_send(self, email: Email) -> Email:
        if email.status != Status.SENDING:
            raise ApplicationError(f"Cannot send non-ready emails. Current status is {email.status}")

        subject = email.subject
        from_email = settings.DEFAULT_FROM_EMAIL
        to = email.to.email
        html = email.html
        plain_text = email.plain_text

        msg = EmailMultiAlternatives(subject=subject, body=plain_text, from_email=from_email, to=[to])
        msg.attach_alternative(html, "text/html")

        msg.send()
        email = self.email_repository.update(instance=email, data={"status": Status.SENT, "sent_at": timezone.now()})
        return email

    @transaction.atomic
    def email_failed(self, email: Email) -> Email:
        if email.status != Status.SENDING:
            raise ApplicationError(f"Cannot fail non-sending emails. Current status is {email.status}")

        email = self.email_repository.update(instance=email, data={"status": Status.FAILED})
        return email

    def email_send_task(
            self,
        payload: EmailDataType,
        template_name: str | None = None,
        context: dict | None = None,
    ) -> None:
        email = EmailService.create(payload=payload, template_name=template_name, context=context)
        with transaction.atomic():
            self.email_repository.filter(id=email.id).update(status=Status.SENDING)
        transaction.on_commit(lambda: email_send_with_celery.delay(email))


email_service = EmailService(email_repository=email_repository)
