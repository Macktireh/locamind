from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.accounts.models import User
from apps.common.models import BaseModel
from apps.dashboard.enum import TenantTypeChoice, TitleChoice
from apps.dashboard.models.address import Address
from apps.dashboard.models.documents import Document
from apps.dashboard.models.landlords import Landlord
from apps.dashboard.models.proof_identity import ProofIdentity


class Tenant(BaseModel):
    landlord = models.ForeignKey(
        verbose_name=_("Landlord"), to=Landlord, on_delete=models.CASCADE, related_name="tenants"
    )
    user = models.ForeignKey(
        verbose_name=_("User"), to=User, on_delete=models.SET_NULL, related_name="tenants", null=True
    )
    tenant_type = models.CharField(verbose_name=_("Type"), choices=TenantTypeChoice.choices, max_length=64)
    title = models.CharField(verbose_name=_("Title"), choices=TitleChoice.choices, max_length=8, blank=True, null=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=128)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=128)
    email = models.EmailField(verbose_name=_("Email"), max_length=128, null=True, blank=True)
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), null=True, blank=True)
    identity = models.ForeignKey(
        verbose_name=_("Proof of identity"), to=ProofIdentity, on_delete=models.SET_NULL, null=True
    )
    profession = models.CharField(verbose_name=_("Profession"), max_length=255, null=True, blank=True)
    income = models.DecimalField(
        verbose_name=_("Monthly Income"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    employer = models.CharField(verbose_name=_("Employer"), max_length=255, null=True, blank=True)
    address = models.ForeignKey(
        verbose_name=_("Address"), to=Address, on_delete=models.SET_NULL, null=True, related_name="tenants"
    )
    compagny_name = models.CharField(verbose_name=_("Company name"), max_length=128, null=True, blank=True)
    guarantor_name = models.CharField(verbose_name=_("Guarantor name"), max_length=128, null=True, blank=True)
    documents = GenericRelation(to=Document, related_query_name="tenant")

    class Meta:
        db_table = "tenants"
        verbose_name = _("Tenant")
        verbose_name_plural = _("Tenants")

    def __str__(self) -> str:
        return f"Tenant<{self.user.get_full_name()}>"
