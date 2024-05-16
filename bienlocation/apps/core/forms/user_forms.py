from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from bienlocation.apps.core.models.user_models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ["email"]


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ["email"]
