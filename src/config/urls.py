from django.conf import settings
from django.contrib import admin
from django.urls import include, path

handler404 = "apps.common.views.error_404_view"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.landing.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
]


if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ] + debug_toolbar_urls()
