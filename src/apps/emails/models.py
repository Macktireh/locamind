from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.common.models import BaseModel
from apps.emails.enum import Status


class Email(BaseModel):
    status = models.CharField(max_length=255, db_index=True, choices=Status.choices, default=Status.READY)
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emails")
    subject = models.CharField(max_length=255)
    plain_text = models.TextField(blank=True)
    html = models.TextField(blank=True)
    sent_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "emails"
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")
        indexes = [
            models.Index(fields=["id"], name="id_idx"),
        ]

    def __str__(self) -> str:
        return self.subject
