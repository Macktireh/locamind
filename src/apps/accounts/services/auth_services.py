from typing import cast

from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db import transaction
from django.http import Http404, HttpRequest
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.accounts.selectors import UserSelectors
from apps.accounts.services.user_services import UserServices
from apps.common.exceptions import AccountDeactivatedError, UserAlreadyExistsError
from apps.common.services import model_update
from apps.common.types import EmailDataType, UserRegistrationDataType
from apps.common.utils import tokenGenerator
from apps.emails.models import Email
from apps.emails.services import EmailServices
from apps.emails.tasks import email_send as email_send_task


class AuthService:
    user_service = UserServices()
    template_email_activation = "accounts/email/activation.html"
    template_email_activation_success = "accounts/email/activation_success.html"
    template_email_request_reset_password = "accounts/email/request_reset_password.html"
    template_email_reset_password_complete = "accounts/email/reset_password_complete.html"

    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    @transaction.atomic
    def register(self, payload: UserRegistrationDataType) -> User:
        if UserSelectors.get_user_by_email(email=payload["email"]):
            raise UserAlreadyExistsError(_("User with this email already exists"))

        user = self.user_service.user_create(**payload)
        self._email_send_register(user)
        return user

    def login(self, email: str, password: str) -> User | None:
        user = cast(User | None, authenticate(email=email, password=password))

        if user and not user.email_confirmed:
            raise AccountDeactivatedError(_("Please activate your account first"))

        return user

    @transaction.atomic
    def activate(self, uidb64: str, token: str) -> None:
        try:
            public_id = force_str(urlsafe_base64_decode(uidb64))
            user = UserSelectors.get_user_by_public_id(public_id=public_id)
        except Exception as e:
            raise Http404("Invalid activation link.") from e

        if not user or not tokenGenerator.check_token(user, token):
            raise Http404("Invalid activation link.")

        user, __ = model_update(instance=user, fields=["email_confirmed"], data={"email_confirmed": True})
        email_payload = EmailDataType(
            to=user,
            subject=_("BienLocation account activation success."),
            plain_text="",
            html="",
        )
        self._email_send(payload=email_payload, template_name=self.template_email_activation_success, context={})

    def request_password_reset(self, payload: dict) -> None:
        if user := UserSelectors.get_user_by_email(email=payload["email"]):
            email_payload = EmailDataType(
                to=user,
                subject=_("Reset your password."),
                plain_text="",
                html="",
            )
            context = {
                "user": user,
                "uidb64": urlsafe_base64_encode(force_bytes(user.public_id)),
                "token": PasswordResetTokenGenerator().make_token(user),
            }
            self._email_send(payload=email_payload, template_name=self.template_email_request_reset_password, context=context)

    def password_reset_confirm_form(self, uidb64: str, token: str) -> None:
        try:
            public_id = force_str(urlsafe_base64_decode(uidb64))
            user = UserSelectors.get_user_by_public_id(public_id=public_id)
        except Exception:
            return None

        if not user or not PasswordResetTokenGenerator().check_token(user, token):
            return None

        return user

    @transaction.atomic
    def password_reset_confirm(self, uidb64: str, token: str, payload: dict) -> User:
        try:
            public_id = force_str(urlsafe_base64_decode(uidb64))
            user = UserSelectors.get_user_by_public_id(public_id=public_id)
        except Exception as e:
            raise Http404("Invalid password reset link.") from e

        if not user or not PasswordResetTokenGenerator().check_token(user, token):
            raise Http404("Invalid password reset link.")

        self.user_service.user_set_password(user=user, password=payload["new_password1"])
        email_payload = EmailDataType(
            to=user,
            subject=_("Password reset successful"),
            plain_text="",
            html="",
        )
        context = {}
        self._email_send(payload=email_payload, template_name=self.template_email_reset_password_complete, context=context)
        return user

    def request_activation(self, payload: dict) -> None:
        if (user := UserSelectors.get_user_by_email(email=payload["email"])) and not user.email_confirmed:
            self._email_send_register(user)

    def _email_send(self, payload: EmailDataType, template_name: str | None = None, context: dict | None = None) -> None:
        email = EmailServices.create(payload=payload, template_name=template_name, context=context, request=self.request)
        with transaction.atomic():
            Email.objects.filter(id=email.id).update(status=Email.Status.SENDING)
        transaction.on_commit(lambda: email_send_task.delay(email.id))

    def _email_send_register(self, user) -> None:
        email_payload = EmailDataType(
            to=user,
            subject=_("Activate your BienLocation account now!"),
            plain_text="",
            html="",
        )
        context = {
            "user": user,
            "uidb64": urlsafe_base64_encode(force_bytes(user.public_id)),
            "token": tokenGenerator.make_token(user),
        }
        self._email_send(email_payload, self.template_email_activation, context)
