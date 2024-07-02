from django.conf import settings
from django.contrib import admin
from django.urls import include, path

handler404 = "apps.common.views.error_404_view"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.home.urls")),
    path("", include("apps.accounts.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
