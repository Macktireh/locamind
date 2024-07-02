from django.urls import path

from apps.dashboard.views.index_view import DashboardIndexView

app_name = "dashboard"

urlpatterns = [
    path(route="", view=DashboardIndexView.as_view(), name="index"),
]
