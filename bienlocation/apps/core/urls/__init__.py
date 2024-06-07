from django.urls import include, path

urlpatterns = [
    path(route="", view=include("bienlocation.apps.core.urls.web")),
]
