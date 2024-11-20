from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_not_required
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.accounts.forms import LoginForm
from apps.accounts.services.auth import auth_service
from apps.common.exceptions import EmailNotConfirmError


@method_decorator(decorator=login_not_required, name="dispatch")
class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name=self.template_name, context={"form": LoginForm()})

    def post(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
        form = LoginForm(data=request.POST or None)
        next_path = request.GET.get("next", reverse("landing:index"))

        if form.is_valid():
            try:
                user = auth_service.login(request=request, **form.cleaned_data)
            except EmailNotConfirmError as e:
                messages.warning(request=request, message=_(e.message))
                return redirect(to="accounts:request_activate")

            if user:
                login(request=request, user=user)
                return redirect(next_path)

            messages.error(request=request, message=_("Invalid email or password"))
        return render(request=request, template_name=self.template_name, context={"form": form})
