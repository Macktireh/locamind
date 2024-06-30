from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'home.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}
        return render(request=request, template_name=self.template_name, context=context)
