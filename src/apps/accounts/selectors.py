from apps.accounts.models import User


class UserSelectors:
    def get_user_by_email(self, email: str) -> User | None:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get_user_by_public_id(self, public_id: str) -> User | None:
        try:
            return User.objects.get(public_id=public_id)
        except User.DoesNotExist:
            return None


user_selectors = UserSelectors()
