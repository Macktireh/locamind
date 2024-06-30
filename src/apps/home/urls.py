from django.urls import path

from apps.home.views.landing_view import LandingView

urlpatterns = [
    path(route="", view=LandingView.as_view(), name="landing"),
]
