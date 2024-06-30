import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class RequireFieldValidator:
    def __init__(self, field_name, message=None) -> None:
        self.field_name = field_name
        self.message = message or _(f"{self.field_name} is required")

    def __call__(self, value) -> None:
        if not value:
            raise ValidationError(self.message)


class RequireFieldMixin:
    def validate_required_fields(self, fields) -> None:
        for field in fields:
            value = getattr(self, field)
            if not value:
                raise ValidationError({field: _(f"{field} is required.")})


@deconstructible
class PasswordFieldValidator:
    def __init__(
        self,
        min_length=6,
        require_digit=True,
        require_upper=True,
        require_lower=True,
        require_special=True,
        message=None,
    ):
        self.min_length = min_length
        self.require_digit = require_digit
        self.require_upper = require_upper
        self.require_lower = require_lower
        self.require_special = require_special
        self.message = message or _("This password does not meet the requirements.")

    def __call__(self, value):
        if not value:
            raise ValidationError(_("The password is required."))

        errors = []

        if len(value) < self.min_length:
            errors.append(
                _("Password must be at least %(min_length)d characters long.") % {"min_length": self.min_length}
            )

        if self.require_digit and not re.search(r"\d", value):
            errors.append(_("Password must contain at least one digit."))

        if self.require_upper and not re.search(r"[A-Z]", value):
            errors.append(_("Password must contain at least one uppercase letter."))

        if self.require_lower and not re.search(r"[a-z]", value):
            errors.append(_("Password must contain at least one lowercase letter."))

        if self.require_special and not re.search(r"[\W_]", value):
            errors.append(_("Password must contain at least one special character."))

        if errors:
            raise ValidationError(errors)


def password_confirmation_validator(password1: str, password2: str) -> None:
    if password1 and password2 and password1 != password2:
        raise ValidationError(
            _("The two password fields didn't match."),
            code="password_mismatch",
        )
