from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.dashboard.enum import PaymentFrequencyChoice, PaymentMethodChoice, ReceiptTitleTypeChoice, TenancyTypeChoice
from apps.dashboard.models.documents import Document
from apps.dashboard.models.landlords import Landlord
from apps.dashboard.models.properties import Property
from apps.dashboard.models.tenants import Tenant


class Tenancy(BaseModel):
    landlord = models.ForeignKey(verbose_name=_("Landlord"), to=Landlord, on_delete=models.CASCADE, related_name="tenancies")
    property = models.ForeignKey(verbose_name=_("Property"), to=Property, on_delete=models.CASCADE, related_name="tenancies")
    type = models.CharField(verbose_name=_("Type"), max_length=128, choices=TenancyTypeChoice.choices)
    start_date = models.DateField(verbose_name=_("Start date"))
    end_date = models.DateField(verbose_name=_("End date"), null=True, blank=True)
    renewal = models.BooleanField(verbose_name=_("Renewal"), default=True)
    frequency_payment = models.CharField(
        verbose_name=_("Payment Frequency"),
        max_length=255,
        choices=PaymentFrequencyChoice.choices,
        default=PaymentFrequencyChoice.MONTHLY,
    )
    payement_method = models.CharField(
        verbose_name=_("Payment Method"), choices=PaymentMethodChoice.choices, max_length=64, blank=True, null=True
    )
    payement_day = models.PositiveSmallIntegerField(verbose_name=_("Payment day"), choices=[(i, i) for i in range(1, 29)])
    rent = models.DecimalField(verbose_name=_("Rent"), max_digits=10, decimal_places=2, blank=True, null=True)
    charges = models.DecimalField(verbose_name=_("Charges"), max_digits=10, decimal_places=2, blank=True, null=True)
    others_payments = models.DecimalField(
        verbose_name=_("Others Payments"), max_digits=10, decimal_places=2, blank=True, null=True
    )
    decription_others_payments = models.TextField(verbose_name=_("Description of Others Payments"), blank=True, null=True)
    tenants = models.ManyToManyField(verbose_name=_("Tenants"), to=Tenant, blank=True, related_name="tenancies")
    amount_repairs_by_landlord = models.DecimalField(
        verbose_name=_("Amount of repairs by landlord"), max_digits=10, decimal_places=2, blank=True, null=True
    )
    description_repairs_by_landlord = models.TextField(
        verbose_name=_("Description of repairs by landlord"), blank=True, null=True
    )
    amount_repairs_by_tenant = models.DecimalField(
        verbose_name=_("Amount of repairs by tenant"), max_digits=10, decimal_places=2, blank=True, null=True
    )
    description_repairs_by_tenant = models.TextField(
        verbose_name=_("Description of repairs by tenant"), blank=True, null=True
    )
    comment = models.TextField(verbose_name=_("Comments on the tenancy"), blank=True, null=True)
    receipt_title = models.CharField(
        verbose_name=_("Title of the receipt"),
        max_length=255,
        choices=ReceiptTitleTypeChoice.choices,
        default=ReceiptTitleTypeChoice.RECEIPT,
    )
    due_notice_day = models.PositiveSmallIntegerField(
        verbose_name=_("Due notice day"),
        choices=[(i, i) for i in range(1, 29)],
        default=1,
        help_text=_("This date defines the day of the month when the tenant must be informed of the amount due for the rent."),
    )
    text_receipt = models.TextField(
        verbose_name=_("Text of the receipt"),
        blank=True,
        null=True,
        help_text=_("Text to automatically display in the receipt. E.g. 'Thank you for your payment.'"),
    )
    text_due_notice = models.TextField(
        verbose_name=_("Text of the due notice"),
        blank=True,
        null=True,
        help_text=_("Text to automatically display in the due notice. E.g. 'Please pay your rent on time.'"),
    )
    documents = GenericRelation(to=Document, related_query_name="tenancy")

    class Meta:
        db_table = "tenancies"
        verbose_name = _(message="Tenancy")
        verbose_name_plural = _("Tenancies")

    def __str__(self) -> str:
        return f"Tenancy<{self.user.get_full_name()}>"
