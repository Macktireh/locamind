from django.db import models
from django.utils.translation import gettext_lazy as _


class TitleChoice(models.TextChoices):
    MISS = "miss", _("Miss")
    MS = "ms", _("Ms")
    MR = "mr", _("Mr")
    MRS = "mrs", _("Mrs")


class PropertyTypeChoice(models.TextChoices):
    APARTMENT = "apartment", _("Apartment")
    GARAGE = "garage", _("Garage")
    HOUSE = "house", _("House")
    OFFICE = "office", _("Office")
    PARKING = "parking", _("Parking")
    ROOM = "room", _("Room")
    SHOP = "shop", _("Shop")
    STORAGE_BOX = "storage_box", _("Storage box")
    STUDIO = "studio", _("Studio")
    TERRACE = "terrace", _("Terrace")
    WAREHOUSE = "warehouse", _("Warehouse")
    OTHER = "other", _("Other")


class PaymentFrequencyChoice(models.TextChoices):
    WEEKLY = "weekly", _("Weekly")
    MONTHLY = "monthly", _("Monthly")
    BIMONTHLY = "bimonthly", _("Bimonthly")
    QUARTERLY = "quarterly", _("Quarterly")
    SEMIANNUAL = "semiannual", _("Semiannual")
    YEARLY = "yearly", _("Yearly")


class TenantTypeChoice(models.TextChoices):
    INDIVIDUAL = "individual", _("Individual")
    COMPANY = "company", _("Company")
    OTHER = "other", _("Other")


class ProofIdentityTypeChoice(models.TextChoices):
    IDENTITY_CARD = "identity_card", _("Identity card")
    PASSPORT = "passport", _("Passport")
    DRIVING_LICENSE = "driving_license", _("Driving license")
    RESIDENCE_PERMIT = "residence_permit", _("Residence permit")


class DocumentTypeChoice(models.TextChoices):
    CONTACT = "contact", _("Contact")
    CONTRACT = "contract", _("Contract")
    DRIVING_LICENSE = "driving_license", _("Driving license")
    IDENTITY_CARD = "identity_card", _("Identity card")
    PASSPORT = "passport", _("Passport")
    RESIDENCE_PERMIT = "residence_permit", _("Residence permit")
    GUARANTOR = "guarantor", _("Guarantor")
    OTHER = "other", _("Other")


class TenancyTypeChoice(models.TextChoices):
    UNFURNISHED_RENTAL_AGREEMENT = "unfurnished_rental_agreement", _("Unfurnished rental agreement")
    FURNISHED_RENTAL_AGREEMENT = "furnished_rental_agreement", _("Furnished rental agreement")
    STUDENT_FURNISHED_RENTAL_AGREEMENT = "student_furnished_rental_agreement", _("Student furnished rental agreement")
    MOBILITY_LEASE = "mobility_lease", _("Mobility lease")
    SEASONAL_RENTAL_AGREEMENT = "seasonal_rental_agreement", _("Seasonal rental agreement")
    MIXED_USE_LEASE = "mixed_use_lease", _("Mixed use lease")
    COMMERCIAL_LEASE = "commercial_lease", _("Commercial lease")
    PROFESSIONAL_LEASE = "professional_lease", _("Professional lease")
    CIVIL_LEASE = "civil_lease", _("Civil lease")
    SERVICE_ACCOMMODATION_LEASE = "service_accommodation_lease", _("Service accommodation lease")
    COMPANY_HOUSING_LEASE = "company_housing_lease", _("Company housing lease")
    OTHER = "other", _("Other")


class PaymentMethodChoice(models.TextChoices):
    CREDIT_CARD = "credit_card", _("Credit card")
    CHEQUE = "cheque", _("Cheque")
    CASH = "cash", _("Cash")
    DIRECT_DEBIT = "direct_debit", _("Direct debit")
    BANK_TRANSFER = "bank_transfer", _("Bank transfer")


class ReceiptTitleTypeChoice(models.TextChoices):
    INVOICE = "invoice", _("Invoice")
    RECEIPT = "receipt", _("Receipt")


class ReceiptStatusChoice(models.TextChoices):
    PAID = "paid", _("Paid")
    PARTIALLY_PAID = "partially_paid", _("Partially paid")
    PENDING = "pending", _("Pending")

