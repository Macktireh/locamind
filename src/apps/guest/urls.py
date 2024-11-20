from django.urls import path

from apps.guest.views.landing_view import LandingView

app_name = "guest"

urlpatterns = [
    path(route="", view=LandingView.as_view(), name="index"),
]
