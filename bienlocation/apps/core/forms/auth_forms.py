from typing import Any

from django import forms
from django.utils.translation import gettext_lazy as _

from bienlocation.apps.core.validators import (
    PasswordFieldValidator,
    RequireFieldValidator,
    password_confirmation_validator,
)


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label=_("first name"),
        max_length=150,
        required=True,
        validators=[RequireFieldValidator("first_name")],
        widget=forms.TextInput(
            attrs={
                "placeholder": _("first name"),
                "class": "grow w-full",
            }
        ),
    )
    last_name = forms.CharField(
        label=_("last name"),
        max_length=150,
        required=True,
        validators=[RequireFieldValidator("first_name")],
        widget=forms.TextInput(
            attrs={
                "placeholder": _("last name"),
                "class": "grow w-full",
            }
        ),
    )
    email = forms.EmailField(
        label=_("email address"),
        max_length=254,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": _("email address"),
                "class": "grow w-full",
            }
        ),
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "grow w-full",
                "placeholder": _("Password"),
            },
        ),
        validators=[PasswordFieldValidator()],
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": _("Password confirmation"),
            "class": "grow w-full",
        }),
        strip=False,
    )

    @property
    def get_data(self) -> dict[str, Any]:
        payload = self.cleaned_data
        payload.pop("password2")
        payload["password"] = payload.pop("password1")
        return payload

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        password_confirmation_validator(password1, password2)
        return password2


class LoginForm(forms.Form):
    email = forms.EmailField(
        label=_("email address"),
        max_length=254,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": _("email address"),
                "class": "grow w-full",
            }
        ),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "grow w-full",
                "placeholder": _("Password"),
            },
        ),
    )
