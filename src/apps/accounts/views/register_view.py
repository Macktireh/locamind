from django.contrib import messages
from django.contrib.auth.decorators import login_not_required
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.accounts.forms import RegisterForm
from apps.accounts.services.auth import auth_service
from apps.common.exceptions import UserAlreadyExistsError


@method_decorator(decorator=login_not_required, name="dispatch")
class RegisterView(View):
    template_name = "accounts/register.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name=self.template_name, context={"form": RegisterForm()})

    def post(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
        form = RegisterForm(data=request.POST or None)

        if form.is_valid():
            try:
                auth_service.register(request=request, **form.get_data)
                messages.success(request=request, message=_("Registration successful. Please activate your account."))
                return redirect("accounts:register_done")
            except UserAlreadyExistsError as e:
                messages.error(request=request, message=_(e.message))
        return render(request=request, template_name=self.template_name, context={"form": form})
