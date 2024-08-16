from django.urls import path

from apps.accounts.views.activation_view import ActivateView
from apps.accounts.views.login_view import LoginView
from apps.accounts.views.login_with_google_view import LoginWithGoogleCallBackView
from apps.accounts.views.logout_view import LogoutView
from apps.accounts.views.password_reset.password_reset_complete_view import PasswordResetCompleteView
from apps.accounts.views.password_reset.password_reset_confirm_view import PasswordResetConfirmView
from apps.accounts.views.password_reset.request_password_reset_done_view import RequestPasswordResetDoneView
from apps.accounts.views.password_reset.request_password_reset_view import RequestPasswordResetView
from apps.accounts.views.register_confirm_view import RegisterConfirmView
from apps.accounts.views.register_view import RegisterView
from apps.accounts.views.request_activation_view import RequestActivateView

app_name = "accounts"

urlpatterns = [
    path(route="login/", view=LoginView.as_view(), name="login"),
    path(route="login/google/callback/", view=LoginWithGoogleCallBackView.as_view(), name="login_with_google"),
    path(route="register/", view=RegisterView.as_view(), name="register"),
    path(route="register/confirm/", view=RegisterConfirmView.as_view(), name="register_done"),
    path(route="activate/<str:uidb64>/<str:token>/", view=ActivateView.as_view(), name="activate"),
    path(route="request/activate/", view=RequestActivateView.as_view(), name="request_activate"),
    path(route="request/password-reset/", view=RequestPasswordResetView.as_view(), name="reset_password"),
    path(route="request/password-reset/done/", view=RequestPasswordResetDoneView.as_view(), name="request_password_reset_done"),
    path(
        route="password-reset/confirm/<str:uidb64>/<str:token>/",
        view=PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(route="password-reset/complete/", view=PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path(route="logout/", view=LogoutView.as_view(), name="logout"),
]
