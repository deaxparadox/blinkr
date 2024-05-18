from django.urls import path, include

from .views import (
    index,
    hash_url,
    IndexView,
    root
)

app_name = "shortener"

urlpatterns = [
    path("", index, name="index"),
    path("redirect/", root, name="root"),
    path("hash/", hash_url, name='hash')
]
