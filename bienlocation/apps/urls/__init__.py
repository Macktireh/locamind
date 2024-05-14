from django.urls import path

from bienlocation.apps.views.index import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
