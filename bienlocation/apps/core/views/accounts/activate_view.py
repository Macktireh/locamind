from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views import View

from bienlocation.apps.core.services.auth_services import AuthService


class ActivateView(View):
    template_name = "accounts/activate_success.html"

    def get(self, request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
        auth_service = AuthService(request=request)
        user = auth_service.activate(uidb64, token)
        if user is None:
            messages.error(request, _("Invalid activation link."))
            return render(request=request, template_name="errors/404.html")
        context = {}
        messages.success(request, _("Account activated successfully."))
        return render(request=request, template_name=self.template_name, context=context)
