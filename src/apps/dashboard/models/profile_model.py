from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.common.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    class Meta:
        db_table = "profiles"
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
