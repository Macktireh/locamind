from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.dashboard.models.documents import Document


class ProofIdentity(BaseModel):
    number = models.CharField(verbose_name=_("Number"), max_length=255, null=True, blank=True)
    expiry = models.DateField(verbose_name=_("Expiry"), null=True, blank=True)
    document = GenericRelation(to=Document, related_query_name="proof_identity")

    class Meta:
        db_table = "proof_identities"
        verbose_name = _("Proof Identity")
        verbose_name_plural = _("Proof Identities")

    def __str__(self) -> str | None:
        return f"{self.document.type} - {self.document.name}"

    def get_document_url(self) -> str | None:
        if not self.document:
            return None
        return self.document.get_document_url()
