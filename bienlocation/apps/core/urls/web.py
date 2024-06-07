from django.urls import include, path

from bienlocation.apps.core.views.home.index_view import IndexView

urlpatterns = [
    path(route="", view=IndexView.as_view(), name="index"),
    path(route="accounts/", view=include("bienlocation.apps.core.urls.accounts_urls")),
]
