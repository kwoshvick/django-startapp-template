from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.urls import include

from config import settings

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("redoc/", SpectacularRedocView.as_view(), name="redoc"),
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    ]

if settings.APP_ENV != "production":
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
    ]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
