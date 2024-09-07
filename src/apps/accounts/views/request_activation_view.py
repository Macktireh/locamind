from django.contrib.auth.decorators import login_not_required
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from apps.accounts.forms import RequestPasswordResetForm
from apps.accounts.services.auth_service import auth_service


@method_decorator(decorator=login_not_required, name="dispatch")
class RequestActivateView(View):
    template_name = "accounts/request_activate_success.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name=self.template_name, context={"form": RequestPasswordResetForm()})

    def post(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
        form = RequestPasswordResetForm(data=request.POST or None)
        if form.is_valid():
            auth_service.request_activation(request=request, email=form.cleaned_data["email"])
            return redirect(to="accounts:register_done")
        return render(request=request, template_name=self.template_name, context={"form": form})
