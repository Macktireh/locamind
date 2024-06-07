from bienlocation.apps.core.models import User


class UserSelectors:
    @staticmethod
    def get_user_by_email(email: str) -> User | None:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user_by_public_id(public_id: str) -> User | None:
        try:
            return User.objects.get(public_id=public_id)
        except User.DoesNotExist:
            return None
