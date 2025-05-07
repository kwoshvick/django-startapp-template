from django.urls import include, re_path

urlpatterns = [
    re_path(
        r"^accounts/",
        include(("apps.accounts.api.urls", "accounts-api"), namespace="accounts-api"),
    ),
]
