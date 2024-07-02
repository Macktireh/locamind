from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class PasswordResetCompleteView(View):
    template_name = "accounts/password_reset/password_reset_complete.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name=self.template_name, context={})
