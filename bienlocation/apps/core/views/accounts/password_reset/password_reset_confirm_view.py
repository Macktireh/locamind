from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from bienlocation.apps.core.forms.auth_forms import ResetPasswordConfirmForm
from bienlocation.apps.core.services.auth_services import AuthService


class PasswordResetConfirmView(View):
    template_name = "accounts/password_reset/password_reset_confirm.html"

    def get(self, request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
        auth_uservice = AuthService(request=request)
        user = auth_uservice.password_reset_confirm_form(uidb64, token)
        if user is None:
            return render(request=request, template_name="errors/404.html")
        context = {
            "form": ResetPasswordConfirmForm(),
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
        form = ResetPasswordConfirmForm(data=request.POST or None)
        auth_uservice = AuthService(request=request)
        if form.is_valid():
            try:
                user = auth_uservice.password_reset_confirm(uidb64, token, form.cleaned_data)
            except Http404:
                return render(request=request, template_name="errors/404.html")

            if user:
                return redirect("accounts:password_reset_complete")

        context = {
            "form": form,
        }
        return render(request=request, template_name=self.template_name, context=context)
