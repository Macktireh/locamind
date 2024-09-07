from django.contrib import messages
from django.contrib.auth.decorators import login_not_required
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.accounts.services.auth_service import auth_service


@method_decorator(decorator=login_not_required, name="dispatch")
class ActivateView(View):
    template_name = "accounts/activate_success.html"

    def get(self, request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
        try:
            auth_service.activate(request=request, uidb64=uidb64, token=token)
        except Http404:
            return render(request=request, template_name="errors/404.html")

        messages.success(request=request, message=_("Account activated successfully."))
        return render(request=request, template_name=self.template_name, context={})
