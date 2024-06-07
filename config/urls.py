from django.conf import settings
from django.contrib import admin
from django.urls import include, path

handler404 = "bienlocation.apps.common.views.error_404_view"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("bienlocation.apps.core.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
