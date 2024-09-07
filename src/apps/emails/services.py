from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.http import HttpRequest
from django.template.loader import get_template
from django.utils import timezone

from apps.common.exceptions import ApplicationError
from apps.common.services import model_update
from apps.common.types import EmailDataType
from apps.emails.models import Email


class EmailServices:
    @transaction.atomic
    @staticmethod
    def create(
        payload: EmailDataType, template_name: str | None = None, context: dict | None = None, request: HttpRequest | None = None
    ) -> Email:
        if not template_name:
            email, _ = Email.objects.get_or_create(**payload)
            return email
        htmlContent = get_template(template_name).render(context, request)
        payload["html"] = htmlContent
        email, _ = Email.objects.get_or_create(**payload)
        return email

    @transaction.atomic
    @staticmethod
    def email_send(email: Email):
        if email.status != Email.Status.SENDING:
            raise ApplicationError(f"Cannot send non-ready emails. Current status is {email.status}")

        subject = email.subject
        from_email = settings.DEFAULT_FROM_EMAIL
        to = email.to.email
        html = email.html
        plain_text = email.plain_text

        msg = EmailMultiAlternatives(subject=subject, body=plain_text, from_email=from_email, to=[to])
        msg.attach_alternative(html, "text/html")

        msg.send()

        email, _ = model_update(
            instance=email, fields=["status", "sent_at"], data={"status": Email.Status.SENT, "sent_at": timezone.now()}
        )
        return email

    @transaction.atomic
    @staticmethod
    def email_failed(email: Email) -> Email:
        if email.status != Email.Status.SENDING:
            raise ApplicationError(f"Cannot fail non-sending emails. Current status is {email.status}")

        email, _ = model_update(instance=email, fields=["status"], data={"status": Email.Status.FAILED})
        return email
