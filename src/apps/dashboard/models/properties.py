from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.dashboard.enum import PaymentFrequencyChoice, PropertyTypeChoice
from apps.dashboard.models.address import Address
from apps.dashboard.models.documents import Document
from apps.dashboard.models.landlords import Landlord


class Property(BaseModel):
    landlord = models.ForeignKey(
        verbose_name=_("landlord"), to=Landlord, on_delete=models.CASCADE, related_name="properties"
    )
    co_landlords = models.ManyToManyField(verbose_name=_("Co-landlords"), to=Landlord, blank=True)
    property_type = models.CharField(verbose_name=_("Type"), choices=PropertyTypeChoice.choices, max_length=255)
    identifier = models.CharField(verbose_name=_("Identifier"), max_length=128, unique=True)
    color = models.CharField(verbose_name=_("Color"), max_length=16, blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT, related_name="property")
    rent = models.DecimalField(verbose_name=_("Rent"), max_digits=10, decimal_places=2, blank=True, null=True)
    charges = models.DecimalField(verbose_name=_("Charges"), max_digits=10, decimal_places=2, blank=True, null=True)
    frequency = models.CharField(
        verbose_name=_("Payment Frequency"),
        choices=PaymentFrequencyChoice.choices,
        max_length=255,
        blank=True,
        null=True,
    )
    size = models.FloatField(verbose_name=_("Size M²"), blank=True, null=True)
    rooms = models.IntegerField(verbose_name=_("Number of rooms"), blank=True, null=True)
    bedrooms = models.IntegerField(verbose_name=_("Number of bedrooms"), blank=True, null=True)
    constructed = models.DateField(verbose_name=_("Date of construction"), blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    documents = GenericRelation(to=Document, related_query_name="property")

    class Meta:
        db_table = "properties"
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def __str__(self) -> str:
        return f"{self.property_type}<{self.owner.get_full_name()}>"
