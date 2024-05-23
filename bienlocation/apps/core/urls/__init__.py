from django.urls import include, path

app_name = "core"

urlpatterns = [
    path(route="", view=include("bienlocation.apps.core.urls.web")),
]
