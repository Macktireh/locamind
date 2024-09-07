from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.dashboard.models.contract_model import Contract


class Receipt(BaseModel):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="receipts")
    issue_date = models.DateField(_("Issue date"))
    amount_paid = models.DecimalField(_("Amount paid"), max_digits=10, decimal_places=2)
    details = models.TextField(_("Details"), blank=True)

    class Meta:
        db_table = "receipts"
        verbose_name = _("Receipt")
        verbose_name_plural = _("Receipts")

    def __str__(self) -> str:
        return f"Receipt<{self.issue_date} - {self.amount_paid}>"
