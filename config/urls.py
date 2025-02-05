from django.contrib import admin
from django.urls import path

from django.urls import include

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.APP_ENV != "production":
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
    ]




