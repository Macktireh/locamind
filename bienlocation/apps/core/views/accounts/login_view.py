from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from bienlocation.apps.common.exceptions import AccountDeactivatedError
from bienlocation.apps.core.forms.auth_forms import LoginForm
from bienlocation.apps.core.services.auth_services import AuthService
from bienlocation.apps.core.services.user_services import UserServices


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

            if user is not None:
                login(request, user=user)
                return redirect("index")

        messages.error(request, _("Invalid email or password"))
        return render(request=request, template_name=self.template_name, context={"form": form})
