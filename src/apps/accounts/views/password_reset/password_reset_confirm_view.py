from django.contrib.auth.decorators import login_not_required
from django.http import Http404, HttpRequest, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from apps.accounts.forms import ResetPasswordConfirmForm
from apps.accounts.services.auth import auth_service


@method_decorator(decorator=login_not_required, name="dispatch")
class PasswordResetConfirmView(View):
    template_name = "accounts/password_reset/password_reset_confirm.html"

    def get(self, request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
        user = auth_service.password_reset_confirm_form(request=request, uidb64=uidb64, token=token)
        if user is None:
            return render(request=request, template_name="errors/404.html")
        return render(request=request, template_name=self.template_name, context={"form": ResetPasswordConfirmForm()})

    def post(
        self, request: HttpRequest, uidb64: str, token: str
    ) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
        form = ResetPasswordConfirmForm(data=request.POST or None)
        if form.is_valid():
            try:
                auth_service.password_reset_confirm(
                    request=request, uidb64=uidb64, token=token, payload=form.cleaned_data
                )
                return redirect(to="accounts:password_reset_complete")
            except Http404:
                return render(request=request, template_name="errors/404.html")

        return render(request=request, template_name=self.template_name, context={"form": form})
