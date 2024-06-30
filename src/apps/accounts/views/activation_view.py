from django.contrib import messages
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.accounts.services.auth_services import AuthService


class ActivateView(View):
    template_name = "accounts/activate_success.html"

    def get(self, request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
        auth_service = AuthService(request=request)

        try:
            auth_service.activate(uidb64, token)
        except Http404:
            return render(request=request, template_name="errors/404.html")

        messages.success(request, _("Account activated successfully."))
        return render(request=request, template_name=self.template_name, context={})
