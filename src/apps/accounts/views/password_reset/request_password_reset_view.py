from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from apps.accounts.forms import RequestPasswordResetForm
from apps.accounts.services.auth_services import AuthService


class RequestPasswordResetView(View):
    template_name = "accounts/password_reset/request_password_reset.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name=self.template_name, context={"form": RequestPasswordResetForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RequestPasswordResetForm(data=request.POST or None)
        auth_uservice = AuthService(request=request)
        if form.is_valid():
            auth_uservice.request_password_reset(form.cleaned_data)
            return redirect("accounts:request_password_reset_done")
        context = {
            "form": form,
        }
        return render(request=request, template_name=self.template_name, context=context)
