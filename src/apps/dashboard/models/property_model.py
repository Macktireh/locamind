from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.common.models import BaseModel
from apps.dashboard.models.address_model import Address


class Property(BaseModel):
    class PropertyType(models.TextChoices):
        APARTMENT = "APARTMENT", _("Apartment")
        HOUSE = "HOUSE", _("House")
        OFFICE = "OFFICE", _("Office")
        PARKING = "PARKING", _("Parking")
        GARAGE = "GARAGE", _("Garage")
        OTHER = "OTHER", _("Other")

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, related_name="property")
    property_type = models.CharField(_("Property type"), max_length=255, choices=PropertyType.choices)
    surface_area = models.FloatField(_("Surface area"))
    rooms = models.IntegerField(_("Rooms"))
    rent = models.DecimalField(_("Rent"), max_digits=10, decimal_places=2)
    charges = models.DecimalField(_("Charges"), max_digits=10, decimal_places=2)
    options = models.JSONField(_("Options"), blank=True, null=True)

    class Meta:
        db_table = "properties"
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def __str__(self) -> str:
        return f"{self.property_type}<{self.owner.get_full_name()}>"
