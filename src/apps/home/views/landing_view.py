from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class LandingView(View):
    template_name = "home/landing.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, template_name=self.template_name)
