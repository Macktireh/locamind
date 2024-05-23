from django.urls import path

from bienlocation.apps.core.views.accounts.login_view import LoginView
from bienlocation.apps.core.views.accounts.register_confirm_view import RegisterConfirmView
from bienlocation.apps.core.views.accounts.register_view import RegisterView
from bienlocation.apps.core.views.home.index_view import IndexView

urlpatterns_auth = [
    path(route="accounts/login/", view=LoginView.as_view(), name="login"),
    path(route="accounts/register/", view=RegisterView.as_view(), name="register"),
    path(route="accounts/register/confirm/", view=RegisterConfirmView.as_view(), name="register_confirm"),
]


urlpatterns = [
    path(route="", view=IndexView.as_view(), name="index"),
    *urlpatterns_auth,
]
