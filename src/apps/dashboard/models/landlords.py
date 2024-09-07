from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.accounts.models import User
from apps.common.models import BaseModel
from apps.dashboard.models.address import Address
from apps.dashboard.models.documents import Document


class Landlord(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="landlords")
    title = models.CharField(verbose_name=_("Title"), max_length=255, blank=True)
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), blank=True)
    photo = models.ImageField(verbose_name=_("Photo"), upload_to="landlords", null=True, blank=True)
    address = models.OneToOneField(
        verbose_name=_("Address"), to=Address, on_delete=models.SET_NULL, null=True, related_name="landlord"
    )
    documents = GenericRelation(to=Document, related_query_name="landlord")

    class Meta:
        db_table = "landlords"
        verbose_name = _("Landlord")
        verbose_name_plural = _("Landlords")

    def __str__(self) -> str:
        return f"Landlord<{self.user.get_full_name()}>"
