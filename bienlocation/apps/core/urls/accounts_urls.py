from django.urls import path

from bienlocation.apps.core.views.accounts.activate_view import ActivateView
from bienlocation.apps.core.views.accounts.login_view import LoginView
from bienlocation.apps.core.views.accounts.password_reset.password_reset_complete_view import PasswordResetCompleteView
from bienlocation.apps.core.views.accounts.password_reset.password_reset_confirm_view import PasswordResetConfirmView
from bienlocation.apps.core.views.accounts.password_reset.request_password_reset_done_view import RequestPasswordResetDoneView
from bienlocation.apps.core.views.accounts.password_reset.request_password_reset_view import RequestPasswordResetView
from bienlocation.apps.core.views.accounts.register_done_view import RegisterDoneView
from bienlocation.apps.core.views.accounts.register_view import RegisterView
from bienlocation.apps.core.views.accounts.request_activate_view import RequestActivateView

app_name = "accounts"

urlpatterns = [
    path(route="login/", view=LoginView.as_view(), name="login"),
    path(route="register/", view=RegisterView.as_view(), name="register"),
    path(route="register/confirm/", view=RegisterDoneView.as_view(), name="register_done"),
    path(route="activate/<str:uidb64>/<str:token>/", view=ActivateView.as_view(), name="activate"),
    path(route="request/activate/", view=RequestActivateView.as_view(), name="request_activate"),
    path(route="request/password-reset/", view=RequestPasswordResetView.as_view(), name="reset_password"),
    path(
        route="request/password-reset/done/",
        view=RequestPasswordResetDoneView.as_view(),
        name="request_password_reset_done",
    ),
    path(
        route="password-reset/confirm/<str:uidb64>/<str:token>/",
        view=PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(route="password-reset/complete/", view=PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
