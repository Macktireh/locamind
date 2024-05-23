from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from bienlocation.apps.common.types import UserRegistrationDataType
from bienlocation.apps.core.models.user_models import User
from bienlocation.apps.core.services.user_services import UserServices


class AuthService:
    user_service = UserServices()

    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    @transaction.atomic
    def register(self, payload: UserRegistrationDataType) -> User:
        user = self.user_service.user_create(**payload, is_active=False)
        messages.success(self.request, _("Registration successful. Please activate your account."))

        # TODO: send activation email


        return user

    def authenticate(self, email: str, password: str) -> User | None:
        user = authenticate(email=email, password=password)

        if user is None:
            messages.error(self.request, _("Invalid email or password"))
            return None

        login(request=self.request, user=user)
        return user
