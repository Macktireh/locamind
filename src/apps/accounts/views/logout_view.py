from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        logout(request=request)
        return redirect(to="accounts:login")
