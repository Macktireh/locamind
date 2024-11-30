from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from apps.common.models import BaseModel


class Address(BaseModel):
    address = models.TextField(verbose_name=_("Address"), max_length=255)
    address_2 = models.TextField(verbose_name=_("Address 2"), max_length=255, blank=True, null=True)
    building = models.CharField(
        verbose_name=_("Building"),
        max_length=128,
        blank=True,
        null=True,
        help_text=_(
            "The building name or identifier, e.g. 'A', 'Main', 'Side', or '1'. Leave blank if not applicable."
        ),
    )
    entrance = models.CharField(
        verbose_name=_("Entrance"),
        max_length=128,
        blank=True,
        null=True,
        help_text=_(
            "The entrance name or identifier, e.g. 'A', 'Main', 'Side', or '1'. Leave blank if not applicable."
        ),
    )
    floor = models.CharField(
        verbose_name=_("Floor"),
        max_length=128,
        blank=True,
        null=True,
        help_text=_("The floor name or identifier, e.g. '1', '2', '3', or 'Ground'. Leave blank if not applicable."),
    )
    number = models.CharField(
        verbose_name=_("Number"),
        max_length=128,
        blank=True,
        null=True,
        help_text=_("The number or identifier, e.g. '1', '2', '3', or 'Ground'. Leave blank if not applicable."),
    )
    city = models.CharField(verbose_name=_("City"), max_length=128)
    postal_code = models.CharField(verbose_name=_("Postal Code"), max_length=8)
    region = models.CharField(verbose_name=_("Region"), max_length=128)
    country = CountryField(verbose_name=_("Country"))

    class Meta:
        db_table = "addresses"
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self) -> str:
        return f"{self.address} - {self.postal_code} - {self.country}"
