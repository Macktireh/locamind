from django.urls import path

from apps.landing.views.landing_view import LandingView

app_name = "landing"

urlpatterns = [
    path(route="", view=LandingView.as_view(), name="index"),
]
