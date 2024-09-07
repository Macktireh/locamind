from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.dashboard.enum import ReceiptStatusChoice
from apps.dashboard.models.properties import Property
from apps.dashboard.models.tenancies import Tenancy


class Receipt(BaseModel):
    """
    A receipt is a document that represents a payment made by a tenant to a landlord.
    """

    property = models.ForeignKey(verbose_name=_("Property"), to=Property, on_delete=models.CASCADE, related_name="receipts")
    tenancy = models.ForeignKey(
        verbose_name=_("Tenancy"),
        to=Tenancy,
        on_delete=models.CASCADE,
        related_name="receipts",
    )
    issue_date = models.DateField(verbose_name=_("Issue date"), help_text=_("The date the receipt was issued"))
    due_date = models.DateField(verbose_name=_("Due date"), help_text=_("The date the receipt is due"))
    amount_due = models.DecimalField(
        verbose_name=_("Amount due"),
        max_digits=10,
        decimal_places=2,
        help_text=_("The amount due"),
    )
    amount_paid = models.DecimalField(
        verbose_name=_("Amount paid"), max_digits=10, decimal_places=2, help_text=_("The amount paid")
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=128,
        choices=ReceiptStatusChoice.choices,
        default=ReceiptStatusChoice.PENDING,
        help_text=_(
            "The status of the receipt. "
            "Pending: The receipt is pending payment. "
            "Partially paid: The receipt is partially paid. "
            "Paid: The receipt is paid. "
        ),
    )

    class Meta:
        db_table = "receipts"
        verbose_name = _("Receipt")
        verbose_name_plural = _("Receipts")

    def __str__(self) -> str:
        return f"Receipt<{self.issue_date} - {self.amount_due}>"
