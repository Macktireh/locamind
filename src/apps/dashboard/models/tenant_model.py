from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.common.models import BaseModel
from apps.dashboard.models.property_model import Property


class Tenant(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tenants")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="tenants")
    details = models.TextField(_("Details"), blank=True)

    class Meta:
        db_table = "tenants"
        verbose_name = _("Tenant")
        verbose_name_plural = _("Tenants")
