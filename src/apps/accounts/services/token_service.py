from abc import ABC, abstractmethod

import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from apps.accounts.models import User


class AbstractTokenService(ABC):
    @abstractmethod
    def generate_token_for_email_confirm(self, user) -> str:
        pass

    @abstractmethod
    def generate_token_for_password_reset(self, user) -> str:
        pass

    @abstractmethod
    def check_token_for_email_confirm(self, user, token) -> bool:
        pass

    @abstractmethod
    def check_token_for_password_reset(self, user, token) -> bool:
        pass


class EmailConfirmTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: User, timestamp: int) -> str:
        return six.text_type(user.public_id) + six.text_type(timestamp) + six.text_type(user.email_confirmed)


class TokenService(AbstractTokenService):
    def __init__(
        self,
        email_comfirm_token_generator: EmailConfirmTokenGenerator,
        password_reset_token_generator: PasswordResetTokenGenerator,
    ) -> None:
        self.email_comfirm_token_generator = email_comfirm_token_generator
        self.password_reset_token_generator = password_reset_token_generator

    def generate_token_for_email_confirm(self, user) -> str:
        return self.email_comfirm_token_generator.make_token(user)

    def generate_token_for_password_reset(self, user) -> str:
        return self.password_reset_token_generator.make_token(user)

    def check_token_for_email_confirm(self, user, token) -> bool:
        return self.email_comfirm_token_generator.check_token(user, token)

    def check_token_for_password_reset(self, user, token) -> bool:
        return self.password_reset_token_generator.check_token(user, token)


token_service = TokenService(EmailConfirmTokenGenerator(), PasswordResetTokenGenerator())
