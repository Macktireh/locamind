from django.contrib.auth import logout as auth_logout
from django.http import HttpRequest, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        auth_logout(request=request)
        return redirect(to="accounts:login")