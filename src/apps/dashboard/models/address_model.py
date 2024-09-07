from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from apps.common.models import BaseModel


class Address(BaseModel):
    street = models.CharField(_("Street"), max_length=255)
    city = models.CharField(_("City"), max_length=255)
    state = models.CharField(_("State"), max_length=255)
    postal_code = models.CharField(_("Postal code"), max_length=255)
    country = CountryField(_("Country"))

    class Meta:
        db_table = "addresses"
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self) -> str:
        return f"{self.street}, {self.postal_code}, {self.city}, {self.country}"
