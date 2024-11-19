from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_not_required
from django.http import HttpRequest, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from simplesocialauthlib.providers.google import GoogleSocialAuth

from apps.accounts.services.user_service import user_service


@method_decorator(decorator=login_not_required, name="dispatch")
class SignInWithGoogleView(View):
    google_auth_service = GoogleSocialAuth(
        client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
        client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URI,
    )

    def get(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        code = request.GET.get("code", None)
        if not code:
            return redirect("accounts:login")
        try:
            user_data = self.google_auth_service.sign_in(code=code)
            user = user_service.create(
                first_name=user_data["first_name"], last_name=user_data["last_name"], email=user_data["email"]
            )
            login(request=request, user=user)
            return redirect("landing:index")
        except Exception as e:
            messages.error(request=request, message=str(e.message))
            return redirect("accounts:login")
