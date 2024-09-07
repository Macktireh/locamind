from uuid import uuid4

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.dashboard.apps import DashboardConfig
from apps.dashboard.enum import DocumentTypeChoice


def document_upload_path(instance: "Document", filename: str) -> str:
    doc_type = slugify(instance.type)
    name = slugify(instance.name)
    ext = filename.split(".")[-1]
    return f"documents/{doc_type}/{name}-{uuid4().hex}.{ext}"


def get_content_type_choices() -> Q:
    from apps.dashboard.models.landlords import Landlord
    from apps.dashboard.models.proof_identity import ProofIdentity
    from apps.dashboard.models.properties import Property
    from apps.dashboard.models.receipts import Receipt
    from apps.dashboard.models.tenancies import Tenancy
    from apps.dashboard.models.tenants import Tenant

    return (
        Q(app_label=DashboardConfig.name, model=Landlord.__name__.lower())
        | Q(app_label=DashboardConfig.name, model=ProofIdentity.__name__.lower())
        | Q(app_label=DashboardConfig.name, model=Property.__name__.lower())
        | Q(app_label=DashboardConfig.name, model=Receipt.__name__.lower())
        | Q(app_label=DashboardConfig.name, model=Tenancy.__name__.lower())
        | Q(app_label=DashboardConfig.name, model=Tenant.__name__.lower())
    )


class Document(BaseModel):
    type = models.CharField(verbose_name=_("Type"), choices=DocumentTypeChoice, max_length=255)
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    document = models.FileField(verbose_name=_("Document"), upload_to=document_upload_path)
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE, limit_choices_to=get_content_type_choices)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_id")

    class Meta:
        db_table = "documents"
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")

    def __str__(self) -> str:
        return self.name

    def get_document_url(self) -> str:
        return self.document.url
