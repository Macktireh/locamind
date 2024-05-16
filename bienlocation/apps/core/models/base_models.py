from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    public_id = models.UUIDField(_("Public ID"), unique=True, editable=False, default=uuid4, db_index=True)
    created = models.DateTimeField(
        _("Created at"), auto_now_add=True, help_text=_("Date time on which the object was created.")
    )
    updated = models.DateTimeField(
        _("Updated at"), auto_now=True, help_text=_("Date time on which the object was updated.")
    )

    class Meta:
        abstract = True
