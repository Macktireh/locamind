from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from bienlocation.apps.core.forms.auth_forms import RequestPasswordResetForm
from bienlocation.apps.core.services.auth_services import AuthService


class RequestActivateView(View):
    template_name = "accounts/request_activate_success.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": RequestPasswordResetForm(),
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RequestPasswordResetForm(data=request.POST or None)
        auth_uservice = AuthService(request=request)
        if form.is_valid():
            auth_uservice.request_activation(form.cleaned_data)
            return redirect("accounts:register_done")
        context = {
            "form": form,
        }
        return render(request=request, template_name=self.template_name, context=context)
