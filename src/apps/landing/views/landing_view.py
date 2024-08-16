from django.contrib.auth.decorators import login_not_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_not_required, name="dispatch")
class LandingView(View):
    template_name = "home/landing.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, template_name=self.template_name)
