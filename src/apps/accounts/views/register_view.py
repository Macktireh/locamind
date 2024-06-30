from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.accounts.forms import RegisterForm
from apps.accounts.services.auth_services import AuthService
from apps.common.exceptions import UserAlreadyExistsError


class RegisterView(View):
    template_name = "accounts/register.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": RegisterForm(),
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(data=request.POST or None)
        auth_service = AuthService(request=request)

        if form.is_valid():
            try:
                auth_service.register(form.get_data)
                messages.success(request, _("Registration successful. Please activate your account."))
                return redirect("accounts:register_done")
            except UserAlreadyExistsError as e:
                messages.error(request, _(e.message))
        return render(request=request, template_name=self.template_name, context={"form": form})
