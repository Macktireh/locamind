import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from apps.accounts.models import User


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: User, timestamp: int) -> str:
        return six.text_type(user.public_id) + six.text_type(timestamp) + six.text_type(user.is_active)


tokenGenerator = TokenGenerator()
