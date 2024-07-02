from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class RegisterConfirmView(View):
    template_name = "accounts/register_done.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name=self.template_name, context={})
