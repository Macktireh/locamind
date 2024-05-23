from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class RegisterConfirmView(View):
    template_name = "auth/register_confirm.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}
        return render(request=request, template_name=self.template_name, context=context)
