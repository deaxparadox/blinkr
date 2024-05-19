from django.urls import path, include

from .views import (
    index,
    hash_url,
    IndexView,
    access,
    history
)

app_name = "shortener"

urlpatterns = [
    path("hash/", hash_url, name='hash'),
    path("history/", history, name='history'),
    path("<str:url_hash>/", access, name="access"),
    path("", index, name="index"),
]
