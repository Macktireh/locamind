from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from bienlocation.apps.core.forms.auth_forms import RegisterForm
from bienlocation.apps.core.services.auth_services import AuthService


class RegisterView(View):
    template_name = "auth/register.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": RegisterForm(),
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(data=request.POST or None)
        auth_uservice = AuthService(request=request)
        if form.is_valid():
            self.user = auth_uservice.register(form.get_data)
            return redirect("core:register_confirm")

        context = {
            "form": form,
        }
        return render(request=request, template_name=self.template_name, context=context)
