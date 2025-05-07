from django.urls import include, path, re_path

urlpatterns = [
    path("accounts", include("apps.accounts.api.urls", namespace="accounts-api")),
]
