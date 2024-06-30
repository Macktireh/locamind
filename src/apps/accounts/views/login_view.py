from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.accounts.forms import LoginForm
from apps.accounts.services.auth_services import AuthService
from apps.accounts.services.user_services import UserServices
from apps.common.exceptions import AccountDeactivatedError


class LoginView(View):
    template_name = "accounts/login.html"
    user_service = UserServices()

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": LoginForm(),
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(data=request.POST or None)
        auth_service = AuthService(request=request)

        if form.is_valid():
            try:
                user = auth_service.login(**form.cleaned_data)
            except AccountDeactivatedError as e:
                messages.warning(request, _(e.message))
                return redirect("accounts:request_activate")

            if user:
                login(request=request, user=user)
                return redirect("landing")

        messages.error(request, _("Invalid email or password"))
        return render(request=request, template_name=self.template_name, context={"form": form})
