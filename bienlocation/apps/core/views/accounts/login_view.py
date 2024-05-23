from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from bienlocation.apps.core.forms.auth_forms import LoginForm
from bienlocation.apps.core.services.auth_services import AuthService
from bienlocation.apps.core.services.user_services import UserServices


class LoginView(View):
    template_name = "auth/login.html"
    user_service = UserServices()

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": LoginForm(),
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(data=request.POST or None)
        auth_service = AuthService(request=request)
        if form.is_valid():
            user = auth_service.authenticate(**form.cleaned_data)
            if user is not None:
                return redirect("core:index")

        context = {
            "form": form,
        }
        return render(request=request, template_name=self.template_name, context=context)
