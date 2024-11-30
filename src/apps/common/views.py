from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def error_404_view(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(request=request, template_name="errors/404.html")
