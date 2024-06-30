from django.contrib import admin

from apps.dashboard.models.address_model import Address
from apps.dashboard.models.contract_model import Contract
from apps.dashboard.models.property_model import Property
from apps.dashboard.models.receipt_model import Receipt
from apps.dashboard.models.tenant_model import Tenant


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "state", "postal_code", "country")


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("property", "tenant", "start_date", "end_date")


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("owner", "address", "property_type", "surface_area", "rooms", "rent", "charges", "options")


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ["contract", "issue_date", "amount_paid"]


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("user", "property")
