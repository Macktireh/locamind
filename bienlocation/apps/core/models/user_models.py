from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from bienlocation.apps.core.managers.user_manager import UserManager
from bienlocation.apps.core.models.base_models import BaseModel


class User(BaseModel, AbstractUser):
    username = None
    created = None
    email = models.EmailField(_("email address"), unique=True, db_index=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    def __str__(self):
        return f"{self.get_full_name()}<{self.email}>"
