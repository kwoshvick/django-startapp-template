from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from config import api_urls, settings

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^(?P<version>(v1))/", include(api_urls)),
]

if settings.DEBUG:
    urlpatterns += [
        path("redoc/", SpectacularRedocView.as_view(), name="redoc"),
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]


if settings.SILK_ENABLED:
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
