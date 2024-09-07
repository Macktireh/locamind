from typing import cast

from django.contrib.auth import authenticate
from django.db import transaction
from django.http import Http404, HttpRequest
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.accounts.selectors import user_selectors
from apps.accounts.services.token_service import AbstractTokenService, token_service
from apps.accounts.services.user_service import user_service
from apps.common.exceptions import EmailNotConfirmError, UserAlreadyExistsError
from apps.common.types import EmailDataType, UserRegistrationDataType
from apps.emails.models import Email
from apps.emails.services import EmailServices
from apps.emails.tasks import email_send as email_send_task


class AuthService:
    template_email_activation = "accounts/email/activation.html"
    template_email_activation_success = "accounts/email/activation_success.html"
    template_email_request_reset_password = "accounts/email/request_reset_password.html"
    template_email_reset_password_complete = "accounts/email/reset_password_complete.html"

    def __init__(self, token_service: AbstractTokenService) -> None:
        self.token_service = token_service

    @transaction.atomic
    def register(self, request: HttpRequest, payload: UserRegistrationDataType) -> User:
        if user_selectors.get_user_by_email(email=payload["email"]):
            raise UserAlreadyExistsError(_("User with this email already exists"))

        user = user_service.create(**payload)
        self._email_send_register(user)
        return user

    def login(self, request: HttpRequest, email: str, password: str) -> User | None:
        user = cast(User | None, authenticate(email=email, password=password))

        if user and not user.email_confirmed:
            raise EmailNotConfirmError(_("Please confirm your email address"))

        return user

    @transaction.atomic
    def activate(self, request: HttpRequest, uidb64: str, token: str) -> None:
        try:
            public_id = force_str(urlsafe_base64_decode(uidb64))
            user = user_selectors.get_user_by_public_id(public_id=public_id)
        except Exception as e:
            raise Http404("Invalid activation link.") from e

        if not user or not self.token_service.check_token_for_email_confirm(user, token):
            raise Http404("Invalid activation link.")

        user = user_service.update(user=user, data={"email_confirmed": True})
        email_payload = EmailDataType(
            to=user,
            subject=_("BienRental account activation success."),
            plain_text="",
            html="",
        )
        self._email_send(payload=email_payload, template_name=self.template_email_activation_success, context={})

    def request_password_reset(self, request: HttpRequest, email: str) -> None:
        if user := user_selectors.get_user_by_email(email=email):
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
            self._email_send(payload=email_payload, template_name=self.template_email_request_reset_password, context=context)

    def password_reset_confirm_form(self, request: HttpRequest, uidb64: str, token: str) -> User | None:
        try:
            public_id = force_str(urlsafe_base64_decode(uidb64))
            user = user_selectors.get_user_by_public_id(public_id=public_id)
        except Exception:
            return None

        if not user or not self.token_service.check_token_for_password_reset(user, token):
            return None

        return user

    @transaction.atomic
    def password_reset_confirm(self, request: HttpRequest, uidb64: str, token: str, payload: dict) -> User:
        try:
            public_id = force_str(urlsafe_base64_decode(uidb64))
            user = user_selectors.get_user_by_public_id(public_id=public_id)
        except Exception as e:
            raise Http404("Invalid password reset link.") from e

        if not user or not self.token_service.check_token_for_password_reset(user, token):
            raise Http404("Invalid password reset link.")

        user_service.set_password(user=user, password=payload["new_password1"])
        email_payload = EmailDataType(
            to=user,
            subject=_("Password reset successful"),
            plain_text="",
            html="",
        )
        context = {}
        self._email_send(payload=email_payload, template_name=self.template_email_reset_password_complete, context=context)
        return user

    def request_activation(self, request: HttpRequest, email: str) -> None:
        if (user := user_selectors.get_user_by_email(email=email)) and not user.email_confirmed:
            self._email_send_register(user)

    def _email_send(
        self, request: HttpRequest, payload: EmailDataType, template_name: str | None = None, context: dict | None = None
    ) -> None:
        email = EmailServices.create(payload=payload, template_name=template_name, context=context, request=request)
        with transaction.atomic():
            Email.objects.filter(id=email.id).update(status=Email.Status.SENDING)
        transaction.on_commit(lambda: email_send_task.delay(email.id))

    def _email_send_register(self, user) -> None:
        email_payload = EmailDataType(
            to=user,
            subject=_("Activate your BienRental account now!"),
            plain_text="",
            html="",
        )
        context = {
            "user": user,
            "uidb64": urlsafe_base64_encode(force_bytes(user.public_id)),
            "token": self.token_service.generate_token_for_email_confirm(user),
        }
        self._email_send(email_payload, self.template_email_activation, context)


auth_service = AuthService(token_service=token_service)
