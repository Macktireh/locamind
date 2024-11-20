from typing import cast

from django.contrib.auth import authenticate
from django.http import Http404
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.accounts.services.token import AbstractTokenService, token_service
from apps.accounts.services.user import UserService, user_service
from apps.accounts.types import UserRegistrationPayloadType
from apps.common.exceptions import EmailNotConfirmError, UserAlreadyExistsError
from apps.emails.services import EmailService, email_service
from apps.emails.types import EmailDataType


class AuthService:
    template_email_activation = "accounts/email/activation.html"
    template_email_activation_success = "accounts/email/activation_success.html"
    template_email_request_reset_password = "accounts/email/request_reset_password.html"
    template_email_reset_password_complete = "accounts/email/reset_password_complete.html"

    def __init__(
        self, user_service: UserService, token_service: AbstractTokenService, email_service: EmailService
    ) -> None:
        self.user_service = user_service
        self.token_service = token_service
        self.email_service = email_service

    def register(self, payload: UserRegistrationPayloadType) -> User:
        if self.user_service.get_by_email(email=payload["email"]):
            raise UserAlreadyExistsError(_("User with this email already exists"))
        user = self.user_service.create(**payload)
        self._email_send_register(user)
        return user

    def login(self, email: str, password: str) -> User | None:
        user = cast(User | None, authenticate(email=email, password=password))
        if user and not user.email_confirmed:
            raise EmailNotConfirmError(_("Please confirm your email address"))
        return user

    def activate(self, uidb64: str, token: str) -> None:
        try:
            public_id = force_str(urlsafe_base64_decode(uidb64))
            user = self.user_service.get_by_public_id(public_id=public_id)
        except Exception as e:
            raise Http404("Invalid activation link.") from e

        if not user or not self.token_service.check_token_for_email_confirm(user, token):
            raise Http404("Invalid activation link.")

        user = self.user_service.update(user=user, data={"email_confirmed": True})
        email_payload = EmailDataType(
            to=user,
            subject=_("Locamind account activation success."),
            plain_text="",
            html="",
        )
        self.email_service.email_send_task(
            payload=email_payload, template_name=self.template_email_activation_success, context={}
        )

    def request_password_reset(self, email: str) -> None:
        if user := self.user_service.get_by_email(email=email):
            email_payload = EmailDataType(
                to=user,
                subject=_("Reset your password."),
                plain_text="",
                html="",
            )
            context = {
                "user": user,
                "uidb64": urlsafe_base64_encode(force_bytes(user.public_id)),
                "token": self.token_service.generate_token_for_password_reset(user),
            }
            self.email_service.email_send_task(
                payload=email_payload,
                template_name=self.template_email_request_reset_password,
                context=context,
            )

    def password_reset_confirm_form(self, uidb64: str, token: str) -> User | None:
        try:
            public_id = force_str(urlsafe_base64_decode(uidb64))
            user = self.user_service.get_by_public_id(public_id=public_id)
        except Exception:
            return None

        if not user or not self.token_service.check_token_for_password_reset(user, token):
            return None

        return user

    def password_reset_confirm(self, uidb64: str, token: str, payload: dict) -> User:
        try:
            public_id = force_str(urlsafe_base64_decode(uidb64))
            user = self.user_service.get_by_public_id(public_id=public_id)
        except Exception as e:
            raise Http404("Invalid password reset link.") from e

        if not user or not self.token_service.check_token_for_password_reset(user, token):
            raise Http404("Invalid password reset link.")

        self.user_service.set_password(user=user, password=payload["new_password1"])
        email_payload = EmailDataType(
            to=user,
            subject=_("Password reset successful"),
            plain_text="",
            html="",
        )
        context = {}
        self.email_service.email_send_task(
            payload=email_payload, template_name=self.template_email_reset_password_complete, context=context
        )
        return user

    def request_activation(self, email: str) -> None:
        if (user := self.user_service.get_by_email(email=email)) and not user.email_confirmed:
            self._email_send_register(user)

    def _email_send_register(self, user) -> None:
        email_payload = EmailDataType(
            to=user,
            subject=_("Activate your LocaMind account now!"),
            plain_text="",
            html="",
        )
        context = {
            "user": user,
            "uidb64": urlsafe_base64_encode(force_bytes(user.public_id)),
            "token": self.token_service.generate_token_for_email_confirm(user),
        }
        self.email_service.email_send_task(email_payload, self.template_email_activation, context)


auth_service = AuthService(user_service=user_service, token_service=token_service, email_service=email_service)
