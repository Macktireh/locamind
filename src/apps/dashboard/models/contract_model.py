from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.dashboard.models.property_model import Property
from apps.dashboard.models.tenant_model import Tenant


class Contract(BaseModel):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="contracts")
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="contracts")
    start_date = models.DateField(_("Start date"))
    end_date = models.DateField(_("End date"))
    special_clauses = models.TextField(_("Special clauses"), blank=True)

    class Meta:
        db_table = "contracts"
        verbose_name = _("Contract")
        verbose_name_plural = _("Contracts")

    def __str__(self):
        return f"Contract<{self.property} - {self.tenant}>"
