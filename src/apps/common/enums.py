from django.db import models
from django.utils.translation import gettext_lazy as _


class PropertyType(models.TextChoices):
    APARTMENT = "APARTMENT", _("Apartment")
    HOUSE = "HOUSE", _("House")
    OFFICE = "OFFICE", _("Office")
    PARKING = "PARKING", _("Parking")
    GARAGE = "GARAGE", _("Garage")
    OTHER = "OTHER", _("Other")
