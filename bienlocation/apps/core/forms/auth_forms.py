from typing import Any

from django import forms
from django.utils.translation import gettext_lazy as _

from bienlocation.apps.common.validators import (
    PasswordFieldValidator,
    RequireFieldValidator,
    password_confirmation_validator,
)


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label=_("first name"),
        max_length=150,
        required=True,
        initial="John",
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
        initial="Doe",
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
        initial="admin@gmail.com",
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
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "placeholder": _("Password confirmation"),
                "class": "grow w-full",
            }
        ),
        strip=False,
    )
    accepted_terms = forms.BooleanField(
        label=_("I accept the terms and conditions"),
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox checkbox-primary",
            }
        ),
        error_messages={
            "required": _("You must accept the terms and conditions."),
        },
        validators=[RequireFieldValidator("accepted_terms")],
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
        initial="admin@gmail.com",
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


class RequestPasswordResetForm(forms.Form):
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


class ResetPasswordConfirmForm(forms.Form):
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "grow w-full",
                "placeholder": _("New password"),
            },
        ),
        validators=[PasswordFieldValidator()],
    )
    new_password2 = forms.CharField(
        label=_("New Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "placeholder": _("New Password confirmation"),
                "class": "grow w-full",
            }
        ),
        strip=False,
    )

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get("new_password1")
        new_password2 = self.cleaned_data.get("new_password2")
        password_confirmation_validator(new_password1, new_password2)
        return new_password2
