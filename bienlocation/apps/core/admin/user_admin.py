from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.forms import Form, ValidationError
from django.utils.translation import gettext_lazy as _

from bienlocation.apps.common.types import AuthenticatedHttpRequest
from bienlocation.apps.core.forms.user_forms import UserChangeForm, UserCreationForm
from bienlocation.apps.core.models.user_models import User
from bienlocation.apps.core.services.user_services import UserServices


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = (
        "email",
        "full_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
        "updated_at",
    )
    list_filter = (
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "updated_at",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "public_id",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "updated_at",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )
    readonly_fields = ("public_id", "date_joined", "last_login", "updated_at")
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("date_joined",)

    def save_model(self, request: AuthenticatedHttpRequest, obj: User, form: Form, change: bool) -> None:
        if change:
            return super().save_model(request, obj, form, change)

        try:
            UserServices().user_create(**form.cleaned_data)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)

    def full_name(self, obj) -> str:
        return obj.get_full_name()
