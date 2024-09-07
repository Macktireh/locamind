from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_not_required
from django.http import HttpRequest, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View

from apps.accounts.services.social_auth_service import GoogleSocialAuthService
from apps.accounts.services.user_service import user_service


@method_decorator(decorator=login_not_required, name="dispatch")
class LoginWithGoogleCallBackView(View):
    google_service = GoogleSocialAuthService(
        google_client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
        google_client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URI,
    )

    def get(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        code = request.GET.get("code", None)
        if not code:
            return redirect("accounts:login")
        try:
            access_token = self.google_service.exchange_code_for_access_token(code=code)
            user_data = self.google_service.retrieve_user_data(access_token=access_token)
            user = user_service.user_create_without_password(**user_data)
            login(request=request, user=user)
            return redirect("landing:index")
        except Exception as e:
            messages.error(request=request, message=str(e.message))
        return redirect("accounts:login")
