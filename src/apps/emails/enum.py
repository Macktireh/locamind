from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.TextChoices):
    READY = "READY", _("Ready")
    SENDING = "SENDING", _("Sending")
    SENT = "SENT", _("Sent")
    FAILED = "FAILED", _("Failed")
