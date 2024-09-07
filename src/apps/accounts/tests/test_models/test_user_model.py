from django.test import TestCase

from apps.core.models import User


class UserModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            first_name="John", last_name="Doe", email="john.doe@example.com", password="password123"
        )

    def test_user_creation(self) -> None:
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertTrue(self.user.check_password("password123"))
        self.assertEqual(str(self.user), "John Doe<john.doe@example.com>")
