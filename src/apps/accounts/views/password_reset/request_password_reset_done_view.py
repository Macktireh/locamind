from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class RequestPasswordResetDoneView(View):
    template_name = "accounts/password_reset/request_password_reset_done.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name=self.template_name, context={})
